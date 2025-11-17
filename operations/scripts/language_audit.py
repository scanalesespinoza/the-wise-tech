#!/usr/bin/env python3
"""Audit repository content to highlight files that are not in English."""

from __future__ import annotations

import argparse
import datetime as dt
import re
import subprocess
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Sequence

from langdetect import DetectorFactory, LangDetectException, detect_langs

DetectorFactory.seed = 0

CODE_BLOCK_RE = re.compile(r"```.*?```", re.DOTALL)
FRONT_MATTER_RE = re.compile(r"^---.*?---", re.DOTALL)
SAMPLE_RE = re.compile(r"\s+")


@dataclass
class LanguageFinding:
    path: Path
    detected_language: str
    detected_probability: float
    english_probability: float
    excerpt: str


@dataclass
class AuditStats:
    scanned: int = 0
    skipped_binary: int = 0
    skipped_short: int = 0


def gather_files(paths: Sequence[str]) -> list[Path]:
    """Return the list of files to inspect."""
    if paths:
        collected: list[Path] = []
        for entry in paths:
            target = Path(entry)
            if target.is_dir():
                collected.extend(sorted(p for p in target.rglob("*") if p.is_file()))
            elif target.is_file():
                collected.append(target)
        return collected

    result = subprocess.run(
        ["git", "ls-files"],
        check=True,
        capture_output=True,
        text=True,
    )
    return [Path(line.strip()) for line in result.stdout.splitlines() if line.strip()]


def is_binary(content: bytes) -> bool:
    return bool(b"\x00" in content)


def prepare_text(text: str) -> str:
    """Strip markdown/yaml sections that can confuse language detection."""
    cleaned = FRONT_MATTER_RE.sub(" ", text, count=1)
    cleaned = CODE_BLOCK_RE.sub(" ", cleaned)
    cleaned = SAMPLE_RE.sub(" ", cleaned)
    return cleaned.strip()


def detect_language_probabilities(text: str):
    """Return detection tuple (best_lang, best_prob, english_prob)."""
    if len(text) < 80:
        return None
    try:
        detections = detect_langs(text)
    except LangDetectException:
        return None

    best = detections[0]
    english_prob = 0.0
    for candidate in detections:
        if candidate.lang == "en":
            english_prob = candidate.prob
            break
    return best.lang, best.prob, english_prob


def build_excerpt(text: str, limit: int = 140) -> str:
    snippet = text.strip().replace("\n", " ")
    snippet = re.sub(r"\s+", " ", snippet)
    if len(snippet) > limit:
        snippet = snippet[: limit - 1].rstrip() + "…"
    return snippet


def audit_files(
    files: Iterable[Path], threshold: float, stats: AuditStats
) -> list[LanguageFinding]:
    findings: list[LanguageFinding] = []
    for path in files:
        try:
            content = path.read_bytes()
        except FileNotFoundError:
            continue
        except PermissionError:
            continue
        if is_binary(content):
            stats.skipped_binary += 1
            continue

        try:
            text = content.decode("utf-8")
        except UnicodeDecodeError:
            stats.skipped_binary += 1
            continue

        cleaned = prepare_text(text)
        detection = detect_language_probabilities(cleaned)
        if detection is None:
            stats.skipped_short += 1
            continue

        stats.scanned += 1
        best_lang, best_prob, english_prob = detection
        if english_prob < threshold:
            excerpt = build_excerpt(cleaned)
            findings.append(
                LanguageFinding(
                    path=path,
                    detected_language=best_lang,
                    detected_probability=best_prob,
                    english_probability=english_prob,
                    excerpt=excerpt,
                )
            )
    return findings


def write_report(
    findings: Sequence[LanguageFinding],
    stats: AuditStats,
    threshold: float,
    report_path: Path,
) -> None:
    lines: list[str] = ["# Language Audit", ""]
    timestamp = dt.datetime.now(dt.timezone.utc).isoformat().replace("+00:00", "Z")
    lines.append(f"- Generated: {timestamp}")
    lines.append(f"- English probability threshold: {threshold:.2f}")
    lines.append(f"- Files scanned: {stats.scanned}")
    lines.append(f"- Files skipped (binary): {stats.skipped_binary}")
    lines.append(f"- Files skipped (too short): {stats.skipped_short}")
    lines.append(f"- Files flagged as non-English: {len(findings)}")
    lines.append("")

    if findings:
        lines.append("## Files requiring review")
        lines.append("")
        lines.append(
            "| File | Detected language | Detected prob. | English prob. | Sample |"
        )
        lines.append("| --- | --- | --- | --- | --- |")
        for finding in findings:
            sample = finding.excerpt.replace("|", r"\|")
            lines.append(
                f"| {finding.path} | {finding.detected_language} | "
                f"{finding.detected_probability:.2f} | {finding.english_probability:.2f} | {sample} |"
            )
    else:
        lines.append("All inspected files meet the English threshold. ✅")

    report_path.write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "paths",
        nargs="*",
        help="Optional subset of files or directories to scan.",
    )
    parser.add_argument(
        "--threshold",
        type=float,
        default=0.8,
        help="Minimum probability required for English content.",
    )
    parser.add_argument(
        "--report",
        type=Path,
        default=Path("operations/reports/language-audit.md"),
        help="Where to write the Markdown report.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    files = gather_files(args.paths)
    stats = AuditStats()
    findings = audit_files(files, args.threshold, stats)
    write_report(findings, stats, args.threshold, args.report)
    print(
        f"Language audit complete. Scanned {stats.scanned} files and flagged {len(findings)} "
        "possible non-English documents."
    )
    if findings:
        for finding in findings[:10]:
            print(
                f"- {finding.path}: detected {finding.detected_language} (english={finding.english_probability:.2f})"
            )


if __name__ == "__main__":
    main()
