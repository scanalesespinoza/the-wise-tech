---
title: "Métricas y auditorías de localización"
tags: ["docs", "i18n", "metrics"]
---
# Métricas y auditorías de localización

Esta guía define cómo medir la salud de traducciones, cuándo auditar nuevo contenido en inglés y qué flujo seguir para contribuir en español.

## Métricas clave

| Métrica | Cómo se calcula | Fuente de datos | Meta/alerta |
| --- | --- | --- | --- |
| **Cobertura de traducción** | `(entradas con status \"done\" en cola / entradas totales sin \"skip\") * 100`. Incluye EN→ES y ES→EN si aplica. | `audit/translation-queue.yml` + reporte generado en `audit/translation-status.md` (`make -f operations/Makefile translate-status`). | Meta ≥90% por wave cerrada; alerta si baja de 80% global. |
| **Bugs lingüísticos por PR** | Conteo de hallazgos de estilo/gramática/glosario anotados en la sección **QA de traducción** del PR. Abre issues con label `i18n-bug` cuando requieran patch. | Plantilla de PR (`QA de traducción`), issues etiquetadas. | Meta ≤1 bug crítico por PR; alerta si se reportan ≥3 no críticos en 7 días. |
| **Tiempo de localización por PR** | Horas entre la creación del PR y el merge. Si se reabre, cuenta desde la reapertura. Incluye iteraciones de revisión. | Timestamps del PR + nota manual `Tiempo de localización: <h>` en la plantilla. | Meta p50 ≤48h; alerta cuando p90 supere 72h. |

> Nota: guarda los cálculos en el comentario final del PR y, cuando corresponda, en un tablero/hoja de seguimiento del equipo.

## Auditorías periódicas de contenido en inglés

- **Cadencia:** semanal (lunes) o al detectar cambios grandes en `docs/` o `knowledge/docs/en/`.
- **Procedimiento:**
  1. Lista archivos nuevos o modificados en inglés desde la última auditoría: `git log --since="-7 days" --name-only --pretty="format:" -- docs knowledge/docs/en | sort -u | grep -v "^docs/es/"`.
  2. Registra cada archivo en `audit/translation-queue.yml` con prioridad y batch (`wave-x`).
  3. Si un archivo no requiere traducción, agrégalo a `audit/translation-skiplist.yml` con la razón.
  4. Genera `audit/translation-status.md` para validar desalineaciones: `make -f operations/Makefile translate-status`.
  5. Abre issue/PR asignando revisor técnico y de estilo por lote.

## Flujo para contribuciones en español

1. **Rama y lote:** crea `i18n-es/<wave>-<batch>` y consulta el lote en `audit/translation-queue.yml`.
2. **Preparación:** ejecuta `make translate-batch BATCH=<id>` si el lote existe. Mantén tags/front-matter en inglés.
3. **Convenciones de redacción:**
   - Usa español neutro + glosario oficial (`docs/es/guides/glosario-terminologia.md`).
   - No traduzcas nombres de archivos, claves YAML ni rutas de API. Traduce narrativa, títulos y alt text.
   - Incluye “See also” en español con rutas espejo (`docs/es/...`).
4. **QA y plantilla:** completa la sección **QA de traducción** en `.github/PULL_REQUEST_TEMPLATE.md` (Batch ID, glosario, validaciones). Ejecuta `make docs-qa` si modificaste contenido.
5. **Revisiones:** asigna revisor técnico + revisor de estilo distintos. Anota bugs lingüísticos y tiempo de localización en el PR.
6. **Cierre:** actualiza la cola (`status: done`) y, si hubo excepciones, documenta en `translation-skiplist.yml`.

## See also
- [Quickstart — primeros pasos](quickstart.md)
- [Migración a español — Proceso por lotes](migracion-es.md)
- [Glosario de terminología](glosario-terminologia.md)
- [Inventario i18n](../../../audit/i18n-inventory.md)
