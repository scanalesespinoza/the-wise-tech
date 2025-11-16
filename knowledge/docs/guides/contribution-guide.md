---
title: "Contribution Guide"
tags: ["developers", "playbooks", "knowledge-capitalization"]
---
<!-- metadata
para_quien: Equipos y contribuidores que consultan "Contribution Guide" en The Wise Tech.
objetivo: Proporcionar un contexto accionable sobre contribution guide.
cuando_usar: Recurre a este documento cuando necesites aplicar o compartir detalles de contribution guide.
estado: active
-->

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

---

🗳️ **¿Te fue útil este documento?**
- [ ] Sí, resolvió mi duda
- [ ] Más o menos, necesito más contexto
- [ ] No me ayudó

📢 [Abre un feedback aquí](https://github.com/scanalesespinoza/the-wise-tech/issues/new?template=feedback.yml)

---
