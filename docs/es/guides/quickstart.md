---
title: "Quickstart — primeros pasos"
tags: ["developers", "quickstart"]
---
# Quickstart — primeros pasos

Sigue estos pasos para levantar el entorno de documentación y validar que todo funciona con español como idioma base.

## Antes de iniciar
- Instala Python 3.11+ y `pip`.
- Instala `just` o asegúrate de poder ejecutar `make`.
- Exporta variables de cuota de traducción si usarás el script (`GT_MAX_CHARS_PER_BATCH`, `GT_MAX_QPS`).

## Pasos
1. Clona el repo y crea una rama `i18n-es/wave-<n>`.
2. Ejecuta `make translate-batch BATCH=w1-b1` para preparar los archivos del lote.
3. Corre `make translation-qa` y corrige cualquier enlace roto o metadata faltante.
4. Abre un PR con la plantilla de “QA de traducción”.

## See also
- [Migración a español — Proceso por lotes](migracion-es.md)
- [Glosario de terminología](glosario-terminologia.md)
