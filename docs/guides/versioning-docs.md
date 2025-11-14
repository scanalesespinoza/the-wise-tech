---
title: "Versioning-Docs — Semver básico"
tags: ["developers", "knowledge-capitalization", "principles"]
---
# Versioning-Docs — Semver básico

## Por-qué-importa
Documentar cambios predecibles ayuda a equipos a sincronizar playbooks, rutas y labs sin adivinar impactos.

## Qué-harás
1. Clasificar cada cambio como PATCH, MINOR o MAJOR.
2. Registrar notas en `CHANGELOG.md` para visibilidad.
3. Planificar redirecciones cuando cambien rutas o títulos.

## Semver-liviano
- **PATCH**: typos, enlaces o aclaraciones menores sin efecto en navegación.
- **MINOR**: nuevas guías, labs o secciones compatibles con lo existente.
- **MAJOR**: reestructuración, cambios de rutas o rompimientos en navegación.

## Prácticas-recomendadas
- Incluye tabla de impactos en el PR cuando subas de versión MINOR o MAJOR.
- Añade banderas de deprecación en páginas antiguas con fecha y ruta nueva.
- Usa redirecciones o avisos temporales mientras migras contenido.

## Herramientas-y-checks
- Anota cambios en `CHANGELOG.md` (sección docs) para visibilidad histórica.
- Ejecuta `mkdocs build --strict` para detectar rutas faltantes.
- Asegura que `make content-meta` pase antes de publicar.

## Coordinación-con-equipo
- Notifica a owners de rutas impactadas y actualiza issues enlazados.
- Etiqueta PRs con tags de taxonomía según rol/tema afectado.
- Documenta decisiones de corte (freeze) en issues para futuras auditorías.

## See-also
- [Content-Style-Guide — Wise Tech](content-style-guide.md)
- [Editorial-Workflow — Propuesta→Draft→Review→Publish](editorial-workflow.md)
- [Taxonomy — Tags permitidos](taxonomy-tags.md)
- [Roadmap — Wise Tech](../roadmap/roadmap.md)
