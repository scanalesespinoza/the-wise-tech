#!/usr/bin/env python3
"""Lint para políticas de resiliencia: valida rangos y consistencia básica."""
from __future__ import annotations

import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
POLICY_PATH = ROOT / "platform" / "policies" / "resilience.yml"


def load() -> dict:
    try:
        return json.loads(POLICY_PATH.read_text(encoding="utf-8"))
    except FileNotFoundError:
        raise SystemExit(f"archivo no encontrado: {POLICY_PATH}")
    except json.JSONDecodeError as exc:
        raise SystemExit(f"{POLICY_PATH} no es JSON/YAML válido: {exc}")


def ensure_positive(value: int | float, label: str, errors: list[str]) -> None:
    if value <= 0:
        errors.append(f"{label} debe ser mayor a 0, obtenido {value}")


def lint() -> int:
    data = load()
    errors: list[str] = []
    warnings: list[str] = []

    timeouts = data.get("timeouts", {})
    for key, value in timeouts.items():
        ensure_positive(value, f"timeouts.{key}", errors)
    if timeouts.get("max_request_ms", 0) < timeouts.get("default_request_ms", 0):
        errors.append("max_request_ms debe ser >= default_request_ms")

    retries = data.get("retries", {})
    for name, policy in retries.items():
        attempts = policy.get("max_attempts", 0)
        backoff = policy.get("backoff_ms", -1)
        if attempts < 1:
            errors.append(f"retries.{name}.max_attempts debe ser >= 1")
        if backoff < 0:
            errors.append(f"retries.{name}.backoff_ms no puede ser negativo")

    quorums = data.get("quorums", {})
    total_nodes = quorums.get("total_nodes", 0)
    ensure_positive(total_nodes, "quorums.total_nodes", errors)
    read_min = quorums.get("read_minimum", 0)
    write_min = quorums.get("write_minimum", 0)
    if read_min < 0 or write_min < 0:
        errors.append("quorums.read_minimum y write_minimum no pueden ser negativos")
    if read_min + write_min <= total_nodes:
        warnings.append(
            "la suma de quórums de lectura y escritura no supera el total de nodos; revisar requisitos de consistencia"
        )

    circuit_breakers = data.get("circuit_breakers", {})
    threshold = circuit_breakers.get("error_rate_threshold", 0)
    if not 0 < threshold < 1:
        errors.append("error_rate_threshold debe estar en (0,1)")
    for key in ("rolling_window_s", "cooldown_s"):
        ensure_positive(circuit_breakers.get(key, 0), f"circuit_breakers.{key}", errors)

    ttl = data.get("ttl", {})
    for key, value in ttl.items():
        ensure_positive(value, f"ttl.{key}", errors)

    replication = data.get("replication", {})
    for name, details in replication.items():
        profiles = details.get("supported_profiles", [])
        if not profiles:
            warnings.append(f"replication.{name} no declara supported_profiles")

    services = data.get("services", [])
    for service in services:
        label = service.get("name", "<sin-nombre>")
        timeout = service.get("timeouts_ms")
        if timeout is not None and timeout > timeouts.get("max_request_ms", sys.maxsize):
            warnings.append(
                f"{label}: timeouts_ms ({timeout}) excede max_request_ms global"
            )
        quorum = service.get("quorum")
        if quorum:
            read = quorum.get("read", 0)
            write = quorum.get("write", 0)
            if read > total_nodes or write > total_nodes:
                errors.append(
                    f"{label}: quórums de lectura/escritura no pueden exceder total_nodes ({total_nodes})"
                )

    if errors:
        for line in errors:
            print(f"ERROR: {line}")
        if warnings:
            for line in warnings:
                print(f"WARN: {line}")
        return 1

    if warnings:
        for line in warnings:
            print(f"WARN: {line}")
    print("Resilience policies OK.")
    return 0


if __name__ == "__main__":
    sys.exit(lint())
