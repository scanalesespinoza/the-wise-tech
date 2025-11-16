#!/usr/bin/env python3
"""Audit Markdown docs to surface context gaps and onboarding needs."""

from __future__ import annotations

import csv
import subprocess
from dataclasses import dataclass
from pathlib import Path
import re
import unicodedata
from typing import Iterable

REPO_ROOT = Path(__file__).resolve().parents[2]
TARGET_DIRECTORIES = [
    REPO_ROOT / "knowledge" / "docs",
    REPO_ROOT / "experience",
    REPO_ROOT / "implementation",
]
MD_LINK = re.compile(r"\[[^\]]+\]\((?P<url>[^\s)]+)\)")
HEADING = re.compile(r"^(?P<level>#{1,6})\s+(?P<title>.+?)\s*$", re.MULTILINE)
PURPOSE_KEYWORDS = (
    "proposito",
    "propósito",
    "para quien",
    "para quién",
    "objetivo",
    "para que",
    "para qué",
)


@dataclass
class AuditRow:
    path: Path
    title: str
    last_modified: str
    has_purpose: bool
    broken_links: int

    @property
    def relative_path(self) -> str:
        return str(self.path.relative_to(REPO_ROOT))


def iter_markdown_files() -> Iterable[Path]:
    for directory in TARGET_DIRECTORIES:
        if not directory.exists():
            continue
        for path in sorted(directory.rglob("*.md")):
            if path.is_file():
                yield path


def read_markdown(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore")


def strip_accents(value: str) -> str:
    normalized = unicodedata.normalize("NFD", value)
    return "".join(ch for ch in normalized if unicodedata.category(ch) != "Mn")


def extract_title(text: str, default: str) -> str:
    match = HEADING.search(text)
    if match:
        return match.group("title").strip()
    return default


def collect_headings(text: str) -> list[str]:
    return [match.group("title").strip() for match in HEADING.finditer(text)]


def has_purpose_section(headings: Iterable[str]) -> bool:
    for heading in headings:
        normalized = strip_accents(heading).lower()
        if any(keyword in normalized for keyword in PURPOSE_KEYWORDS):
            return True
    return False


def is_internal_link(url: str) -> bool:
    return not (
        url.startswith("http://")
        or url.startswith("https://")
        or url.startswith("mailto:")
        or url.startswith("#")
    )


def normalize_link(url: str, base: Path) -> Path | None:
    clean = url.split("#", 1)[0].strip()
    if not clean:
        return None
    return (base / clean).resolve()


def count_broken_internal_links(path: Path, text: str) -> int:
    base = path.parent
    count = 0
    for match in MD_LINK.finditer(text):
        url = match.group("url")
        if not is_internal_link(url):
            continue
        target = normalize_link(url, base)
        if target is None:
            continue
        try:
            target.relative_to(REPO_ROOT)
        except ValueError:
            count += 1
            continue
        if not target.exists():
            count += 1
    return count


def last_modified_date(path: Path) -> str:
    try:
        result = subprocess.run(
            ["git", "log", "-1", "--format=%cs", str(path.relative_to(REPO_ROOT))],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
            check=True,
        )
    except (subprocess.CalledProcessError, FileNotFoundError):
        return "N/A"
    return result.stdout.strip() or "N/A"


def analyze_file(path: Path) -> AuditRow:
    text = read_markdown(path)
    title = extract_title(text, path.stem)
    headings = collect_headings(text)
    return AuditRow(
        path=path,
        title=title,
        last_modified=last_modified_date(path),
        has_purpose=has_purpose_section(headings),
        broken_links=count_broken_internal_links(path, text),
    )


def write_csv(rows: list[AuditRow], destination: Path) -> None:
    with destination.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(
            ["path", "title", "last_modified", "has_purpose", "broken_internal_links"]
        )
        for row in rows:
            writer.writerow(
                [
                    row.relative_path,
                    row.title,
                    row.last_modified,
                    "yes" if row.has_purpose else "no",
                    row.broken_links,
                ]
            )


def write_todo(rows: list[tuple[AuditRow, list[str]]], destination: Path) -> None:
    lines = ["# TODO — Auditoría de contenido", ""]
    if not rows:
        lines.append(
            "Todos los archivos auditados tienen propósito y menos de 5 enlaces rotos. ✅"
        )
    else:
        lines.append("Archivos que requieren intervención inmediata:")
        lines.append("")
        for entry, reasons in rows:
            reason_text = "; ".join(reasons)
            lines.append(f"- **{entry.relative_path}** — {reason_text}")
    lines.append("")
    destination.write_text("\n".join(lines), encoding="utf-8")


def write_onboarding(destination: Path, total_files: int) -> None:
    content = f"""# Onboarding Hub — The Wise Tech

Bienvenido/a 👋. Usa esta landing para elegir tu camino según rol e intención.

## Selecciona tu perfil

| Perfil | Objetivo clave | Acción inmediata |
| --- | --- | --- |
| Fundadores & Leadership | Entender principios y métricas de resiliencia | [Explorar visión](README.md) |
    | Engineering Managers | Planificar adopción 30/60/90 y priorizar labs | [Rutas 30/60/90](experience/routes/README.md) |
| Devs & SRE | Practicar mediante labs guiados y escenarios | [Labs y escenarios](knowledge/docs/labs) |
| Product & CX | Mapear experiencias y diagnósticos | [Experience toolkit](experience) |
| Contributors nuevos | Configurar entorno y abrir PRs | [Start Here](README.md#start-here) |

## Quick Actions

- [⚡ Quick technical start (7 pasos)](README.md#quick-start-tecnico)
- [📚 Principios y governance](governance)
- [🧭 Mapas de navegación](operations/navigation-map.ascii)
- [🧪 Escenarios Payments](experience/scenarios/payments)

## Estado y feedback

- Total de archivos auditados: **{total_files}**
- Prioriza los elementos listados en `TODO.md`.
- Registra feedback en issues o en la futura encuesta in situ.
"""
    destination.write_text(content, encoding="utf-8")


def build_todo_requirements(rows: list[AuditRow]) -> list[tuple[AuditRow, list[str]]]:
    todo_entries: list[tuple[AuditRow, list[str]]] = []
    for row in rows:
        reasons: list[str] = []
        if not row.has_purpose:
            reasons.append("sin sección de propósito")
        if row.broken_links > 5:
            reasons.append(f"{row.broken_links} enlaces rotos")
        if reasons:
            todo_entries.append((row, reasons))
    return todo_entries


def main() -> None:
    rows = [analyze_file(path) for path in iter_markdown_files()]
    write_csv(rows, REPO_ROOT / "auditoria.csv")
    write_todo(build_todo_requirements(rows), REPO_ROOT / "TODO.md")
    write_onboarding(REPO_ROOT / "onboarding.md", len(rows))


if __name__ == "__main__":
    main()
