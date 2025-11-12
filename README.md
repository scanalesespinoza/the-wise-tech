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

## Recommendations by Interest
- **Productividad y simplicidad:** Empieza por el [quickstart](docs/guides/quickstart.md) y profundiza en [principios](docs/principles/wise-tech-principles.md).
- **Resiliencia operacional:** Sigue el [platform playbook](docs/playbooks/platform-playbook.md) y el [escenario de pagos](docs/scenarios/payments-overview.md).
- **Mejora continua y mentoring:** Usa la [guía de contribución](docs/guides/contribution-guide.md) y revisa el [roadmap](docs/roadmap/roadmap.md).

## Popular paths

| Ruta | ¿Por qué? |
| --- | --- |
| [Wise Tech principles](docs/principles/wise-tech-principles.md) | Punto de partida para alinear decisiones. |
| [Wise Tech approach](docs/principles/wise-tech-approach.md) | Cómo combinamos juicio humano y automatización. |
| [Developers overview](docs/personas/developers-overview.md) | Ruta rápida de onboarding técnico. |
| [Platform playbook](docs/playbooks/platform-playbook.md) | Expectativas de resiliencia y operabilidad. |
| [Payments overview](docs/scenarios/payments-overview.md) | Escenario completo para ensayar prácticas. |
| [Wise Tech ASCII](docs/diagrams/wise-tech-approach-ascii.md) | Visual simple para contar la historia. |
| [Roadmap](docs/roadmap/roadmap.md) | Próximos hitos y métricas compartidas. |
| [Contribution guide](docs/guides/contribution-guide.md) | Pasos concretos para proponer cambios. |
| [ADR index](adr/README.md) | Historial de decisiones estratégicas. |

## How we work
- **Simplicidad:** Buscamos el menor esfuerzo que entregue valor. [Ver principios](docs/principles/wise-tech-principles.md#simplicity)
- **Mejora continua:** Iteramos con experimentos pequeños y visibles. [Ver principios](docs/principles/wise-tech-principles.md#mejora-continua)
- **Resiliencia:** Diseñamos para fallar con gracia y recuperarnos rápido. [Ver principios](docs/principles/wise-tech-principles.md#resiliencia)
- **Capitalización del conocimiento:** Documentamos para escalar aprendizajes. [Ver principios](docs/principles/wise-tech-principles.md#capitalización-del-conocimiento)
- **Propósito humano:** Alineamos la tecnología con necesidades reales. [Ver principios](docs/principles/wise-tech-principles.md#propósito-humano)
- **Conexión humana:** Priorizamos relaciones y feedback transparente. [Ver principios](docs/principles/wise-tech-principles.md#conexión-humana)

## Contribute
- Sigue la [guía de contribución](docs/guides/contribution-guide.md) para abrir issues y PRs.
- Usa la plantilla de issues [Feedback User Experience](.github/ISSUE_TEMPLATE/feedback-user-experience.md).
- Completa la [plantilla de Pull Request](.github/PULL_REQUEST_TEMPLATE.md) para resaltar principios reforzados.

## FAQ
- **¿Dónde encuentro los principios originales?** → [Principles hub](docs/principles/_index.md)
- **¿Cómo valido enlaces antes de publicar?** → Ejecuta `python scripts/check-links.py --strict`.
- **¿Existe un escenario de referencia?** → Sí, visita [payments overview](docs/scenarios/payments-overview.md).
- **¿Dónde documento decisiones?** → Usa el [índice de ADR](adr/README.md) y enlaza desde tu PR.
- **¿Qué hago si detecto fricciones de usuario?** → Abre un issue con la plantilla de experiencia.

## Footer
- Licencia: [MIT](LICENSE)
- Badges: [![Docs validation](https://github.com/scanalesespinoza/the-wise-tech/actions/workflows/docs-validation.yml/badge.svg)](https://github.com/scanalesespinoza/the-wise-tech/actions/workflows/docs-validation.yml)
