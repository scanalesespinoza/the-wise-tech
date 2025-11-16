<!-- metadata
para_quien: Equipos y contribuidores que consultan "Payments Incident Runbook" en The Wise Tech.
objetivo: Proporcionar un contexto accionable sobre payments incident runbook.
cuando_usar: Recurre a este documento cuando necesites aplicar o compartir detalles de payments incident runbook.
estado: active
-->

# Payments Incident Runbook

This document shows how Wise Tech teams respond to customer-facing issues
in the payments scenario.

## Scope

- Checkout errors surfaced through the `checkout-ui` channel.
- Declines propagated from external issuers.
- Timeouts or unknown failures when calling the acquiring provider.

## First response checklist

1. **Validate telemetry.** Open the `payments_authorizations` dashboard
   (see observability guide) and confirm the spike or degradation.
2. **Acknowledge alerts.** The on-call rotation receives PagerDuty event
   `payments-critical`. Acknowledge within 5 minutes.
3. **Communicate.** Update the shared `#status-payments` channel and tag
   customer support with the current status.

## Triage by error type

| Signal | Action |
| --- | --- |
| `PAYMENT_DECLINED` | Confirm issuer response code, share bilingual
| remediation hint with support, and collect examples for the daily trend
| review. |
| `PAYMENT_TIMEOUT` | Trigger the automated retry job. If more than 3
| consecutive timeouts occur per provider, engage the provider liaison and
| consider traffic shaping. |
| `PAYMENT_UNKNOWN` | Escalate to Level 2 after gathering request/response
| payloads and correlation IDs. |

## Recovery and follow-up

- Create an incident timeline using the Wise Tech retrospective template.
- File learnings back into the `knowledge/docs/es/runbook.md` and `knowledge/docs/en/runbook.md`
  pair to maintain bilingual knowledge.
- Update contract tests if new response fields were involved, preserving
  observability parity.

---

🗳️ **¿Te fue útil este documento?**
- [ ] Sí, resolvió mi duda
- [ ] Más o menos, necesito más contexto
- [ ] No me ayudó

📢 [Abre un feedback aquí](https://github.com/scanalesespinoza/the-wise-tech/issues/new?template=feedback.yml)

---
