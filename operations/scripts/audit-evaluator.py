#!/usr/bin/env python3
import json
import logging
import os
import re
import subprocess
import sys
import urllib.error
import urllib.request
from collections import OrderedDict
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Optional, Sequence
from urllib.parse import quote, urljoin, urlparse

import yaml

try:
    from git import InvalidGitRepositoryError, Repo
except ImportError:  # pragma: no cover - GitPython is optional during tests
    InvalidGitRepositoryError = Repo = None  # type: ignore

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
AUDIT = os.path.join(ROOT, "experience", "audit")
CONTENT_DIRECTORIES: Sequence[str] = (
    "knowledge",
    "experience",
    "implementation",
    "governance",
)
AUDIT_REPORT_PATH = os.path.join(ROOT, "audit-report.md")
ISSUES_REPORT_PATH = os.path.join(ROOT, "docs-with-issues.md")
JSON_REPORT_PATH = os.path.join(ROOT, "audit-report.json")

CRITERIA_CONFIG = OrderedDict(
    [
        (
            "purpose",
            {
                "label": "🎯 Propósito explícito",
                "keywords": [
                    "purpose",
                    "objetivo",
                    "goal",
                    "problem",
                    "reto",
                    "desafío",
                    "why",
                ],
                "suggestion": "Explica qué problema resuelve el documento y por qué importa.",
            },
        ),
        (
            "audience",
            {
                "label": "👥 Audiencia definida",
                "keywords": [
                    "audience",
                    "para quién",
                    "personas",
                    "rol",
                    "stakeholder",
                    "equipo",
                    "quién",
                ],
                "suggestion": "Alinea el contenido con la persona, rol o contexto que debe usarlo.",
            },
        ),
        (
            "behavior",
            {
                "label": "🧠 Comportamiento esperado",
                "keywords": [
                    "should",
                    "debe",
                    "debería",
                    "expected",
                    "comportamiento",
                    "cambio",
                    "habito",
                    "behavior",
                    "adoptar",
                ],
                "suggestion": "Describe qué cambio o decisión concreta debe ocurrir después de leerlo.",
            },
        ),
        (
            "applicability",
            {
                "label": "⚙️ Aplicabilidad práctica",
                "keywords": [
                    "paso",
                    "step",
                    "cómo",
                    "implement",
                    "usar",
                    "aplicar",
                    "checklist",
                    "run",
                ],
                "suggestion": "Incluye pasos accionables, checklists o ejemplos rápidos para ejecutarlo.",
                "type": "applicability",
            },
        ),
        (
            "reflection",
            {
                "label": "💡 Reflexión / sabiduría",
                "keywords": [
                    "why",
                    "principio",
                    "reflexión",
                    "aprendizaje",
                    "sabiduría",
                    "insight",
                    "porque",
                    "razón",
                ],
                "suggestion": "Conecta el qué con el por qué/para qué y rescata aprendizajes clave.",
            },
        ),
        (
            "consistency",
            {
                "label": "✍️ Consistencia visual",
                "keywords": [],
                "suggestion": "Revisa encabezados, emojis y enlaces para que tengan un estilo uniforme.",
                "type": "consistency",
            },
        ),
    ]
)

EMOJI_PATTERN = re.compile(r"[\U0001F300-\U0001FAFF]")
GITHUB_API_URL = os.environ.get("GITHUB_API_URL", "https://api.github.com")

logging.basicConfig(level=logging.INFO, format="[%(levelname)s] %(message)s")


def load_yaml(path):
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


@dataclass
class DocumentAudit:
    path: str
    title: str
    scores: Dict[str, int]
    missing_sections: List[str] = field(default_factory=list)
    suggestions: List[str] = field(default_factory=list)
    issues: List[str] = field(default_factory=list)
    last_modified: str = "N/A"

    @property
    def total_score(self) -> int:
        return sum(self.scores.values())

    @property
    def max_score(self) -> int:
        return len(CRITERIA_CONFIG) * 5

    @property
    def completion_ratio(self) -> float:
        if not self.max_score:
            return 0.0
        return self.total_score / self.max_score

    @property
    def status_icon(self) -> str:
        ratio = self.completion_ratio
        if ratio >= 0.85:
            return "🟢"
        if ratio >= 0.6:
            return "🟡"
        return "🔴"

    def to_dict(self) -> Dict[str, object]:
        return {
            "path": self.path,
            "title": self.title,
            "scores": self.scores,
            "missing_sections": self.missing_sections,
            "suggestions": self.suggestions,
            "issues": self.issues,
            "total_score": self.total_score,
            "max_score": self.max_score,
            "status": self.status_icon,
            "last_modified": self.last_modified,
        }


def _score_with_icon(value: int) -> str:
    if value >= 4:
        icon = "✅"
    elif value == 3:
        icon = "🟡"
    else:
        icon = "❌"
    return f"{icon} {value}"


def _ratio_to_score(ratio: float) -> int:
    if ratio >= 0.85:
        return 5
    if ratio >= 0.6:
        return 4
    if ratio >= 0.4:
        return 3
    if ratio >= 0.2:
        return 2
    return 1


def _utcnow() -> datetime:
    return datetime.now(timezone.utc)


def _utc_timestamp() -> str:
    return _utcnow().isoformat().replace("+00:00", "Z")


def _try_load_repo():
    if Repo is None:
        logging.warning("GitPython no disponible; se utilizará git CLI para fechas.")
        return None
    try:
        return Repo(ROOT)
    except InvalidGitRepositoryError:
        logging.warning("No se pudo inicializar Repo desde %s", ROOT)
        return None


