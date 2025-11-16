#!/usr/bin/env python3
"""Generate documentation health insights and onboarding artifacts."""

from __future__ import annotations

import csv
import os
import re
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable

from git import Repo
from markdown import Markdown
from requests import Response, Session
from xml.etree import ElementTree as ET

REPO_ROOT = Path(__file__).resolve().parents[2]
REPORTS_DIR = REPO_ROOT / "operations" / "reports"
GITHUB_REPO = "scanalesespinoza/the-wise-tech"
ISSUE_TITLE = "Improve onboarding flow – landing page"
ISSUE_LABEL = "onboarding"
ISSUE_BODY = (
    "The documentation audit highlighted that new contributors still struggle "
    "to find the right entry point. Let's design a visual, role-driven "
    "landing page that surfaces videos, interactive tours, and quick role "
    "selectors. This issue was created automatically by the documentation "
    "insights script."
)
LANGUAGES = ("en", "es")
USAGE_SECTION_KEYWORDS = (
    "para quién es",
    "para quien es",
    "cuándo usarlo",
    "cuando usarlo",
    "who is this for",
    "when to use",
)
LINK_IGNORE_PREFIXES = ("http://", "https://", "mailto:", "tel:", "data:")


@dataclass
class DocumentMetadata:
    """Normalized metadata for a Markdown document."""

    path: Path
    title: str
    languages: list[str]
    last_modified: str
    has_usage_section: bool
    broken_links: int

    @property
    def relative_path(self) -> str:
        return str(self.path.relative_to(REPO_ROOT))


def discover_doc_roots() -> list[Path]:
    """Return every docs directory that supports multilingual structure."""

    roots: list[Path] = []
    for docs_dir in REPO_ROOT.rglob("docs"):
        if not docs_dir.is_dir():
            continue
        if any((docs_dir / lang).is_dir() for lang in LANGUAGES):
            roots.append(docs_dir)
    return roots


def build_language_matrix(
    doc_roots: Iterable[Path],
) -> dict[tuple[Path, Path], set[str]]:
    """Map document relative locations to the languages that exist."""

    matrix: dict[tuple[Path, Path], set[str]] = {}
    for docs_root in doc_roots:
        for lang in LANGUAGES:
            lang_dir = docs_root / lang
            if not lang_dir.is_dir():
                continue
            for doc in lang_dir.rglob("*.md"):
                key = (docs_root.relative_to(REPO_ROOT), doc.relative_to(lang_dir))
                matrix.setdefault(key, set()).add(lang)
    return matrix


def extract_title(markdown_text: str) -> str:
    """Return the first heading using the Markdown parser."""

    md = Markdown()
    html = md.convert(markdown_text)
    md.reset()
    wrapped = f"<div>{html}</div>"
    try:
        root = ET.fromstring(wrapped)
    except ET.ParseError:
        return ""
    for tag in root.iter():
        if tag.tag.lower() in {"h1", "h2"}:
            title = "".join(tag.itertext()).strip()
            if title:
                return title
    return ""


def has_usage_section(markdown_text: str) -> bool:
    """Detect if the usage guidance section is present."""

    for match in re.finditer(r"^#{2,6}\s+(.*)$", markdown_text, re.MULTILINE):
        heading = match.group(1).strip().lower()
        if any(keyword in heading for keyword in USAGE_SECTION_KEYWORDS):
            return True
    return False


def count_broken_internal_links(markdown_text: str, current_file: Path) -> int:
    """Count local links that point to missing resources."""

    md = Markdown()
    html = md.convert(markdown_text)
    md.reset()
    wrapped = f"<div>{html}</div>"
    broken = 0
    try:
        root = ET.fromstring(wrapped)
    except ET.ParseError:
        return broken
    for anchor in root.findall(".//a"):
        href = anchor.attrib.get("href", "").strip()
        if not href or href.startswith("#"):
            continue
        if any(href.startswith(prefix) for prefix in LINK_IGNORE_PREFIXES):
            continue
        if "://" in href and not href.startswith("http"):
            continue
        target_path = href.split("#", maxsplit=1)[0]
        if not target_path:
            continue
        if target_path.startswith("/"):
            candidate = REPO_ROOT / target_path.lstrip("/")
        else:
            candidate = (current_file.parent / target_path).resolve()
        try:
            candidate.relative_to(REPO_ROOT)
        except ValueError:
            continue
        if not candidate.exists():
            broken += 1
    return broken


