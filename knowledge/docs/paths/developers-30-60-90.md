---
title: "Developers — 30/60/90"
tags: ["developers", "paths", "quickstart"]
---
<!-- metadata
para_quien: Equipos y contribuidores que consultan "Developers — 30/60/90" en The Wise Tech.
objetivo: Proporcionar un contexto accionable sobre developers — 30/60/90.
cuando_usar: Recurre a este documento cuando necesites aplicar o compartir detalles de developers — 30/60/90.
estado: active
-->

# Developers — 30/60/90

## 30 min
- Ejecuta `make -f operations/Makefile install && make -f operations/Makefile test && make -f operations/Makefile parity && make -f operations/Makefile docs` para asegurar paridad local.
- Corre un test focalizado del escenario de pagos (`python -m pytest experience/scenarios/payments/systems/tests/test_payments_flow.py::test_successful_payment`).

## 60 min (first win)
- Agrega un test nuevo o corrige un enlace/documento relacionado con payments.
- Prepara una PR pequeña que referencie al menos un principio de Wise Tech.

## 90 min (resiliencia mínima)
- Añade timeout/retry o aplica el snippet de idempotencia en un ejemplo.
- Documenta el impacto con una nota breve y enlázala en la PR.

**KPIs**
- TTFC < 1 día.
- 1 PR con test + doc.
- Flaky tests detectados: 0.

---

# Developers — 30/60/90 (EN)

## 30 min
- Run `make -f operations/Makefile install && make -f operations/Makefile test && make -f operations/Makefile parity && make -f operations/Makefile docs` to secure local parity.
- Execute a focused payments scenario test (`python -m pytest experience/scenarios/payments/systems/tests/test_payments_flow.py::test_successful_payment`).

## 60 min (first win)
- Add a new test or fix a payment-related link/doc.
- Prepare a small PR referencing at least one Wise Tech principle.

## 90 min (minimum resilience)
- Add a timeout/retry or apply the idempotency snippet in an example.
- Document the impact with a short note and link it in the PR.

**KPIs**
- TTFC < 1 day.
- One PR including tests + docs.
- Flaky tests detected: 0.

## See also / Ver también
- [Developers overview](../personas/developers-overview.md)
- [Developer Playbook](../playbooks/developer-playbook.md)
- [Payments overview](../scenarios/payments-overview.md)
- [Quickstart](../guides/quickstart.md)

---

🗳️ **¿Te fue útil este documento?**
- [ ] Sí, resolvió mi duda
- [ ] Más o menos, necesito más contexto
- [ ] No me ayudó

📢 [Abre un feedback aquí](https://github.com/scanalesespinoza/the-wise-tech/issues/new?template=feedback.yml)

---