def _last_modified(repo, rel_path: str) -> str:
    rel_posix = Path(rel_path).as_posix()
    if repo is not None:
        try:
            commit = next(repo.iter_commits(paths=rel_posix, max_count=1))
        except StopIteration:
            commit = None
        if commit is not None:
            return datetime.fromtimestamp(commit.committed_date).strftime("%Y-%m-%d")

    timestamp = _run_git_command(["log", "-1", "--format=%ct", "--", rel_posix])
    if timestamp:
        try:
            return datetime.utcfromtimestamp(int(timestamp)).strftime("%Y-%m-%d")
        except ValueError:
            pass
    return "N/A"


def _collect_markdown_documents() -> List[str]:
    documents: List[str] = []
    for directory in CONTENT_DIRECTORIES:
        root_dir = os.path.join(ROOT, directory)
        if not os.path.isdir(root_dir):
            continue
        for base, _, files in os.walk(root_dir):
            for name in files:
                if not name.endswith(".md"):
                    continue
                rel_path = os.path.relpath(os.path.join(base, name), ROOT)
                documents.append(rel_path)
    return sorted(documents)


def _parse_markdown_structure(path: str, text: str) -> Dict[str, object]:
    lines = text.splitlines()
    headings: List[Dict[str, object]] = []
    list_items = 0
    ordered_items = 0
    checkbox_items = 0
    code_blocks = 0
    in_code = False
    paragraphs: List[str] = []
    buffer: List[str] = []
    emoji_headings = 0
    broken_links: List[str] = []
    heading_texts: List[str] = []
    base_dir = os.path.dirname(os.path.join(ROOT, path))
    link_pattern = re.compile(r"\[(?P<label>[^\]]+)\]\((?P<target>[^)]+)\)")

    def _flush_paragraph():
        nonlocal buffer
        if buffer:
            paragraphs.append(" ".join(buffer).strip())
            buffer = []

    def _collect_links(line: str):
        for match in link_pattern.finditer(line):
            target = match.group("target").strip()
            if not target or target.startswith("http") or target.startswith("mailto"):
                continue
            if target.startswith("#"):
                continue
            local_target = target.split("#", 1)[0]
            if not local_target:
                continue
            resolved = os.path.normpath(os.path.join(base_dir, local_target))
            if not os.path.exists(resolved):
                broken_links.append(
                    f"Enlace roto: {match.group('label')} -> {target}"
                )

    for line in lines:
        stripped = line.strip()
        if stripped.startswith("```") or stripped.startswith("~~~"):
            in_code = not in_code
            if in_code:
                code_blocks += 1
            continue
        if in_code:
            continue
        heading_match = re.match(r"^(#{1,6})\s+(.*)", line)
        if heading_match:
            _flush_paragraph()
            level = len(heading_match.group(1))
            text_value = heading_match.group(2).strip()
            headings.append({"level": level, "text": text_value})
            heading_texts.append(text_value.lower())
            if EMOJI_PATTERN.search(text_value):
                emoji_headings += 1
            _collect_links(line)
            continue
        _collect_links(line)
        list_match = re.match(r"^\s*([-*+]\s+|\d+\.\s+)(.*)", line)
        if list_match:
            content = list_match.group(2).strip()
            if list_match.group(1).strip().endswith("."):
                ordered_items += 1
            else:
                list_items += 1
            if content.startswith("[ ") or content.startswith("[x"):
                checkbox_items += 1
            paragraphs.append(content)
            continue
        if not stripped:
            _flush_paragraph()
        else:
            buffer.append(stripped)

    _flush_paragraph()

    return {
        "headings": headings,
        "heading_texts": heading_texts,
        "paragraphs": paragraphs,
        "list_items": list_items,
        "ordered_items": ordered_items,
        "checkbox_items": checkbox_items,
        "code_blocks": code_blocks,
        "emoji_headings": emoji_headings,
        "broken_links": broken_links,
        "lower_text": text.lower(),
        "word_count": len(text.split()),
    }


def _keyword_score(structure: Dict[str, object], keywords: List[str]) -> float:
    if not keywords:
        return 0.0
    lowered = structure.get("lower_text", "")
    matches = 0
    normalized = {kw.lower() for kw in keywords}
    for keyword in normalized:
        if keyword and keyword in lowered:
            matches += 1
    ratio = matches / max(1, len(normalized))
    heading_texts = structure.get("heading_texts", [])
    if heading_texts:
        for heading in heading_texts:
            if any(keyword in heading for keyword in normalized):
                ratio = min(1.0, ratio + 0.2)
                break
    return ratio


def _evaluate_consistency(structure: Dict[str, object]) -> float:
    penalty = 0.0
    headings: List[Dict[str, object]] = structure.get("headings", [])
    if not headings or headings[0].get("level") != 1:
        penalty += 0.3
    heading_levels = {item.get("level") for item in headings if item.get("level")}
    if len(heading_levels) > 3:
        penalty += 0.2
    if structure.get("emoji_headings", 0) == 0:
        penalty += 0.1
    broken_links = structure.get("broken_links", [])
    if broken_links:
        penalty += min(0.4, 0.1 * len(broken_links))
    ratio = max(0.0, 1.0 - penalty)
    return ratio


def _evaluate_applicability(structure: Dict[str, object], keywords: List[str]) -> float:
    ratio = _keyword_score(structure, keywords)
    action_signals = (
        structure.get("list_items", 0)
        + structure.get("ordered_items", 0)
        + structure.get("checkbox_items", 0)
        + structure.get("code_blocks", 0)
    )
    if action_signals >= 6:
        ratio = max(ratio, 1.0)
    elif action_signals >= 4:
        ratio = max(ratio, 0.75)
    elif action_signals >= 2:
        ratio = max(ratio, 0.5)
    elif action_signals >= 1:
        ratio = max(ratio, 0.3)
    return min(1.0, ratio)


