#!/usr/bin/env python3
"""Insert metadata comments into Markdown files lacking explicit context."""

from __future__ import annotations

import subprocess
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
TARGET_DIRS = [
    REPO_ROOT / "knowledge",
    REPO_ROOT / "implementation",
    REPO_ROOT / "experience",
]


def iter_markdown_files() -> list[Path]:
    files: list[Path] = []
    for directory in TARGET_DIRS:
        if not directory.exists():
            continue
        files.extend(sorted(directory.rglob("*.md")))
    return files


def last_modified_days(path: Path) -> int:
    result = subprocess.run(
        ["git", "log", "-1", "--format=%ct", "--", str(path.relative_to(REPO_ROOT))],
        capture_output=True,
        text=True,
        check=False,
        cwd=REPO_ROOT,
    )
    if result.returncode != 0 or not result.stdout.strip():
        return 0
    timestamp = int(result.stdout.strip())
    modified = datetime.fromtimestamp(timestamp, tz=timezone.utc)
    return int((datetime.now(tz=timezone.utc) - modified).days)


def derive_status(days: int) -> str:
    if days <= 120:
        return "active"
    if days <= 365:
        return "draft"
    return "archived"


def extract_title(lines: list[str], fallback: str) -> str:
    for line in lines:
        stripped = line.strip()
        if stripped.startswith("#"):
            return stripped.lstrip("#").strip() or fallback
    return fallback


def build_metadata_block(title: str, status: str) -> list[str]:
    lower_title = title.lower()
    return [
        "<!-- metadata",
        f'para_quien: Equipos y contribuidores que consultan "{title}" en The Wise Tech.',
        f"objetivo: Proporcionar un contexto accionable sobre {lower_title}.",
        f"cuando_usar: Recurre a este documento cuando necesites aplicar o compartir detalles de {lower_title}.",
        f"estado: {status}",
        "-->",
        "",
    ]


def insertion_index(lines: list[str]) -> int:
    if lines and lines[0].strip() == "---":
        idx = 1
        while idx < len(lines):
            if lines[idx].strip() == "---":
                return idx + 1
            idx += 1
        return len(lines)
    return 0


def add_metadata(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    if "<!-- metadata" in text:
        return False
    lines = text.splitlines()
    title = extract_title(lines, path.stem.replace("-", " ").title())
    days = last_modified_days(path)
    status = derive_status(days)
    idx = insertion_index(lines)
    block = build_metadata_block(title, status)
    updated = lines[:idx] + block + lines[idx:]
    path.write_text("\n".join(updated).rstrip() + "\n", encoding="utf-8")
    return True


def main() -> None:
    modified = 0
    for md_file in iter_markdown_files():
        if md_file.is_file():
            modified += 1 if add_metadata(md_file) else 0
    print(f"Metadata blocks inserted in {modified} files.")


if __name__ == "__main__":
    main()
