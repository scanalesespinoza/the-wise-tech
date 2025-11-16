#!/usr/bin/env python3
"""Lint for resilience policies that validates ranges and basic consistency."""

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
        raise SystemExit(f"file not found: {POLICY_PATH}")
    except json.JSONDecodeError as exc:
        raise SystemExit(f"{POLICY_PATH} is not valid JSON/YAML: {exc}")


def ensure_positive(value: int | float, label: str, errors: list[str]) -> None:
    if value <= 0:
        errors.append(f"{label} must be greater than 0, found {value}")


def lint() -> int:
    data = load()
    errors: list[str] = []
    warnings: list[str] = []

    timeouts = data.get("timeouts", {})
    for key, value in timeouts.items():
        ensure_positive(value, f"timeouts.{key}", errors)
    if timeouts.get("max_request_ms", 0) < timeouts.get("default_request_ms", 0):
        errors.append("max_request_ms must be >= default_request_ms")

    retries = data.get("retries", {})
    for name, policy in retries.items():
        attempts = policy.get("max_attempts", 0)
        backoff = policy.get("backoff_ms", -1)
        if attempts < 1:
            errors.append(f"retries.{name}.max_attempts must be >= 1")
        if backoff < 0:
            errors.append(f"retries.{name}.backoff_ms cannot be negative")

    quorums = data.get("quorums", {})
    total_nodes = quorums.get("total_nodes", 0)
    ensure_positive(total_nodes, "quorums.total_nodes", errors)
    read_min = quorums.get("read_minimum", 0)
    write_min = quorums.get("write_minimum", 0)
    if read_min < 0 or write_min < 0:
        errors.append("quorums.read_minimum and write_minimum cannot be negative")
    if read_min + write_min <= total_nodes:
        warnings.append(
            "the sum of read/write quorums does not exceed total nodes; revisit consistency requirements"
        )

    circuit_breakers = data.get("circuit_breakers", {})
    threshold = circuit_breakers.get("error_rate_threshold", 0)
    if not 0 < threshold < 1:
        errors.append("error_rate_threshold must be within (0,1)")
    for key in ("rolling_window_s", "cooldown_s"):
        ensure_positive(circuit_breakers.get(key, 0), f"circuit_breakers.{key}", errors)

    ttl = data.get("ttl", {})
    for key, value in ttl.items():
        ensure_positive(value, f"ttl.{key}", errors)

    replication = data.get("replication", {})
    for name, details in replication.items():
        profiles = details.get("supported_profiles", [])
        if not profiles:
            warnings.append(f"replication.{name} does not declare supported_profiles")

    services = data.get("services", [])
    for service in services:
        label = service.get("name", "<unnamed>")
        timeout = service.get("timeouts_ms")
        if timeout is not None and timeout > timeouts.get(
            "max_request_ms", sys.maxsize
        ):
            warnings.append(
                f"{label}: timeouts_ms ({timeout}) exceeds global max_request_ms"
            )
        quorum = service.get("quorum")
        if quorum:
            read = quorum.get("read", 0)
            write = quorum.get("write", 0)
            if read > total_nodes or write > total_nodes:
                errors.append(
                    f"{label}: read/write quorums cannot exceed total_nodes ({total_nodes})"
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
