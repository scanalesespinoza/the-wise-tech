#!/usr/bin/env python3
"""Validate front-matter metadata and See also sections in Markdown docs."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from typing import Iterable

import yaml

ROOT = Path(__file__).resolve().parents[2]
DOC_PREFIX = ("knowledge", "docs")
MONITORED_SECTIONS = {
    "guides",
    "playbooks",
    "principles",
    "paths",
    "scenarios",
    "roadmap",
    "snippets",
}
FRONT_MATTER_PATTERN = re.compile(r"^---\n(.*?)\n---", re.DOTALL | re.MULTILINE)
ALLOWED_TAGS = {
    "roles": {"consumers", "developers", "platform-engineers"},
    "topics": {
        "simplicity",
        "resilience",
        "knowledge-capitalization",
        "human-connection",
        "aDevelopment",
        "observability",
        "slo",
        "playbooks",
        "paths",
        "labs",
        "quickstart",
        "principles",
    },
}
EXCLUDED_PARTS = {"assets", "templates"}


def find_markdown_files() -> Iterable[Path]:
    for path in ROOT.rglob("*.md"):
        try:
            relative = path.relative_to(ROOT)
        except ValueError:
            continue
        if len(relative.parts) < len(DOC_PREFIX) + 1:
            continue
        if tuple(relative.parts[: len(DOC_PREFIX)]) != DOC_PREFIX:
            continue
        section = relative.parts[len(DOC_PREFIX)]
        if section not in MONITORED_SECTIONS:
            continue
        if any(part in EXCLUDED_PARTS for part in relative.parts):
            continue
        yield path


def has_see_also(path: Path) -> bool:
    text = path.read_text(encoding="utf-8", errors="ignore").lower()
    return "## see also" in text or "## see-also" in text


def validate_file(path: Path) -> list[str]:
    errors: list[str] = []
    text = path.read_text(encoding="utf-8", errors="ignore")

    if path.name == "index.md" or path.name == "_index.md":
        return errors

    match = FRONT_MATTER_PATTERN.search(text)
    if not match:
        errors.append("missing front-matter")
        return errors

    try:
        metadata = yaml.safe_load(match.group(1)) or {}
    except Exception:
        errors.append("invalid front-matter yaml")
        return errors

    tags = metadata.get("tags")
    if not isinstance(tags, list) or not tags:
        errors.append("missing tags")
        return errors

    tag_set = {str(tag) for tag in tags}
    allowed_roles = tag_set & ALLOWED_TAGS["roles"]
    allowed_topics = tag_set & ALLOWED_TAGS["topics"]
    if not (allowed_roles or allowed_topics):
        errors.append("tags must include at least one role or topic from allow-list")

    if not has_see_also(path):
        errors.append("missing 'See also' section")

    return errors


def main() -> None:
    failures: list[tuple[Path, list[str]]] = []
    for markdown_file in find_markdown_files():
        file_errors = validate_file(markdown_file)
        if file_errors:
            failures.append((markdown_file, file_errors))

    if failures:
        print("Content metadata validation failed:")
        for path, error_list in failures:
            for error in error_list:
                print(f" - {path}: {error}")
        sys.exit(1)

    print("Content metadata validation OK.")


if __name__ == "__main__":
    main()
