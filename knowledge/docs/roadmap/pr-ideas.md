---
title: "PR ideas"
tags: ["developers", "knowledge-capitalization"]
---
# PR ideas

Pequeñas tareas para practicar el flujo de contribución:

1. **Documentar métricas del sitio**
   - Actualiza `docs/metrics/site-metrics.md` con la última ejecución de CI.
   - Añade una nota breve en el README dentro de "Learning outcomes" si cambia el indicador principal.
2. **Mejorar enlaces de "See also"**
   - Elige una guía en `docs/guides/` que aún no tenga sección "See also".
   - Agrega referencias cruzadas relevantes y valida con `make content-meta`.
3. **Traducir un snippet**
   - Crea la versión inglesa o española faltante en `docs/snippets/`.
   - Ejecuta `make -f operations/Makefile parity` para confirmar que las rutas entre idiomas se mantienen alineadas.

Cada idea debe incluir una nota en la PR explicando qué guía, snippet o métrica tocaste.

## See also
- [Roadmap](roadmap.md)
- [Contribution guide](../guides/contribution-guide.md)
