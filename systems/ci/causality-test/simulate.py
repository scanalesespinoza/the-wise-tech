#!/usr/bin/env python3
"""Simulate causal scenarios and partial failures using vector clocks."""

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

    def __repr__(self) -> str:  # pragma: no cover - manual debugging helper
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

    # Step 1: r1 processes a user write
    replicas["r1"].increment("r1")
    session_vectors["session-123"].merge(replicas["r1"])
    timeline.append("r1:update_cart")

    # Step 2: r2 tries to read before receiving the update
    local_view = replicas["r2"].copy()
    assert_condition(
        not local_view.dominates(session_vectors["session-123"]),
        "r2 should not have the session synchronized yet",
    )
    # Middleware waits until state reflects the session
    replicas["r2"].merge(session_vectors["session-123"])
    local_view = replicas["r2"].copy()
    assert_condition(
        local_view.dominates(session_vectors["session-123"]),
        "r2 must guarantee read-your-writes before responding",
    )
    timeline.append("r2:sync_read")

    # Step 3: r3 performs a concurrent update (partial r1 failure slows delivery)
    replicas["r3"].increment("r3")
    timeline.append("r3:inventory_patch")

    # r1 receives r3's event after recovering from the partial failure
    incoming = replicas["r3"].copy()
    r1_before = replicas["r1"].copy()
    concurrent = not incoming.happened_before(
        r1_before
    ) and not r1_before.happened_before(incoming)
    assert_condition(
        concurrent,
        "r3's event must be detected as concurrent relative to r1's state",
    )
    replicas["r1"].merge(incoming)
    timeline.append("r1:merge_concurrent")

    # Step 4: replay to ensure idempotency on active strategies
    replay = incoming.copy()
    replicas["r1"].merge(replay)
    assert_condition(
        replicas["r1"].dominates(replay),
        "After replay, the state must remain convergent",
    )
    timeline.append("r1:replay_idempotent")

    return " -> ".join(timeline)


if __name__ == "__main__":
    try:
        trail = simulate()
    except SimulationError as exc:
        print(f"ERROR: {exc}")
        raise SystemExit(1)
    print("Causality OK:", trail)
