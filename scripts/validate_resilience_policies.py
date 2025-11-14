#!/usr/bin/env python3
"""Validate the structure and contents of the resilience policies catalogue."""

from __future__ import annotations

import sys
from pathlib import Path

try:
    import yaml
except ModuleNotFoundError as exc:  # pragma: no cover - handled via CI dependency
    raise SystemExit(
        "PyYAML is required to validate resilience policies. Install it with 'pip install pyyaml'."
    ) from exc


ALLOWED_TIERS = {"critical", "important", "standard"}
ALLOWED_BACKOFFS = {"exponential", "linear", "jitter"}


class ValidationError(Exception):
    """Raised when the policies file violates an expected constraint."""


def _require(condition: bool, message: str) -> None:
    if not condition:
        raise ValidationError(message)


def load_policies(policies_path: Path) -> dict:
    _require(policies_path.exists(), f"Policies file not found: {policies_path}")
    data = yaml.safe_load(policies_path.read_text(encoding="utf-8"))
    _require(
        isinstance(data, dict), "Policies file must define a mapping at the root level"
    )
    return data


def validate_dependency(service: str, name: str, spec: dict) -> None:
    prefix = f"services.{service}.dependencies.{name}"
    _require(isinstance(spec, dict), f"{prefix} must be a mapping")

    tier = spec.get("tier")
    _require(
        tier in ALLOWED_TIERS,
        f"{prefix}.tier must be one of {sorted(ALLOWED_TIERS)} (got {tier!r})",
    )

    timeout = spec.get("timeout_ms")
    _require(
        isinstance(timeout, int) and timeout > 0,
        f"{prefix}.timeout_ms must be a positive integer",
    )

    retry = spec.get("retry")
    _require(isinstance(retry, dict), f"{prefix}.retry must be a mapping")
    attempts = retry.get("attempts")
    _require(
        isinstance(attempts, int) and attempts >= 0,
        f"{prefix}.retry.attempts must be a non-negative integer",
    )
    backoff = retry.get("backoff")
    _require(
        backoff in ALLOWED_BACKOFFS,
        f"{prefix}.retry.backoff must be one of {sorted(ALLOWED_BACKOFFS)} (got {backoff!r})",
    )
    base_delay = retry.get("base_delay_ms")
    _require(
        isinstance(base_delay, int) and base_delay >= 0,
        f"{prefix}.retry.base_delay_ms must be a non-negative integer",
    )

    circuit_breaker = spec.get("circuit_breaker")
    _require(
        isinstance(circuit_breaker, dict), f"{prefix}.circuit_breaker must be a mapping"
    )
    failure_threshold = circuit_breaker.get("failure_threshold")
    _require(
        isinstance(failure_threshold, int) and failure_threshold > 0,
        f"{prefix}.circuit_breaker.failure_threshold must be a positive integer",
    )
    recovery_seconds = circuit_breaker.get("recovery_seconds")
    _require(
        isinstance(recovery_seconds, int) and recovery_seconds > 0,
        f"{prefix}.circuit_breaker.recovery_seconds must be a positive integer",
    )

    fallback = spec.get("fallback")
    _require(isinstance(fallback, dict), f"{prefix}.fallback must be a mapping")
    strategy_en = fallback.get("strategy_en")
    strategy_es = fallback.get("strategy_es")
    _require(
        isinstance(strategy_en, str) and strategy_en.strip(),
        f"{prefix}.fallback.strategy_en must be a non-empty string",
    )
    _require(
        isinstance(strategy_es, str) and strategy_es.strip(),
        f"{prefix}.fallback.strategy_es must be a non-empty string",
    )


def validate_policies(data: dict) -> None:
    services = data.get("services")
    _require(
        isinstance(services, dict) and services,
        "Policies must define at least one service",
    )

    for service_name, service_spec in services.items():
        service_prefix = f"services.{service_name}"
        _require(isinstance(service_spec, dict), f"{service_prefix} must be a mapping")
        dependencies = service_spec.get("dependencies")
        _require(
            isinstance(dependencies, dict) and dependencies,
            f"{service_prefix}.dependencies must define at least one dependency",
        )
        for dependency_name, dependency_spec in dependencies.items():
            validate_dependency(service_name, dependency_name, dependency_spec)


def main() -> int:
    repo_root = Path(__file__).resolve().parents[1]
    policies_path = repo_root / "infra" / "resilience" / "policies.yml"

    try:
        policies = load_policies(policies_path)
        validate_policies(policies)
    except ValidationError as exc:
        print(f"Validation failed: {exc}")
        return 1
    else:
        print("Resilience policies look good ✅")
        return 0


if __name__ == "__main__":
    sys.exit(main())
