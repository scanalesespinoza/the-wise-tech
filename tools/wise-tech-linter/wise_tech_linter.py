"""Validator inicial para contratos de componentes.

Valida que `component-contract.yaml` exista y cumpla el esquema 1.1.0
alineado a los pilares PCC.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Any, Dict, Iterable, List

try:
    import yaml  # type: ignore
except ModuleNotFoundError as exc:  # pragma: no cover
    raise SystemExit(
        "PyYAML es requerido para ejecutar wise-tech-linter. Instálelo con `pip install pyyaml`."
    ) from exc

REQUIRED_PATHS: dict[str, type | tuple[type, ...]] = {
    "version": str,
    "component.name": str,
    "component.domain": str,
    "component.description": str,
    "ownership.team": str,
    "ownership.service_slack": str,
    "ownership.escalation": str,
    "runtime.tier": str,
    "runtime.language": str,
    "runtime.deployment": str,
    "resilience.error_handling_strategy.expected_errors": list,
    "resilience.error_handling_strategy.boundary_cases": list,
    "resilience.error_handling_strategy.detection_channels": list,
    "resilience.cleanup_strategy.steps": list,
    "resilience.states_implemented": list,
    "resilience.recovery.fallback_paths": list,
    "resilience.recovery.degraded_mode_playbook": str,
    "performance.max_threads": (int, float),
    "performance.max_requests_per_second": (int, float),
    "performance.max_clients_per_minute": (int, float),
    "performance.resource_budgets.cpu_percent": (int, float),
    "performance.resource_budgets.memory_percent": (int, float),
    "performance.overflow_strategy": str,
    "performance.overflow_messaging.code": str,
    "performance.overflow_messaging.business_message": str,
    "observability.metrics_exposed": list,
    "observability.events_emitted": list,
    "observability.overload_signal.channel": str,
    "observability.overload_signal.description": str,
    "observability.degradation_signal.channel": str,
    "observability.degradation_signal.description": str,
    "zero_trust.input_validation": list,
    "zero_trust.dependency_assumptions": list,
    "audit.last_review": str,
    "audit.reviewers": list,
}

MIN_LIST_REQUIREMENTS: dict[str, tuple[str, ...]] = {
    "resilience.cleanup_strategy.steps": ("description", "automation"),
    "resilience.recovery.fallback_paths": ("name", "trigger", "impact"),
    "observability.metrics_exposed": ("name", "type", "description"),
    "observability.events_emitted": ("name", "when", "payload_contract"),
    "zero_trust.input_validation": ("interface", "rules"),
    "zero_trust.dependency_assumptions": ("dependency", "verification"),
    "audit.reviewers": ("name",),
}

ALLOWED_OVERFLOW_STRATEGIES = {"queue", "reject", "throttle"}
MANDATORY_STATES = {"in-service", "degraded", "out-of-service-controlled"}


def load_contract(path: Path) -> Dict[str, Any]:
    if not path.exists():
        raise FileNotFoundError(f"No se encontró el archivo de contrato: {path}")
    with path.open("r", encoding="utf-8") as fh:
        data = yaml.safe_load(fh) or {}
        if not isinstance(data, dict):
            raise ValueError("El contrato debe ser un objeto YAML de nivel superior")
        return data


def get_nested(data: Dict[str, Any], dotted_path: str) -> Any:
    node: Any = data
    for segment in dotted_path.split("."):
        if not isinstance(node, dict) or segment not in node:
            return None
        node = node[segment]
    return node


def validate_required_paths(contract: Dict[str, Any]) -> List[str]:
    errors: List[str] = []
    for dotted, expected_type in REQUIRED_PATHS.items():
        value = get_nested(contract, dotted)
        if value is None:
            errors.append(f"Falta el campo obligatorio `{dotted}`")
            continue
        if not isinstance(value, expected_type):
            errors.append(
                f"El campo `{dotted}` debe ser de tipo {expected_type} (valor actual: {type(value).__name__})"
            )
        elif isinstance(value, str) and not value.strip():
            errors.append(f"El campo `{dotted}` no puede estar vacío")
        elif isinstance(value, list) and not value:
            errors.append(f"El campo `{dotted}` debe contener al menos un elemento")
    return errors


def validate_list_items(contract: Dict[str, Any]) -> List[str]:
    errors: List[str] = []
    for dotted, required_keys in MIN_LIST_REQUIREMENTS.items():
        value = get_nested(contract, dotted)
        if value is None:
            continue
        if not isinstance(value, list):
            errors.append(f"`{dotted}` debe ser una lista")
            continue
        for index, item in enumerate(value):
            if not isinstance(item, dict):
                errors.append(
                    f"`{dotted}[{index}]` debe ser un objeto con campos {required_keys}"
                )
                continue
            for key in required_keys:
                field = item.get(key)
                if field is None or (isinstance(field, str) and not field.strip()):
                    errors.append(
                        f"`{dotted}[{index}].{key}` es obligatorio y debe tener contenido"
                    )
    return errors


def validate_custom_rules(contract: Dict[str, Any]) -> List[str]:
    errors: List[str] = []

    states = set(get_nested(contract, "resilience.states_implemented") or [])
    missing_states = MANDATORY_STATES - states
    if missing_states:
        errors.append(
            "`resilience.states_implemented` debe incluir: "
            + ", ".join(sorted(MANDATORY_STATES))
        )

    strategy = get_nested(contract, "performance.overflow_strategy")
    if isinstance(strategy, str) and strategy not in ALLOWED_OVERFLOW_STRATEGIES:
        errors.append(
            f"`performance.overflow_strategy` debe ser uno de {sorted(ALLOWED_OVERFLOW_STRATEGIES)}"
        )

    version = contract.get("version")
    if version not in {"1.1.0"}:
        errors.append("`version` debe ser '1.1.0' para esta iteración")

    return errors


def parse_args(argv: Iterable[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Valida contratos de componentes")
    parser.add_argument(
        "path",
        nargs="?",
        default="audit/component-contract.yaml",
        help="Ruta al archivo component-contract.yaml (por defecto: audit/component-contract.yaml)",
    )
    return parser.parse_args(list(argv))


def main(argv: Iterable[str] | None = None) -> int:
    args = parse_args(argv or sys.argv[1:])
    path = Path(args.path)
    try:
        contract = load_contract(path)
    except (FileNotFoundError, ValueError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1

    errors = validate_required_paths(contract)
    errors.extend(validate_list_items(contract))
    errors.extend(validate_custom_rules(contract))

    if errors:
        print(
            "Contrato inválido:\n- " + "\n- ".join(sorted(set(errors))), file=sys.stderr
        )
        return 2

    print(f"Contrato válido: {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