def _evaluate_document(path: str, repo) -> Optional[DocumentAudit]:
    abs_path = os.path.join(ROOT, path)
    try:
        with open(abs_path, "r", encoding="utf-8") as handle:
            content = handle.read()
    except FileNotFoundError:
        logging.warning("No se pudo leer %s", abs_path)
        return None

    if not content.strip():
        logging.info("%s está vacío, se omite en el resumen", path)
        return None

    structure = _parse_markdown_structure(path, content)
    scores: Dict[str, int] = {}
    missing: List[str] = []
    suggestions: List[str] = []
    issues: List[str] = list(structure.get("broken_links", []))

    for key, config in CRITERIA_CONFIG.items():
        ratio = 0.0
        if config.get("type") == "consistency":
            ratio = _evaluate_consistency(structure)
        elif config.get("type") == "applicability":
            ratio = _evaluate_applicability(structure, config.get("keywords", []))
        else:
            ratio = _keyword_score(structure, config.get("keywords", []))
        score = _ratio_to_score(ratio)
        scores[key] = score
        if score <= 2:
            missing.append(config["label"])
        if score <= 3 and config.get("suggestion"):
            suggestions.append(f"{config['label']}: {config['suggestion']}")

    title = next(
        (heading["text"] for heading in structure.get("headings", []) if heading),
        os.path.basename(path),
    )
    last_modified = _last_modified(repo, path)
    return DocumentAudit(
        path=path,
        title=title,
        scores=scores,
        missing_sections=missing,
        suggestions=suggestions,
        issues=issues,
        last_modified=last_modified,
    )


def _render_audit_report(reports: List[DocumentAudit]) -> str:
    if not reports:
        return "# Content Audit Report\n\nNo se encontraron documentos para auditar."

    generated = _utcnow().strftime("%Y-%m-%d %H:%M UTC")
    headers = [
        "Documento",
        "Última edición",
        *[config["label"] for config in CRITERIA_CONFIG.values()],
        "Total",
        "Estado",
        "Notas",
    ]
    lines = ["# Content Audit Report", "", f"Generado: {generated}", ""]
    lines.append("| " + " | ".join(headers) + " |")
    lines.append("| " + " | ".join(["---"] * len(headers)) + " |")
    max_score = len(CRITERIA_CONFIG) * 5

    for report in reports:
        row = [f"[{report.path}]({report.path})", report.last_modified]
        for key in CRITERIA_CONFIG.keys():
            row.append(_score_with_icon(report.scores.get(key, 0)))
        row.append(f"{report.total_score}/{max_score}")
        row.append(report.status_icon)
        note = ", ".join(report.missing_sections[:1] + report.issues[:1])
        row.append(note or "Listo")
        lines.append("| " + " | ".join(row) + " |")

    lines.append("")
    for report in reports:
        lines.append(f"## {report.title} (`{report.path}`)")
        lines.append(
            f"- Puntaje: {report.status_icon} {report.total_score}/{max_score}"
        )
        lines.append(f"- Última edición: {report.last_modified}")
        if report.missing_sections:
            lines.append("- Secciones a reforzar:")
            for item in report.missing_sections:
                lines.append(f"  - {item}")
        if report.suggestions:
            lines.append("- Sugerencias rápidas:")
            for suggestion in report.suggestions:
                lines.append(f"  - {suggestion}")
        if report.issues:
            lines.append("- Problemas detectados:")
            for issue in report.issues:
                lines.append(f"  - {issue}")
        lines.append("")

    return "\n".join(lines)


def _render_docs_with_issues(reports: List[DocumentAudit]) -> str:
    pending = [
        report
        for report in reports
        if report.missing_sections or report.issues or report.suggestions
    ]
    if not pending:
        return "# Docs with issues\n\nTodo está alineado."

    generated = _utcnow().strftime("%Y-%m-%d %H:%M UTC")
    lines = ["# Docs with issues", "", f"Generado: {generated}", ""]
    max_score = len(CRITERIA_CONFIG) * 5
    for report in pending:
        lines.append(f"## {report.title} (`{report.path}`)")
        lines.append(f"- Estado: {report.status_icon} {report.total_score}/{max_score}")
        lines.append(f"- Última edición: {report.last_modified}")
        for item in report.missing_sections:
            lines.append(f"- [ ] Profundizar en {item.lower()}.")
        for suggestion in report.suggestions:
            lines.append(f"- [ ] {suggestion}")
        for issue in report.issues:
            lines.append(f"- [ ] {issue}")
        lines.append("")
    return "\n".join(lines)


def _write_content_audit_reports(reports: List[DocumentAudit]) -> Dict[str, str]:
    if not reports:
        return {}
    audit_md = _render_audit_report(reports)
    issues_md = _render_docs_with_issues(reports)
    with open(AUDIT_REPORT_PATH, "w", encoding="utf-8") as handle:
        handle.write(audit_md)
    with open(ISSUES_REPORT_PATH, "w", encoding="utf-8") as handle:
        handle.write(issues_md)
    payload = {
        "generated_at": _utc_timestamp(),
        "max_score": len(CRITERIA_CONFIG) * 5,
        "documents": [report.to_dict() for report in reports],
    }
    with open(JSON_REPORT_PATH, "w", encoding="utf-8") as handle:
        json.dump(payload, handle, ensure_ascii=False, indent=2)
    return {
        "audit": os.path.relpath(AUDIT_REPORT_PATH, ROOT),
        "issues": os.path.relpath(ISSUES_REPORT_PATH, ROOT),
        "json": os.path.relpath(JSON_REPORT_PATH, ROOT),
    }


