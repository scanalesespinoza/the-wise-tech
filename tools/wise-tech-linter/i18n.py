"""Lightweight translation helpers for the wise-tech linter UI."""

from __future__ import annotations

import datetime as dt
from dataclasses import dataclass
from typing import Any

DEFAULT_LANGUAGE = "es"


@dataclass(frozen=True)
class ResourceMessage:
    """Represents a translatable message with optional parameters."""

    key: str
    params: dict[str, Any] | None = None

    def resolve_params(self) -> dict[str, Any]:
        return self.params or {}


LANGUAGE_RESOURCES: dict[str, dict[str, Any]] = {
    "cli.description": {
        "en": "Validate component contracts against the PCC-ready schema.",
        "es": "Valida contratos de componentes contra el esquema alineado a PCC.",
    },
    "cli.valid_contract": {
        "en": "Valid contract: {path} (checked on {timestamp})",
        "es": "Contrato válido: {path} (verificado el {timestamp})",
    },
    "cli.path_help": {
        "en": "Path to component-contract.yaml (default: {default_path})",
        "es": "Ruta al archivo component-contract.yaml (por defecto: {default_path})",
    },
    "cli.lang_help": {
        "en": "ISO language code used to render messages (default: {lang})",
        "es": "Código de idioma ISO para mostrar mensajes (por defecto: {lang})",
    },
    "cli.invalid_contract": {
        "en": {
            "one": "1 validation issue found",
            "other": "{count} validation issues found",
        },
        "es": {
            "one": "1 incidencia de validación encontrada",
            "other": "{count} incidencias de validación encontradas",
        },
    },
    "cli.contact_support": {
        "en": {
            "masculine": "Ask the support agent to follow the remediation runbook.",
            "feminine": "Ask the support agent to follow the remediation runbook.",
            "neutral": "Ask the support agent to follow the remediation runbook.",
        },
        "es": {
            "masculine": "Pide al agente de soporte que siga el runbook de remediación.",
            "feminine": "Pide a la agente de soporte que siga el runbook de remediación.",
            "neutral": "Pide a la persona de soporte que siga el runbook de remediación.",
        },
    },
    "errors.file_not_found": {
        "en": "Contract file not found: {path}",
        "es": "No se encontró el archivo de contrato: {path}",
    },
    "errors.contract_not_mapping": {
        "en": "The contract must be a YAML mapping at the top level.",
        "es": "El contrato debe ser un objeto YAML de nivel superior.",
    },
    "errors.missing_field": {
        "en": "Missing required field `{field}`",
        "es": "Falta el campo obligatorio `{field}`",
    },
    "errors.type_mismatch": {
        "en": "Field `{field}` must be of type {expected} (current: {observed})",
        "es": "El campo `{field}` debe ser de tipo {expected} (valor actual: {observed})",
    },
    "errors.empty_field": {
        "en": "Field `{field}` cannot be empty",
        "es": "El campo `{field}` no puede estar vacío",
    },
    "errors.list_required": {
        "en": "`{field}` must be a list",
        "es": "`{field}` debe ser una lista",
    },
    "errors.list_item_missing": {
        "en": "`{field}[{index}]` must include {required}",
        "es": "`{field}[{index}]` debe incluir {required}",
    },
    "errors.invalid_strategy": {
        "en": "`performance.overflow_strategy` must be one of {options}",
        "es": "`performance.overflow_strategy` debe ser uno de {options}",
    },
    "errors.missing_states": {
        "en": "`resilience.states_implemented` must include: {states}",
        "es": "`resilience.states_implemented` debe incluir: {states}",
    },
    "errors.version_mismatch": {
        "en": "`version` must be '1.1.0' for this iteration",
        "es": "`version` debe ser '1.1.0' para esta iteración",
    },
    "format.validation_header": {
        "en": "Invalid contract",
        "es": "Contrato inválido",
    },
}


def _normalize_language(language: str | None) -> str:
    return (language or DEFAULT_LANGUAGE).split("-")[0].lower()


def _select_variant(entry: Any, *, count: int | None, gender: str | None) -> str:
    if isinstance(entry, dict):
        if gender and gender in entry:
            return _select_variant(entry[gender], count=count, gender=None)
        if count is not None:
            if count == 1 and "one" in entry:
                return entry["one"]
            if "other" in entry:
                return entry["other"]
        for fallback_key in ("neutral", "other"):
            if fallback_key in entry:
                return entry[fallback_key]
        return next(iter(entry.values()))
    return str(entry)


def format_number(value: float | int, *, language: str | None = None) -> str:
    lang = _normalize_language(language)
    if lang == "es":
        return format(value, ",").replace(",", ".")
    return format(value, ",")


def format_datetime(value: dt.datetime, *, language: str | None = None) -> str:
    lang = _normalize_language(language)
    if lang == "es":
        return value.strftime("%d/%m/%Y %H:%M")
    return value.strftime("%Y-%m-%d %H:%M")


class Translator:
    """Resolve resource keys into localized strings."""

    def __init__(self, language: str | None = None) -> None:
        self.language = _normalize_language(language)

    def render(
        self,
        key: str,
        *,
        count: int | None = None,
        gender: str | None = None,
        **params: Any,
    ) -> str:
        entry = LANGUAGE_RESOURCES.get(
            key, LANGUAGE_RESOURCES.get("cli.description", {})
        )
        template = (
            entry.get(self.language) or entry.get(DEFAULT_LANGUAGE) or entry.get("en")
        )
        resolved = _select_variant(template, count=count, gender=gender)
        substitutions = {
            **params,
            "count": format_number(
                count if count is not None else 0, language=self.language
            ),
        }
        return resolved.format(**substitutions)

    def render_message(
        self,
        message: ResourceMessage,
        *,
        count: int | None = None,
        gender: str | None = None,
    ) -> str:
        merged = {**message.resolve_params()}
        if count is not None:
            merged.setdefault("count", count)
        return self.render(message.key, count=count, gender=gender, **merged)

    def timestamp(self, *, value: dt.datetime | None = None) -> str:
        return format_datetime(value or dt.datetime.now(), language=self.language)
