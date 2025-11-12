# The Wise Tech

[![Quality Gate](https://github.com/the-wise-tech/the-wise-tech/actions/workflows/quality-gate.yml/badge.svg)](https://github.com/the-wise-tech/the-wise-tech/actions/workflows/quality-gate.yml)
[![Docs Validation](https://github.com/the-wise-tech/the-wise-tech/actions/workflows/docs-validation.yml/badge.svg)](https://github.com/the-wise-tech/the-wise-tech/actions/workflows/docs-validation.yml)
[![Bilingual Parity](https://github.com/the-wise-tech/the-wise-tech/actions/workflows/bilingual-parity.yml/badge.svg)](https://github.com/the-wise-tech/the-wise-tech/actions/workflows/bilingual-parity.yml)

El repositorio que convierte la filosofía Wise Tech en acciones compartidas: un mapa navegable para aprender, construir y operar tecnología con propósito humano.

## Choose your path

| Rol | Descripción | CTA |
| --- | --- | --- |
| Consumidores de tecnología | Explora cómo protegemos experiencias claras y confiables. | [Ir a la ruta](docs/personas/consumers-overview.md) |
| Software Developers | Acelera entregas resilientes con prácticas compartidas. | [Ir a la ruta](docs/personas/developers-overview.md) |
| Platform Engineers | Escala operaciones y feedback continuo entre equipos. | [Ir a la ruta](docs/personas/platform-engineers-overview.md) |

## Quick start
1. `git clone https://github.com/the-wise-tech/the-wise-tech.git`
2. `cd the-wise-tech`
3. `make install`
4. `make test && make parity`
5. `make docs`

Consulta el [quickstart extendido](docs/guides/quickstart.md) para entender qué valida cada comando y cómo compartir resultados.

## Navigation Map

```
/ (README one-page)
├─ Principles → docs/principles/
├─ Personas → docs/personas/
│  ├─ Consumers → consumers-overview.md
│  ├─ Developers → developers-overview.md
│  └─ Platform Engineers → platform-engineers-overview.md
├─ Guides → docs/guides/
│  ├─ Quickstart → quickstart.md
│  └─ Contribution → contribution-guide.md
├─ Playbooks → docs/playbooks/
│  ├─ Developer → developer-playbook.md
│  └─ Platform → platform-playbook.md
├─ Scenarios → docs/scenarios/
│  └─ Payments → scenarios/payments/
│      ├─ Contracts → contracts/
│      ├─ Tests → tests/
│      └─ Runbooks → docs/
├─ Diagrams → docs/diagrams/
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

**Productividad y simplicidad**
- [aDevelopment summary (ES)](docs/knowledge/articles/adevelopment-la-nueva-era-del-desarrollo-aumentado/adevelopment-la-nueva-era-del-desarrollo-aumentado-summary-es.md) / [summary (EN)](docs/knowledge/articles/adevelopment-la-nueva-era-del-desarrollo-aumentado/adevelopment-la-nueva-era-del-desarrollo-aumentado-summary-en.md)
- [Whitepaper: Measuring the Impact of Augmented Development — resumen (ES)](docs/knowledge/articles/whitepaper-measuring-the-impact-of-augmented-development/whitepaper-measuring-the-impact-of-augmented-development-summary-es.md) / [summary (EN)](docs/knowledge/articles/whitepaper-measuring-the-impact-of-augmented-development/whitepaper-measuring-the-impact-of-augmented-development-summary-en.md)
- [Future-Proof Technology practices](docs/knowledge/articles/future-proof-technology/future-proof-technology-practices.md)

**Resiliencia y operabilidad**
- [Don’t Blame the Cloud practices](docs/knowledge/articles/dont-blame-the-cloud-empowering-resilient-applications/dont-blame-the-cloud-empowering-resilient-applications-practices.md)
- [Super Apps checklist](docs/knowledge/articles/what-about-having-super-apps/what-about-having-super-apps-practices.md)
- [Hadron pattern summary (EN)](docs/knowledge/articles/the-hadron-pattern-for-microservices/the-hadron-pattern-for-microservices-summary-en.md)

**Personas y experiencia**
- [La arquitectura que se habita — resumen (ES)](docs/knowledge/articles/la-arquitectura-que-se-habita/la-arquitectura-que-se-habita-summary-es.md) / [summary (EN)](docs/knowledge/articles/la-arquitectura-que-se-habita/la-arquitectura-que-se-habita-summary-en.md)
- [Going into the Unknown — resumen (ES)](docs/knowledge/articles/going-into-the-unknown/going-into-the-unknown-summary-es.md) / [summary (EN)](docs/knowledge/articles/going-into-the-unknown/going-into-the-unknown-summary-en.md)
- [2024 IT Team Experience practices](docs/knowledge/articles/2024-the-year-of-it-team-experience/2024-the-year-of-it-team-experience-practices.md)

## Learning outcomes & KPIs

- [Developer playbook](docs/playbooks/developer-playbook.md#indicadores-clave-de-experimento) detalla KPIs como tiempo de ciclo del escenario de pagos y defectos detectados antes del merge.
- [Platform playbook](docs/playbooks/platform-playbook.md#indicadores-clave-de-experimento) explica cómo medir MTTR simulado, cobertura de runbooks y satisfacción de equipos.
- Cada [ruta por rol](docs/personas/_index.md) incluye "Primeros 60 minutos" para convertir aprendizaje en acción inmediata.

## Contributing

When proposing changes, please update the English document first and then provide an equivalent translation under `es/`. Use the pull request template checklist and link back to the Essential principles, recipes, and onboarding guides whenever you introduce new knowledge.

Automation keeps both languages synchronized. Ejecuta `make parity` o confía en la acción de GitHub **Bilingual Parity** antes de fusionar.

For detailed expectations, consult [Contributing Guide (English)](CONTRIBUTING.md) and [Guía de Contribución (Español)](CONTRIBUTING.es.md).

---

For licensing information, see [LICENSE](LICENSE).