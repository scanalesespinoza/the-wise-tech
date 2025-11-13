# The Wise Tech

[![Quality](https://github.com/the-wise-tech/the-wise-tech/actions/workflows/quality.yml/badge.svg)](https://github.com/the-wise-tech/the-wise-tech/actions/workflows/quality.yml)
[![Links](https://github.com/the-wise-tech/the-wise-tech/actions/workflows/links.yml/badge.svg)](https://github.com/the-wise-tech/the-wise-tech/actions/workflows/links.yml)

El repositorio que convierte la filosofía Wise Tech en acciones compartidas: una one-page navegable para aprender, construir y operar tecnología con propósito humano.

➡️ Explora la documentación completa en [Docs Home](docs/index.md).

## Choose your path

- **Technology Consumers** → [consumers overview](docs/personas/consumers-overview.md)
- **Software Developers** → [developers overview](docs/personas/developers-overview.md)
- **Platform Engineers** → [platform engineers overview](docs/personas/platform-engineers-overview.md)

## Quick start (5 pasos)

1) make install
2) make test
3) make parity
4) make docs
5) abre http://127.0.0.1:8000 y sigue “Choose your path”

Consulta el [quickstart general](docs/guides/quickstart.md) cuando necesites la versión ultracorta para compartir con tu equipo.

## Navigation map

/ (README one-page)
├─ Principles → [docs/principles/](docs/principles/)  
├─ Personas  
│  ├─ Consumers → [docs/personas/consumers-overview.md](docs/personas/consumers-overview.md)  
│  ├─ Developers → [docs/personas/developers-overview.md](docs/personas/developers-overview.md)  
│  └─ Platform Engineers → [docs/personas/platform-engineers-overview.md](docs/personas/platform-engineers-overview.md)  
├─ Guides → [docs/guides/](docs/guides/)  
├─ Playbooks → [docs/playbooks/](docs/playbooks/)  
├─ Scenarios → [docs/scenarios/](docs/scenarios/)  
└─ Roadmap → [docs/roadmap/roadmap.md](docs/roadmap/roadmap.md)

## Recommended by interest

- **Productividad & simplicidad** → [docs/guides/quickstart.md](docs/guides/quickstart.md), [docs/principles/](docs/principles/)
- **Resiliencia & operación** → [docs/playbooks/](docs/playbooks/), [docs/scenarios/](docs/scenarios/)
- **Mentoría & mejora continua** → [docs/roadmap/roadmap.md](docs/roadmap/roadmap.md), [.github/](.github/)

> Social preview: ver [assets/social/wise-tech-1280x640.png](assets/social/wise-tech-1280x640.png)

## Key resources
- [Wise Tech principles](docs/principles/wise-tech-principles.md) condensan los acuerdos fundacionales del repositorio.
- [Contribution guide](docs/guides/contribution-guide.md) explica cómo documentar aprendizajes y referencias cruzadas.
- [Developer playbook](docs/playbooks/developer-playbook.md) / [Platform playbook](docs/playbooks/platform-playbook.md) proponen primeros wins y KPIs por rol.
- [Wise Tech approach (EN)](en/wise-tech-approach.md) / [Enfoque Wise Tech (ES)](es/wise-tech-approach.md) articulan la narrativa estratégica.
- [Payments Scenario](scenarios/payments/README.md) integra código, contratos, pruebas y runbooks bilingües.

El escenario de pagos funciona como caso de negocio canónico: los errores del servicio muestran recetas de manejo de fallas, los contratos ilustran consumer-driven testing y los runbooks bilingües hacen que la resiliencia sea accionable.

## Learning outcomes & KPIs
- [Developer playbook](docs/playbooks/developer-playbook.md#indicadores-clave-de-experimento) detalla KPIs como tiempo de ciclo del escenario de pagos y defectos detectados antes del merge.
- [Platform playbook](docs/playbooks/platform-playbook.md#indicadores-clave-de-experimento) explica cómo medir MTTR simulado, cobertura de runbooks y satisfacción de equipos.
- Cada [ruta por rol](docs/personas/_index.md) incluye "Primeros 60 minutos" para convertir aprendizaje en acción inmediata.

## FAQ
### ¿Qué comandos ejecutan los workflows de CI?
Los pipelines [`quality`](.github/workflows/quality.yml) y [`links`](.github/workflows/links.yml) reutilizan las tareas del Makefile, por lo que `make install && make lint && make fmt && make test && make parity` más `python scripts/check-links.py --strict` entregan el mismo veredicto antes de abrir una PR.

### ¿Cómo valido bilingüismo cuando sólo edito una lengua?
Ejecuta `make parity` para comparar las rutas `en/` y `es/`. Si todavía no existe la traducción, agrega una nota `TODO (parity)` en el archivo y documenta el plan en tu PR para que el pipeline no falle.

### ¿Qué hacer si MkDocs ya usa el puerto 8000?
Puedes redefinir el puerto temporalmente con `mkdocs serve -a 127.0.0.1:8010` o exportar `MKDOCS_SERVE_ADDR=127.0.0.1:8010` antes de correr `make docs`.

## Contributing
When proposing changes, please update the English document first and then provide an equivalent translation under `es/`. Use the pull request template checklist and link back to the Essential principles, recipes, and onboarding guides whenever you introduce new knowledge.

Automation keeps both languages synchronized. Ejecuta `make parity` o confía en la acción de GitHub **Bilingual Parity** antes de fusionar.

For detailed expectations, consult [Contributing Guide (English)](CONTRIBUTING.md) and [Guía de Contribución (Español)](CONTRIBUTING.es.md).

---

For licensing information, see [LICENSE](LICENSE).
