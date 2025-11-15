# Guía de Contribución

Gracias por aportar a The Wise Tech. Toda la documentación vive ahora en `docs/` con recorridos por rol.

## Flujo recomendado
1. Revisa el [quickstart](docs/guides/quickstart.md) y configura tu entorno (`make install`).
2. Trabaja en ramas pequeñas y descriptivas (`feat-docs-one-page`).
3. Ejecuta `make ci` para alinear tu veredicto local con los pipelines antes de pedir revisión.
4. Completa la [plantilla de PR](.github/PULL_REQUEST_TEMPLATE.md) resaltando el principio reforzado.
5. Solicita revisión cruzada de las personas impactadas (Consumidores, Developers, Platform Engineers).

## Recursos esenciales
- [Principios Wise Tech](docs/principles/wise-tech-principles.md)
- [Ruta de Developers](docs/personas/developers-overview.md)
- [Platform playbook](docs/playbooks/platform-playbook.md)
- [Roadmap](docs/roadmap/roadmap.md)

## Automatización
- Los workflows [`quality`](.github/workflows/quality.yml) y [`docs-and-links`](.github/workflows/docs-and-links.yml) ejecutan exactamente los comandos del Makefile (`make ci` y la validación de documentación) para mantener paridad entre local y remoto.
- Ejecuta `make verify-links` o `python scripts/check-links.py` cuando edites documentación extensa para detectar enlaces internos rotos a tiempo.
- Documenta decisiones estratégicas en el [índice de ADR](adr/INDEX.md).

Para referencia en inglés, visita [CONTRIBUTING.md](CONTRIBUTING.md).
