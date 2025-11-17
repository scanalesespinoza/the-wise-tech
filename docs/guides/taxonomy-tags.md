---
title: "Taxonomy & Tags"
tags: ["developers", "knowledge-capitalization", "paths"]
---
# Taxonomy & Tags

Define una lista única de tags para roles y temas. Estos metadatos permiten filtros consistentes en MkDocs y en las automatizaciones de QA.

## Tags permitidos
- **Roles**: `consumers`, `developers`, `platform-engineers`
- **Temas**: `simplicity`, `resilience`, `knowledge-capitalization`, `human-connection`, `aDevelopment`, `observability`, `slo`, `playbooks`, `paths`, `labs`, `quickstart`, `principles`, `ci`, `security`, `knowledge`, `docs`, `i18n`

> Los tags se mantienen en inglés, incluso cuando el contenido está en español, para facilitar búsqueda y consistencia global.

## Uso recomendado
1. Incluye al menos un tag de rol o tema en cada documento.
2. Repite exactamente los mismos tags en traducciones espejo (`es/`, `en/`).
3. Valida la metadata con `make translation-qa` antes del PR.

## Ejemplo de front-matter
```yaml
---
title: "Page title"
tags: ["developers", "resilience"]
---
```

## See also
- [Content Style Guide](content-style-guide.md)
- [Glosario de terminología](../es/guides/glosario-terminologia.md)
