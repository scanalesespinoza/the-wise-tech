#!/usr/bin/env python3
"""Append a standardized feedback section to every Markdown document."""

from __future__ import annotations

from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
BLOCK = """---

🗳️ **¿Te fue útil este documento?**
- [ ] Sí, resolvió mi duda
- [ ] Más o menos, necesito más contexto
- [ ] No me ayudó

📢 [Abre un feedback aquí](https://github.com/scanalesespinoza/the-wise-tech/issues/new?template=feedback.yml)

---
""".strip()


def iter_markdown() -> list[Path]:
    return [path for path in sorted(REPO_ROOT.rglob("*.md")) if path.is_file()]


def ensure_feedback(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    if "🗳️ **¿Te fue útil este documento?**" in text:
        return False
    updated = text.rstrip() + "\n\n" + BLOCK + "\n"
    path.write_text(updated, encoding="utf-8")
    return True


def main() -> None:
    inserted = 0
    for md_file in iter_markdown():
        inserted += 1 if ensure_feedback(md_file) else 0
    print(f"Feedback section added to {inserted} files.")


if __name__ == "__main__":
    main()
