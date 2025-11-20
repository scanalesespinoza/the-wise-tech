#!/usr/bin/env python3
"""Generate a bilingual parity report for documentation trees."""

from __future__ import annotations

import argparse
import datetime as dt
import os
import re
from collections import Counter
from dataclasses import dataclass
from pathlib import Path

import yaml

from .i18n_utils import DEFAULT_DOMAIN, DEFAULT_LOCALE_DIR, get_translator

REPO_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_OUTPUT = REPO_ROOT / "audit" / "translation-status.md"
SKIPLIST_FILE = REPO_ROOT / "audit" / "translation-skiplist.yml"
DEFAULT_LANGUAGE = os.getenv("WISE_TECH_LANG", "en")

PARITY_MARKERS = (
    "todo (parity",  # i18n: ignore - file markers
    "todo(parity",  # i18n: ignore - file markers
    "todo parity",  # i18n: ignore - file markers
    "todo traducción",  # i18n: ignore - file markers
    "todo translation",  # i18n: ignore - file markers
)

_TRANSLATOR = get_translator(
    DEFAULT_LANGUAGE, domain=DEFAULT_DOMAIN, locale_dir=DEFAULT_LOCALE_DIR
)
_ = _TRANSLATOR.gettext

DESCRIPTION_FALLBACK = _("Generate a bilingual parity report for documentation trees.")


@dataclass
class DocStatus:
    scope: str
    relative_path: str
    status: str
    notes: str = ""


@dataclass
class ScopeReport:
    scope: str
    entries: list[DocStatus]

    @property
    def summary(self) -> Counter:
        counter: Counter[str] = Counter()
        for entry in self.entries:
            counter[entry.status] += 1
        return counter


def activate_language(language: str | None) -> None:
    """Update the active gettext translator."""

    global _TRANSLATOR, _
    _TRANSLATOR = get_translator(
        language, domain=DEFAULT_DOMAIN, locale_dir=DEFAULT_LOCALE_DIR
    )
    _ = _TRANSLATOR.gettext


def load_skiplist(path: Path) -> set[str]:
    if not path.exists():
        return set()
    data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    skip_paths = data.get("skip_paths", [])
    return {str(item) for item in skip_paths}


def collect_markdown(base: Path) -> dict[str, Path]:
    files: dict[str, Path] = {}
    for md_file in base.rglob("*.md"):
        if md_file.is_file():
            rel = md_file.relative_to(base).as_posix()
            files[rel] = md_file
    return files


def extract_heading_levels(markdown_text: str) -> list[int]:
    pattern = re.compile(r"^(#+)\s+", re.MULTILINE)
    return [len(match.group(1)) for match in pattern.finditer(markdown_text)]


def has_parity_marker(text: str) -> bool:
    lowered = text.lower()
    return any(marker in lowered for marker in PARITY_MARKERS)


def analyze_pair(
    scope_name: str,
    en_dir: Path,
    es_dir: Path,
    skiplist: set[str],
) -> ScopeReport:
    english_files = collect_markdown(en_dir)
    spanish_files = collect_markdown(es_dir)
    entries: list[DocStatus] = []
    for rel in sorted(set(english_files) | set(spanish_files)):
        en_path = english_files.get(rel)
        es_path = spanish_files.get(rel)
        repo_en = (en_path or (en_dir / rel)).relative_to(REPO_ROOT).as_posix()
        repo_es = (es_path or (es_dir / rel)).relative_to(REPO_ROOT).as_posix()
        if repo_en in skiplist or repo_es in skiplist:
            entries.append(DocStatus(scope_name, rel, "SKIP", _("Skip list")))
            continue
        if en_path is None:
            entries.append(
                DocStatus(scope_name, rel, "MISSING_EN", _("Only exists in ES tree"))
            )
            continue
        if es_path is None:
            entries.append(
                DocStatus(
                    scope_name, rel, "MISSING_ES", _("Create Spanish counterpart")
                )
            )
            continue

        es_text = es_path.read_text(encoding="utf-8")
        en_text = en_path.read_text(encoding="utf-8")
        if has_parity_marker(es_text):
            entries.append(
                DocStatus(
                    scope_name,
                    rel,
                    "OUTDATED_ES",
                    _("Contains pending translation marker"),
                )
            )
            continue

        en_structure = extract_heading_levels(en_text)
        es_structure = extract_heading_levels(es_text)
        if en_structure != es_structure:
            entries.append(
                DocStatus(
                    scope_name,
                    rel,
                    "OUTDATED_ES",
                    _("Heading structure mismatch"),
                )
            )
            continue

        entries.append(DocStatus(scope_name, rel, "OK", ""))
    return ScopeReport(scope_name, entries)


