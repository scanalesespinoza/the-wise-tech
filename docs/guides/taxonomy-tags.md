---
title: "Taxonomy — Tags permitidos"
tags: ["developers", "knowledge-capitalization", "paths"]
---
# Taxonomy — Tags permitidos

## Por-qué-importa
Una taxonomía consistente hace que las rutas de aprendizaje y playbooks sean fáciles de filtrar y descubrir.

## Qué-harás
1. Elegir tags de roles y temas permitidos en cada página nueva.
2. Mantener "See also" con enlaces que refuercen la narrativa.
3. Automatizar validaciones mínimas desde el repositorio.

## Tags-permitidos
**Roles**: `consumers`, `developers`, `platform-engineers`  
**Temas**: `simplicity`, `resilience`, `knowledge-capitalization`, `human-connection`, `aDevelopment`, `observability`, `slo`, `playbooks`, `paths`, `labs`, `quickstart`, `principles`

## Front-matter-ejemplo
```yaml
---
title: "Page title"
tags: ["developers", "resilience"]
---
```

## Reglas-de-uso
- Incluye al menos un tag de roles o temas por página.
- Evita tags libres fuera del listado; solicita ampliaciones vía issue.
- Replica tags en traducciones espejo (`es/` y `en/`).

## See-also
- [Content-Style-Guide — Wise Tech](content-style-guide.md)
- [Editorial-Workflow — Propuesta→Draft→Review→Publish](editorial-workflow.md)
- [Versioning-Docs — Semver básico](versioning-docs.md)
- [Front-Matter Example](../snippets/front-matter-example.md)
