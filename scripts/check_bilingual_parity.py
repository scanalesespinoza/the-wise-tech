#!/usr/bin/env python3
"""Ensure documentation pairs stay in sync across languages."""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Iterable


def collect_markdown_files(base: Path) -> set[Path]:
    return {path.relative_to(base) for path in base.rglob("*.md") if path.is_file()}


def compare_pairs(pairs: Iterable[tuple[Path, Path]]) -> int:
    exit_code = 0
    for left, right in pairs:
        left_files = collect_markdown_files(left)
        right_files = collect_markdown_files(right)
        missing_in_right = sorted(left_files - right_files)
        missing_in_left = sorted(right_files - left_files)

        if missing_in_right or missing_in_left:
            exit_code = 1
            print(f"\nMismatch between {left} and {right}:")
            if missing_in_right:
                print("  Missing on right:")
                for rel in missing_in_right:
                    print(f"    {rel}")
            if missing_in_left:
                print("  Missing on left:")
                for rel in missing_in_left:
                    print(f"    {rel}")
    return exit_code


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check-scenarios",
        action="store_true",
        help="Check scenario documentation parity as well",
    )
    args = parser.parse_args()

    repo_root = Path(__file__).resolve().parents[1]
    pairs: list[tuple[Path, Path]] = [
        (repo_root / "en", repo_root / "es"),
    ]

    if args.check_scenarios:
        pairs.append(
            (
                repo_root / "scenarios" / "payments" / "docs" / "en",
                repo_root / "scenarios" / "payments" / "docs" / "es",
            )
        )

    for left, right in pairs:
        if not left.exists() or not right.exists():
            raise SystemExit(f"Both directories must exist: {left} {right}")

    return compare_pairs(pairs)


if __name__ == "__main__":
    raise SystemExit(main())
