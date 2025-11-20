## What/Why
- …

## Wise Tech Principle Reinforced
- [ ] Simplicity
- [ ] Continuous Improvement
- [ ] Resilience
- [ ] Knowledge Capitalization
- [ ] Human Purpose & Connection

## Ops Signals
- Expected SLO impact (latency/errors): ☐ none ☐ low ☐ medium ☐ high
- `x-correlation-id` propagation: ☐ yes ☐ no
- Structured logs + p95 metric present: ☐ yes ☐ no
- Evidence: (paste from `make telemetry-smoke` or link to SLO/policies)

## Human Feedback References
- Related user-feedback issue(s): #____ (link)
- Postmortem or proposal referenced: #____ (link)
- Summary of feedback applied: …

## Checks
- [ ] Tests pass (`make test`)
- [ ] Bilingual parity (`make parity`)
- [ ] Lint/format (`make lint` / `make fmt`)
- [ ] Docs updated / links verified
- [ ] Resilience/SLOs reviewed if impacta (`make resilience-check` / `make slos`)

## QA de traducción (obligatorio en i18n)
- Batch ID: w?-b?
- Archivos cubiertos: …
- Términos clave (glosario): …
- `mkdocs build --strict`: ☐ OK
- Ortografía/gramática + glosario (`python scripts/validate-spanish-quality.py`): ☐ OK
- Links verificados (`scripts/check-links.py --root docs --strict`): ☐ OK
- Front-matter / See also / tags (ES): ☐ OK (`python scripts/validate-content-metadata.py`)
- Revisión técnica: ☐ OK (by …)
- Revisión de estilo: ☐ OK (by …)

---

🗳️ **¿Te fue útil este documento?**
- [ ] Sí, resolvió mi duda
- [ ] Más o menos, necesito más contexto
- [ ] No me ayudó

📢 [Abre un feedback aquí](https://github.com/scanalesespinoza/the-wise-tech/issues/new?template=feedback.yml)

---
