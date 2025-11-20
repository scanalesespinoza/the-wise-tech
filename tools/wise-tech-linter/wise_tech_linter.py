"""Validator inicial para contratos de componentes.

Valida que `component-contract.yaml` exista y cumpla el esquema 1.1.0
alineado a los pilares PCC.
"""

from __future__ import annotations

import argparse
import os
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, Iterable, List

import yaml  # type: ignore

from i18n import (
    DEFAULT_LANGUAGE as I18N_DEFAULT_LANGUAGE,
    ResourceMessage,
    Translator,
)

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

DEFAULT_LANGUAGE = os.getenv("WISE_TECH_LANG", I18N_DEFAULT_LANGUAGE)
DEFAULT_CONTRACT_PATH = "audit/component-contract.yaml"


@dataclass(frozen=True)
class LocalizedError(Exception):
    """Carries a message key for user-facing errors."""

    message: ResourceMessage


def _format_expected_type(expected_type: type | tuple[type, ...]) -> str:
    if isinstance(expected_type, tuple):
        return ", ".join(sorted(type_item.__name__ for type_item in expected_type))
    return (
        expected_type.__name__
        if isinstance(expected_type, type)
        else str(expected_type)
    )


def load_contract(path: Path) -> Dict[str, Any]:
    if not path.exists():
        raise LocalizedError(
            ResourceMessage("errors.file_not_found", {"path": str(path)})
        )
    with path.open("r", encoding="utf-8") as fh:
        data = yaml.safe_load(fh) or {}
        if not isinstance(data, dict):
            raise LocalizedError(ResourceMessage("errors.contract_not_mapping"))
        return data


def get_nested(data: Dict[str, Any], dotted_path: str) -> Any:
    node: Any = data
    for segment in dotted_path.split("."):
        if not isinstance(node, dict) or segment not in node:
            return None
        node = node[segment]
    return node


def validate_required_paths(contract: Dict[str, Any]) -> List[ResourceMessage]:
    errors: List[ResourceMessage] = []
    for dotted, expected_type in REQUIRED_PATHS.items():
        value = get_nested(contract, dotted)
        if value is None:
            errors.append(ResourceMessage("errors.missing_field", {"field": dotted}))
            continue
        if not isinstance(value, expected_type):
            errors.append(
                ResourceMessage(
                    "errors.type_mismatch",
                    {
                        "field": dotted,
                        "expected": _format_expected_type(expected_type),
                        "observed": type(value).__name__,
                    },
                )
            )
        elif isinstance(value, str) and not value.strip():
            errors.append(ResourceMessage("errors.empty_field", {"field": dotted}))
        elif isinstance(value, list) and not value:
            errors.append(ResourceMessage("errors.empty_field", {"field": dotted}))
    return errors


def validate_list_items(contract: Dict[str, Any]) -> List[ResourceMessage]:
    errors: List[ResourceMessage] = []
    for dotted, required_keys in MIN_LIST_REQUIREMENTS.items():
        value = get_nested(contract, dotted)
        if value is None:
            continue
        if not isinstance(value, list):
            errors.append(ResourceMessage("errors.list_required", {"field": dotted}))
            continue
        required_description = ", ".join(required_keys)
        for index, item in enumerate(value):
            if not isinstance(item, dict):
                errors.append(
                    ResourceMessage(
                        "errors.list_item_missing",
                        {
                            "field": dotted,
                            "index": index,
                            "required": required_description,
                        },
                    )
                )
                continue
            for key in required_keys:
                field = item.get(key)
                if field is None or (isinstance(field, str) and not field.strip()):
                    errors.append(
                        ResourceMessage(
                            "errors.list_item_missing",
                            {
                                "field": dotted,
                                "index": index,
                                "required": f"{key}",
                            },
                        )
                    )
    return errors


def validate_custom_rules(contract: Dict[str, Any]) -> List[ResourceMessage]:
    errors: List[ResourceMessage] = []

    states = set(get_nested(contract, "resilience.states_implemented") or [])
    missing_states = MANDATORY_STATES - states
    if missing_states:
        errors.append(
            ResourceMessage(
                "errors.missing_states", {"states": ", ".join(sorted(MANDATORY_STATES))}
            )
        )

    strategy = get_nested(contract, "performance.overflow_strategy")
    if isinstance(strategy, str) and strategy not in ALLOWED_OVERFLOW_STRATEGIES:
        errors.append(
            ResourceMessage(
                "errors.invalid_strategy",
                {"options": ", ".join(sorted(ALLOWED_OVERFLOW_STRATEGIES))},
            )
        )

    version = contract.get("version")
    if version not in {"1.1.0"}:
        errors.append(ResourceMessage("errors.version_mismatch"))

    return errors


def parse_args(argv: Iterable[str]) -> argparse.Namespace:
    translator = Translator(DEFAULT_LANGUAGE)
    parser = argparse.ArgumentParser(description=translator.render("cli.description"))
    parser.add_argument(
        "path",
        nargs="?",
        default=DEFAULT_CONTRACT_PATH,
        help=translator.render(
            "cli.path_help", {"default_path": DEFAULT_CONTRACT_PATH}
        ),
    )
    parser.add_argument(
        "--lang",
        default=DEFAULT_LANGUAGE,
        help=translator.render("cli.lang_help", {"lang": DEFAULT_LANGUAGE}),
    )
    return parser.parse_args(list(argv))


def main(argv: Iterable[str] | None = None) -> int:
    args = parse_args(argv or sys.argv[1:])
    translator = Translator(args.lang)
    path = Path(args.path)
    try:
        contract = load_contract(path)
    except LocalizedError as exc:
        print(translator.render_message(exc.message), file=sys.stderr)
        return 1

    errors = validate_required_paths(contract)
    errors.extend(validate_list_items(contract))
    errors.extend(validate_custom_rules(contract))

    if errors:
        header = translator.render("format.validation_header")
        issues = [
            translator.render_message(message)
            for message in sorted(errors, key=lambda msg: (msg.key, str(msg.params)))
        ]
        summary = translator.render("cli.invalid_contract", count=len(errors))
        support_hint = translator.render("cli.contact_support", gender="neutral")
        body = "\n- ".join(issues)
        print(f"{header}: {summary}\n- {body}\n{support_hint}", file=sys.stderr)
        return 2

    timestamp = translator.timestamp()
    print(translator.render("cli.valid_contract", path=path, timestamp=timestamp))
    return 0


if __name__ == "__main__":
    sys.exit(main())
