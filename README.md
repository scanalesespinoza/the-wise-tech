# The Wise Tech

## Status
[![quality](https://github.com/scanalesespinoza/the-wise-tech/actions/workflows/quality.yml/badge.svg)](https://github.com/scanalesespinoza/the-wise-tech/actions/workflows/quality.yml)
[![docs-and-links](https://github.com/scanalesespinoza/the-wise-tech/actions/workflows/docs-and-links.yml/badge.svg)](https://github.com/scanalesespinoza/the-wise-tech/actions/workflows/docs-and-links.yml)
[![gitleaks](https://github.com/scanalesespinoza/the-wise-tech/actions/workflows/gitleaks.yml/badge.svg)](https://github.com/scanalesespinoza/the-wise-tech/actions/workflows/gitleaks.yml)
[![pre-commit](https://github.com/scanalesespinoza/the-wise-tech/actions/workflows/pre-commit.yml/badge.svg)](https://github.com/scanalesespinoza/the-wise-tech/actions/workflows/pre-commit.yml)

This repository turns the Wise Tech philosophy into shared actions: a navigable one-page hub for learning, building, and operating technology with a human purpose.

## Vision and purpose

This repository is an expanding knowledge base that elevates technology quality by prioritizing lessons learned, established patterns, and validated designs. Its mission is to break the cycle of low-cost, low-quality software that dominates the market today—software that generates collateral issues such as security gaps, unnecessary spending driven by technical debt, and economic plus environmental harm.

Wise Tech focuses on modern needs while helping orient the future. As experience gaps widen and professionals rely on increasingly shallow tooling and artificial intelligence, durable knowledge becomes the shared advantage. Captured expertise empowers both traditional teams building technology by hand and emerging teams orchestrating AI-led development.

This site curates a taxonomic body of principles, models, and methodologies for delivering world-class technology. Although still young, it aims to become a reference for training AI systems and professionals who must respond to demanding, high-stakes scenarios.

## Start here

1. Read the overview in [Docs Home](knowledge/docs/index.md) to locate the principles, paths, and labs.
2. Find your role in [Choose your path](#choose-your-path) and follow the corresponding "Learning Path 30/60/90" link.
3. If you want to spin up the local environment, continue with [Quick start (7 steps)](#quick-start-7-steps).

➡️ Explore the full documentation in [Docs Home](knowledge/docs/index.md) or visit the published version on GitHub Pages: https://scanalesespinoza.github.io/the-wise-tech/.

## Choose your path

- **Technology Consumers** → [consumers overview](knowledge/docs/personas/consumers-overview.md)
  - Learning Path 30/60/90 → [knowledge/docs/paths/consumers-30-60-90.md](knowledge/docs/paths/consumers-30-60-90.md)
- **Software Developers** → [developers overview](knowledge/docs/personas/developers-overview.md)
  - Learning Path 30/60/90 → [knowledge/docs/paths/developers-30-60-90.md](knowledge/docs/paths/developers-30-60-90.md)
- **Platform Engineers** → [platform engineers overview](knowledge/docs/personas/platform-engineers-overview.md)
  - Learning Path 30/60/90 → [knowledge/docs/paths/platform-engineers-30-60-90.md](knowledge/docs/paths/platform-engineers-30-60-90.md)
- **Labs** → [Lab 01 — Resilience Basics](knowledge/docs/labs/lab-01-resilience-basics.md)
  - Observability Minimum → [knowledge/docs/labs/lab-02-observability-minima.md](knowledge/docs/labs/lab-02-observability-minima.md)
  - aDevelopment Loop → [knowledge/docs/labs/lab-03-adevelopment-loop.md](knowledge/docs/labs/lab-03-adevelopment-loop.md)

## Quick start (7 steps)

1) git clone https://github.com/scanalesespinoza/the-wise-tech.git
2) cd the-wise-tech
3) make -f operations/Makefile install
4) make -f operations/Makefile test
5) make -f operations/Makefile parity
6) make -f operations/Makefile docs
7) open http://127.0.0.1:8000 and follow “Choose your path”

Optional (dev stack):

- `make -f operations/Makefile dev-up` → Jaeger at `http://127.0.0.1:16686`, OTLP at `:4318`
- `make -f operations/Makefile docs-live` → Docs at `http://127.0.0.1:8000`

Check the [general quickstart](knowledge/docs/guides/quickstart.md) when you need the ultra-short version to share with your team.

## Repository layout by focus area

- `knowledge/` — **Knowledge Capitalization.** Documentation, ADRs, historical archives, and shared assets.
- `experience/` — **Human Connection.** Audits, personas, and living scenarios to rehearse resilience decisions.
- `systems/` — **Resilience.** Platform policies, infrastructure prototypes, local dev stack, and automated tests.
- `operations/` — **Continuous Improvement.** Automation toolchain (Makefile, scripts, MkDocs, requirements, navigation map).
- `governance/` — **Simplicity & alignment.** Contribution guides, changelog, and decision guardrails.

Keep `LICENSE`, `.github/`, and `.devcontainer/` at the root so automation and legal notices stay discoverable.

Optional (DX)

Install just: https://github.com/casey/just

Use just as a shortcut to Make:
`just --justfile operations/justfile install | test | docs | ci | links | slos | telemetry`

## Do I only want to read or contribute?

- 🧭 **I only want to read** → open the published version on [GitHub Pages](https://scanalesespinoza.github.io/the-wise-tech/) and follow [Choose your path](#choose-your-path) to navigate by role.
- 🛠️ **I want to contribute** → prepare your environment with [Dev environment — devcontainer, pre-commit, and just](knowledge/docs/guides/dev-environment.md) and pick a small task from [PR ideas](knowledge/docs/roadmap/pr-ideas.md).

### How to give feedback
- Open an issue using the **Feedback — User Experience** or **Proposal — Improvement** template.
- For operational incidents, use **Ops — Postmortem**.
- In your PRs, complete **Human Feedback References** and **Ops Signals**.

## Navigation map

/ (README one-page)
├─ Principles → [knowledge/docs/principles/](knowledge/docs/principles/)  
├─ Personas  
│  ├─ Consumers → [knowledge/docs/personas/consumers-overview.md](knowledge/docs/personas/consumers-overview.md)  
│  ├─ Developers → [knowledge/docs/personas/developers-overview.md](knowledge/docs/personas/developers-overview.md)  
│  └─ Platform Engineers → [knowledge/docs/personas/platform-engineers-overview.md](knowledge/docs/personas/platform-engineers-overview.md)  
├─ Guides → [knowledge/docs/guides/](knowledge/docs/guides/)
│  ├─ Content Style Guide → [knowledge/docs/guides/content-style-guide.md](knowledge/docs/guides/content-style-guide.md)
│  ├─ Editorial Workflow → [knowledge/docs/guides/editorial-workflow.md](knowledge/docs/guides/editorial-workflow.md)
│  ├─ Versioning Docs → [knowledge/docs/guides/versioning-docs.md](knowledge/docs/guides/versioning-docs.md)
│  ├─ Taxonomy & Tags → [knowledge/docs/guides/taxonomy-tags.md](knowledge/docs/guides/taxonomy-tags.md)
│  ├─ Resilience Policies → [knowledge/docs/guides/resilience-policies.md](knowledge/docs/guides/resilience-policies.md)
│  ├─ SLOs & Error Budget → [knowledge/docs/guides/slo-how-to.md](knowledge/docs/guides/slo-how-to.md)
│  ├─ Security (Minimum) → [knowledge/docs/guides/security-minima.md](knowledge/docs/guides/security-minima.md)
│  ├─ Local Dev Stack → [knowledge/docs/guides/dev-stack-local.md](knowledge/docs/guides/dev-stack-local.md)
│  └─ Telemetry (Minimum) → [knowledge/docs/guides/telemetry-minima.md](knowledge/docs/guides/telemetry-minima.md)
├─ Snippets → [knowledge/docs/snippets/](knowledge/docs/snippets/)
│  └─ Python — Correlation ID → [knowledge/docs/snippets/python-correlation-id.md](knowledge/docs/snippets/python-correlation-id.md)
├─ Templates → [knowledge/docs/templates/](knowledge/docs/templates/)
│  ├─ ADR — short form → [knowledge/docs/templates/adr-short.md](knowledge/docs/templates/adr-short.md)
│  └─ Postmortem — quick capture → [knowledge/docs/templates/postmortem-light.md](knowledge/docs/templates/postmortem-light.md)
├─ CI → [knowledge/docs/continuous-integration/index.md](knowledge/docs/continuous-integration/index.md)
├─ Playbooks → [knowledge/docs/playbooks/](knowledge/docs/playbooks/)
├─ Scenarios → [knowledge/docs/scenarios/](knowledge/docs/scenarios/)
└─ Roadmap → [knowledge/docs/roadmap/roadmap.md](knowledge/docs/roadmap/roadmap.md)

## Recommended by interest

- **Productivity & simplicity** → [knowledge/docs/guides/quickstart.md](knowledge/docs/guides/quickstart.md), [knowledge/docs/principles/](knowledge/docs/principles/), [Learning Path 30/60/90 — Consumers](knowledge/docs/paths/consumers-30-60-90.md)
- **Resilience & operations** → [knowledge/docs/playbooks/](knowledge/docs/playbooks/), [knowledge/docs/scenarios/](knowledge/docs/scenarios/), [knowledge/docs/guides/resilience-policies.md](knowledge/docs/guides/resilience-policies.md), [knowledge/docs/guides/slo-how-to.md](knowledge/docs/guides/slo-how-to.md), [Policies YAML (payments)](experience/scenarios/payments/policies/resilience.yml), [SLO Spec (payments)](experience/scenarios/payments/slo/slo-spec.yml), [Learning Path 30/60/90 — Platform](knowledge/docs/paths/platform-engineers-30-60-90.md)
- **Mentorship & continuous improvement** → [knowledge/docs/roadmap/roadmap.md](knowledge/docs/roadmap/roadmap.md), [knowledge/docs/roadmap/pr-ideas.md](knowledge/docs/roadmap/pr-ideas.md), [.github/](.github/), [Learning Path 30/60/90 — Developers](knowledge/docs/paths/developers-30-60-90.md)
- **Feedback loops** → [knowledge/docs/guides/feedback-loops.md](knowledge/docs/guides/feedback-loops.md)
- **Postmortems** → [knowledge/docs/guides/postmortem-guide.md](knowledge/docs/guides/postmortem-guide.md)
- **Contribution mentoring** → [knowledge/docs/guides/contribution-mentoring.md](knowledge/docs/guides/contribution-mentoring.md)
- **Observability & traceability** → [knowledge/docs/guides/telemetry-minima.md](knowledge/docs/guides/telemetry-minima.md)
- **Local dev stack (docs + OTEL/Jaeger)** → [knowledge/docs/guides/dev-stack-local.md](knowledge/docs/guides/dev-stack-local.md)
- **Correlation ID (Python)** → [knowledge/docs/snippets/python-correlation-id.md](knowledge/docs/snippets/python-correlation-id.md)
- **Hands-on labs with KPIs** → [knowledge/docs/labs/lab-01-resilience-basics.md](knowledge/docs/labs/lab-01-resilience-basics.md), [knowledge/docs/labs/lab-02-observability-minima.md](knowledge/docs/labs/lab-02-observability-minima.md), [knowledge/docs/labs/lab-03-adevelopment-loop.md](knowledge/docs/labs/lab-03-adevelopment-loop.md)
- **Security & supply chain** → [.github/SECURITY.md](.github/SECURITY.md), [knowledge/docs/guides/security-minima.md](knowledge/docs/guides/security-minima.md)
- **How we write (Style Guide)** → [knowledge/docs/guides/content-style-guide.md](knowledge/docs/guides/content-style-guide.md), [Editorial workflow](knowledge/docs/guides/editorial-workflow.md), [Versioning Docs](knowledge/docs/guides/versioning-docs.md), [Taxonomy & tags](knowledge/docs/guides/taxonomy-tags.md)

> Social preview: view [knowledge/assets/social/wise-tech-1280x640.png](knowledge/assets/social/wise-tech-1280x640.png)

## Key resources
- [Wise Tech principles](knowledge/docs/principles/wise-tech-principles.md) summarize the repository’s foundational agreements.
- [Contribution guide](knowledge/docs/guides/contribution-guide.md) explains how to document learnings and cross-references.
- [Developer playbook](knowledge/docs/playbooks/developer-playbook.md) / [Platform playbook](knowledge/docs/playbooks/platform-playbook.md) propose early wins and KPIs by role.
- [Wise Tech approach (EN)](knowledge/docs/en/wise-tech-approach.md) / [Wise Tech approach (ES)](knowledge/docs/es/wise-tech-approach.md) articulate the strategic narrative.
- [Architecture decisions](knowledge/adr/INDEX.md) centralizes the ADRs with their history and tags.
- [Payments Scenario](experience/scenarios/payments/README.md) integrates code, contracts, tests, and bilingual runbooks.

The payments scenario functions as the canonical business case: service failures demonstrate fault-handling playbooks, the contracts illustrate consumer-driven testing, and the bilingual runbooks keep resilience actionable.

## Learning outcomes & KPIs
- [Developer playbook](knowledge/docs/playbooks/developer-playbook.md#indicadores-clave-de-experimento) details KPIs such as the payments scenario cycle time and defects detected before merge.
- [Platform playbook](knowledge/docs/playbooks/platform-playbook.md#indicadores-clave-de-experimento) explains how to measure simulated MTTR, runbook coverage, and team satisfaction.
- Each [role path](knowledge/docs/personas/_index.md) includes “First 60 minutes” guidance to convert learning into immediate action.

## FAQ
### Which commands do the CI workflows run?
The [`quality`](.github/workflows/quality.yml) pipeline runs `make -f operations/Makefile ci`, chaining `install`, `fmt`, `lint`, `test`, `parity`, `docs`, and `verify-links`. Running the same command locally gives you the verdict before opening a PR.

### How are the documentation and links validated?
The [`docs-and-links`](.github/workflows/docs-and-links.yml) workflow triggers when Markdown or MkDocs files change. It rebuilds the site with `mkdocs build --strict -f operations/mkdocs.yml`, validates front matter and “See also” sections with `python operations/scripts/validate-content-metadata.py`, and runs `python operations/scripts/check-links.py` to detect broken internal links. Locally you can run `make -f operations/Makefile content-meta` before pushing changes.

### How do I validate bilingual parity when I edit only one language?
Run `make -f operations/Makefile parity` to compare the `knowledge/docs/en/` and `knowledge/docs/es/` paths. If the translation does not exist yet, add a `TODO (parity)` note in the file and document the plan in your PR so the pipeline does not fail.

### What if MkDocs is already using port 8000?
You can redefine the port temporarily with `mkdocs serve -a 127.0.0.1:8010` or export `MKDOCS_SERVE_ADDR=127.0.0.1:8010` before running `make -f operations/Makefile docs`.

## Contributing
When proposing changes, please update the English document first and then provide an equivalent translation under `es/`. Use the pull request template checklist and link back to the Essential principles, recipes, and onboarding guides whenever you introduce new knowledge.

Automation keeps both languages synchronized. Run `make -f operations/Makefile parity` or rely on the **Bilingual Parity** GitHub Action before merging.

For detailed expectations, consult [Contributing Guide (English)](governance/CONTRIBUTING.md) and [Contribution Guide (Spanish)](governance/CONTRIBUTING.es.md).

---

For licensing information, see [LICENSE](LICENSE).
