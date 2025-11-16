---
title: "PR ideas"
tags: ["developers", "knowledge-capitalization"]
---
<!-- metadata
para_quien: Equipos y contribuidores que consultan "PR ideas" en The Wise Tech.
objetivo: Proporcionar un contexto accionable sobre pr ideas.
cuando_usar: Recurre a este documento cuando necesites aplicar o compartir detalles de pr ideas.
estado: active
-->

# PR ideas

Small tasks to practice the contribution flow:

1. **Document site metrics**
   - Update `docs/metrics/site-metrics.md` with the latest CI run.
   - Add a short note to the README inside "Learning outcomes" if the primary indicator changes.
2. **Improve "See also" links**
   - Pick a guide in `docs/guides/` that does not yet have a "See also" section.
   - Add relevant cross-references and validate them with `make content-meta`.
3. **Translate a snippet**
   - Create the missing English or Spanish version in `docs/snippets/`.
   - Run `make -f operations/Makefile parity` to confirm the routes between languages stay aligned.

Each idea must include a note in the PR explaining which guide, snippet, or metric you changed.

## See also
- [Roadmap](roadmap.md)
- [Contribution guide](../guides/contribution-guide.md)

---

🗳️ **¿Te fue útil este documento?**
- [ ] Sí, resolvió mi duda
- [ ] Más o menos, necesito más contexto
- [ ] No me ayudó

📢 [Abre un feedback aquí](https://github.com/scanalesespinoza/the-wise-tech/issues/new?template=feedback.yml)

---
