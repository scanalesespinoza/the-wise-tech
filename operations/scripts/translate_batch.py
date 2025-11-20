#!/usr/bin/env python3
#!/usr/bin/env python3
"""Traduce lotes de Markdown listados en audit/translation-queue.yml."""

from __future__ import annotations

import argparse
import json
import os
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable

import yaml

REPO_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_QUEUE = REPO_ROOT / "audit" / "translation-queue.yml"
CODE_BLOCK_PATTERN = re.compile(r"(```[\s\S]*?```)", re.MULTILINE)


class TranslationClient:
    """Abstracción mínima que puede reemplazarse por una llamada real a API."""

    def __init__(self) -> None:
        self.api_key = os.getenv("TRANSLATE_API_KEY")
        self.endpoint = os.getenv("TRANSLATE_API_URL")

    def translate(self, text: str) -> str:
        """Devuelve el texto traducido.

        Esta implementación por defecto es un no-op para evitar que el
        repositorio intente llamar a un API externo. Conecta tu proveedor
        reemplazando este método con la llamada HTTP que mejor se adapte a tu
        stack.
        """

        if not self.api_key or not self.endpoint:
            return text
        raise NotImplementedError(
            "Configure your translation provider before enabling live calls"
        )


GLOSSARY = {
    "error budget": "presupuesto de error",
    "observability": "observabilidad",
    "feedback loop": "bucle de feedback",
    "runbook": "runbook",
}


def apply_glossary(text: str) -> str:
    for source, target in GLOSSARY.items():
        text = re.sub(rf"\\b{re.escape(source)}\\b", target, text, flags=re.IGNORECASE)
    return text


def split_front_matter(markdown: str) -> tuple[str, str]:
    if not markdown.startswith("---"):
        return "", markdown
    closing = markdown.find("\n---", 3)
    if closing == -1:
        return "", markdown
    closing += len("\n---")
    # incluir la nueva línea final si está presente
    if len(markdown) > closing and markdown[closing] == "\n":
        closing += 1
    return markdown[:closing], markdown[closing:]


def chunk_markdown(body: str) -> Iterable[tuple[str, str]]:
    segments = CODE_BLOCK_PATTERN.split(body)
    for index, segment in enumerate(segments):
        if index % 2 == 1:
            yield "code", segment
        else:
            yield "text", segment


def translate_body(text: str, client: TranslationClient) -> str:
    translated_parts: list[str] = []
    for kind, chunk in chunk_markdown(text):
        if kind == "code":
            translated_parts.append(chunk)
            continue
        translated = client.translate(chunk)
        translated_parts.append(apply_glossary(translated))
    return "".join(translated_parts)


def read_queue(path: Path) -> dict[str, Any]:
    return yaml.safe_load(path.read_text(encoding="utf-8")) or {}


def find_batch(
    queue: dict[str, Any], batch_id: str
) -> tuple[dict[str, Any], dict[str, Any]]:
    for wave in queue.get("waves", []):
        for batch in wave.get("batches", []):
            if batch.get("id") == batch_id:
                return wave, batch
    raise KeyError(f"Batch {batch_id} not found")


def ensure_parent(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)


def update_queue(path: Path, queue: dict[str, Any]) -> None:
    path.write_text(
        yaml.safe_dump(queue, sort_keys=False, allow_unicode=True),
        encoding="utf-8",
    )


def process_entry(
    entry: dict[str, Any],
    client: TranslationClient,
    remaining_chars: int,
    dry_run: bool,
) -> tuple[int, dict[str, Any]]:
    status = entry.get("status", "pending")
    if status not in {"pending", "in-progress"}:
        return remaining_chars, {
            "path": entry.get("path_es"),
            "result": "skipped-status",
        }

    source = REPO_ROOT / entry["path_en"]
    target = REPO_ROOT / entry["path_es"]
    if not source.exists():
        entry["status"] = "blocked"
        entry["notes"] = f"Missing EN source: {entry['path_en']}"
        return remaining_chars, {"path": entry["path_en"], "result": "missing-en"}

    content = source.read_text(encoding="utf-8")
    front_matter, body = split_front_matter(content)
    char_cost = len(body)
    if char_cost > remaining_chars:
        return remaining_chars, {"path": entry["path_en"], "result": "skipped-budget"}

    translated = translate_body(body, client)
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    result = {
        "path": entry["path_en"],
        "chars": char_cost,
        "result": "preview" if dry_run else "translated",
    }

    if not dry_run:
        ensure_parent(target)
        target.write_text(front_matter + translated, encoding="utf-8")
        entry["status"] = "done"
        entry["last_run"] = now
        entry.setdefault("notes", "")
        entry["notes"] = entry["notes"].strip() or ""
    return remaining_chars - char_cost, result


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--batch", required=True, help="Batch ID (e.g. w1-b1)")
    parser.add_argument(
        "--queue",
        default=str(DEFAULT_QUEUE),
        help="Override queue path (defaults to audit/translation-queue.yml)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Simulate the process without writing files or updating the queue",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    queue_path = Path(args.queue)
    queue = read_queue(queue_path)
    wave, batch = find_batch(queue, args.batch)
    char_budget = int(
        batch.get("char_budget") or os.getenv("GT_MAX_CHARS_PER_BATCH", 80000)
    )
    remaining = char_budget
    client = TranslationClient()
    processed: list[dict[str, Any]] = []

    for entry in batch.get("entries", []):
        remaining, result = process_entry(entry, client, remaining, args.dry_run)
        processed.append(result)
        if remaining <= 0:
            break

    if not args.dry_run:
        batch["last_run"] = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
        wave.setdefault("history", []).append(
            {
                "batch": batch["id"],
                "timestamp": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC"),
                "processed": len(processed),
            }
        )
        update_queue(queue_path, queue)

    summary = {
        "batch": batch["id"],
        "char_budget": char_budget,
        "remaining_chars": remaining,
        "dry_run": args.dry_run,
        "processed": processed,
    }
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