def generate_report(
    scopes: list[tuple[str, Path, Path]],
    skiplist: set[str],
) -> list[ScopeReport]:
    reports: list[ScopeReport] = []
    for scope, en_dir, es_dir in scopes:
        if not en_dir.exists() or not es_dir.exists():
            raise FileNotFoundError(
                _("Both directories must exist: %(en_dir)s vs %(es_dir)s")
                % {"en_dir": en_dir, "es_dir": es_dir}
            )
        reports.append(analyze_pair(scope, en_dir, es_dir, skiplist))
    return reports


def build_markdown(reports: list[ScopeReport]) -> str:
    date_format = _("%Y-%m-%d %H:%M UTC")
    generated_at = dt.datetime.now(dt.timezone.utc).strftime(date_format)
    lines = [
        _("# Translation status"),
        "",
        _("Generated: %(generated_at)s") % {"generated_at": generated_at},
        "",
        _("This file is auto-generated by `operations/scripts/translation_status.py`."),
        _(
            "Use `make -f operations/Makefile translate-status` to refresh it after editing docs."
        ),
        "",
        _("## Summary by scope"),
        "",
        _("| Scope | OK | Missing ES | Missing EN | Outdated ES | Skip | Total |"),
        "| --- | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for report in reports:
        summary = report.summary
        total = sum(summary.values())
        lines.append(
            f"| {report.scope} | {summary.get('OK', 0)} | {summary.get('MISSING_ES', 0)} | "
            f"{summary.get('MISSING_EN', 0)} | {summary.get('OUTDATED_ES', 0)} | "
            f"{summary.get('SKIP', 0)} | {total} |"
        )
    lines.append("")
    for report in reports:
        lines.append(f"## {report.scope}")
        lines.append("")
        lines.append(_("| File | Status | Notes |"))
        lines.append("| --- | --- | --- |")
        sorted_entries = sorted(
            report.entries,
            key=lambda entry: (
                {
                    "MISSING_ES": 0,
                    "OUTDATED_ES": 1,
                    "MISSING_EN": 2,
                    "OK": 3,
                    "SKIP": 4,
                }.get(entry.status, 5),
                entry.relative_path,
            ),
        )
        for entry in sorted_entries:
            note = entry.notes.replace("|", "\\|")
            lines.append(f"| {entry.relative_path} | {entry.status} | {note} |")
        lines.append("")
    return "\n".join(lines).strip() + "\n"


def parse_args() -> argparse.Namespace:
    description_text = _(__doc__) if __doc__ else DESCRIPTION_FALLBACK
    parser = argparse.ArgumentParser(description=description_text)
    parser.add_argument(
        "--output",
        default=str(DEFAULT_OUTPUT),
        help=_("Path to the markdown report that will be overwritten."),
    )
    parser.add_argument(
        "--skip-write",
        action="store_true",
        help=_("Print the report but do not update the markdown file."),
    )
    parser.add_argument(
        "--fail-on",
        nargs="*",
        default=[],
        help=_(
            "Statuses that should make the script exit with code 1 (e.g. MISSING_ES)."
        ),
    )
    parser.add_argument(
        "--lang",
        default=DEFAULT_LANGUAGE,
        help=_("Language code used to render the report (default: %(lang)s)")
        % {"lang": DEFAULT_LANGUAGE},
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    activate_language(args.lang)
    skiplist = load_skiplist(SKIPLIST_FILE)
    scopes = [
        (
            _("Knowledge base"),
            REPO_ROOT / "knowledge" / "docs" / "en",
            REPO_ROOT / "knowledge" / "docs" / "es",
        ),
        (
            _("Payments scenario"),
            REPO_ROOT / "experience" / "scenarios" / "payments" / "docs" / "en",
            REPO_ROOT / "experience" / "scenarios" / "payments" / "docs" / "es",
        ),
    ]
    reports = generate_report(scopes, skiplist)
    markdown = build_markdown(reports)
    if not args.skip_write:
        Path(args.output).write_text(markdown, encoding="utf-8")
    else:
        print(markdown)

    fail_statuses = {status.upper() for status in args.fail_on}
    if fail_statuses:
        for report in reports:
            for entry in report.entries:
                if entry.status in fail_statuses:
                    return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
