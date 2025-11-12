# The Wise Tech

[![Quality](https://github.com/the-wise-tech/the-wise-tech/actions/workflows/quality.yml/badge.svg)](https://github.com/the-wise-tech/the-wise-tech/actions/workflows/quality.yml)
[![Links](https://github.com/the-wise-tech/the-wise-tech/actions/workflows/links.yml/badge.svg)](https://github.com/the-wise-tech/the-wise-tech/actions/workflows/links.yml)

El repositorio que convierte la filosofía Wise Tech en acciones compartidas: un mapa navegable para aprender, construir y operar tecnología con propósito humano.

## Choose your path

- Developers → [docs/personas/developers-overview.md](docs/personas/developers-overview.md)
  - Flujo express (install → test → parity → docs) y fixtures listos para experimentar.
- Platform Engineers → [docs/personas/platform-engineers-overview.md](docs/personas/platform-engineers-overview.md)
  - Cadena de feedback entre escenarios y pipelines de observabilidad.
- Technology Consumers → [docs/personas/consumers-overview.md](docs/personas/consumers-overview.md)
  - Recorridos para evaluar claridad de runbooks y decisiones de resiliencia.

## Quick start
1. `git clone https://github.com/the-wise-tech/the-wise-tech.git`
2. `cd the-wise-tech`
3. `make install`
4. `make test && make parity`
5. `make docs` (sirve MkDocs en `http://127.0.0.1:8000`)

Consulta el [quickstart extendido](docs/guides/quickstart.md) para entender qué valida cada comando y cómo compartir resultados.

## Navigation Map

```
/ (README)
├─ Principles → docs/principles/
├─ Personas → docs/personas/
├─ Guides → docs/guides/
├─ Playbooks → docs/playbooks/
├─ Scenarios → docs/scenarios/
│  └─ Payments → scenarios/payments/
└─ Roadmap → docs/roadmap/roadmap.md
```

Both language trees contain:

- A language-specific `README.md` that expands on The Wise Tech vision and provides curated links.
- Conceptual guides that contrast The Wise Tech approach with traditional practices.
- Visual ASCII diagrams that illustrate the end-to-end process and symbiotic feedback loops.
- The "The Wise Tech + aDevelopment" playbook describing how to blend accumulated expertise with AI-augmented workflows.

## Key Resources

- [Wise Tech principles](docs/principles/wise-tech-principles.md) condensan los acuerdos fundacionales del repositorio.
- [Contribution guide](docs/guides/contribution-guide.md) explica cómo documentar aprendizajes y referencias cruzadas.
- [Quickstart detallado](docs/guides/quickstart.md) expone qué valida cada comando del flujo local.
- [Developer playbook](docs/playbooks/developer-playbook.md) / [Platform playbook](docs/playbooks/platform-playbook.md) proponen primeros wins y KPIs por rol.
- [Wise Tech approach (EN)](en/wise-tech-approach.md) / [Enfoque Wise Tech (ES)](es/wise-tech-approach.md) articulan la narrativa estratégica.
- [Payments Scenario](scenarios/payments/README.md) integra código, contratos, pruebas y runbooks bilingües.

The payments folder acts as a canonical business scenario: the service errors showcase error-handling recipes, the contracts illustrate consumer-driven testing, and bilingual runbooks make resilience actionable.

## Recommended by interest

| Interés | Objetivo | Lecturas |
| --- | --- | --- |
| Productividad & simplicidad | Reducir fricción y acelerar la instalación. | [aDevelopment summary](docs/knowledge/articles/adevelopment-la-nueva-era-del-desarrollo-aumentado/adevelopment-la-nueva-era-del-desarrollo-aumentado-summary-es.md) · [Whitepaper impacto](docs/knowledge/articles/whitepaper-measuring-the-impact-of-augmented-development/whitepaper-measuring-the-impact-of-augmented-development-summary-es.md) |
| Resiliencia & operabilidad | Validar escenarios end-to-end y detección temprana. | [Don’t Blame the Cloud practices](docs/knowledge/articles/dont-blame-the-cloud-empowering-resilient-applications/dont-blame-the-cloud-empowering-resilient-applications-practices.md) · [Super Apps checklist](docs/knowledge/articles/what-about-having-super-apps/what-about-having-super-apps-practices.md) |
| Mentoring & experiencia | Compartir aprendizajes y decisiones humanas. | [Arquitectura habitada](docs/knowledge/articles/la-arquitectura-que-se-habita/la-arquitectura-que-se-habita-summary-es.md) · [Going into the Unknown](docs/knowledge/articles/going-into-the-unknown/going-into-the-unknown-summary-es.md) |

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