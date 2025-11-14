# The Wise Tech

## Status
[![quality](https://github.com/scanalesespinoza/the-wise-tech/actions/workflows/quality.yml/badge.svg)](https://github.com/scanalesespinoza/the-wise-tech/actions/workflows/quality.yml)
[![docs-and-links](https://github.com/scanalesespinoza/the-wise-tech/actions/workflows/docs-and-links.yml/badge.svg)](https://github.com/scanalesespinoza/the-wise-tech/actions/workflows/docs-and-links.yml)
[![gitleaks](https://github.com/scanalesespinoza/the-wise-tech/actions/workflows/gitleaks.yml/badge.svg)](https://github.com/scanalesespinoza/the-wise-tech/actions/workflows/gitleaks.yml)

El repositorio que convierte la filosofía Wise Tech en acciones compartidas: una one-page navegable para aprender, construir y operar tecnología con propósito humano.

➡️ Explora la documentación completa en [Docs Home](docs/index.md).

## Choose your path

- **Technology Consumers** → [consumers overview](docs/personas/consumers-overview.md)
  - Learning Path 30/60/90 → [docs/paths/consumers-30-60-90.md](docs/paths/consumers-30-60-90.md)
- **Software Developers** → [developers overview](docs/personas/developers-overview.md)
  - Learning Path 30/60/90 → [docs/paths/developers-30-60-90.md](docs/paths/developers-30-60-90.md)
- **Platform Engineers** → [platform engineers overview](docs/personas/platform-engineers-overview.md)
  - Learning Path 30/60/90 → [docs/paths/platform-engineers-30-60-90.md](docs/paths/platform-engineers-30-60-90.md)
- **Labs** → [Lab 01 — Resilience Basics](docs/labs/lab-01-resilience-basics.md)
  - Observability Minimum → [docs/labs/lab-02-observability-minima.md](docs/labs/lab-02-observability-minima.md)
  - aDevelopment Loop → [docs/labs/lab-03-adevelopment-loop.md](docs/labs/lab-03-adevelopment-loop.md)

## Quick start (5 pasos)

1) make install
2) make test
3) make parity
4) make docs
5) abre http://127.0.0.1:8000 y sigue “Choose your path”

Consulta el [quickstart general](docs/guides/quickstart.md) cuando necesites la versión ultracorta para compartir con tu equipo.

### How to give feedback
- Abre un Issue con la plantilla **Feedback — User Experience** o **Proposal — Improvement**.
- Para incidentes operacionales, usa **Ops — Postmortem**.
- En tus PRs, completa **Human Feedback References** y **Ops Signals**.

## Navigation map

/ (README one-page)
├─ Principles → [docs/principles/](docs/principles/)  
├─ Personas  
│  ├─ Consumers → [docs/personas/consumers-overview.md](docs/personas/consumers-overview.md)  
│  ├─ Developers → [docs/personas/developers-overview.md](docs/personas/developers-overview.md)  
│  └─ Platform Engineers → [docs/personas/platform-engineers-overview.md](docs/personas/platform-engineers-overview.md)  
├─ Guides → [docs/guides/](docs/guides/)
│  ├─ Content Style Guide → [docs/guides/content-style-guide.md](docs/guides/content-style-guide.md)
│  ├─ Editorial Workflow → [docs/guides/editorial-workflow.md](docs/guides/editorial-workflow.md)
│  ├─ Versioning Docs → [docs/guides/versioning-docs.md](docs/guides/versioning-docs.md)
│  ├─ Taxonomy & Tags → [docs/guides/taxonomy-tags.md](docs/guides/taxonomy-tags.md)
│  ├─ Resilience Policies → [docs/guides/resilience-policies.md](docs/guides/resilience-policies.md)
│  ├─ SLOs & Error Budget → [docs/guides/slo-how-to.md](docs/guides/slo-how-to.md)
│  ├─ Security (Minimum) → [docs/guides/security-minima.md](docs/guides/security-minima.md)
│  └─ Telemetry (Minimum) → [docs/guides/telemetry-minima.md](docs/guides/telemetry-minima.md)
├─ Snippets → [docs/snippets/](docs/snippets/)
│  └─ Python — Correlation ID → [docs/snippets/python-correlation-id.md](docs/snippets/python-correlation-id.md)
├─ Playbooks → [docs/playbooks/](docs/playbooks/)
├─ Scenarios → [docs/scenarios/](docs/scenarios/)  
└─ Roadmap → [docs/roadmap/roadmap.md](docs/roadmap/roadmap.md)

## Recommended by interest

- **Productividad & simplicidad** → [docs/guides/quickstart.md](docs/guides/quickstart.md), [docs/principles/](docs/principles/), [Learning Path 30/60/90 — Consumers](docs/paths/consumers-30-60-90.md)
- **Resiliencia & operación** → [docs/playbooks/](docs/playbooks/), [docs/scenarios/](docs/scenarios/), [docs/guides/resilience-policies.md](docs/guides/resilience-policies.md), [docs/guides/slo-how-to.md](docs/guides/slo-how-to.md), [Policies YAML (payments)](platform/policies/resilience.yml), [SLO Spec (payments)](platform/slo/slo-spec.yml), [Learning Path 30/60/90 — Platform](docs/paths/platform-engineers-30-60-90.md)
- **Mentoría & mejora continua** → [docs/roadmap/roadmap.md](docs/roadmap/roadmap.md), [.github/](.github/), [Learning Path 30/60/90 — Developers](docs/paths/developers-30-60-90.md)
- **Feedback Loops** → [docs/guides/feedback-loops.md](docs/guides/feedback-loops.md)
- **Postmortems** → [docs/guides/postmortem-guide.md](docs/guides/postmortem-guide.md)
- **Contribution Mentoring** → [docs/guides/contribution-mentoring.md](docs/guides/contribution-mentoring.md)
- **Observability & Traceability** → [docs/guides/telemetry-minima.md](docs/guides/telemetry-minima.md)
- **Correlation-ID (Python)** → [docs/snippets/python-correlation-id.md](docs/snippets/python-correlation-id.md)
- **Labs prácticos con KPIs** → [docs/labs/lab-01-resilience-basics.md](docs/labs/lab-01-resilience-basics.md), [docs/labs/lab-02-observability-minima.md](docs/labs/lab-02-observability-minima.md), [docs/labs/lab-03-adevelopment-loop.md](docs/labs/lab-03-adevelopment-loop.md)
- **Security & Supply Chain** → [.github/SECURITY.md](.github/SECURITY.md), [docs/guides/security-minima.md](docs/guides/security-minima.md)
- **How we write (Style Guide)** → [docs/guides/content-style-guide.md](docs/guides/content-style-guide.md), [Editorial workflow](docs/guides/editorial-workflow.md), [Versioning Docs](docs/guides/versioning-docs.md), [Taxonomy & tags](docs/guides/taxonomy-tags.md)

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
El pipeline [`quality`](.github/workflows/quality.yml) ejecuta exactamente `make ci`, que encadena `install`, `fmt`, `lint`, `test`, `parity`, `docs` y `verify-links`. Ejecutar `make ci` en local te entrega el mismo veredicto antes de abrir una PR.

### ¿Cómo se validan la documentación y los enlaces?
El workflow [`docs-and-links`](.github/workflows/docs-and-links.yml) se activa cuando cambian archivos Markdown o de MkDocs. Reconstruye el sitio con `mkdocs build --strict`, valida front-matter y "See also" con `python scripts/validate-content-metadata.py`, y ejecuta `python scripts/check-links.py` para detectar enlaces internos rotos. En local puedes correr `make content-meta` antes de subir cambios.

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