def run_content_audit() -> Dict[str, object]:
    documents = _collect_markdown_documents()
    if not documents:
        logging.info("No hay documentos markdown bajo las carpetas objetivo.")
        return {}
    repo = _try_load_repo()
    reports: List[DocumentAudit] = []
    for doc in documents:
        report = _evaluate_document(doc, repo)
        if report:
            reports.append(report)
    if not reports:
        return {}
    outputs = _write_content_audit_reports(reports)
    return {
        "documents": [report.to_dict() for report in reports],
        "generated_at": _utc_timestamp(),
        "reports": outputs,
    }


def file_contains(path, substrings):
    try:
        with open(
            os.path.join(ROOT, path), "r", encoding="utf-8", errors="ignore"
        ) as f:
            text = f.read()
        return all(s in text for s in substrings)
    except FileNotFoundError:
        return False


def path_exists(all_paths):
    return all(os.path.exists(os.path.join(ROOT, p)) for p in all_paths)


def score_rules(rules):
    score = 0
    breakdown = []
    for name, rule in rules.items():
        ok = True
        if "file" in rule and "must_contain" in rule:
            ok = file_contains(rule["file"], rule["must_contain"])
        if "path_exists" in rule:
            ok = ok and path_exists(rule["path_exists"])
        pts = rule.get("weight", 1) if ok else 0
        score += pts
        breakdown.append({"rule": name, "ok": ok, "weight": rule.get("weight", 1)})
    return score, breakdown


def summarize_audit_inputs():
    personas = scenarios = impacts = 0
    for sub in ("personas", "escenarios", "impactos"):
        directory = os.path.join(AUDIT, sub)
        if os.path.isdir(directory):
            count = sum(
                1 for f in os.listdir(directory) if f.endswith((".yml", ".yaml"))
            )
            if sub == "personas":
                personas = count
            if sub == "escenarios":
                scenarios = count
            if sub == "impactos":
                impacts = count
    return {"personas": personas, "scenarios": scenarios, "impacts": impacts}


def _extract_section_lines(lines: List[str], heading_prefix: str) -> List[str]:
    """Return the lines under a level-two heading matching the prefix."""

    if not heading_prefix:
        return []

    buffer: List[str] = []
    collecting = False
    target = heading_prefix.strip().lower()

    for line in lines:
        if line.startswith("## "):
            title = line[3:].strip()
            if title.lower().startswith(target):
                collecting = True
                continue
            if collecting:
                break
        if collecting:
            buffer.append(line.rstrip())

    return buffer


def _extract_list_items(lines: List[str], limit: int = 10) -> List[str]:
    """Parse ordered or unordered markdown list items."""

    items: List[str] = []
    pattern = re.compile(r"^(?:[-*]|\d+\.)\s+(.*)")

    for line in lines:
        stripped = line.strip()
        if not stripped:
            continue
        match = pattern.match(stripped)
        if match:
            items.append(match.group(1).strip())
        if len(items) >= limit:
            break

    return items


def _collect_stage_blocks(lines: List[str]) -> List[Dict[str, object]]:
    """Capture the stage headings and their descriptive text."""

    stages: List[Dict[str, object]] = []
    current_title: Optional[str] = None
    buffer: List[str] = []

    def _flush_current():
        nonlocal buffer
        if current_title:
            stages.append(
                {
                    "title": current_title,
                    "details": "\n".join(line.rstrip() for line in buffer).strip(),
                }
            )
            buffer = []

    for line in lines:
        if line.startswith("### Stage"):
            _flush_current()
            current_title = line.strip("# ").strip()
            continue
        if line.startswith("## "):
            _flush_current()
            current_title = None
            continue
        if current_title is not None:
            buffer.append(line)

    if current_title:
        _flush_current()

    return stages


def _summarize_block(text: str, max_lines: int = 6) -> List[str]:
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    return lines[:max_lines]


def extract_roadmap_context(path: Optional[str] = None) -> Dict[str, object]:
    """Read implementation/roadmap.md and expose the key planning context."""

    target_path = path or os.path.join(ROOT, "implementation", "roadmap.md")
    try:
        with open(target_path, "r", encoding="utf-8") as handle:
            raw_lines = handle.read().splitlines()
    except FileNotFoundError:
        return {}

    context: Dict[str, object] = {"source": os.path.relpath(target_path, ROOT)}

    current_heading = None
    for line in raw_lines:
        if line.startswith("## "):
            title = line[3:].strip()
            if title.lower().startswith("current state"):
                current_heading = title
                break
    if current_heading:
        context["current_state_heading"] = current_heading

    current_lines = _extract_section_lines(raw_lines, "Current state")
    current_points = _extract_list_items(current_lines, limit=5)
    if current_points:
        context["current_state_points"] = current_points

    steps_lines = _extract_section_lines(raw_lines, "Immediate next steps")
    next_steps = _extract_list_items(steps_lines, limit=10)
    if next_steps:
        context["immediate_next_steps"] = next_steps

    stages = _collect_stage_blocks(raw_lines)
    for stage in stages:
        title = stage.get("title", "")
        if title and "✅" not in title:
            summary = _summarize_block(stage.get("details", ""))
            context["next_stage"] = {"title": title, "summary": summary}
            break

    if len(context) == 1:  # only the source path was captured
        return {}

    return context


def _summarize_failures(summary):
    """Build a terse rationale based on the deterministic audit results."""

    breakdown = summary.get("breakdown", [])
    failed_rules = [
        item.get("rule", "unknown") for item in breakdown if not item.get("ok", False)
    ]

    if summary.get("passed"):
        return (
            f"Score {summary.get('score')} meets the pass threshold "
            f"of {summary.get('pass_score')}"
            + (
                ". All required rules passed."
                if not failed_rules
                else ". Minor rule deviations detected but overall score passed."
            )
        )

    if failed_rules:
        failures = ", ".join(failed_rules[:5])
        if len(failed_rules) > 5:
            failures += ", …"
        return (
            f"Score {summary.get('score')} below pass threshold "
            f"{summary.get('pass_score')}. Failing rules: {failures}."
        )

    return (
        f"Score {summary.get('score')} below pass threshold {summary.get('pass_score')}"
    )


