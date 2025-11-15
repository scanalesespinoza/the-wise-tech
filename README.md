# The Wise Tech

## Status
[![quality](https://github.com/scanalesespinoza/the-wise-tech/actions/workflows/quality.yml/badge.svg)](https://github.com/scanalesespinoza/the-wise-tech/actions/workflows/quality.yml)
[![docs-and-links](https://github.com/scanalesespinoza/the-wise-tech/actions/workflows/docs-and-links.yml/badge.svg)](https://github.com/scanalesespinoza/the-wise-tech/actions/workflows/docs-and-links.yml)
[![gitleaks](https://github.com/scanalesespinoza/the-wise-tech/actions/workflows/gitleaks.yml/badge.svg)](https://github.com/scanalesespinoza/the-wise-tech/actions/workflows/gitleaks.yml)
[![pre-commit](https://github.com/scanalesespinoza/the-wise-tech/actions/workflows/pre-commit.yml/badge.svg)](https://github.com/scanalesespinoza/the-wise-tech/actions/workflows/pre-commit.yml)

This repository turns the Wise Tech philosophy into shared actions: a navigable one-page hub for learning, building, and operating technology with a human purpose.

## Start here

1. Read the overview in [Docs Home](docs/index.md) to locate the principles, paths, and labs.
2. Find your role in [Choose your path](#choose-your-path) and follow the corresponding "Learning Path 30/60/90" link.
3. If you want to spin up the local environment, continue with [Quick start (7 steps)](#quick-start-7-steps).

➡️ Explore the full documentation in [Docs Home](docs/index.md) or visit the published version on GitHub Pages: https://scanalesespinoza.github.io/the-wise-tech/.

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

## Quick start (7 steps)

1) git clone https://github.com/scanalesespinoza/the-wise-tech.git
2) cd the-wise-tech
3) make install
4) make test
5) make parity
6) make docs
7) open http://127.0.0.1:8000 and follow “Choose your path”

Optional (dev stack):

- `make dev-up` → Jaeger at `http://127.0.0.1:16686`, OTLP at `:4318`
- `make docs-live` → Docs at `http://127.0.0.1:8000`

Check the [general quickstart](docs/guides/quickstart.md) when you need the ultra-short version to share with your team.

Optional (DX)

Install just: https://github.com/casey/just

Use just as a shortcut to Make:
just install | test | docs | ci | links | slos | telemetry

## Do I only want to read or contribute?

- 🧭 **I only want to read** → open the published version on [GitHub Pages](https://scanalesespinoza.github.io/the-wise-tech/) and follow [Choose your path](#choose-your-path) to navigate by role.
- 🛠️ **I want to contribute** → prepare your environment with [Dev environment — devcontainer, pre-commit, and just](docs/guides/dev-environment.md) and pick a small task from [PR ideas](docs/roadmap/pr-ideas.md).

### How to give feedback
- Open an issue using the **Feedback — User Experience** or **Proposal — Improvement** template.
- For operational incidents, use **Ops — Postmortem**.
- In your PRs, complete **Human Feedback References** and **Ops Signals**.

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
│  ├─ Local Dev Stack → [docs/guides/dev-stack-local.md](docs/guides/dev-stack-local.md)
│  └─ Telemetry (Minimum) → [docs/guides/telemetry-minima.md](docs/guides/telemetry-minima.md)
├─ Snippets → [docs/snippets/](docs/snippets/)
│  └─ Python — Correlation ID → [docs/snippets/python-correlation-id.md](docs/snippets/python-correlation-id.md)
├─ Templates → [docs/templates/](docs/templates/)
│  ├─ ADR — short form → [docs/templates/adr-short.md](docs/templates/adr-short.md)
│  └─ Postmortem — quick capture → [docs/templates/postmortem-light.md](docs/templates/postmortem-light.md)
├─ CI → [docs/continuous-integration/index.md](docs/continuous-integration/index.md)
├─ Playbooks → [docs/playbooks/](docs/playbooks/)
├─ Scenarios → [docs/scenarios/](docs/scenarios/)
└─ Roadmap → [docs/roadmap/roadmap.md](docs/roadmap/roadmap.md)

## Recommended by interest

- **Productivity & simplicity** → [docs/guides/quickstart.md](docs/guides/quickstart.md), [docs/principles/](docs/principles/), [Learning Path 30/60/90 — Consumers](docs/paths/consumers-30-60-90.md)
- **Resilience & operations** → [docs/playbooks/](docs/playbooks/), [docs/scenarios/](docs/scenarios/), [docs/guides/resilience-policies.md](docs/guides/resilience-policies.md), [docs/guides/slo-how-to.md](docs/guides/slo-how-to.md), [Policies YAML (payments)](scenarios/payments/policies/resilience.yml), [SLO Spec (payments)](scenarios/payments/slo/slo-spec.yml), [Learning Path 30/60/90 — Platform](docs/paths/platform-engineers-30-60-90.md)
- **Mentorship & continuous improvement** → [docs/roadmap/roadmap.md](docs/roadmap/roadmap.md), [docs/roadmap/pr-ideas.md](docs/roadmap/pr-ideas.md), [.github/](.github/), [Learning Path 30/60/90 — Developers](docs/paths/developers-30-60-90.md)
- **Feedback loops** → [docs/guides/feedback-loops.md](docs/guides/feedback-loops.md)
- **Postmortems** → [docs/guides/postmortem-guide.md](docs/guides/postmortem-guide.md)
- **Contribution mentoring** → [docs/guides/contribution-mentoring.md](docs/guides/contribution-mentoring.md)
- **Observability & traceability** → [docs/guides/telemetry-minima.md](docs/guides/telemetry-minima.md)
- **Local dev stack (docs + OTEL/Jaeger)** → [docs/guides/dev-stack-local.md](docs/guides/dev-stack-local.md)
- **Correlation ID (Python)** → [docs/snippets/python-correlation-id.md](docs/snippets/python-correlation-id.md)
- **Hands-on labs with KPIs** → [docs/labs/lab-01-resilience-basics.md](docs/labs/lab-01-resilience-basics.md), [docs/labs/lab-02-observability-minima.md](docs/labs/lab-02-observability-minima.md), [docs/labs/lab-03-adevelopment-loop.md](docs/labs/lab-03-adevelopment-loop.md)
- **Security & supply chain** → [.github/SECURITY.md](.github/SECURITY.md), [docs/guides/security-minima.md](docs/guides/security-minima.md)
- **How we write (Style Guide)** → [docs/guides/content-style-guide.md](docs/guides/content-style-guide.md), [Editorial workflow](docs/guides/editorial-workflow.md), [Versioning Docs](docs/guides/versioning-docs.md), [Taxonomy & tags](docs/guides/taxonomy-tags.md)

> Social preview: view [assets/social/wise-tech-1280x640.png](assets/social/wise-tech-1280x640.png)

## Key resources
- [Wise Tech principles](docs/principles/wise-tech-principles.md) summarize the repository’s foundational agreements.
- [Contribution guide](docs/guides/contribution-guide.md) explains how to document learnings and cross-references.
- [Developer playbook](docs/playbooks/developer-playbook.md) / [Platform playbook](docs/playbooks/platform-playbook.md) propose early wins and KPIs by role.
- [Wise Tech approach (EN)](docs/en/wise-tech-approach.md) / [Wise Tech approach (ES)](docs/es/wise-tech-approach.md) articulate the strategic narrative.
- [Architecture decisions](adr/INDEX.md) centralizes the ADRs with their history and tags.
- [Payments Scenario](scenarios/payments/README.md) integrates code, contracts, tests, and bilingual runbooks.

The payments scenario functions as the canonical business case: service failures demonstrate fault-handling playbooks, the contracts illustrate consumer-driven testing, and the bilingual runbooks keep resilience actionable.

## Learning outcomes & KPIs
- [Developer playbook](docs/playbooks/developer-playbook.md#indicadores-clave-de-experimento) details KPIs such as the payments scenario cycle time and defects detected before merge.
- [Platform playbook](docs/playbooks/platform-playbook.md#indicadores-clave-de-experimento) explains how to measure simulated MTTR, runbook coverage, and team satisfaction.
- Each [role path](docs/personas/_index.md) includes “First 60 minutes” guidance to convert learning into immediate action.

## FAQ
### Which commands do the CI workflows run?
The [`quality`](.github/workflows/quality.yml) pipeline runs `make ci`, chaining `install`, `fmt`, `lint`, `test`, `parity`, `docs`, and `verify-links`. Running `make ci` locally gives you the same verdict before opening a PR.

### How are the documentation and links validated?
The [`docs-and-links`](.github/workflows/docs-and-links.yml) workflow triggers when Markdown or MkDocs files change. It rebuilds the site with `mkdocs build --strict`, validates front matter and “See also” sections with `python scripts/validate-content-metadata.py`, and runs `python scripts/check-links.py` to detect broken internal links. Locally you can run `make content-meta` before pushing changes.

### How do I validate bilingual parity when I edit only one language?
Run `make parity` to compare the `docs/en/` and `docs/es/` paths. If the translation does not exist yet, add a `TODO (parity)` note in the file and document the plan in your PR so the pipeline does not fail.

### What if MkDocs is already using port 8000?
You can redefine the port temporarily with `mkdocs serve -a 127.0.0.1:8010` or export `MKDOCS_SERVE_ADDR=127.0.0.1:8010` before running `make docs`.

## Contributing
When proposing changes, please update the English document first and then provide an equivalent translation under `es/`. Use the pull request template checklist and link back to the Essential principles, recipes, and onboarding guides whenever you introduce new knowledge.

Automation keeps both languages synchronized. Run `make parity` or rely on the **Bilingual Parity** GitHub Action before merging.

For detailed expectations, consult [Contributing Guide (English)](CONTRIBUTING.md) and [Contribution Guide (Spanish)](CONTRIBUTING.es.md).

---

For licensing information, see [LICENSE](LICENSE).
