#!/usr/bin/env python3
"""Detect English bleed-through and enforce glossary usage in Spanish docs."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

from spellchecker import SpellChecker

REPO_ROOT = Path(__file__).resolve().parent.parent
DOCS_ROOT = REPO_ROOT / "docs" / "es"
GLOSSARY_PATH = DOCS_ROOT / "guides" / "glosario-terminologia.md"

CODE_BLOCK_RE = re.compile(r"```.*?```", re.DOTALL)
INLINE_CODE_RE = re.compile(r"`[^`]+`")
LINK_RE = re.compile(r"!?\[[^\]]*\]\([^)]*\)")
WORD_RE = re.compile(r"[A-Za-zÁÉÍÓÚÜÑáéíóúüñ]+(?:'[A-Za-zÁÉÍÓÚÜÑáéíóúüñ]+)?")
FRONT_MATTER_RE = re.compile(r"^---.*?---", re.DOTALL)

TECH_ALLOWLIST = {
    "slo",
    "sli",
    "sla",
    "http",
    "https",
    "api",
    "apis",
    "yaml",
    "json",
    "ops",
    "cli",
    "mkdocs",
    "dev",
    "qa",
    "pr",
    "ci",
    "cd",
    "url",
    "urls",
    "frontend",
    "backend",
    "playbook",
    "playbooks",
    "retry",
    "backoff",
    "observability",
    "latency",
    "telemetry",
    "glosario",
    "i18n",
}

ENGLISH_ALLOWLIST = {
    "also",
    "see",
    "lab",
    "labs",
    "checklist",
    "logs",
    "python",
    "script",
    "variables",
    "batch",
    "batches",
    "build",
    "chars",
    "check",
    "content",
    "docs",
    "links",
    "make",
    "issue",
    "issues",
    "feedback",
    "roles",
    "platform",
    "engineers",
    "developers",
    "consumers",
    "personas",
    "describe",
    "budget",
    "control",
    "correlation",
    "endpoints",
    "exponential",
    "flags",
    "resume",
    "contributions",
    "key",
    "landing",
    "pages",
    "rae",
    "sea",
    "tag",
    "max",
    "quality",
    "root",
    "scripts",
    "spanish",
    "strict",
    "validate",
    "waves",
    "the",
    "wise",
    "claros",
    "evita",
}

SPANISH_STOPWORDS = {
    "de",
    "del",
    "en",
    "el",
    "la",
    "las",
    "los",
    "para",
    "como",
    "con",
    "este",
    "esta",
    "estas",
    "estos",
    "que",
    "porque",
    "donde",
    "cuando",
    "saber",
    "quien",
    "cual",
    "donde",
    "sin",
    "sobre",
    "por",
    "desde",
    "hasta",
    "entre",
    "segun",
    "tambien",
}


def load_glossary() -> dict[str, str]:
    mapping: dict[str, str] = {}
    if not GLOSSARY_PATH.exists():
        return mapping

    pattern = re.compile(
        r"\*\*(?P<source>[^*]+)\*\*\s*→\s*\*\*(?P<target>[^*]+)\*\*",
        re.IGNORECASE,
    )
    for line in GLOSSARY_PATH.read_text(encoding="utf-8", errors="ignore").splitlines():
        match = pattern.search(line)
        if match:
            source = match.group("source").strip().lower()
            target = match.group("target").strip()
            mapping[source] = target
    return mapping


def strip_markup(text: str) -> str:
    cleaned = FRONT_MATTER_RE.sub(" ", text, count=1)
    cleaned = CODE_BLOCK_RE.sub(" ", cleaned)
    cleaned = INLINE_CODE_RE.sub(" ", cleaned)
    cleaned = LINK_RE.sub(" ", cleaned)
    cleaned = re.sub(r"see also", " ", cleaned, flags=re.IGNORECASE)
    return cleaned


def extract_words(text: str) -> list[str]:
    return [match.group(0).lower() for match in WORD_RE.finditer(text)]


def build_allowlist(glossary: dict[str, str]) -> set[str]:
    allowlist = set(TECH_ALLOWLIST)
    allowlist.update(ENGLISH_ALLOWLIST)
    allowlist.update(glossary.keys())
    allowlist.update(target.lower() for target in glossary.values())
    return allowlist


def check_file(
    path: Path,
    english_spell: SpellChecker,
    spanish_spell: SpellChecker,
    glossary: dict[str, str],
    allowlist: set[str],
) -> tuple[list[str], list[str]]:
    text = path.read_text(encoding="utf-8", errors="ignore")
    cleaned = strip_markup(text)
    words = extract_words(cleaned)

    english_hits = sorted(
        {
            word
            for word in words
            if len(word) >= 3
            and word not in allowlist
            and word not in SPANISH_STOPWORDS
            and not spanish_spell.known([word])
            and word not in english_spell.unknown([word])
        }
    )
    glossary_issues: list[str] = []
    lowered = cleaned.lower()
    for source, target in glossary.items():
        if re.search(rf"\b{re.escape(source)}\b", lowered) and not re.search(
            rf"\b{re.escape(target.lower())}\b", lowered
        ):
            glossary_issues.append(
                f"'{source}' debe acompañarse de la traducción '{target}'"
            )

    return english_hits, glossary_issues


def collect_markdown_files(root: Path) -> list[Path]:
    if not root.exists():
        return []
    return [path for path in root.rglob("*.md") if path.is_file()]


def run_checks() -> int:
    glossary = load_glossary()
    allowlist = build_allowlist(glossary)
    english_spell = SpellChecker(language="en")
    spanish_spell = SpellChecker(language="es")

    spelling_failures: list[tuple[Path, list[str]]] = []
    glossary_failures: list[tuple[Path, list[str]]] = []

    for md_file in collect_markdown_files(DOCS_ROOT):
        english_hits, glossary_issues = check_file(
            md_file, english_spell, spanish_spell, glossary, allowlist
        )
        if english_hits:
            spelling_failures.append((md_file, english_hits))
        if glossary_issues:
            glossary_failures.append((md_file, glossary_issues))

    exit_code = 0
    if spelling_failures:
        exit_code = 1
        print("Palabras en inglés detectadas:")
        for path, words in spelling_failures:
            preview = ", ".join(words[:10])
            remainder = "" if len(words) <= 10 else f" (+{len(words) - 10} más)"
            print(f" - {path.relative_to(REPO_ROOT)}: {preview}{remainder}")

    if glossary_failures:
        exit_code = 1
        print("Incumplimientos del glosario detectados:")
        for path, issues in glossary_failures:
            for issue in issues:
                print(f" - {path.relative_to(REPO_ROOT)}: {issue}")

    if exit_code == 0:
        print("Ortografía básica, ausencia de inglés y glosario OK en docs/es.")
    return exit_code


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.parse_args()
    sys.exit(run_checks())


if __name__ == "__main__":
    main()
