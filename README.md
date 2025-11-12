# The Wise Tech

El repositorio que convierte la filosofía Wise Tech en acciones compartidas: un mapa navegable para aprender, construir y operar tecnología con propósito humano.

## Choose your path

| Rol | Descripción | CTA |
| --- | --- | --- |
| Consumidores de tecnología | Explora cómo protegemos experiencias claras y confiables. | [Ir a la ruta](docs/personas/consumers-overview.md) |
| Software Developers | Acelera entregas resilientes con prácticas compartidas. | [Ir a la ruta](docs/personas/developers-overview.md) |
| Platform Engineers | Escala operaciones y feedback continuo entre equipos. | [Ir a la ruta](docs/personas/platform-engineers-overview.md) |

## Quick start
1. Lee el [quickstart](docs/guides/quickstart.md) y prepara el entorno.
2. Ejecuta `python scripts/check-links.py --strict` para validar enlaces.
3. Abre un issue o PR siguiendo la [guía de contribución](docs/guides/contribution-guide.md).

## Navigation Map

```
/ (README one-page)
├─ Principles → docs/principles/
├─ Personas
│ ├─ Consumers → docs/personas/consumers-overview.md
│ ├─ Developers → docs/personas/developers-overview.md
│ └─ Platform Engineers → docs/personas/platform-engineers-overview.md
├─ Guides → docs/guides/
├─ Playbooks → docs/playbooks/
├─ Scenarios → docs/scenarios/
├─ Diagrams → docs/diagrams/
└─ Roadmap → docs/roadmap/roadmap.md
```

Both language trees contain:

- A language-specific `README.md` that expands on The Wise Tech vision and provides curated links.
- Conceptual guides that contrast The Wise Tech approach with traditional practices.
- Visual ASCII diagrams that illustrate the end-to-end process and symbiotic feedback loops.
- The "The Wise Tech + aDevelopment" playbook describing how to blend accumulated expertise with AI-augmented workflows.

## Key Resources

- [Essential Principles](en/docs/principles-essential.md) / [Principios Esenciales](es/docs/principles-essential.md)
- [PR Checklist](en/docs/checklist-pr.md) / [Checklist de PR](es/docs/checklist-pr.md)
- [Recipe Catalog](en/docs/recipes/README.md) / [Catálogo de Recetas](es/docs/recipes/README.md)
- [Onboarding Assets](en/docs/onboarding/README.md) / [Recursos de Onboarding](es/docs/onboarding/README.md)
- [Narrative Changelog Guidelines](en/docs/changelog-guidelines.md) / [Guías de Changelog Narrativo](es/docs/changelog-guidelines.md)
- [Living Glossary](en/docs/glossary.md) / [Glosario Vivo](es/docs/glossary.md)
- [Payments Scenario](scenarios/payments/README.md) bundles code, contracts, tests, and runbooks that operationalize the principles.

The payments folder acts as a canonical business scenario: the service errors showcase error-handling recipes, the contracts illustrate consumer-driven testing, and bilingual runbooks make resilience actionable.

## Recommended by interest

- Augmented delivery, metrics, and ROI: [aDevelopment summary (ES)](docs/knowledge/articles/adevelopment-la-nueva-era-del-desarrollo-aumentado/adevelopment-la-nueva-era-del-desarrollo-aumentado-summary-es.md) / [summary (EN)](docs/knowledge/articles/adevelopment-la-nueva-era-del-desarrollo-aumentado/adevelopment-la-nueva-era-del-desarrollo-aumentado-summary-en.md)
- Measuring augmented development impact: [whitepaper summary (ES)](docs/knowledge/articles/whitepaper-measuring-the-impact-of-augmented-development/whitepaper-measuring-the-impact-of-augmented-development-summary-es.md) / [summary (EN)](docs/knowledge/articles/whitepaper-measuring-the-impact-of-augmented-development/whitepaper-measuring-the-impact-of-augmented-development-summary-en.md)
- Human-centered architecture: [la arquitectura que se habita summary (ES)](docs/knowledge/articles/la-arquitectura-que-se-habita/la-arquitectura-que-se-habita-summary-es.md) / [summary (EN)](docs/knowledge/articles/la-arquitectura-que-se-habita/la-arquitectura-que-se-habita-summary-en.md)
- Cloud resilience baseline: [Don’t Blame the Cloud practices](docs/knowledge/articles/dont-blame-the-cloud-empowering-resilient-applications/dont-blame-the-cloud-empowering-resilient-applications-practices.md)
- People-before-platform strategy: [Future-Proof Technology practices](docs/knowledge/articles/future-proof-technology/future-proof-technology-practices.md)
- Open source team dynamics: [Architecting Open Source Teams summary (EN)](docs/knowledge/articles/architecting-open-source-teams-building-people-before-platforms/architecting-open-source-teams-building-people-before-platforms-summary-en.md)
- Resilient capabilities for distributed systems: [Super Apps checklist](docs/knowledge/articles/what-about-having-super-apps/what-about-having-super-apps-practices.md)
- Team experience scorecards: [2024 IT Team Experience practices](docs/knowledge/articles/2024-the-year-of-it-team-experience/2024-the-year-of-it-team-experience-practices.md)
- Microservices coordination pattern: [Hadron summary (EN)](docs/knowledge/articles/the-hadron-pattern-for-microservices/the-hadron-pattern-for-microservices-summary-en.md)

## Contributing

When proposing changes, please update the English document first and then provide an equivalent translation under `es/`. Use the pull request template checklist and link back to the Essential principles, recipes, and onboarding guides whenever you introduce new knowledge.

Automation keeps both languages synchronized. Run `python scripts/check_bilingual_parity.py --check-scenarios` locally or rely on the **Bilingual Parity** GitHub Action before merging.

For detailed expectations, consult [Contributing Guide (English)](CONTRIBUTING.md) and [Guía de Contribución (Español)](CONTRIBUTING.es.md).

---

For licensing information, see [LICENSE](LICENSE).