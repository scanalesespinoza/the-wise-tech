#!/usr/bin/env python3
"""Validate compatibility between consistency profiles, access patterns, and replica strategies."""

from __future__ import annotations

import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
CONSISTENCY_PATH = ROOT / "platform" / "policies" / "consistency.yml"
RESILIENCE_PATH = ROOT / "platform" / "policies" / "resilience.yml"


def load_json(path: Path) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        raise SystemExit(f"file not found: {path}")
    except json.JSONDecodeError as exc:
        raise SystemExit(f"{path} is not valid JSON/YAML: {exc}")


def validate() -> int:
    data = load_json(CONSISTENCY_PATH)
    resilience = load_json(RESILIENCE_PATH)

    profiles = data.get("profiles", {})
    patterns = data.get("access_patterns", {})
    replication_catalog = {
        key: value for key, value in resilience.get("replication", {}).items()
    }

    errors = []
    warnings = []

    for service in data.get("services", []):
        name = service.get("name", "<unnamed>")
        profile = service.get("profile")
        pattern = service.get("access_pattern")
        strategy = service.get("replica_strategy")

        if profile not in profiles:
            errors.append(f"{name}: unknown profile '{profile}'")
            continue
        if pattern not in patterns:
            errors.append(f"{name}: unknown access pattern '{pattern}'")
            continue
        if strategy not in replication_catalog:
            errors.append(f"{name}: unknown replica strategy '{strategy}'")
            continue

        allowed = patterns[pattern].get("allowed_profiles", [])
        if profile not in allowed:
            errors.append(
                f"{name}: profile '{profile}' is not allowed for pattern '{pattern}'"
            )

        compatible_strategies = profiles[profile].get("compatible_replication", [])
        if strategy not in compatible_strategies:
            errors.append(
                f"{name}: strategy '{strategy}' is incompatible with profile '{profile}'"
            )

        supported_profiles = replication_catalog[strategy].get("supported_profiles", [])
        if supported_profiles and profile not in supported_profiles:
            errors.append(
                f"{name}: profile '{profile}' is not supported by strategy '{strategy}'"
            )

        requires_idempotency = replication_catalog[strategy].get("requires_idempotency")
        if requires_idempotency and pattern == "write_conflict":
            warnings.append(
                f"{name}: verify idempotency keys for '{strategy}' when handling conflict scenarios"
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

    print("Consistency OK: profiles, patterns, and strategies are compatible.")
    return 0


if __name__ == "__main__":
    sys.exit(validate())
