# Contributing Guide

Thank you for helping grow The Wise Tech knowledge base. This repository now uses a single navigation tree in `docs/` with role-
based journeys.

## Workflow Overview
1. Lee el [quickstart](docs/guides/quickstart.md) y prepara tu entorno (`make install`).
2. Crea una rama descriptiva (`feat-docs-one-page`) y realiza cambios pequeños y revisables.
3. Ejecuta `python scripts/check-links.py --strict` y cualquier prueba relevante antes de subir cambios.
4. Abre una PR usando la [plantilla oficial](.github/PULL_REQUEST_TEMPLATE.md) y enlaza el principio reforzado.
5. Solicita revisión cruzada a personas de los roles impactados (Consumers, Developers, Platform Engineers).

## Documentación clave
- [Wise Tech principles](docs/principles/wise-tech-principles.md)
- [Developers overview](docs/personas/developers-overview.md)
- [Platform playbook](docs/playbooks/platform-playbook.md)
- [Roadmap](docs/roadmap/roadmap.md)

## Automatización
- Los workflows [`quality`](.github/workflows/quality.yml) y [`links`](.github/workflows/links.yml) ejecutan el mismo flujo de comandos del Makefile (install → lint → fmt → test → parity) y aseguran que los enlaces internos sigan funcionando.
- Reutiliza `scripts/check-links.py` en tu CI local para iterar más rápido.
- Documenta decisiones en [ADR](adr/README.md) cuando cambies procesos estratégicos.

For guidance in Spanish, consulta [CONTRIBUTING.es.md](CONTRIBUTING.es.md).
