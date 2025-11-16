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

---

🗳️ **¿Te fue útil este documento?**
- [ ] Sí, resolvió mi duda
- [ ] Más o menos, necesito más contexto
- [ ] No me ayudó

📢 [Abre un feedback aquí](https://github.com/scanalesespinoza/the-wise-tech/issues/new?template=feedback.yml)

---
