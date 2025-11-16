## Propósito
Enmarca cómo Payments Observability Guide ayuda a mantener decisiones alineadas con The Wise Tech.

## Audiencia
Personas y equipos que necesitan una guía rápida sobre Payments Observability Guide.

## Cuándo usarlo
Consúltalo cuando requieras referencias inmediatas para Payments Observability Guide o debas compartir el enfoque con otros equipos.

> **Propósito:** Dar contexto accionable sobre Payments Observability Guide dentro de The Wise Tech.
> **Audiencia:** Equipos y perfiles interesados en los escenarios y rutas de experiencia práctica.
> **Uso recomendado:** Consulta este documento cuando necesites aplicar o compartir detalles de Payments Observability Guide.
> **Estado:** Activo.


## Tabla de navegación

- [Key dashboards](#key-dashboards)
- [Alerts](#alerts)
- [Traces and logging](#traces-and-logging)
- [Feedback loop](#feedback-loop)

# Payments Observability Guide

Wise Tech favors purposeful telemetry. This guide connects the payments
scenario with dashboards, alerts, and trace signals.

## Key dashboards

- **`payments_authorizations`.** Tracks authorization volume, decline
  ratio, timeout ratio, and P95 latency. The runbook references it during
  triage.
- **`payments_retries`.** Monitors the automated retry job. Alerts when
  more than 5% of retries end in `PAYMENT_UNKNOWN`.

## Alerts

| Name | Source | Threshold | Owner |
| --- | --- | --- | --- |
| `payments-critical` | PagerDuty | Timeout ratio > 3% for 5 minutes | Payments on-call |
| `payments-contract-drift` | GitHub Actions | Pact verification fails | Scenario maintainer |

## Traces and logging

- Inject `correlation_id` into every request. The service errors expose
  the value through the `reference_id` attribute to support post-mortems.
- Log bilingual remediation hints so customer care can act without
  translation delays.

## Feedback loop

After every incident update the dashboards or alert thresholds and record
changes in both language versions of this document to preserve parity.
---
Última modificación: 2025-11-16

🗳️ **¿Te fue útil este documento?**
- [ ] Sí, resolvió mi duda
- [ ] Más o menos
- [ ] No me ayudó

💬 [Deja tu feedback](https://github.com/scanalesespinoza/the-wise-tech/issues/new?template=feedback.yml)

---

