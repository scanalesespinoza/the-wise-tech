#!/usr/bin/env python3
"""Validate relative Markdown links within the repository."""

from __future__ import annotations

import argparse
import re
import sys
import unicodedata
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Set, Tuple

MARKDOWN_PATTERN = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
HEADING_PATTERN = re.compile(r"^(#{1,6})\s+(.+)$")
IGNORED_PREFIXES = ("http://", "https://", "mailto:", "tel:", "{{", "{#")


def extract_links(markdown: str) -> Iterable[str]:
    for match in MARKDOWN_PATTERN.finditer(markdown):
        yield match.group(1)


def is_relative(link: str) -> bool:
    if link.startswith("#"):
        return False
    if link.startswith("/"):
        return True
    return not link.startswith(IGNORED_PREFIXES)


def slugify_anchor(text: str) -> str:
    normalized = unicodedata.normalize("NFKD", text)
    ascii_text = normalized.encode("ascii", "ignore").decode("ascii")
    sanitized = re.sub(r"[^a-z0-9\s-]", "", ascii_text.lower())
    collapsed = re.sub(r"[\s_-]+", "-", sanitized)
    return collapsed.strip("-")


def collect_anchors(text: str) -> Set[str]:
    anchors: Set[str] = set()
    for line in text.splitlines():
        match = HEADING_PATTERN.match(line.strip())
        if not match:
            continue
        slug = slugify_anchor(match.group(2))
        if slug:
            anchors.add(slug)
    return anchors


def get_anchors_for(path: Path, cache: Dict[Path, Set[str]]) -> Optional[Set[str]]:
    if path.suffix != ".md":
        return None
    if path in cache:
        return cache[path]
    if not path.exists():
        return None
    text = path.read_text(encoding="utf-8")
    anchors = collect_anchors(text)
    cache[path] = anchors
    return anchors


def validate_file(
    md_file: Path, anchor_cache: Dict[Path, Set[str]]
) -> List[Tuple[str, str]]:
    text = md_file.read_text(encoding="utf-8")
    errors: List[Tuple[str, str]] = []
    anchor_cache[md_file] = collect_anchors(text)
    for link in extract_links(text):
        if not is_relative(link):
            continue
        if link.startswith("/"):
            errors.append((link, "absolute paths are not allowed"))
            continue
        target, *_anchor = (link.split("#", 1) + [None])[:2]
        target_path = (md_file.parent / target).resolve()
        if not target_path.exists():
            errors.append((link, "target does not exist"))
            continue
        anchor = _anchor[0]
        if anchor:
            anchor_slug = slugify_anchor(anchor)
            if target:
                anchor_set = get_anchors_for(target_path, anchor_cache)
            else:
                anchor_set = anchor_cache.get(md_file)
            if anchor_set is not None and anchor_slug not in anchor_set:
                errors.append((link, "anchor not found"))
    return errors


def run(root: Path, strict: bool) -> int:
    markdown_files = sorted(root.rglob("*.md"))
    all_errors: List[Tuple[Path, str, str]] = []
    anchor_cache: Dict[Path, Set[str]] = {}
    for md_file in markdown_files:
        posix_path = md_file.as_posix()
        if ".git/" in posix_path:
            continue
        if "/archive/" in posix_path:
            continue
        for link, reason in validate_file(md_file, anchor_cache):
            all_errors.append((md_file, link, reason))
    if all_errors:
        for path, link, reason in all_errors:
            print(f"[ERROR] {path.relative_to(root)} → {link} ({reason})")
        return 1
    if strict:
        print("All Markdown links are valid.")
    return 0


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Print success message when no issues are found.",
    )
    parser.add_argument(
        "path",
        nargs="?",
        default=".",
        type=Path,
        help="Root path to scan (defaults to current directory).",
    )
    args = parser.parse_args()
    root = args.path.resolve()
    sys.exit(run(root, args.strict))


if __name__ == "__main__":
    main()
