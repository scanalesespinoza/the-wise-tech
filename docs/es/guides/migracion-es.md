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
- **QA automática**:
  - `mkdocs build --strict`
  - `make verify-links`
  - `make content-meta`
- **QA humana**:
  - 1 revisor técnico (significado correcto).
  - 1 revisor de estilo (tono y claridad).

## Flujo por batch
1. Ejecuta el script de traducción con `--batch-id`.
2. Ejecuta `make translation-qa`.
3. Realiza revisión técnica + de estilo.
4. Abre un PR pequeño con la sección “QA de traducción” completada.

## Cuotas
- `GT_MAX_CHARS_PER_BATCH` (por ejemplo, 80000).
- `GT_MAX_QPS` (por ejemplo, 10).
- Usa backoff exponencial si la API devuelve errores de cuota.

## See also
- [Glosario](./glosario-terminologia.md)
- [Content Style Guide](../../guides/content-style-guide.md)
