#!/usr/bin/env python3
"""Validate internal markdown links for translated docs."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

MD_LINK = re.compile(r"\[[^\]]+\]\((?P<url>[^\s)]+)\)")


def is_internal(url: str) -> bool:
    return not (
        url.startswith("http://")
        or url.startswith("https://")
        or url.startswith("#")
    )


def normalize(url: str, base: Path) -> Path | None:
    if url.startswith("#"):
        return None
    clean = url.split("#", 1)[0].strip()
    if not clean:
        return None
    return (base / clean).resolve()


def check_markdown(md_path: Path, repo_root: Path) -> list[str]:
    errors: list[str] = []
    text = md_path.read_text(encoding="utf-8", errors="ignore")
    base = md_path.parent

    for match in MD_LINK.finditer(text):
        url = match.group("url")
        if not is_internal(url):
            continue
        target = normalize(url, base)
        if target is None:
            continue
        try:
            target.relative_to(repo_root)
        except ValueError:
            errors.append(f"fuera del repo: {url}")
            continue
        if not target.exists():
            errors.append(f"rota: {url}")
    return errors


def collect_markdown_files(root: Path) -> list[Path]:
    return [path for path in root.rglob("*.md") if path.is_file()]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--root",
        type=Path,
        default=Path("docs"),
        help="Raíz donde buscar Markdown (default: docs)",
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Falla si encuentra cualquier enlace roto.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    repo_root = Path(__file__).resolve().parent.parent
    scan_root = (repo_root / args.root).resolve()

    failures: list[tuple[Path, list[str]]] = []
    for md_file in collect_markdown_files(scan_root):
        issues = check_markdown(md_file, repo_root)
        if issues:
            failures.append((md_file, issues))

    if failures:
        for path, issues in failures:
            for issue in issues:
                print(f"- {path.relative_to(repo_root)} -> {issue}")
        if args.strict:
            sys.exit(1)
        print("⚠️  Se encontraron enlaces rotos pero --strict no está activado.")
    else:
        print("Links internos OK.")


if __name__ == "__main__":
    main()
