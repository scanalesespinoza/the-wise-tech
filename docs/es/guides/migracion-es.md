---
title: "Migración a español — Proceso por lotes"
tags: ["docs", "i18n", "editorial"]
---
# Migración a español — Proceso por lotes

- **Español canónico**: el contenido se prioriza en español.
- Migramos en **waves** (3–5 días) y **batches** (10–20 archivos o ≤80k caracteres).
- **No traducir**:
  - Bloques de código (```), nombres de archivos, rutas, carpetas, claves YAML.
  - Tags de front-matter (mantenerlos en inglés).
- **Sí traducir**:
  - Títulos, párrafos, listas, “See also”, alt text, texto de navegación.
- **QA automática** (usa `make docs-qa`):
  - `mkdocs build --strict`
  - `python scripts/check-links.py --root docs --strict`
  - `python scripts/validate-content-metadata.py`
  - `python scripts/validate-spanish-quality.py`
- **QA humana**:
  - 1 revisor técnico (significado correcto).
  - 1 revisor de estilo (tono y claridad).

## Flujo por batch
1. Ejecuta el script de traducción con `--batch-id`.
2. Ejecuta `make docs-qa`.
3. Realiza revisión técnica + de estilo.
4. Abre un PR pequeño con la sección “QA de traducción” completada.

## Checklist de PR (migración a español)
- [ ] Plantilla de “QA de traducción” completada con evidencias.
- [ ] Ortografía, gramática básica y glosario validados.
- [ ] Links internos y front-matter revisados.
- [ ] Revisión técnica y de estilo asignadas a personas distintas.

## Cuotas
- `GT_MAX_CHARS_PER_BATCH` (por ejemplo, 80000).
- `GT_MAX_QPS` (por ejemplo, 10).
- Usa backoff exponencial si la API devuelve errores de cuota.

## See also
- [Glosario](./glosario-terminologia.md)
- [Content Style Guide](../../guides/content-style-guide.md)
