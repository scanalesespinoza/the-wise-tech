---
title: "Platform Playbook — mínimos operables"
tags: ["platform-engineers", "playbooks", "resilience"]
---
## Propósito
Enmarca cómo Platform Playbook — mínimos operables ayuda a mantener decisiones alineadas con The Wise Tech.

## Audiencia
Personas y equipos que necesitan una guía rápida sobre Platform Playbook — mínimos operables.

## Cuándo usarlo
Consúltalo cuando requieras referencias inmediatas para Platform Playbook — mínimos operables o debas compartir el enfoque con otros equipos.

> **Propósito:** Dar contexto accionable sobre Platform Playbook — mínimos operables dentro de The Wise Tech.
> **Audiencia:** Equipos y perfiles interesados en las bases de conocimiento y lineamientos del programa.
> **Uso recomendado:** Consulta este documento cuando necesites aplicar o compartir detalles de Platform Playbook — mínimos operables.
> **Estado:** Activo.


## Tabla de navegación

- [Contratos de operación](#contratos-de-operacin)
- [Runbooks & feedback](#runbooks--feedback)
- [Checklist PR (platform)](#checklist-pr-platform)
- [KPIs mínimos (platform)](#kpis-mnimos-platform)
- [Operating contracts](#operating-contracts)
- [Runbooks & feedback loops](#runbooks--feedback-loops)
- [PR checklist (platform)](#pr-checklist-platform)
- [Minimum KPIs (platform)](#minimum-kpis-platform)
- [See also / Ver también](#see-also--ver-tambin)

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
---
Última modificación: 2025-11-16

🗳️ **¿Te fue útil este documento?**
- [ ] Sí, resolvió mi duda
- [ ] Más o menos
- [ ] No me ayudó

💬 [Deja tu feedback](https://github.com/scanalesespinoza/the-wise-tech/issues/new?template=feedback.yml)

---

