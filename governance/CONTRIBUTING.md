## 🎯 Purpose

## 👥 Audience

## 🤔 When to use it

## 🧠 What behavior should this enable?

## 💡 Why this matters (wisdom)

# Contributing Guide

Thank you for helping grow The Wise Tech knowledge base. This repository now uses a single navigation tree in `knowledge/docs/` with role-based journeys.

## Workflow Overview
1. Review the [quickstart](../knowledge/docs/guides/quickstart.md) and set up your environment (`make -f operations/Makefile install`).
2. Create a descriptive branch (`feat-docs-one-page`) and keep each change small and reviewable.
3. Run `make -f operations/Makefile ci` to align your local validation with the pipelines before pushing.
4. Open a PR with the [official template](../.github/PULL_REQUEST_TEMPLATE.md) and highlight the principle being reinforced.
5. Request cross-review from people in the impacted roles (Consumers, Developers, Platform Engineers).

## Key Documentation
- [Wise Tech principles](../knowledge/docs/principles/wise-tech-principles.md)
- [Developers overview](../knowledge/docs/personas/developers-overview.md)
- [Platform playbook](../knowledge/docs/playbooks/platform-playbook.md)
- [Roadmap](../knowledge/docs/roadmap/roadmap.md)

## Automation
- The [`quality`](../.github/workflows/quality.yml) and [`docs-and-links`](../.github/workflows/docs-and-links.yml) workflows run the same commands defined in the Makefile (`make -f operations/Makefile ci` plus the documentation validation) to preserve parity between local and remote environments.
- Run `make -f operations/Makefile verify-links` or `python operations/scripts/check-links.py` when you edit long-form documentation so you can catch broken internal links early.
- Record strategic decisions in the [ADR index](../knowledge/adr/INDEX.md) whenever you change a core process.

## Bilingual workflow (EN ➜ ES)
- Track the work in [`audit/translation-queue.yml`](../audit/translation-queue.yml). Each entry maps the canonical English file to its destination under `knowledge/docs/es/` and lists the reviewers per batch.
- Generate the Spanish file with `make -f operations/Makefile translate-batch BATCH=<id>`. Pass `DRY_RUN=1` the first time so you can inspect the output without touching the repo; the command uses [`operations/scripts/translate_batch.py`](../operations/scripts/translate_batch.py) to keep code blocks intact.
- Refresh the parity report with `make -f operations/Makefile translate-status` and include the updated [`audit/translation-status.md`](../audit/translation-status.md) in your PR. The docs workflow runs `translate-status-check`, so mismatches surface in CI alongside the usual parity check.

---

🗳️ **¿Te fue útil este documento?**
- [ ] Sí, resolvió mi duda
- [ ] Más o menos, necesito más contexto
- [ ] No me ayudó

📢 [Abre un feedback aquí](https://github.com/scanalesespinoza/the-wise-tech/issues/new?template=feedback.yml)

---
