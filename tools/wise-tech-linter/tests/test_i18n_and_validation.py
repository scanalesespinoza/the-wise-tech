from __future__ import annotations

import datetime as dt
import sys
from pathlib import Path

import pytest

LINTER_DIR = Path(__file__).resolve().parents[1]
if str(LINTER_DIR) not in sys.path:
    sys.path.insert(0, str(LINTER_DIR))

import i18n  # noqa: E402
import wise_tech_linter as linter  # noqa: E402


@pytest.fixture()
def translator() -> i18n.Translator:
    return i18n.Translator("es")


def test_translator_formats_pluralization_and_numbers(
    translator: i18n.Translator,
) -> None:
    message = translator.render("cli.invalid_contract", count=1500)
    expected = i18n.LANGUAGE_RESOURCES["cli.invalid_contract"]["es"]["other"].format(
        count=i18n.format_number(1500, language="es")
    )
    assert message == expected


def test_translator_supports_gender(translator: i18n.Translator) -> None:
    feminine_hint = translator.render("cli.contact_support", gender="feminine")
    neutral_hint = translator.render("cli.contact_support", gender="neutral")
    assert (
        feminine_hint
        == i18n.LANGUAGE_RESOURCES["cli.contact_support"]["es"]["feminine"]
    )
    assert (
        neutral_hint == i18n.LANGUAGE_RESOURCES["cli.contact_support"]["es"]["neutral"]
    )


def test_timestamp_respects_locale(translator: i18n.Translator) -> None:
    frozen_time = dt.datetime(2025, 5, 6, 14, 30)
    assert translator.timestamp(value=frozen_time) == "06/05/2025 14:30"


def test_required_paths_return_resource_keys() -> None:
    errors = linter.validate_required_paths({})
    assert errors
    assert all(isinstance(message, i18n.ResourceMessage) for message in errors)
    assert {message.key for message in errors}  # uses resource keys instead of literals


def test_custom_rules_use_resource_keys() -> None:
    errors = linter.validate_custom_rules({})
    keys = {message.key for message in errors}
    assert "errors.missing_states" in keys
    assert "errors.version_mismatch" in keys


def test_list_item_validation_uses_resource_keys() -> None:
    contract = {
        "resilience": {"cleanup_strategy": {"steps": "not-a-list"}},
        "observability": {},
        "zero_trust": {},
        "audit": {},
    }
    errors = linter.validate_list_items(contract)
    assert errors
    assert all(message.key == "errors.list_required" for message in errors)
