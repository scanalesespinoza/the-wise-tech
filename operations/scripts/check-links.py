#!/usr/bin/env python3
"""Detect broken internal Markdown links after the repository restructuring."""

from __future__ import annotations

import re
import sys
from pathlib import Path

MD_LINK = re.compile(r"\[[^\]]+\]\((?P<url>[^\s)]+)\)")
REPO_ROOT = Path(__file__).resolve().parents[2]


def is_internal(path: str) -> bool:
    return not (
        path.startswith("http://")
        or path.startswith("https://")
        or path.startswith("#")
    )


def normalize(path: str, base: Path) -> Path | None:
    if path.startswith("#"):
        return None
    clean_path = path.split("#", 1)[0]
    if not clean_path:
        return None
    return (base / clean_path).resolve()


def check_markdown(md_path: Path) -> list[tuple[Path, str]]:
    errors: list[tuple[Path, str]] = []
    base = md_path.parent
    text = md_path.read_text(encoding="utf-8", errors="ignore")
    for match in MD_LINK.finditer(text):
        url = match.group("url")
        if not is_internal(url):
            continue
        target = normalize(url, base)
        if target is None:
            continue
        try:
            target.relative_to(REPO_ROOT)
        except ValueError:
            # Links pointing outside of the repository root are not supported.
            errors.append((md_path, url))
            continue
        if not target.exists():
            errors.append((md_path, url))
    return errors


def collect_markdown_files(root: Path) -> list[Path]:
    return [path for path in root.rglob("*.md") if path.is_file()]


def main() -> None:
    failures: list[tuple[Path, str]] = []
    for md_file in collect_markdown_files(REPO_ROOT):
        failures.extend(check_markdown(md_file))

    if failures:
        print("Broken internal links found:")
        for src, url in failures:
            print(f" - {src.relative_to(REPO_ROOT)} -> {url}")
        sys.exit(1)

    print("All internal markdown links OK.")


if __name__ == "__main__":
    main()