def _llm_payload(summary, endpoint="chat"):
    model = os.environ.get("LLM_MODEL", "DeepSeek-R1-Distill-Qwen-14B-W4A16")
    system_prompt = (
        "You are assisting with an internal audit. Given the JSON summary of the "
        "automated checks, return a short JSON object with the fields 'status' "
        "(values: PASS or FAIL) and 'rationale' (a concise explanation)."
    )
    summary_text = json.dumps(summary, ensure_ascii=False)
    if endpoint == "responses":
        return {
            "model": model,
            "input": [
                {
                    "role": "system",
                    "content": [{"type": "text", "text": system_prompt}],
                },
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": (
                                "Audit summary:\n"
                                + summary_text
                                + "\nRespond only with JSON."
                            ),
                        }
                    ],
                },
            ],
            "temperature": 0.1,
            "max_output_tokens": 200,
        }

    return {
        "model": model,
        "messages": [
            {"role": "system", "content": system_prompt},
            {
                "role": "user",
                "content": (
                    "Audit summary:\n" + summary_text + "\nRespond only with JSON."
                ),
            },
        ],
        "temperature": 0.1,
        "max_tokens": 200,
    }


def _join_url(base, path):
    """Helper to safely append a path segment to the provided base URL."""

    return urljoin(base.rstrip("/") + "/", path.lstrip("/"))


def _expand_candidate(seed):
    """Return candidate URLs inferred from the provided seed value."""

    if not seed:
        return []

    seed = seed.strip()
    if not seed:
        return []

    parsed = urlparse(seed)
    path = parsed.path.rstrip("/")

    if path.endswith("/chat/completions"):
        return [(seed.rstrip("/"), "chat")]
    if path.endswith("/responses"):
        return [(seed.rstrip("/"), "responses")]

    # If the seed already includes a path (e.g. /v1) treat it as a base path.
    if path:
        base = seed.rstrip("/")
        return [
            (_join_url(base, "chat/completions"), "chat"),
            (_join_url(base, "responses"), "responses"),
        ]

    # Otherwise assume it is only the origin and append the OpenAI-compatible paths.
    with_v1 = _join_url(seed, "v1")
    return [
        (_join_url(with_v1, "chat/completions"), "chat"),
        (_join_url(with_v1, "responses"), "responses"),
    ]


def _candidate_urls():
    """Determine the sequence of URLs to try when contacting the LLM service."""

    env_url = os.environ.get("LLM_API_URL")
    default_seed = "https://litellm-litemaas.apps.prod.rhoai.rh-aiservices-bu.com/v1/chat/completions"
    candidates = OrderedDict()

    for seed in filter(None, [env_url, default_seed]):
        for url, endpoint in _expand_candidate(seed):
            candidates.setdefault((url, endpoint), None)

    # Ensure we also consider the responses endpoint for the default seed.
    for url, endpoint in _expand_candidate(
        "https://litellm-litemaas.apps.prod.rhoai.rh-aiservices-bu.com/v1/responses"
    ):
        candidates.setdefault((url, endpoint), None)

    return list(candidates.keys())


def _extract_message(payload):
    """Extract the textual message from different response schemas."""

    # OpenAI / LiteLLM chat completion format
    choices = payload.get("choices")
    if choices:
        message = choices[0].get("message", {})

        # OpenAI compatible responses normally return a string in "content"
        content = message.get("content", "")
        if isinstance(content, str) and content.strip():
            return content.strip()

        # Some providers (including LiteLLM reasoning models) return a list of
        # message parts. Collect the textual pieces if present.
        if isinstance(content, list):
            parts = []
            for item in content:
                if isinstance(item, str) and item.strip():
                    parts.append(item.strip())
                elif isinstance(item, dict):
                    text = item.get("text") or item.get("value")
                    if isinstance(text, str) and text.strip():
                        parts.append(text.strip())
            if parts:
                return "\n".join(parts)

        # Reasoning models (e.g. DeepSeek-R1) may surface the assistant reply
        # under "reasoning_content" while leaving "content" empty when the
        # response is truncated. Treat it as a fallback so we can surface the
        # provider's output instead of treating it as an empty response.
        reasoning = message.get("reasoning_content")
        if isinstance(reasoning, str) and reasoning.strip():
            return reasoning.strip()

    # OpenAI responses API format
    output = payload.get("output") or payload.get("outputs")
    if output:
        parts = []
        for item in output:
            for content in item.get("content", []):
                if content.get("type") in {"output_text", "text"}:
                    text = content.get("text", "")
                    if text:
                        parts.append(text.strip())
        if parts:
            return "\n".join(part for part in parts if part)

    # Some providers return the message directly at the top level
    for key in ("message", "response", "result"):
        value = payload.get(key)
        if isinstance(value, str) and value.strip():
            return value.strip()

    return ""


