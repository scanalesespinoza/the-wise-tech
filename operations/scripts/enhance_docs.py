#!/usr/bin/env python3
import os
import re
from pathlib import Path
from datetime import datetime
from typing import Tuple, List

from git import Repo
from markdown import markdown

REPO_ROOT = Path(
    os.environ.get("WISE_TECH_ROOT", str(Path(__file__).resolve().parents[2]))
)
REPO_ROOT = Path(REPO_ROOT)
TARGET_DIRS = [
    REPO_ROOT / "knowledge",
    REPO_ROOT / "experience",
    REPO_ROOT / "implementation",
]
CONTEXT_HEADERS = ["Propósito", "Audiencia", "Cuándo usarlo"]
ICON_MAP = {
    "conceptos": "🧠",
    "concepts": "🧠",
    "labs": "🛠",
    "laboratorios": "🛠",
    "escenarios": "🔍",
    "scenarios": "🔍",
}
TIP_KEYWORDS = ["make", "git", "kubectl", "docker", "az ", "aws "]

repo = Repo(REPO_ROOT)


def slugify(value: str) -> str:
    value = re.sub(r"[\s]+", "-", value.strip().lower())
    value = re.sub(r"[^a-z0-9\-]", "", value)
    return value


def split_front_matter(text: str) -> Tuple[str, str]:
    if text.startswith("---\n"):
        end = text.find("\n---", 3)
        if end != -1:
            end += len("\n---\n")
            return text[:end], text[end:]
    return "", text


def guess_title(path: Path, body: str) -> str:
    heading_match = re.search(r"^#\s+(.+)$", body, flags=re.MULTILINE)
    if heading_match:
        return heading_match.group(1).strip()
    return path.stem.replace("-", " ").replace("_", " ").title()


def ensure_context(body: str, title: str) -> Tuple[str, bool]:
    missing = False
    required = {}
    for header in CONTEXT_HEADERS:
        pattern = rf"^##\s+[^\n]*{header}[^\n]*$"
        if not re.search(pattern, body, flags=re.MULTILINE | re.IGNORECASE):
            missing = True
            required[header] = True
    if not missing:
        return body, False
    block = []
    if required.get("Propósito"):
        block.append(
            f"## Propósito\nEnmarca cómo {title} ayuda a mantener decisiones alineadas con The Wise Tech.\n"
        )
    if required.get("Audiencia"):
        block.append(
            f"## Audiencia\nPersonas y equipos que necesitan una guía rápida sobre {title}.\n"
        )
    if required.get("Cuándo usarlo"):
        block.append(
            f"## Cuándo usarlo\nConsúltalo cuando requieras referencias inmediatas para {title} o debas compartir el enfoque con otros equipos.\n"
        )
    insertion = "\n".join(block) + "\n"
    return insertion + body.lstrip(), True


def add_nav_table(body: str) -> str:
    if "Tabla de navegación" in body:
        return body
    headings = re.findall(r"^##\s+([^#\n]+)$", body, flags=re.MULTILINE)
    filtered = [
        h.strip()
        for h in headings
        if not any(key in h for key in CONTEXT_HEADERS + ["Tabla de navegación"])
    ]
    if len(filtered) < 3:
        return body
    nav_lines = ["## Tabla de navegación", ""]
    for h in filtered:
        nav_lines.append(f"- [{h}](#{slugify(h)})")
    nav_lines.append("")
    nav_block = "\n".join(nav_lines)
    pattern = re.search(
        r"(##\s+Cuándo usarlo[^#]*)", body, flags=re.MULTILINE | re.DOTALL
    )
    if pattern:
        idx = pattern.end()
        return body[:idx] + "\n" + nav_block + "\n" + body[idx:]
    return nav_block + body


def add_icons(body: str) -> str:
    def replace_heading(match):
        hashes = match.group(1)
        title = match.group(2).strip()
        lower = title.lower()
        for keyword, icon in ICON_MAP.items():
            if keyword in lower and not title.startswith(icon):
                return f"{hashes} {icon} {title}"
        return match.group(0)

    return re.sub(r"^(#{2,4})\s+(.+)$", replace_heading, body, flags=re.MULTILINE)


def add_tip_boxes(body: str) -> str:
    pattern = re.compile(r"(^```[\s\S]*?^```)", flags=re.MULTILINE)
    inserts = []
    for match in pattern.finditer(body):
        block = match.group(1)
        lower = block.lower()
        if not any(keyword in lower for keyword in TIP_KEYWORDS):
            continue
        start = match.start()
        snippet = body[max(0, start - 120) : start]
        if "ℹ️ Consejo" in snippet:
            continue
        inserts.append(
            (
                start,
                "> ℹ️ Consejo: Ajusta el comando a tu entorno antes de ejecutarlo.\n",
            )
        )
    if not inserts:
        return body
    offset = 0
    text = body
    for index, tip in inserts:
        text = text[: index + offset] + tip + text[index + offset :]
        offset += len(tip)
    return text


