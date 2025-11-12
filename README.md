# The Wise Tech

The Wise Tech repository captures the methodology, diagrams, and playbooks that describe how the organization blends human expertise with AI-assisted practices across the software lifecycle.

Welcome to The Wise Tech knowledge base. This repository is organized in two fully synchronized language trees so that every document is available both in English and in Spanish. Choose the path that best fits your needs:

- [English content](en/README.md)
- [Contenido en español](es/README.md)

Each language folder mirrors the same structure (guides, visual references, and practice playbooks) to make navigation predictable regardless of the language you select. If you update a document in one language, remember to reflect the change in the counterpart file so that both versions remain aligned.

## How the repository is organized

```text
├── en/                 # English source of truth for every document
├── es/                 # Spanish translation with the same structure and filenames
└── scenarios/payments/ # Business scenario that demonstrates Wise Tech end-to-end
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

## Contributing

When proposing changes, please update the English document first and then provide an equivalent translation under `es/`. Use the pull request template checklist and link back to the Essential principles, recipes, and onboarding guides whenever you introduce new knowledge.

Automation keeps both languages synchronized. Run `python scripts/check_bilingual_parity.py --check-scenarios` locally or rely on the **Bilingual Parity** GitHub Action before merging.

For detailed expectations, consult [Contributing Guide (English)](CONTRIBUTING.md) and [Guía de Contribución (Español)](CONTRIBUTING.es.md).

---

For licensing information, see [LICENSE](LICENSE).
