#!/usr/bin/env python3
"""Simula escenarios de causalidad y fallos parciales usando relojes vectoriales."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List


@dataclass
class VectorClock:
    values: Dict[str, int]

    def copy(self) -> "VectorClock":
        return VectorClock(self.values.copy())

    def increment(self, replica: str) -> None:
        self.values[replica] = self.values.get(replica, 0) + 1

    def merge(self, other: "VectorClock") -> None:
        for key, value in other.values.items():
            self.values[key] = max(self.values.get(key, 0), value)

    def happened_before(self, other: "VectorClock") -> bool:
        strictly_less = False
        for replica in set(self.values) | set(other.values):
            a = self.values.get(replica, 0)
            b = other.values.get(replica, 0)
            if a > b:
                return False
            if a < b:
                strictly_less = True
        return strictly_less

    def dominates(self, other: "VectorClock") -> bool:
        for replica in set(self.values) | set(other.values):
            if self.values.get(replica, 0) < other.values.get(replica, 0):
                return False
        return True

    def __repr__(self) -> str:  # pragma: no cover - ayuda para debugging manual
        return f"VectorClock({self.values})"


class SimulationError(RuntimeError):
    pass


def assert_condition(condition: bool, message: str) -> None:
    if not condition:
        raise SimulationError(message)


def simulate() -> str:
    replicas = {
        "r1": VectorClock({"r1": 0}),
        "r2": VectorClock({"r2": 0}),
        "r3": VectorClock({"r3": 0}),
    }
    session_vectors: Dict[str, VectorClock] = {"session-123": VectorClock({})}

    timeline: List[str] = []

    # Paso 1: r1 procesa una escritura del usuario
    replicas["r1"].increment("r1")
    session_vectors["session-123"].merge(replicas["r1"])
    timeline.append("r1:update_cart")

    # Paso 2: r2 intenta leer antes de recibir la actualización
    local_view = replicas["r2"].copy()
    assert_condition(
        not local_view.dominates(session_vectors["session-123"]),
        "r2 no debería tener todavía la sesión sincronizada",
    )
    # El middleware espera hasta que el estado refleje la sesión
    replicas["r2"].merge(session_vectors["session-123"])
    local_view = replicas["r2"].copy()
    assert_condition(
        local_view.dominates(session_vectors["session-123"]),
        "r2 debe garantizar read-your-writes antes de responder",
    )
    timeline.append("r2:sync_read")

    # Paso 3: r3 realiza un update concurrente (fallo parcial en r1 ralentiza la entrega)
    replicas["r3"].increment("r3")
    timeline.append("r3:inventory_patch")

    # r1 recibe el evento de r3 después de recuperarse del fallo parcial
    incoming = replicas["r3"].copy()
    r1_before = replicas["r1"].copy()
    concurrent = not incoming.happened_before(
        r1_before
    ) and not r1_before.happened_before(incoming)
    assert_condition(
        concurrent,
        "El evento de r3 debe detectarse como concurrente respecto al estado de r1",
    )
    replicas["r1"].merge(incoming)
    timeline.append("r1:merge_concurrent")

    # Paso 4: simular reproceso (replay) para garantizar idempotencia en estrategias activas
    replay = incoming.copy()
    replicas["r1"].merge(replay)
    assert_condition(
        replicas["r1"].dominates(replay),
        "Después de un replay, el estado debe permanecer convergente",
    )
    timeline.append("r1:replay_idempotent")

    return " -> ".join(timeline)


if __name__ == "__main__":
    try:
        trail = simulate()
    except SimulationError as exc:
        print(f"ERROR: {exc}")
        raise SystemExit(1)
    print("Causalidad OK:", trail)