def maybe_llm_verdict(summary):
    """Optional step that relies on OPENAI_API_KEY to request a qualitative verdict."""

    api_key = os.environ.get("LITELLM_API_KEY") or os.environ.get("OPENAI_API_KEY")
    if not api_key:
        return {
            "llm_used": False,
            "verdict": {
                "status": "PASS" if summary.get("passed") else "FAIL",
                "rationale": _summarize_failures(summary),
            },
            "basis": "deterministic audit rules",
        }

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}",
    }

    errors = []

    for api_url, endpoint in _candidate_urls():
        request_body = json.dumps(_llm_payload(summary, endpoint)).encode("utf-8")
        request = urllib.request.Request(
            api_url,
            data=request_body,
            headers=headers,
            method="POST",
        )

        try:
            with urllib.request.urlopen(request, timeout=30) as response:
                raw_body = response.read().decode("utf-8")
                payload = json.loads(raw_body)
        except urllib.error.HTTPError as exc:
            body = exc.read().decode("utf-8", errors="ignore") if exc.fp else ""
            logging.error("LLM request failed for %s: %s", api_url, body or exc)
            if exc.code in {404, 405}:
                errors.append({"url": api_url, "status": exc.code, "error": body})
                continue
            return {
                "llm_used": False,
                "verdict": f"error contacting LLM (status {exc.code})",
                "error": body or str(exc),
            }
        except (urllib.error.URLError, TimeoutError) as exc:
            logging.error("LLM request error for %s: %s", api_url, exc)
            errors.append({"url": api_url, "error": str(exc)})
            continue
        except json.JSONDecodeError as exc:
            logging.error("Invalid JSON from LLM response: %s", exc)
            return {"llm_used": False, "verdict": "invalid JSON from LLM response"}

        message = _extract_message(payload)

        if not message:
            logging.warning(
                "Empty message from LLM response (%s): %s", api_url, payload
            )
            errors.append({"url": api_url, "error": "empty response", "raw": payload})
            continue

        try:
            verdict = json.loads(message)
        except json.JSONDecodeError:
            verdict = {"status": "UNKNOWN", "rationale": message}

        return {
            "llm_used": True,
            "verdict": verdict,
            "raw": payload,
            "endpoint": api_url,
        }

    return {
        "llm_used": False,
        "verdict": "error contacting LLM",
        "attempts": errors,
    }


def _run_git_command(args: List[str]) -> str:
    try:
        result = subprocess.run(
            ["git", *args],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as exc:
        logging.warning("git %s failed: %s", " ".join(args), exc)
        return ""


def _determine_base_commit() -> Optional[str]:
    event_path = os.environ.get("GITHUB_EVENT_PATH")
    if event_path and os.path.isfile(event_path):
        try:
            with open(event_path, "r", encoding="utf-8") as fp:
                payload = json.load(fp)
        except (OSError, json.JSONDecodeError) as exc:
            logging.warning("Unable to parse event payload: %s", exc)
        else:
            pr = payload.get("pull_request")
            if isinstance(pr, dict):
                sha = pr.get("base", {}).get("sha")
                if sha:
                    return sha
            before = payload.get("before")
            if isinstance(before, str) and before.strip():
                return before.strip()

    base_ref = os.environ.get("GITHUB_BASE_REF")
    if base_ref:
        ref = f"origin/{base_ref}"
        sha = _run_git_command(["rev-parse", ref])
        if sha:
            return sha

    sha = _run_git_command(["rev-parse", "HEAD^"])
    return sha or None


def collect_change_summary() -> Dict[str, object]:
    base = _determine_base_commit()
    summary: Dict[str, object] = {}
    if base:
        summary["base_commit"] = base
        names = _run_git_command(["diff", f"{base}...HEAD", "--name-only"])
        if names:
            files = [line for line in names.splitlines() if line.strip()]
            summary["changed_files"] = files
            summary["changed_file_count"] = len(files)
        diffstat = _run_git_command(["diff", f"{base}...HEAD", "--stat"])
        if diffstat:
            lines = diffstat.splitlines()
            if len(lines) > 20:
                lines = lines[:19] + ["…" + lines[-1]]
            summary["diffstat"] = "\n".join(lines)
    else:
        logging.info("Unable to determine base commit; diff summary unavailable")

    return summary


def _github_request(
    method: str,
    path: str,
    token: str,
    payload: Optional[Dict[str, object]] = None,
) -> Dict[str, object]:
    url = f"{GITHUB_API_URL.rstrip('/')}/{path.lstrip('/')}"
    data = json.dumps(payload).encode("utf-8") if payload is not None else None
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {token}",
    }
    if data is not None:
        headers["Content-Type"] = "application/json"

    request = urllib.request.Request(url, data=data, headers=headers, method=method)
    with urllib.request.urlopen(request, timeout=30) as response:
        body = response.read().decode("utf-8")
    return json.loads(body) if body else {}


def _ensure_label(
    repo: str, token: str, name: str, color: str, description: str
) -> None:
    try:
        _github_request("GET", f"/repos/{repo}/labels/{quote(name)}", token)
        return
    except urllib.error.HTTPError as exc:
        if exc.code != 404:
            raise

    payload = {"name": name, "color": color, "description": description}
    try:
        _github_request("POST", f"/repos/{repo}/labels", token, payload)
    except urllib.error.HTTPError as exc:
        # Ignore race conditions where another workflow created it first
        if exc.code != 422:
            raise


def _find_existing_issue(
    repo: str, token: str, fingerprint: str
) -> Optional[Dict[str, object]]:
    params = f"state=open&labels={quote('automation:audit')}"  # urlencoded
    try:
        issues = _github_request(
            "GET", f"/repos/{repo}/issues?{params}&per_page=100", token
        )
    except urllib.error.HTTPError as exc:
        logging.warning("Unable to list issues: %s", exc)
        return None

    if isinstance(issues, list):
        marker = f"<!-- audit-fingerprint: {fingerprint} -->"
        for issue in issues:
            if marker in issue.get("body", ""):
                return issue
    return None


