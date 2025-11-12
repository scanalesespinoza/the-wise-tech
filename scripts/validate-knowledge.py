#!/usr/bin/env python3
from __future__ import annotations

"""Validate knowledge base metadata, quotes, and links."""

import json
import re
import sys
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Iterable

ROOT = Path(__file__).resolve().parents[1]
ARTICLES_DIR = ROOT / "docs" / "knowledge" / "articles"

ALLOWED_SOURCES = {"LinkedIn", "Medium"}
ALLOWED_PERSONAS = {"developers", "platform-engineers", "consumers"}
ALLOWED_PRINCIPLES = {
    "continuous-improvement",
    "simplicity",
    "resilience",
    "knowledge-capitalization",
    "human-purpose",
    "human-connection",
}

REQUIRED_FILES = (
    "metadata.json",
    "summary-es.md",
    "summary-en.md",
    "wise-tech-alignment.md",
    "practices.md",
    "quotes.md",
    "links.md",
)

WORD_RE = re.compile(r"[A-Za-zÁÉÍÓÚÜÑáéíóúüñ0-9']+")


@dataclass
class ValidationError(Exception):
    message: str

    def __str__(self) -> str:  # pragma: no cover - simple wrapper
        return self.message


def iter_article_dirs() -> Iterable[Path]:
    if not ARTICLES_DIR.exists():
        raise ValidationError("Knowledge articles directory not found")
    for path in sorted(p for p in ARTICLES_DIR.iterdir() if p.is_dir()):
        yield path


def expect_files(slug_dir: Path) -> None:
    slug = slug_dir.name
    missing = []
    for suffix in REQUIRED_FILES:
        expected = slug_dir / f"{slug}-{suffix}"
        if not expected.exists():
            missing.append(expected.relative_to(ROOT))
    if missing:
        raise ValidationError(f"Missing required files for {slug}: {', '.join(map(str, missing))}")


def validate_metadata(slug_dir: Path) -> None:
    slug = slug_dir.name
    path = slug_dir / f"{slug}-metadata.json"
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:  # pragma: no cover - safety guard
        raise ValidationError(f"Invalid JSON in {path.relative_to(ROOT)}: {exc}")

    required_fields = {
        "title": str,
        "author": str,
        "source": str,
        "original_url": str,
        "published_date": str,
        "topics": list,
        "personas": list,
        "wise_tech_principles": list,
        "license_notes": str,
        "extraction_mode": str,
        "hash": str,
    }
    for field, expected_type in required_fields.items():
        if field not in data:
            raise ValidationError(f"Missing field '{field}' in {path.relative_to(ROOT)}")
        if not isinstance(data[field], expected_type):
            raise ValidationError(
                f"Field '{field}' in {path.relative_to(ROOT)} must be {expected_type.__name__}"
            )

    if data["source"] not in ALLOWED_SOURCES:
        raise ValidationError(f"Unsupported source '{data['source']}' in {path.relative_to(ROOT)}")

    try:
        datetime.strptime(data["published_date"], "%Y-%m-%d")
    except ValueError:
        raise ValidationError(
            f"Invalid published_date '{data['published_date']}' in {path.relative_to(ROOT)}"
        )

    if not data["topics"]:
        raise ValidationError(f"Field 'topics' must not be empty in {path.relative_to(ROOT)}")
    if any(not isinstance(topic, str) or not topic for topic in data["topics"]):
        raise ValidationError(f"All topics must be non-empty strings in {path.relative_to(ROOT)}")

    personas = data["personas"]
    if not personas or any(p not in ALLOWED_PERSONAS for p in personas):
        raise ValidationError(
            f"Personas must be subset of {sorted(ALLOWED_PERSONAS)} in {path.relative_to(ROOT)}"
        )

    principles = data["wise_tech_principles"]
    if not principles or any(p not in ALLOWED_PRINCIPLES for p in principles):
        raise ValidationError(
            f"Wise Tech principles must be subset of {sorted(ALLOWED_PRINCIPLES)} in {path.relative_to(ROOT)}"
        )

    if len(data["hash"]) != 64 or not all(c in "0123456789abcdef" for c in data["hash"].lower()):
        raise ValidationError(f"Hash must be a 64-char hex string in {path.relative_to(ROOT)}")

    if data["extraction_mode"] not in {"structured-summary", "full-text"}:
        raise ValidationError(
            f"Extraction mode must be 'structured-summary' or 'full-text' in {path.relative_to(ROOT)}"
        )


def validate_quotes(slug_dir: Path) -> None:
    slug = slug_dir.name
    path = slug_dir / f"{slug}-quotes.md"
    content = path.read_text(encoding="utf-8")
    blocks: list[list[str]] = []
    current: list[str] = []
    for line in content.splitlines():
        if line.startswith(">"):
            if line.strip() == ">":
                continue
            current.append(line.lstrip("> "))
        else:
            if current:
                blocks.append(current)
                current = []
    if current:
        blocks.append(current)

    for block in blocks:
        quote_lines = [ln for ln in block if not ln.startswith("—")]
        text = " ".join(quote_lines)
        words = WORD_RE.findall(text)
        if len(words) > 100:
            raise ValidationError(
                f"Quote exceeds 100 words in {path.relative_to(ROOT)}: '{text[:60]}…' ({len(words)} words)"
            )


def validate_links(slug_dir: Path) -> None:
    slug = slug_dir.name
    path = slug_dir / f"{slug}-links.md"
    for line in path.read_text(encoding="utf-8").splitlines():
        if "Relacionados en el repo:" in line and "http" in line:
            raise ValidationError(
                f"Repository links must be relative in {path.relative_to(ROOT)}: {line.strip()}"
            )


def main() -> int:
    try:
        for article_dir in iter_article_dirs():
            expect_files(article_dir)
            validate_metadata(article_dir)
            validate_quotes(article_dir)
            validate_links(article_dir)
    except ValidationError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":  # pragma: no cover - script entry point
    sys.exit(main())
