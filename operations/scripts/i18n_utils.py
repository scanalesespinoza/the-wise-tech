"""Helpers for loading gettext translations."""

from __future__ import annotations

import gettext
import os
from pathlib import Path
from typing import Iterable

REPO_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_DOMAIN = "wise_tech"
DEFAULT_LOCALE_DIR = REPO_ROOT / "locales"
DEFAULT_LANGUAGE = "en"


def _language_candidates(language: str | None) -> list[str]:
    env_lang = os.getenv("WISE_TECH_LANG")
    candidates = [item for item in [language, env_lang, DEFAULT_LANGUAGE] if item]
    return list(dict.fromkeys(candidates))


def get_translator(
    language: str | None = None,
    *,
    domain: str = DEFAULT_DOMAIN,
    locale_dir: Path | str = DEFAULT_LOCALE_DIR,
    fallback: bool = True,
) -> gettext.NullTranslations:
    """Return a gettext translator for the requested language."""

    languages: Iterable[str] = _language_candidates(language)
    return gettext.translation(
        domain, localedir=str(locale_dir), languages=languages, fallback=fallback
    )
