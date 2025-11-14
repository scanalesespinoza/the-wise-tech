#!/usr/bin/env python3
"""Valida compatibilidad entre perfiles de consistencia, patrones de acceso y estrategias de réplica."""

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
        raise SystemExit(f"archivo no encontrado: {path}")
    except json.JSONDecodeError as exc:
        raise SystemExit(f"{path} no es JSON/YAML válido: {exc}")


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
        name = service.get("name", "<sin-nombre>")
        profile = service.get("profile")
        pattern = service.get("access_pattern")
        strategy = service.get("replica_strategy")

        if profile not in profiles:
            errors.append(f"{name}: perfil desconocido '{profile}'")
            continue
        if pattern not in patterns:
            errors.append(f"{name}: patrón de acceso desconocido '{pattern}'")
            continue
        if strategy not in replication_catalog:
            errors.append(f"{name}: estrategia de réplica desconocida '{strategy}'")
            continue

        allowed = patterns[pattern].get("allowed_profiles", [])
        if profile not in allowed:
            errors.append(
                f"{name}: perfil '{profile}' no permitido para patrón '{pattern}'"
            )

        compatible_strategies = profiles[profile].get("compatible_replication", [])
        if strategy not in compatible_strategies:
            errors.append(
                f"{name}: estrategia '{strategy}' incompatible con perfil '{profile}'"
            )

        supported_profiles = replication_catalog[strategy].get("supported_profiles", [])
        if supported_profiles and profile not in supported_profiles:
            errors.append(
                f"{name}: perfil '{profile}' no soportado por estrategia '{strategy}'"
            )

        requires_idempotency = replication_catalog[strategy].get("requires_idempotency")
        if requires_idempotency and pattern == "write_conflict":
            warnings.append(
                f"{name}: verificar claves de idempotencia para '{strategy}' en escenarios de conflicto"
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

    print("Consistencia OK: perfiles, patrones y estrategias compatibles.")
    return 0


if __name__ == "__main__":
    sys.exit(validate())
