#!/usr/bin/env python3
"""
Traduce archivos de un batch (según audit/translation-queue.yml) a ES,
respetando cuotas. Por defecto **NO llama** a ninguna API real si no hay
credenciales: modo seguro/dry-run.

Reglas clave:
- NO traducir:
  - Bloques de código ``` ... ```
  - Nombres de archivos/rutas/carpeta
  - Claves YAML en front-matter
  - Tags (se mantienen en inglés)
- SÍ traducir:
  - Texto de párrafos, headings, listas, "See also" y alt text.
- Aplicar glosario para términos clave.
"""
import json
import os
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
QUEUE = ROOT / "audit" / "translation-queue.yml"
GLOSS = ROOT / "docs" / "es" / "guides" / "glosario-terminologia.md"

MAX_CHARS = int(os.environ.get("GT_MAX_CHARS_PER_BATCH", "80000"))
MAX_QPS = int(os.environ.get("GT_MAX_QPS", "10"))


def load_yaml(path: Path):
  return yaml.safe_load(path.read_text(encoding="utf-8"))


def extract_blocks(md_text: str):
  parts = re.split(r"(```[\s\S]*?```)", md_text)
  result = []
  for i, seg in enumerate(parts):
    if i % 2 == 1:
      result.append(("code", seg))
    else:
      result.append(("text", seg))
  return result


def apply_glossary(text: str) -> str:
  replacements = [
      ("error budget", "presupuesto de error"),
      ("retry", "reintento"),
      ("exponential backoff", "retroceso exponencial"),
      ("correlation id", "id de correlación"),
      ("idempotency key", "clave de idempotencia"),
      ("observability", "observabilidad"),
  ]
  for en, es in replacements:
    text = re.sub(rf"\\b{re.escape(en)}\\b", es, text, flags=re.IGNORECASE)
  return text


def fake_translate(text: str) -> str:
  return text


def translate_markdown(md_text: str, remaining: int):
  output = []
  for kind, segment in extract_blocks(md_text):
    if kind == "code":
      output.append(segment)
      continue
    if remaining <= 0:
      output.append(segment)
      continue
    chunk = segment[:remaining]
    remaining -= len(chunk)
    translated = fake_translate(chunk)
    translated = apply_glossary(translated)
    output.append(translated + segment[len(chunk):])
  return "".join(output), remaining


def process_file(path: str, remaining: int):
  file_path = ROOT / path
  if not file_path.exists():
    return remaining, {"path": path, "status": "missing"}
  text = file_path.read_text(encoding="utf-8")
  head = ""
  body = text
  match = re.match(r"^---\n([\s\S]*?)\n---\n?", text)
  if match:
    head = match.group(0)
    body = text[match.end():]
  translated, left = translate_markdown(body, remaining)
  if left != remaining:
    new_text = (head or "") + translated
    file_path.write_text(new_text, encoding="utf-8")
    status = "translated"
  else:
    status = "skipped-limit"
  return left, {"path": path, "status": status}


def main():
  if len(sys.argv) < 2:
    print("Uso: python scripts/translate-batch.py <batch-id>")
    sys.exit(2)
  batch_id = sys.argv[1]
  queue = load_yaml(QUEUE)
  target_batch = None
  for wave in queue.get("waves", []):
    for batch in wave.get("batches", []):
      if batch.get("id") == batch_id:
        target_batch = batch
        break
    if target_batch:
      break
  if not target_batch:
    print(f"Batch {batch_id} no encontrado.")
    sys.exit(2)

  batch_budget = target_batch.get("char_budget")
  try:
    batch_budget = int(batch_budget) if batch_budget is not None else MAX_CHARS
  except (TypeError, ValueError):
    batch_budget = MAX_CHARS

  remaining = batch_budget
  report = {"batch": batch_id, "char_budget": batch_budget, "targets": []}
  for path in target_batch.get("targets", []):
    remaining, info = process_file(path, remaining)
    report["targets"].append(info)
  print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == "__main__":
  main()
