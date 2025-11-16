## Propósito
Enmarca cómo Payments Incident Runbook ayuda a mantener decisiones alineadas con The Wise Tech.

## Audiencia
Personas y equipos que necesitan una guía rápida sobre Payments Incident Runbook.

## Cuándo usarlo
Consúltalo cuando requieras referencias inmediatas para Payments Incident Runbook o debas compartir el enfoque con otros equipos.

> **Propósito:** Dar contexto accionable sobre Payments Incident Runbook dentro de The Wise Tech.
> **Audiencia:** Equipos y perfiles interesados en los escenarios y rutas de experiencia práctica.
> **Uso recomendado:** Consulta este documento cuando necesites aplicar o compartir detalles de Payments Incident Runbook.
> **Estado:** Activo.


## Tabla de navegación

- [Scope](#scope)
- [First response checklist](#first-response-checklist)
- [Triage by error type](#triage-by-error-type)
- [Recovery and follow-up](#recovery-and-follow-up)

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
Última modificación: 2025-11-16

🗳️ **¿Te fue útil este documento?**
- [ ] Sí, resolvió mi duda
- [ ] Más o menos
- [ ] No me ayudó

💬 [Deja tu feedback](https://github.com/scanalesespinoza/the-wise-tech/issues/new?template=feedback.yml)

---