def enforce_section_density(body: str) -> str:
    html = markdown(body)
    text = re.sub(r"<[^>]+>", " ", html)
    words = [w for w in text.split() if w.strip()]
    word_count = len(words)
    headings = re.findall(r"^##\s+", body, flags=re.MULTILINE)
    if word_count <= 800 or len(headings) >= 4 or "Sección enfocada" in body:
        return body
    paragraphs = body.split("\n\n")
    chunk = max(1, len(paragraphs) // 3)
    pieces: List[str] = []
    section_id = 1
    for idx, para in enumerate(paragraphs):
        if idx % chunk == 0:
            pieces.append(f"## Sección enfocada {section_id}")
            section_id += 1
        pieces.append(para)
    return "\n\n".join(pieces)


def ensure_feedback(text: str, path: Path) -> Tuple[str, bool]:
    try:
        last_date = repo.git.log("-1", "--format=%cs", str(path.relative_to(REPO_ROOT)))
    except Exception:
        last_date = datetime.utcnow().date().isoformat()
    block = (
        "\n---\n"
        f"Última modificación: {last_date}\n\n"
        "🗳️ **¿Te fue útil este documento?**\n"
        "- [ ] Sí, resolvió mi duda\n"
        "- [ ] Más o menos\n"
        "- [ ] No me ayudó\n\n"
        "💬 [Deja tu feedback](https://github.com/scanalesespinoza/the-wise-tech/issues/new?template=feedback.yml)\n\n"
        "---\n"
    )
    ultima_idx = text.find("Última modificación:")
    if ultima_idx != -1:
        clean = text[:ultima_idx].rstrip()
        clean = re.sub(r"(\n---\s*)+$", "", clean).rstrip()
        return clean + block + "\n", True
    markers = [
        text.find("🗳️ **¿Te fue útil este documento?**"),
        text.find("¿Te fue útil este documento?"),
        text.find("[ ] Sí  [ ] Algo  [ ] No"),
    ]
    indices = [idx for idx in markers if idx != -1]
    if indices:
        cut = min(indices)
        clean = text[:cut].rstrip()
        clean = re.sub(r"(\n---\s*)+$", "", clean).rstrip()
        return clean + block + "\n", True
    return text.rstrip() + block + "\n", False


def process_file(
    path: Path, missing_list: List[str], feedback_list: List[str], feedback_status: dict
):
    rel = path.relative_to(REPO_ROOT)
    original = path.read_text(encoding="utf-8")
    front, body = split_front_matter(original)
    title = guess_title(path, body)
    body, missing = ensure_context(body, title)
    if missing:
        missing_list.append(str(rel))
    body = add_nav_table(body)
    body = add_icons(body)
    body = add_tip_boxes(body)
    body = enforce_section_density(body)
    updated = front + body
    updated, _ = ensure_feedback(updated, path)
    feedback_status[str(rel)] = True
    if updated != original:
        path.write_text(updated, encoding="utf-8")
        feedback_list.append(str(rel))


def main():
    missing_context = []
    feedback_ready = []
    feedback_status = {}
    for directory in TARGET_DIRS:
        for path in directory.rglob("*.md"):
            process_file(path, missing_context, feedback_ready, feedback_status)
    report = REPO_ROOT / "missing-context-report.md"
    if missing_context:
        content = [
            "# Reporte de contexto faltante",
            "",
            "Los siguientes archivos carecían de al menos una sección de contexto (Propósito, Audiencia o Cuándo usarlo) antes de la estandarización:",
        ]
        content.extend([f"- {item}" for item in sorted(missing_context)])
    else:
        content = [
            "# Reporte de contexto faltante",
            "",
            "Todos los documentos contienen las secciones de contexto requeridas.",
        ]
    report.write_text("\n".join(content) + "\n", encoding="utf-8")

    feedback_summary = REPO_ROOT / "feedback-summary.md"
    summary_lines = [
        "# Feedback aplicado",
        "",
        "## Documentos con feedback habilitado",
        "",
    ]
    summary_lines.extend([f"- {item}" for item in sorted(feedback_status)])
    summary_lines.append("")
    pending = sorted(set(feedback_status.keys()) - set(feedback_ready))
    summary_lines.append("## Documentos que ya lo tenían configurado")
    if pending:
        summary_lines.extend([f"- {item}" for item in pending])
    else:
        summary_lines.append(
            "- Ninguno, todos quedaron estandarizados en esta ejecución."
        )
    feedback_summary.write_text("\n".join(summary_lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