def _render_issue_body(
    failing_rules: List[str],
    rubric_rules: Dict[str, object],
    summary: Dict[str, object],
    fingerprint: str,
) -> str:
    body_lines = [
        "## Audit improvement opportunity",
        "",
        "The automated audit detected the following failing rules:",
    ]

    for rule in failing_rules:
        body_lines.append(f"- `{rule}`")

    body_lines.extend(["", "### Rule requirements"])
    for rule in failing_rules:
        body_lines.append(f"- `{rule}`")
        rule_details = _describe_rule(rule, rubric_rules.get(rule, {}))
        for detail in rule_details:
            for detail_line in detail.splitlines():
                body_lines.append(f"  {detail_line}")

    body_lines.extend(
        [
            "",
            "### Suggested next steps",
            "- Review the failing rule(s) and propose concrete improvements.",
            "- Use the local LLM workflow to draft changes that address the issues.",
            "- Open a pull request referencing this issue and ensure the audit passes.",
        ]
    )

    diff = summary.get("changes", {})
    if diff:
        body_lines.extend(["", "### Context from the triggering run"])
        base_commit = diff.get("base_commit")
        if base_commit:
            body_lines.append(f"- Base commit: `{base_commit}`")
        file_count = diff.get("changed_file_count")
        if file_count:
            body_lines.append(f"- Files changed: {file_count}")
        changed_files = diff.get("changed_files", [])
        if changed_files:
            preview = "\n".join(f"  - {name}" for name in changed_files[:15])
            if preview:
                body_lines.extend(["- Sample of changed files:", preview])
        diffstat = diff.get("diffstat")
        if diffstat:
            body_lines.extend(["", "```", diffstat, "```"])

    roadmap_lines = _roadmap_issue_lines(summary.get("roadmap") or {})
    if roadmap_lines:
        body_lines.extend(["", "### Roadmap alignment context"])
        body_lines.extend(roadmap_lines)

    codex_prompt = _build_codex_prompt(summary, failing_rules, rubric_rules)
    if codex_prompt.strip():
        body_lines.extend(
            [
                "",
                "### Prompt for Codex or other LLM",
                "Copy the following block into Codex to generate a remediation plan:",
                "",
                "```",
                codex_prompt,
                "```",
            ]
        )

    body_lines.extend(
        [
            "",
            f"<!-- audit-fingerprint: {fingerprint} -->",
        ]
    )

    return "\n".join(body_lines)


def _describe_rule(name: str, rule: Dict[str, object]) -> List[str]:
    """Return a human-readable bullet list describing the rule requirements."""

    if not rule:
        return [f"- No metadata available for `{name}`."]

    details = []
    weight = rule.get("weight")
    if weight is not None:
        details.append(f"- Weight: {weight}")

    target_file = rule.get("file")
    if target_file:
        details.append(f"- File to inspect: `{target_file}`")

    must_contain = rule.get("must_contain") or []
    if must_contain:
        formatted = "\n".join(f"    - `{value}`" for value in must_contain)
        details.append("- Required content in file:\n" + formatted)

    paths = rule.get("path_exists") or []
    if paths:
        formatted = "\n".join(f"    - `{path}`" for path in paths)
        details.append("- Required paths:\n" + formatted)

    return details or [f"- `{name}` is marked as failing but has no extra details."]


def _roadmap_issue_lines(roadmap: Dict[str, object]) -> List[str]:
    if not roadmap:
        return []

    lines: List[str] = []
    source = roadmap.get("source")
    if source:
        lines.append(f"- Source: `{source}`")

    heading = roadmap.get("current_state_heading")
    if heading:
        lines.append(f"- Current state: {heading}")

    state_points = roadmap.get("current_state_points", [])
    if state_points:
        lines.append("  - Signals:")
        lines.extend(f"    - {point}" for point in state_points)

    next_stage = roadmap.get("next_stage") or {}
    if next_stage.get("title"):
        lines.append(f"- Upcoming stage: {next_stage['title']}")
        for snippet in next_stage.get("summary", []):
            lines.append(f"  {snippet}")

    steps = roadmap.get("immediate_next_steps", [])
    if steps:
        lines.append("- Immediate next steps:")
        lines.extend(f"  - {step}" for step in steps)

    return lines


def _build_codex_prompt(
    summary: Dict[str, object],
    failing_rules: List[str],
    rubric_rules: Dict[str, object],
) -> str:
    """Create a detailed prompt that can be copied into Codex or another LLM."""

    score = summary.get("score")
    pass_score = summary.get("pass_score")
    audit_inputs = summary.get("audit_inputs", {})
    changes = summary.get("changes", {})

    lines: List[str] = [
        "You are assisting with thewise.tech internal audit automation.",
        "Update the repository so the audit passes.",
        "",
        f"Current audit score: {score} (pass threshold: {pass_score}).",
        "Failing rules:",
    ]

    for rule_name in failing_rules:
        rule = rubric_rules.get(rule_name, {})
        lines.append(f"- {rule_name}:")
        for detail in _describe_rule(rule_name, rule):
            # indent nested bullet lines for readability inside the prompt block
            detail_lines = detail.splitlines()
            if detail_lines:
                lines.extend(f"  {line}" for line in detail_lines)

    persona_count = audit_inputs.get("personas")
    scenario_count = audit_inputs.get("scenarios")
    impact_count = audit_inputs.get("impacts")

    lines.append("")
    lines.append("Repository context:")
    if persona_count is not None:
        lines.append(f"- Personas defined: {persona_count}")
    if scenario_count is not None:
        lines.append(f"- Scenarios defined: {scenario_count}")
    if impact_count is not None:
        lines.append(f"- Impact analyses defined: {impact_count}")

    base_commit = changes.get("base_commit")
    if base_commit:
        lines.append(f"- Base commit for comparison: {base_commit}")
    file_count = changes.get("changed_file_count")
    if file_count:
        lines.append(f"- Files changed in triggering ref: {file_count}")

    changed_files = changes.get("changed_files", [])
    if changed_files:
        lines.append("- Recently modified files:")
        preview = changed_files[:15]
        lines.extend(f"  - {name}" for name in preview)
        if len(changed_files) > len(preview):
            lines.append("  - …")

    diffstat = changes.get("diffstat")
    if diffstat:
        lines.append("")
        lines.append("Diff summary:")
        lines.extend(diffstat.splitlines())

    roadmap_lines = _roadmap_prompt_lines(summary.get("roadmap") or {})
    if roadmap_lines:
        lines.append("")
        lines.append("Roadmap alignment:")
        lines.extend(roadmap_lines)

    lines.extend(
        [
            "",
            "Deliverables:",
            "- Implement the necessary files and content updates to satisfy all failing rules.",
            "- Run the local quality checks (ruff, tests, knowledge/docs/link validation) before opening a PR.",
            "- Provide a summary of the changes in the PR description.",
        ]
    )

    return "\n".join(lines)


