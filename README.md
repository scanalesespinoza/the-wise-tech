# The Wise Tech

> 📑 ¿Buscas la versión en español? Visita [README.es.md](README.es.md). Keep bilingual sections below for historical and legal context.

## Status
[![quality](https://github.com/scanalesespinoza/the-wise-tech/actions/workflows/quality.yml/badge.svg)](https://github.com/scanalesespinoza/the-wise-tech/actions/workflows/quality.yml)
[![docs-and-links](https://github.com/scanalesespinoza/the-wise-tech/actions/workflows/docs-and-links.yml/badge.svg)](https://github.com/scanalesespinoza/the-wise-tech/actions/workflows/docs-and-links.yml)
[![gitleaks](https://github.com/scanalesespinoza/the-wise-tech/actions/workflows/gitleaks.yml/badge.svg)](https://github.com/scanalesespinoza/the-wise-tech/actions/workflows/gitleaks.yml)
[![pre-commit](https://github.com/scanalesespinoza/the-wise-tech/actions/workflows/pre-commit.yml/badge.svg)](https://github.com/scanalesespinoza/the-wise-tech/actions/workflows/pre-commit.yml)
[![Based on The Wise Tech – Last sync: 2024-06-01 (manually updated)](https://img.shields.io/badge/%F0%9F%94%84%20Based%20on%20The%20Wise%20Tech-Last%20sync%3A%202024--06--01%20(manually%20updated)-6f42c1)](UPSTREAM_CHANGES.md)

> 🔄 This repository is based on **The Wise Tech** template. Check for upstream updates [here](UPSTREAM_CHANGES.md).

This repository turns the Wise Tech philosophy into shared actions: a navigable one-page hub for learning, building, and operating technology with a human purpose.

### ⚡ TL;DR — What is *The Wise Tech*?

**The Wise Tech** is not just about learning technology. It is about applying it intentionally to shape behavior.

This repository helps you move beyond knowing how tech works into understanding **when, why, and for whom** it should be applied to create predictable, valuable outcomes.

It is based on **experience as a learning engine**, where context, action, and feedback are core.

It is not only about connecting information—it is about driving results that maximize benefits and make the leap from knowledge to wisdom.

> **Information → Knowledge → Behavior → Real Value**

That is what *The Wise Tech* is all about.

## Vision and purpose

This repository is an expanding knowledge base that elevates technology quality by prioritizing lessons learned, established patterns, and validated designs. Its mission is to break the cycle of low-cost, low-quality software that dominates the market today—software that generates collateral issues such as security gaps, unnecessary spending driven by technical debt, and economic plus environmental harm.

Wise Tech focuses on modern needs while helping orient the future. As experience gaps widen and professionals rely on increasingly shallow tooling and artificial intelligence, durable knowledge becomes the shared advantage. Captured expertise empowers both traditional teams building technology by hand and emerging teams orchestrating AI-led development.

The highest priority is the business logic itself—the workloads where behavior, reliability, and revenue intersect. Platform and infrastructure assets are mature enough to act as supporting tools, but the center of gravity is in defining robust architectures plus the mandatory principles that describe expected behavior and implementation.

This site curates a taxonomic body of principles, models, and methodologies for delivering world-class technology. Although still young, it aims to become a reference for training AI systems and professionals who must respond to demanding, high-stakes scenarios.

## Start here

1. Read the overview in [Docs Home](knowledge/docs/index.md) to locate the principles, paths, and labs.
2. Use the [Value index](#value-index) to jump directly to the most relevant docs for your goal.
3. If you want to spin up the local environment, continue with [Quick start (7 steps)](#quick-start-7-steps).
4. ¿Necesitas resultados inmediatos? Usa los Fast Track de cada perfil: [Consumers](knowledge/docs/paths/consumers/fast-track.md), [Developers](knowledge/docs/paths/developers/fast-track.md) y [Platform Engineers](knowledge/docs/paths/platform-engineers/fast-track.md).

Para una vista tipo “panel con botones”, visita la [Navegación visual](docs/visual-navigation.md).

➡️ Explore the full documentation in [Docs Home](knowledge/docs/index.md) or visit the published version on GitHub Pages: https://scanalesespinoza.github.io/the-wise-tech/.

## Value index

Use this lightweight index as a shortcut to the highest-signal docs:

- **Orientation**
  - [Docs Home](knowledge/docs/index.md) — one-page map of principles, guides, and personas.
  - [Quickstart](knowledge/docs/guides/quickstart.md) — 7 commands to install, test, and preview docs locally.
  - [Navigation map](docs/visual-navigation.md) — visual “button panel” that pairs roles with expected outcomes.
- **Role essentials**
  - **Technology Consumers** → [overview](knowledge/docs/personas/consumers-overview.md), [Fast Track](knowledge/docs/paths/consumers/fast-track.md), [Learning Path 30/60/90](knowledge/docs/paths/consumers-30-60-90.md).
  - **Software Developers** → [overview](knowledge/docs/personas/developers-overview.md), [Fast Track](knowledge/docs/paths/developers/fast-track.md), [Learning Path 30/60/90](knowledge/docs/paths/developers-30-60-90.md).
  - **Platform Engineers** → [overview](knowledge/docs/personas/platform-engineers-overview.md), [Fast Track](knowledge/docs/paths/platform-engineers/fast-track.md), [Learning Path 30/60/90](knowledge/docs/paths/platform-engineers-30-60-90.md).
- **Hands-on labs**
  - [Lab 01 — Resilience Basics](knowledge/docs/labs/lab-01-resilience-basics.md) — build the baseline service guardrails.
  - [Lab 02 — Observability Minima](knowledge/docs/labs/lab-02-observability-minima.md) — apply telemetry and tracing standards.
  - [Lab 03 — aDevelopment Loop](knowledge/docs/labs/lab-03-adevelopment-loop.md) — connect dev/test feedback loops.
- **Operational references**
  - [Developer playbook](knowledge/docs/playbooks/developer-playbook.md) & [Platform playbook](knowledge/docs/playbooks/platform-playbook.md) — KPIs, runbooks, and role-specific wins.
  - [Resilience policies guide](knowledge/docs/guides/resilience-policies.md) — narrative + YAML controls ready to reuse.
  - [Telemetry minimum guide](knowledge/docs/guides/telemetry-minima.md) — the “good enough” instrumentation checklist.
- **Feedback & contributions**
  - [Contribution guide](knowledge/docs/guides/contribution-guide.md) — expectations, templates, and bilingual workflow.
  - [Feedback loops guide](knowledge/docs/guides/feedback-loops.md) — playbook for closing the action/learning gap.
  - [Roadmap](knowledge/docs/roadmap/roadmap.md) — backlog of proposed improvements you can pick up.

## Quick start (7 steps)

1) git clone https://github.com/scanalesespinoza/the-wise-tech.git
2) cd the-wise-tech
3) make -f operations/Makefile install
4) make -f operations/Makefile test
5) make -f operations/Makefile parity
6) make -f operations/Makefile docs
7) open http://127.0.0.1:8000 and use the Value index to jump to the resources you need

Optional (dev stack):

- `make -f operations/Makefile dev-up` → Jaeger at `http://127.0.0.1:16686`, OTLP at `:4318`
- `make -f operations/Makefile docs-live` → Docs at `http://127.0.0.1:8000`

Check the [general quickstart](knowledge/docs/guides/quickstart.md) when you need the ultra-short version to share with your team.

## Bilingual workflow (English ➜ Español)

1. **Prioritize the English source.** Edit the canonical file (for example `knowledge/docs/guides/resilience-policies.md`).
2. **Queue the translation.** Add or update the corresponding entry in [`audit/translation-queue.yml`](audit/translation-queue.yml) so it points to the target path under `knowledge/docs/es/`.
3. **Preview the batch.** Run `make -f operations/Makefile translate-batch BATCH=<id> DRY_RUN=1` to simulate the translation for the selected batch without writing files. The command uses [`operations/scripts/translate_batch.py`](operations/scripts/translate_batch.py), which keeps code blocks intact and applies the glossary automatically.
4. **Generate/update the Spanish file.** Re-run the same command without `DRY_RUN=1` (and after configuring your translation provider) to create or refresh the `.es` file. Each run updates the queue with the new status.
5. **Publish the status.** Execute `make -f operations/Makefile translate-status` to rewrite [`audit/translation-status.md`](audit/translation-status.md) and capture the new parity snapshot.
6. **Validate before the PR.** Run `make -f operations/Makefile translate-verify` (which chains `parity` + `translate-status-check`) to ensure the pipeline will not regress the bilingual coverage.

The documentation-only workflows now invoke the same checks, so every PR exposes the current parity state without requiring access to external translation APIs.

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

- 🧭 **I only want to read** → open the published version on [GitHub Pages](https://scanalesespinoza.github.io/the-wise-tech/) and follow the [Value index](#value-index) to navigate by outcome.
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
  - Three Context Framework → [knowledge/docs/principles/three-context-framework.md](knowledge/docs/principles/three-context-framework.md)
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

---

🗳️ **¿Te fue útil este documento?**
- [ ] Sí, resolvió mi duda
- [ ] Más o menos, necesito más contexto
- [ ] No me ayudó

📢 [Abre un feedback aquí](https://github.com/scanalesespinoza/the-wise-tech/issues/new?template=feedback.yml)

---
