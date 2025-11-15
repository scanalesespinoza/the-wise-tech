---
title: "Contribution Guide"
tags: ["developers", "playbooks", "knowledge-capitalization"]
---
# Contribution Guide

## Cómo proponer cambios
- Abre un issue describiendo objetivo, métricas y principio reforzado.
- Crea una rama con nombre descriptivo (`feat-docs-one-page`).
- Usa la plantilla de PR para detallar impacto y feedback referenciado.

## Flujo de aceptación
- Ejecuta `make -f operations/Makefile ci` para validar formato, lint, pruebas, paridad, docs y enlaces antes del PR.
- Busca revisiones cruzadas de al menos una persona por rol impactado.
- Documenta decisiones en `knowledge/adr/` cuando introduzcas cambios estratégicos.

## See also
- [Quickstart](quickstart.md)
- [Wise Tech principles](../principles/wise-tech-principles.md)
- [Developer playbook](../playbooks/developer-playbook.md)
- [Platform playbook](../playbooks/platform-playbook.md)
- [Roadmap](../roadmap/roadmap.md)
