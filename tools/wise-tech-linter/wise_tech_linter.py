#!/usr/bin/env python3
"""Validator inicial para contratos de componentes.

Valida que `component-contract.yaml` exista y contenga los campos críticos
necesarios para las listas de verificación de resiliencia, desempeño y
observabilidad. La integración con CI quedará pendiente.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Any, Dict, Iterable, List

try:
    import yaml  # type: ignore
except ModuleNotFoundError as exc:  # pragma: no cover - se reporta en runtime
    raise SystemExit(
        "PyYAML es requerido para ejecutar wise-tech-linter. Instálelo con"
        " `pip install pyyaml`."
    ) from exc

REQUIRED_PATHS = {
    "version": str,
    "component.name": str,
    "component.description": str,
    "component.owner.team": str,
    "component.owner.slack_channel": str,
    "component.owner.escalation": str,
    "component.lifecycle.tier": str,
    "component.lifecycle.data_classification": str,
    "component.dependencies.runtime": list,
    "resilience.availability_slo": str,
    "resilience.failure_modes": list,
    "resilience.recovery_runbooks": list,
    "resilience.chaos_validation.frequency": str,
    "resilience.chaos_validation.scope": str,
    "resilience.fallbacks": list,
    "resilience.backup_and_restore.medium": str,
    "resilience.backup_and_restore.last_successful_test": str,
    "performance.latency_slo_ms": (int, float),
    "performance.error_budget_policy": str,
    "performance.load_profile.expected_qps": (int, float),
    "performance.capacity_plan.current_utilization": str,
    "performance.capacity_plan.scale_strategy": str,
    "performance.benchmark_evidence": list,
    "performance.regression_tests": list,
    "observability.metrics": list,
    "observability.logs.structured": bool,
    "observability.logs.retention_days": (int, float),
    "observability.traces.coverage": str,
    "observability.alerts": list,
    "observability.data_quality.validations": list,
    "observability.access_controls": str,
    "compliance.threat_model": str,
    "evidence.resilience_checklist": str,
    "evidence.performance_checklist": str,
    "evidence.observability_checklist": str,
    "evidence.last_reviewed": str,
}

MIN_LIST_REQUIREMENTS = {
    "component.dependencies.runtime": ("name", "owner", "contract"),
    "resilience.failure_modes": ("scenario", "impact", "mitigation"),
    "resilience.recovery_runbooks": ("name", "url"),
    "resilience.fallbacks": ("dependency", "strategy"),
    "performance.benchmark_evidence": ("name", "url"),
    "performance.regression_tests": ("name", "trigger"),
    "observability.metrics": ("name", "owner", "retention_days", "sli_relation"),
    "observability.alerts": ("name", "condition", "channel", "runbook"),
    "observability.data_quality.validations": ("name", "frequency"),
}


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
    for segment in dotted_path.split('.'):
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
        elif isinstance(value, (list, tuple)) and not value:
            errors.append(f"El campo `{dotted}` debe contener al menos un elemento")
    return errors


def validate_list_items(contract: Dict[str, Any]) -> List[str]:
    errors: List[str] = []
    for dotted, required_keys in MIN_LIST_REQUIREMENTS.items():
        value = get_nested(contract, dotted)
        if value is None:
            # La ausencia ya será reportada si aplica en REQUIRED_PATHS
            continue
        if not isinstance(value, Iterable):
            errors.append(f"`{dotted}` debe ser una lista de elementos con {required_keys}")
            continue
        for index, item in enumerate(value):
            if not isinstance(item, dict):
                errors.append(f"`{dotted}[{index}]` debe ser un objeto con campos {required_keys}")
                continue
            for key in required_keys:
                if key not in item or (isinstance(item[key], str) and not item[key].strip()):
                    errors.append(
                        f"`{dotted}[{index}].{key}` es obligatorio y debe tener contenido"
                    )
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

    if errors:
        print("Contrato inválido:\n- " + "\n- ".join(sorted(set(errors))), file=sys.stderr)
        return 2

    print(f"Contrato válido: {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
