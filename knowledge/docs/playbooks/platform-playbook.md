---
title: "Platform Playbook — mínimos operables"
tags: ["platform-engineers", "playbooks", "resilience"]
---
# Platform Playbook — mínimos operables

## Contratos de operación
- Revisa SLOs y error budgets vigentes; documenta acciones ante cada brecha.
- Aplica políticas de resiliencia: timeouts, retries, circuit-breakers y bulkheads alineados al escenario.
- Asegura telemetría mínima: métricas accionables, logs estructurados y trazas enlazadas a `correlation-id`.

## Runbooks & feedback
- Runbook del escenario “payments”: sigue el [Payments overview](../scenarios/payments-overview.md) y navega a `experience/scenarios/payments/docs/`.
- Plantilla de postmortem (coming soon): [Knowledge base](../knowledge/index.md).
- Usa issues y plantillas de PR como bucle de feedback continuo.

## Checklist PR (platform)
- [ ] Validar políticas (`make resilience-check`).
- [ ] Validar SLOs (`make slos`) si existe.
- [ ] Verificar enlaces (`make -f operations/Makefile verify-links`).
- [ ] CI verde (quality + docs-and-links).

## KPIs mínimos (platform)
- 0 enlaces rotos en cada PR.
- 100% de políticas válidas en PRs que toquen `systems/platform/**`.
- Reducir tiempo de diagnóstico local en 20% con trazas, métricas y logs presentes.

---

# Platform Playbook — operational minimums (EN)

## Operating contracts
- Review active SLOs and error budgets; document actions for each breach.
- Enforce resilience policies: timeouts, retries, circuit breakers, and bulkheads aligned with the scenario.
- Guarantee baseline telemetry: actionable metrics, structured logs, and traces linked to the `correlation-id`.

## Runbooks & feedback loops
- Payments scenario runbook: follow the [Payments overview](../scenarios/payments-overview.md) and browse `experience/scenarios/payments/docs/`.
- Postmortem template (coming soon): [Knowledge base](../knowledge/index.md).
- Use issue and PR templates as continuous feedback loops.

## PR checklist (platform)
- [ ] Validate policies (`make resilience-check`).
- [ ] Validate SLOs (`make slos`) if available.
- [ ] Verify links (`make -f operations/Makefile verify-links`).
- [ ] Green CI (quality + docs-and-links).

## Minimum KPIs (platform)
- Zero broken links per PR.
- 100% of policies validated on PRs touching `systems/platform/**`.
- Reduce local diagnostic time by 20% through traces, metrics, and logs.

## See also / Ver también
- [Developer playbook](developer-playbook.md)
- [Payments overview](../scenarios/payments-overview.md)
- [Platform engineers overview](../personas/platform-engineers-overview.md)
- [Roadmap](../roadmap/roadmap.md)
