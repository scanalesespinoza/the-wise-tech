from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, List

ROOT = Path(__file__).resolve().parent.parent
CONTEXT_DIRS = [ROOT / "knowledge", ROOT / "experience", ROOT / "implementation"]
CONTEXT_TEMPLATE = (
    "---\n"
    "🎯 **Propósito:** Describe brevemente qué problema resuelve este documento.\n"
    "👤 **Audiencia:** ¿Para quién está diseñado?\n"
    "🧭 **Cuándo usarlo:** Contextos ideales de uso.\n"
    "📌 **Estado:** Activo / Borrador / En revisión\n"
    "---\n\n"
)
FEEDBACK_BLOCK = (
    "\n---\n"
    "📣 **¿Te fue útil este documento?**\n"
    "- [ ] Sí, resolvió mi duda\n"
    "- [ ] Más o menos\n"
    "- [ ] No me ayudó\n\n"
    "💬 [Deja tu comentario o sugerencia aquí](https://github.com/scanalesespinoza/the-wise-tech/issues/new?template=feedback.yml)\n"
    "---\n"
)
FEEDBACK_IDENTIFIER = (
    "https://github.com/scanalesespinoza/the-wise-tech/issues/new?template=feedback.yml"
)


@dataclass
class ContextStatus:
    path: Path
    had_all_sections: bool


@dataclass
class FeedbackStatus:
    path: Path
    already_had_block: bool


def ensure_context_sections(path: Path) -> ContextStatus:
    text = path.read_text(encoding="utf-8")
    keywords = ["Propósito", "Audiencia", "Cuándo", "Estado"]
    had_all = all(keyword in text for keyword in keywords)
    if not had_all:
        updated = CONTEXT_TEMPLATE + text if text else CONTEXT_TEMPLATE
        path.write_text(updated, encoding="utf-8")
    return ContextStatus(path=path.relative_to(ROOT), had_all_sections=had_all)


def ensure_feedback_block(path: Path) -> FeedbackStatus:
    text = path.read_text(encoding="utf-8")
    already_there = FEEDBACK_IDENTIFIER in text
    if not already_there:
        suffix = FEEDBACK_BLOCK if text.endswith("\n") else "\n" + FEEDBACK_BLOCK
        path.write_text(text + suffix, encoding="utf-8")
    return FeedbackStatus(path=path.relative_to(ROOT), already_had_block=already_there)


def iter_markdown_files(paths: Iterable[Path]) -> List[Path]:
    result: List[Path] = []
    for base in paths:
        if not base.exists():
            continue
        for file in base.rglob("*.md"):
            if ".git" in file.parts:
                continue
            result.append(file)
    return sorted(result)


def generate_context_status_report(entries: List[ContextStatus]) -> None:
    template_path = ROOT / "context-status.md"
    added = [e.path for e in entries if not e.had_all_sections]
    complete = [e.path for e in entries if e.had_all_sections]
    lines = ["# Context Status", "", "## Plantilla agregada"]
    if added:
        lines.extend(f"- {path}" for path in added)
    else:
        lines.append("- Ningún archivo necesitó plantilla nueva.")
    lines.extend(["", "## Archivos completos"])
    if complete:
        lines.extend(f"- {path}" for path in complete)
    else:
        lines.append(
            "- Ningún archivo contaba con todas las secciones antes de esta ejecución."
        )
    template_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def generate_feedback_map(entries: List[FeedbackStatus]) -> None:
    template_path = ROOT / "feedback-map.md"
    with_block = [e.path for e in entries if e.already_had_block]
    added_block = [e.path for e in entries if not e.already_had_block]
    lines = ["# Feedback Map", "", "## Ya contaban con sección de feedback"]
    if with_block:
        lines.extend(f"- {path}" for path in with_block)
    else:
        lines.append("- Ningún archivo la tenía antes de esta ejecución.")
    lines.extend(["", "## Se agregó la sección de feedback"])
    if added_block:
        lines.extend(f"- {path}" for path in added_block)
    else:
        lines.append("- No se requirieron cambios en esta ejecución.")
    template_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    context_files = iter_markdown_files(CONTEXT_DIRS)
    context_results = [ensure_context_sections(path) for path in context_files]
    generate_context_status_report(context_results)
    feedback_targets = sorted(
        path for path in ROOT.rglob("*.md") if ".git" not in path.parts
    )
    feedback_results = [
        ensure_feedback_block(path)
        for path in feedback_targets
        if path != ROOT / "feedback-map.md"
    ]
    generate_feedback_map(feedback_results)
    ensure_feedback_block(ROOT / "context-status.md")
    ensure_feedback_block(ROOT / "feedback-map.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