def _roadmap_prompt_lines(roadmap: Dict[str, object]) -> List[str]:
    if not roadmap:
        return []

    lines: List[str] = []

    heading = roadmap.get("current_state_heading")
    if heading:
        lines.append(f"- Current state: {heading}")

    next_stage = roadmap.get("next_stage") or {}
    if next_stage.get("title"):
        lines.append(f"- Upcoming stage: {next_stage['title']}")
        for snippet in next_stage.get("summary", []):
            lines.append(f"  {snippet}")

    steps = roadmap.get("immediate_next_steps", [])
    if steps:
        lines.append("- Immediate next steps:")
        lines.extend(f"  - {step}" for step in steps)

    return lines


def maybe_create_issue(
    summary: Dict[str, object], rubric: Dict[str, object]
) -> Dict[str, object]:
    failing_rules = [
        item.get("rule", "unknown")
        for item in summary.get("breakdown", [])
        if not item.get("ok", False)
    ]

    if not failing_rules:
        return {"created": False, "reason": "no failing rules"}

    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    repo = os.environ.get("GITHUB_REPOSITORY")
    if not token or not repo:
        return {"created": False, "reason": "missing GitHub credentials"}

    fingerprint = "|".join(sorted(failing_rules))
    try:
        _ensure_label(
            repo,
            token,
            "automation:audit",
            color="0E8A16",
            description="Automated audit improvements",
        )
    except Exception as exc:  # pragma: no cover
        logging.error("Unable to ensure audit label: %s", exc)
        return {"created": False, "error": str(exc)}

    rules = rubric.get("rules", {})
    rendered_body = _render_issue_body(failing_rules, rules, summary, fingerprint)

    existing = _find_existing_issue(repo, token, fingerprint)
    if existing:
        logging.info(
            "Audit improvement already tracked in issue #%s", existing.get("number")
        )
        existing_body = (existing.get("body") or "").strip()
        updated = False
        if existing_body != rendered_body.strip():
            logging.info(
                "Updating audit issue #%s with latest context", existing.get("number")
            )
            try:
                _github_request(
                    "PATCH",
                    f"/repos/{repo}/issues/{existing.get('number')}",
                    token,
                    {"body": rendered_body},
                )
                updated = True
            except urllib.error.HTTPError as exc:
                logging.error("Unable to update audit issue: %s", exc)
        return {
            "created": False,
            "reason": "existing issue",
            "issue": {
                "number": existing.get("number"),
                "url": existing.get("html_url"),
                "updated": updated,
            },
        }

    payload = {
        "title": f"Audit improvement: {', '.join(failing_rules[:3])}",
        "body": rendered_body,
        "labels": ["automation:audit"],
    }

    try:
        response = _github_request("POST", f"/repos/{repo}/issues", token, payload)
    except urllib.error.HTTPError as exc:
        error_body = exc.read().decode("utf-8", errors="ignore") if exc.fp else str(exc)
        logging.error("Unable to create audit issue: %s", error_body)
        return {"created": False, "error": error_body or str(exc)}

    logging.info("Created audit improvement issue #%s", response.get("number"))
    return {
        "created": True,
        "issue": {
            "number": response.get("number"),
            "url": response.get("html_url"),
        },
    }


def main():
    rubric = load_yaml(os.path.join(AUDIT, "rubric.yml"))
    score, breakdown = score_rules(rubric.get("rules", {}))
    thresholds = rubric.get("thresholds", {})
    pass_score = thresholds.get("pass_score", 30)
    inputs = summarize_audit_inputs()
    changes = collect_change_summary()
    roadmap = extract_roadmap_context()
    content_audit = run_content_audit()

    summary = {
        "score": score,
        "pass_score": pass_score,
        "passed": score >= pass_score,
        "breakdown": breakdown,
        "audit_inputs": inputs,
    }
    if changes:
        summary["changes"] = changes
    if roadmap:
        summary["roadmap"] = roadmap
    if content_audit:
        summary["content_audit"] = content_audit
    summary["failing_rules"] = [
        item.get("rule", "unknown") for item in breakdown if not item.get("ok", False)
    ]
    print(json.dumps(summary, ensure_ascii=False, indent=2))

    llm = maybe_llm_verdict(summary)
    print(json.dumps({"llm_evaluation": llm}, ensure_ascii=False))

    issue = maybe_create_issue(summary, rubric)
    print(json.dumps({"improvement_issue": issue}, ensure_ascii=False))

    if score < pass_score:
        print("Audit NOK: score below threshold.")
        sys.exit(2)

    print("Audit OK.")
    sys.exit(0)


if __name__ == "__main__":
    main()
