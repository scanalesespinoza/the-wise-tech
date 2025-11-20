---
title: "Content Style Guide"
tags: ["developers", "knowledge-capitalization", "principles"]
---
# Content Style Guide

Esta guía resume cómo escribir, revisar y publicar contenido en The Wise Tech.

## Propósito
Mantener una narrativa coherente, accesible y alineada con la estructura técnica del repositorio.

## Reglas de idioma y estructura
- **Visible para usuario (ES)**:
  - Títulos H1–H3, texto de los docs, secciones “See also” y menús visibles de MkDocs deben estar en **español**.
  - Descripciones SEO y textos alternativos (alt text) se redactan en **español**.
- **Rutas, carpetas y nombres de archivo (EN)**:
  - Archivos y directorios permanecen en **inglés**, usando `kebab-case`, ASCII, sin tildes ni ñ.
  - Ejemplo: `docs/guides/telemetry-minima.md` con título “Telemetría mínima”.
- **Tags de front-matter (EN)**:
  - `tags` siempre en inglés y tomando la lista canónica (`developers`, `platform-engineers`, `resilience`, `observability`, `simplicity`, etc.).
  - Evita mezclar traducciones como `resilience` vs `resiliencia`.
- **Código, claves YAML y paths técnicos (EN)**:
  - No traduzcas nombres de carpetas de código, nombres de archivos de código, claves YAML, nombres de campos o rutas de API.
  - Bloques de código y ejemplos de configuración siempre quedan en inglés.
- **Identificadores internos sin contrato público (ES permitido)**:
  - Variables temporales, ejemplos didácticos o scripts de soporte pueden nombrarse en español si no forman parte de APIs, rutas ni
    configuraciones consumidas por terceros.
  - Si decides renombrar algo que ya usan otras personas, conserva alias o documenta la deprecación para no romper integraciones.
- **Commits/branches (EN)**:
  - Usa inglés para nombres de ramas y mensajes de commit para alinearte con el ecosistema OSS.
- **Recordatorio**: se traduce la **narrativa**, no la estructura técnica ni los identificadores.

## Checklist rápido
- Front-matter válido (title, tags).
- Sección “See also” con enlaces relativos.
- QA ejecutada con `make docs-qa` antes del PR.

## See also
- [Taxonomy & Tags](taxonomy-tags.md)
- [Migración a español](../es/guides/migracion-es.md)
- [Glosario](../es/guides/glosario-terminologia.md)
