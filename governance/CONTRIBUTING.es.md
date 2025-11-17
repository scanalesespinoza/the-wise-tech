## 🎯 Purpose

## 👥 Audience

## 🤔 When to use it

## 🧠 What behavior should this enable?

## 💡 Why this matters (wisdom)

# Contribution Guide

Thanks for contributing to The Wise Tech. All documentation now lives in `knowledge/docs/` with curated paths per role.

## Recommended Flow
1. Review the [quickstart](../knowledge/docs/guides/quickstart.md) and configure your environment (`make -f operations/Makefile install`).
2. Work on small, descriptive branches (`feat-docs-one-page`) so reviews stay focused.
3. Run `make -f operations/Makefile ci` to mirror the pipeline verdict before you request feedback.
4. Complete the [PR template](../.github/PULL_REQUEST_TEMPLATE.md) and highlight the principle being reinforced.
5. Ask for cross-review from the impacted roles (Consumers, Developers, Platform Engineers).

## Essential Resources
- [Wise Tech principles](../knowledge/docs/principles/wise-tech-principles.md)
- [Developers journey](../knowledge/docs/personas/developers-overview.md)
- [Platform playbook](../knowledge/docs/playbooks/platform-playbook.md)
- [Roadmap](../knowledge/docs/roadmap/roadmap.md)

## Automation
- The [`quality`](../.github/workflows/quality.yml) and [`docs-and-links`](../.github/workflows/docs-and-links.yml) workflows run exactly the Makefile commands (`make -f operations/Makefile ci` plus documentation validation) to maintain parity between local and remote runs.
- Run `make -f operations/Makefile verify-links` or `python operations/scripts/check-links.py` whenever you edit large docs to catch broken internal links early.
- Document strategic decisions in the [ADR index](../knowledge/adr/INDEX.md).

## Flujo bilingüe (EN ➜ ES)
- Documenta el trabajo en [`audit/translation-queue.yml`](../audit/translation-queue.yml). Cada entrada apunta al archivo fuente en inglés y a la ruta objetivo bajo `knowledge/docs/es/`, además de indicar los revisores del batch.
- Ejecuta `make -f operations/Makefile translate-batch BATCH=<id>` para generar el `.es.md`. Usa `DRY_RUN=1` cuando sólo quieras revisar la salida: el script [`operations/scripts/translate_batch.py`](../operations/scripts/translate_batch.py) respeta los bloques de código y aplica el glosario.
- Actualiza el tablero con `make -f operations/Makefile translate-status` y sube el nuevo [`audit/translation-status.md`](../audit/translation-status.md). El workflow `docs-and-links` corre `translate-status-check`, así que cualquier desbalance aparece en CI junto al chequeo de `parity`.

---

🗳️ **¿Te fue útil este documento?**
- [ ] Sí, resolvió mi duda
- [ ] Más o menos, necesito más contexto
- [ ] No me ayudó

📢 [Abre un feedback aquí](https://github.com/scanalesespinoza/the-wise-tech/issues/new?template=feedback.yml)

---
