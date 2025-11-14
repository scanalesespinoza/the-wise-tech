---
title: "Developer Playbook — mínimos accionables"
tags: ["developers", "playbooks", "resilience"]
---
# Developer Playbook — mínimos accionables

## Principios operativos (≤5)
- Idempotencia en handlers críticos usando llaves de idempotencia asociadas a cada solicitud.
- Registra `correlation-id` en logs y trazas para seguir el flujo end-to-end.
- Escala tus pruebas en orden: unitarias → contractuales → resiliencia.
- CI local debe reflejar CI remoto (`make ci` como contrato de salud).
- Documenta decisiones con ADR breves que enlacen principios de Wise Tech.

## Snippets rápidos
- [Snippet de correlation-id en Python](../snippets/python-correlation-id.md).
- Ejecuta `python -m pytest scenarios/payments/tests/test_payments_flow.py::test_successful_payment` como test focalizado.
- Inspírate en `scenarios/payments/tests/test_service_errors.py` para validar reintentos e idempotencia.

## Checklist PR (dev)
- [ ] Tests verdes (`make test`).
- [ ] Paridad bilingüe (`make parity`).
- [ ] Lint/format (`make lint` / `make fmt`).
- [ ] Documentación actualizada con enlaces relativos.
- [ ] Referencia explícita al/los principio(s) de Wise Tech aplicados.

## KPIs mínimos (dev)
- Tiempo hasta el primer commit (TTFC) < 1 día.
- 1 PR pequeño que combine test + doc.
- Flaky tests detectados en la PR: 0.

---

# Developer Playbook — actionable minimums (EN)

## Operating principles (≤5)
- Enforce idempotency on critical handlers via request-scoped idempotency keys.
- Capture the `correlation-id` in logs and traces to follow the end-to-end flow.
- Layer your testing strategy: unit → contract → resilience checks.
- Local CI must mirror remote CI (`make ci` as the shared health contract).
- Record decisions with concise ADRs referencing Wise Tech principles.

## Quick snippets
- [Python correlation-id snippet](../snippets/python-correlation-id.md).
- Run `python -m pytest scenarios/payments/tests/test_payments_flow.py::test_successful_payment` as a focused test example.
- Use `scenarios/payments/tests/test_service_errors.py` to validate retries and idempotency behaviour.

## PR checklist (dev)
- [ ] Tests are green (`make test`).
- [ ] Bilingual parity verified (`make parity`).
- [ ] Lint/format checks (`make lint` / `make fmt`).
- [ ] Documentation refreshed with relative links.
- [ ] Explicit reference to the applicable Wise Tech principle(s).

## Minimum KPIs (dev)
- Time to first commit (TTFC) < 1 day.
- One small PR combining tests + docs.
- Flaky tests detected in the PR: 0.

## See also / Ver también
- [Wise Tech principles](../principles/wise-tech-principles.md)
- [Quickstart](../guides/quickstart.md)
- [Payments overview](../scenarios/payments-overview.md)
- [Platform playbook](platform-playbook.md)
