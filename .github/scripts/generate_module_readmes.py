#!/usr/bin/env python3
"""Generate catalog READMEs for recipes and onboarding assets in both languages."""

from __future__ import annotations

import pathlib
from dataclasses import dataclass
from typing import Iterable

REPO_ROOT = pathlib.Path(__file__).resolve().parents[2]
LANGUAGES = ("en", "es")


@dataclass(frozen=True)
class SectionConfig:
    language: str
    folder: pathlib.Path
    heading: str
    intro: str


def iter_markdown_files(folder: pathlib.Path) -> Iterable[pathlib.Path]:
    for path in sorted(folder.glob("*.md")):
        if path.name.lower() == "readme.md":
            continue
        yield path


def extract_title(markdown_path: pathlib.Path) -> str:
    for line in markdown_path.read_text(encoding="utf-8").splitlines():
        stripped = line.strip()
        if stripped.startswith("#"):
            return stripped.lstrip("# ").strip()
    return markdown_path.stem.replace("-", " ").title()


def build_list_items(files: Iterable[pathlib.Path], base_path: pathlib.Path) -> str:
    items = []
    for file_path in files:
        title = extract_title(file_path)
        relative = file_path.relative_to(base_path)
        items.append(f"- [{title}]({relative.as_posix()})")
    return "\n".join(items) if items else "- _No documents available yet._"


def write_readme(config: SectionConfig) -> None:
    files = list(iter_markdown_files(config.folder))
    empty_placeholder = (
        "- _No documents available yet._"
        if config.language == "en"
        else "- _Aún no hay documentos disponibles._"
    )
    list_items = build_list_items(files, config.folder) if files else empty_placeholder
    content_lines = [config.heading, "", config.intro.strip(), "", list_items]
    config.folder.joinpath("README.md").write_text(
        "\n".join(content_lines) + "\n", encoding="utf-8"
    )


def main() -> None:
    configs = []
    docs_root = REPO_ROOT / "knowledge" / "docs"
    for language in LANGUAGES:
        lang_root = docs_root / language / "docs"
        configs.extend(
            [
                SectionConfig(
                    language=language,
                    folder=lang_root / "recipes",
                    heading="# Recipe Catalog"
                    if language == "en"
                    else "# Catálogo de Recetas",
                    intro=(
                        "Browse repeatable patterns grounded in real repository examples."
                        if language == "en"
                        else "Explora patrones repetibles basados en ejemplos reales del repositorio."
                    ),
                ),
                SectionConfig(
                    language=language,
                    folder=lang_root / "onboarding",
                    heading="# Onboarding Assets"
                    if language == "en"
                    else "# Recursos de Onboarding",
                    intro=(
                        "Guided tours and learning paths that accelerate contributors' first deliveries."
                        if language == "en"
                        else "Recorridos guiados y rutas de aprendizaje que aceleran las primeras entregas."
                    ),
                ),
            ]
        )

    for config in configs:
        if not config.folder.exists():
            continue
        write_readme(config)


if __name__ == "__main__":
    main()
