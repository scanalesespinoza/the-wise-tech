---
title: "Content-Style-Guide — Wise Tech"
tags: ["developers", "knowledge-capitalization", "principles"]
---
# Content-Style-Guide — Wise Tech

## Por-qué-importa
Este estilo evita ruido y ayuda a publicar actualizaciones rápidas en ES/EN sin perder claridad.

## Qué-harás
1. Define propósito y audiencia en la propuesta.
2. Redacta borradores cortos con ejemplos ejecutables primero.
3. Cierra con "See also" para conectar guías relacionadas.

## Tono-y-lenguaje
- Prefiere voz activa y lenguaje humano, evita jerga innecesaria.
- Redacta en español primero y añade versión en inglés cuando habilite a equipos globales.
- Mantén párrafos de hasta seis líneas; usa listas de máximo siete ítems.

## Estructura-de-cada-página
1. Abre con "Por qué importa" y "Qué harás" en menos de cinco líneas combinadas.
2. Inserta ejemplos o snippets ejecutables antes de explicaciones largas.
3. Usa títulos con guiones medios para reflejar la estructura modular del contenido.

## Snippets-y-ejemplos
- Incluye comandos reproducibles o pseudocódigo corto que la audiencia pueda correr en minutos.
- Añade bloques ES/EN cuando existan matices culturales o técnicos distintos.
- Guarda imágenes en `assets/` con texto alternativo claro y ancho menor a 1280px.

## Referencias-y-enlaces
- Usa enlaces relativos; evita URLs absolutas al propio sitio.
- Revisa enlaces con `make content-meta` y `mkdocs build --strict` antes de enviar PR.
- Asegura una sección "See also" con 3–5 enlaces internos relevantes por rol o tema.

## Bilingüe-y-accesible
- Proporciona espejos en carpetas `es/` o `en/` cuando el contenido diverge significativamente.
- Resume conceptos clave en ambas lenguas para mantener la inclusión de equipos híbridos.
- Añade notas breves que enlacen glosarios o definiciones compartidas.

## Control-de-cambios
- Usa semver liviano para documentar cambios según la guía de versionado.
- Registra actualizaciones relevantes en `CHANGELOG.md` (sección docs).
- Documenta redirecciones cuando cambies rutas o títulos principales.

## Checklist-rápido-antes-del-PR
- [ ] Front-matter válido con tags permitidos.
- [ ] "See also" con vínculos relevantes y revisados.
- [ ] Ejemplos prácticos o snippets que permitan acción inmediata.
- [ ] Cumplimiento de límites de párrafos y listas.

## See-also
- [Editorial Workflow — Propuesta→Draft→Review→Publish](editorial-workflow.md)
- [Versioning Docs — Semver básico](versioning-docs.md)
- [Taxonomy — Tags permitidos](taxonomy-tags.md)
- [Quickstart](quickstart.md)