def read_file(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore")


def get_last_modified(repo: Repo, path: Path) -> str:
    rel_path = path.relative_to(REPO_ROOT)
    commits = list(repo.iter_commits(paths=str(rel_path), max_count=1))
    if not commits:
        return ""
    dt = datetime.fromtimestamp(commits[0].committed_date, tz=timezone.utc)
    return dt.strftime("%Y-%m-%d")


def collect_metadata(repo: Repo) -> list[DocumentMetadata]:
    doc_roots = discover_doc_roots()
    matrix = build_language_matrix(doc_roots)
    metadata: list[DocumentMetadata] = []
    for docs_root in doc_roots:
        for lang in LANGUAGES:
            lang_dir = docs_root / lang
            if not lang_dir.is_dir():
                continue
            for doc in lang_dir.rglob("*.md"):
                text = read_file(doc)
                relative_key = (
                    docs_root.relative_to(REPO_ROOT),
                    doc.relative_to(lang_dir),
                )
                languages = sorted(matrix.get(relative_key, {lang}))
                metadata.append(
                    DocumentMetadata(
                        path=doc,
                        title=extract_title(text),
                        languages=languages,
                        last_modified=get_last_modified(repo, doc),
                        has_usage_section=has_usage_section(text),
                        broken_links=count_broken_internal_links(text, doc),
                    )
                )
    return metadata


def write_csv_report(records: list[DocumentMetadata]) -> Path:
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    csv_path = REPORTS_DIR / "docs-metadata-report.csv"
    with csv_path.open("w", encoding="utf-8", newline="") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(
            [
                "path",
                "title",
                "languages",
                "has_usage_section",
                "last_modified",
                "broken_internal_links",
            ]
        )
        for record in sorted(records, key=lambda item: item.relative_path):
            writer.writerow(
                [
                    record.relative_path,
                    record.title,
                    ",".join(record.languages),
                    "yes" if record.has_usage_section else "no",
                    record.last_modified,
                    record.broken_links,
                ]
            )
    return csv_path


def write_summary_todo(records: list[DocumentMetadata]) -> Path:
    summary_path = REPORTS_DIR / "SUMMARY-TODO.md"
    summary_lines = ["# Documentation review backlog", ""]
    summary_lines.extend(
        [
            "The following documents lack the usage guidance section or have more",
            "than five broken internal links.",
            "",
        ]
    )
    offenders = [
        record
        for record in sorted(records, key=lambda item: item.relative_path)
        if (not record.has_usage_section) or record.broken_links > 5
    ]
    if not offenders:
        summary_lines.append("Great news! No documents require immediate attention.")
    else:
        for record in offenders:
            problems: list[str] = []
            if not record.has_usage_section:
                problems.append("missing usage guidance")
            if record.broken_links > 5:
                problems.append(f"{record.broken_links} broken links")
            summary_lines.append(f"- **{record.relative_path}**")
            summary_lines.append(f"  - Languages: {', '.join(record.languages)}")
            summary_lines.append(f"  - Issues: {'; '.join(problems)}")
    summary_lines.append("")
    summary_path.write_text("\n".join(summary_lines), encoding="utf-8")
    return summary_path


def write_onboarding_walkthrough() -> Path:
    onboarding_path = REPORTS_DIR / "onboarding_walkthrough.md"
    content = """# Wise Tech onboarding walkthrough

> Drafted automatically to support a visual, role-based landing experience.

## Step 1 – Welcome video

- ![Placeholder for welcome video](assets/onboarding/video-placeholder.png)
- _Insert a 60-second video introducing The Wise Tech mission, navigation tips,
  and how to ask for help._

## Step 2 – Choose your role

- **Consumidor** – Aprende cómo beneficiarte del ecosistema Wise y entender
  escenarios clave.
  [Empieza aquí](../../knowledge/docs/paths/consumers-30-60-90.md)
- **Desarrollador** – Accede a labs, APIs y guías para construir sobre Wise.
  [Explora tu ruta](../../knowledge/docs/paths/developers-30-60-90.md)
- **Ingeniero de Plataforma** – Configura entornos, automatiza despliegues y
  opera la plataforma.
  [Construye tu base](../../knowledge/docs/paths/platform-engineers-30-60-90.md)

## Step 3 – Visual quick start

1. **Configura tu entorno** – enlaza a `implementation/quick-start` y muestra un
   gif corto.
2. **Ejecuta tu primer lab** – botón destacado que abra los labs recomendados
   por rol.
3. **Comparte feedback** – botón que abra la plantilla "Feedback – User
   Experience".

## Step 4 – Embedded help

- Incrusta un carrusel corto (GIF o video) mostrando cómo navegar por personas →
  rutas → labs.
- Agrega un CTA "¿Necesitas ayuda?" que abra el canal de soporte interno.

## Step 5 – Métricas y siguientes pasos

- Indicadores sugeridos: tiempo al primer lab, satisfacción (emoji feedback) e
  issues abiertos de UX.
- Añade enlaces rápidos a "Reportar problema" y "Solicitar nuevo lab".
"""
    onboarding_path.write_text(content, encoding="utf-8")
    return onboarding_path


def ensure_issue_exists() -> None:
    token = os.getenv("GITHUB_TOKEN")
    if not token:
        print("GITHUB_TOKEN not set; skipping issue creation.")
        return
    session = Session()
    session.headers.update(
        {"Authorization": f"Bearer {token}", "Accept": "application/vnd.github+json"}
    )
    if not open_issue_with_label(session):
        ensure_label(session)
        create_issue(session)


def github_api(session: Session, method: str, endpoint: str, **kwargs) -> Response:
    url = f"https://api.github.com/repos/{GITHUB_REPO}/{endpoint.lstrip('/')}"
    response = session.request(method, url, timeout=30, **kwargs)
    if response.status_code >= 400:
        print(f"GitHub API error {response.status_code}: {response.text}")
    return response


def open_issue_with_label(session: Session) -> bool:
    response = github_api(
        session,
        "GET",
        "issues",
        params={"state": "open", "labels": ISSUE_LABEL, "per_page": 100},
    )
    if response.status_code != 200:
        return False
    issues = response.json()
    return bool(issues)


def ensure_label(session: Session) -> None:
    response = github_api(session, "GET", f"labels/{ISSUE_LABEL}")
    if response.status_code == 200:
        return
    if response.status_code == 404:
        github_api(
            session,
            "POST",
            "labels",
            json={
                "name": ISSUE_LABEL,
                "color": "fbca04",
                "description": "Onboarding improvements",
            },
        )


def create_issue(session: Session) -> None:
    payload = {"title": ISSUE_TITLE, "body": ISSUE_BODY, "labels": [ISSUE_LABEL]}
    github_api(session, "POST", "issues", json=payload)


def main() -> int:
    repo = Repo(REPO_ROOT)
    records = collect_metadata(repo)
    if not records:
        print("No multilingual documentation found.")
        return 0
    csv_path = write_csv_report(records)
    summary_path = write_summary_todo(records)
    onboarding_path = write_onboarding_walkthrough()
    ensure_issue_exists()
    print("Generated reports:")
    print(f" - {csv_path.relative_to(REPO_ROOT)}")
    print(f" - {summary_path.relative_to(REPO_ROOT)}")
    print(f" - {onboarding_path.relative_to(REPO_ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
