#!/usr/bin/env python3
"""Validate front-matter and See also sections for translated docs."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from typing import Iterable

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
DOCS_ROOT = REPO_ROOT / "docs"
TARGETS = [DOCS_ROOT / "es", DOCS_ROOT / "index.md"]
FRONT_MATTER_PATTERN = re.compile(r"^---\n(.*?)\n---", re.DOTALL | re.MULTILINE)
EXCLUDED_PARTS = {"assets", "templates"}

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
        "docs",
        "i18n",
        "editorial",
        "taxonomy",
        "terminology",
        "security",
        "ci",
    },
}


def collect_markdown() -> Iterable[Path]:
    for target in TARGETS:
        if target.is_file():
            yield target
            continue
        if target.is_dir():
            yield from (
                path
                for path in target.rglob("*.md")
                if not any(part in EXCLUDED_PARTS for part in path.parts)
            )


def has_see_also(path: Path) -> bool:
    text = path.read_text(encoding="utf-8", errors="ignore").lower()
    return "## see also" in text or "## see-also" in text


def validate_file(path: Path) -> list[str]:
    errors: list[str] = []
    text = path.read_text(encoding="utf-8", errors="ignore")

    match = FRONT_MATTER_PATTERN.search(text)
    if not match:
        errors.append("missing front-matter")
        return errors

    try:
        metadata = yaml.safe_load(match.group(1)) or {}
    except Exception:
        errors.append("invalid front-matter yaml")
        return errors

    if not isinstance(metadata, dict):
        errors.append("front-matter must be a mapping")
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
    for md_file in collect_markdown():
        file_errors = validate_file(md_file)
        if file_errors:
            failures.append((md_file, file_errors))

    if failures:
        print("Metadata validation failed:")
        for path, file_errors in failures:
            for error in file_errors:
                print(f" - {path.relative_to(REPO_ROOT)}: {error}")
        sys.exit(1)

    print("Front-matter y 'See also' OK en docs.")


if __name__ == "__main__":
    main()
