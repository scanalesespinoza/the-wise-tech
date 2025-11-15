---
title: "Editorial-Workflow — Propuesta→Draft→Review→Publish"
tags: ["developers", "playbooks", "knowledge-capitalization"]
---
# Editorial-Workflow — Propuesta→Draft→Review→Publish

## Por-qué-importa
El ciclo editorial uniforme reduce sorpresas en releases, acelera revisiones y deja trazabilidad de decisiones.

## Qué-harás
1. Proponer objetivos, audiencia y tags antes de escribir.
2. Subir borradores con front-matter completo y enlaces relativos.
3. Revisar contra checklist común y publicar con cambios en navegación.

## Etapas
1. **Propuesta (Issue)**: describe objetivo, audiencia, tags y enlaces tentativos para "See also".
2. **Draft (PR)**: incluye contenido mínimo viable, front-matter válido y navegación actualizada si aplica.
3. **Review**: verifica guía de estilo, claridad, métricas o KPIs relevantes y consistencia de enlaces.
4. **Publish**: realiza merge, actualiza `operations/mkdocs.yml`, `README.md` y `CHANGELOG.md` si es necesario.

## Roles-y-responsabilidades
- **Author**: redacta la propuesta, crea el draft y actualiza referencias.
- **Reviewer**: aplica checklist de estilo, navegación, claridad y métricas.
- **Maintainer (CODEOWNERS)**: habilita merge, confirma cumplimiento de CI y de versionado.

## Definition-of-Done-mínimo
- Front-matter con tags alineados a la taxonomía aprobada.
- Sección "See also" con al menos tres enlaces internos relevantes.
- Enlaces verificados localmente (`mkdocs build --strict`) y en CI.
- Guía de estilo cumplida, títulos con guiones medios y snippet estándar aplicado.

## Automatización-y-CI
- Ejecuta `make content-meta` antes de enviar PR para validar front-matter y "See also".
- La CI corre `operations/scripts/validate-content-metadata.py` y verificación de enlaces.
- Registra excepciones en el issue/PR para mantener historial del porqué.

## Versionado-y-seguimiento
- Documenta cambios relevantes de docs en `CHANGELOG.md` usando semver liviano.
- Coordina redirecciones o avisos cuando cambien rutas para evitar enlaces rotos.
- Etiqueta issues/PRs con tags de taxonomía para facilitar búsquedas futuras.

## See-also
- [Content-Style-Guide — Wise Tech](content-style-guide.md)
- [Versioning Docs — Semver básico](versioning-docs.md)
- [Taxonomy — Tags permitidos](taxonomy-tags.md)
- [Quickstart](quickstart.md)
