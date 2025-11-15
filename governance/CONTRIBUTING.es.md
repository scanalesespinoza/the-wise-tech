# Guía de Contribución

Gracias por aportar a The Wise Tech. Toda la documentación vive ahora en `knowledge/docs/` con recorridos por rol.

## Flujo recomendado
1. Revisa el [quickstart](../knowledge/docs/guides/quickstart.md) y configura tu entorno (`make -f operations/Makefile install`).
2. Trabaja en ramas pequeñas y descriptivas (`feat-docs-one-page`).
3. Ejecuta `make -f operations/Makefile ci` para alinear tu veredicto local con los pipelines antes de pedir revisión.
4. Completa la [plantilla de PR](../.github/PULL_REQUEST_TEMPLATE.md) resaltando el principio reforzado.
5. Solicita revisión cruzada de las personas impactadas (Consumidores, Developers, Platform Engineers).

## Recursos esenciales
- [Principios Wise Tech](../knowledge/docs/principles/wise-tech-principles.md)
- [Ruta de Developers](../knowledge/docs/personas/developers-overview.md)
- [Platform playbook](../knowledge/docs/playbooks/platform-playbook.md)
- [Roadmap](../knowledge/docs/roadmap/roadmap.md)

## Automatización
- Los workflows [`quality`](../.github/workflows/quality.yml) y [`docs-and-links`](../.github/workflows/docs-and-links.yml) ejecutan exactamente los comandos del Makefile (`make -f operations/Makefile ci` y la validación de documentación) para mantener paridad entre local y remoto.
- Ejecuta `make -f operations/Makefile verify-links` o `python operations/scripts/check-links.py` cuando edites documentación extensa para detectar enlaces internos rotos a tiempo.
- Documenta decisiones estratégicas en el [índice de ADR](../knowledge/adr/INDEX.md).

Para referencia en inglés, visita [CONTRIBUTING.md](CONTRIBUTING.md).
