<!-- metadata
para_quien: Equipos y contribuidores que consultan "Payments Observability Guide" en The Wise Tech.
objetivo: Proporcionar un contexto accionable sobre payments observability guide.
cuando_usar: Recurre a este documento cuando necesites aplicar o compartir detalles de payments observability guide.
estado: active
-->

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

🗳️ **¿Te fue útil este documento?**
- [ ] Sí, resolvió mi duda
- [ ] Más o menos, necesito más contexto
- [ ] No me ayudó

📢 [Abre un feedback aquí](https://github.com/scanalesespinoza/the-wise-tech/issues/new?template=feedback.yml)

---
