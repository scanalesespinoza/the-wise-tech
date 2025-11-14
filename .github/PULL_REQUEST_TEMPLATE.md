## What/Why
- Describe el objetivo y qué experiencia desbloquea.
- Enlaza notas de soporte, issues o métricas relevantes.

## Wise Tech Principle Reinforced
- [ ] Simplicity
- [ ] Continuous Improvement
- [ ] Resilience
- [ ] Knowledge Capitalization
- [ ] Human Purpose & Connection

## Ops Signals
- Expected SLO impact (latency/errors): ☐ none ☐ low ☐ medium ☐ high
- x-correlation-id propagation: ☐ yes ☐ no
- Structured logs + p95 metric present: ☐ yes ☐ no
- Evidence (paste `make telemetry-smoke` summary or log extract):
  <!-- attach snippet -->

## Checks
- [ ] Tests pass locally (`make test`)
- [ ] Bilingual parity (`make parity`)
- [ ] Lint & format (`make lint` / `make fmt`)
- [ ] Docs updated / links verificados (`python scripts/check-links.py --strict`)
- [ ] Telemetry smoke ejecutado (cuando aplique)

## Mentoring signal
- Notifica a las personas de CODEOWNERS correspondientes.
- Añade ejemplos de buenas prácticas (idempotencia, trazas, ADR) si aplica.
