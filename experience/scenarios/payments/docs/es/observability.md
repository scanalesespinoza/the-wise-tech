<!-- metadata
para_quien: Equipos y contribuidores que consultan "Guía de Observabilidad de Pagos" en The Wise Tech.
objetivo: Proporcionar un contexto accionable sobre guía de observabilidad de pagos.
cuando_usar: Recurre a este documento cuando necesites aplicar o compartir detalles de guía de observabilidad de pagos.
estado: active
-->

# Guía de Observabilidad de Pagos

Wise Tech favorece la telemetría con propósito. Esta guía conecta el
escenario de pagos con dashboards, alertas y trazas.

## Dashboards clave

- **`payments_authorizations`.** Monitorea el volumen de autorizaciones,
  ratio de rechazos, ratio de timeouts y latencia P95. El runbook lo
  referencia durante el triage.
- **`payments_retries`.** Observa el job automático de reintentos. Alerta
  cuando más del 5% de reintentos terminan en `PAYMENT_UNKNOWN`.

## Alertas

| Nombre | Fuente | Umbral | Dueño |
| --- | --- | --- | --- |
| `payments-critical` | PagerDuty | Ratio de timeouts > 3% por 5 minutos | On-call de Pagos |
| `payments-contract-drift` | GitHub Actions | Falla la verificación de Pact | Responsable del escenario |

## Trazas y logging

- Inyecta `correlation_id` en cada petición. Las excepciones del servicio
  exponen el valor a través de `reference_id` para facilitar los
  post-mortems.
- Registra las pistas de remediación bilingües para que atención a
  clientes actúe sin retrasos de traducción.

## Bucle de retroalimentación

Después de cada incidente actualiza los dashboards o umbrales de alertas y
registra los cambios en ambas versiones idiomáticas de este documento para
preservar la paridad.

---

🗳️ **¿Te fue útil este documento?**
- [ ] Sí, resolvió mi duda
- [ ] Más o menos, necesito más contexto
- [ ] No me ayudó

📢 [Abre un feedback aquí](https://github.com/scanalesespinoza/the-wise-tech/issues/new?template=feedback.yml)

---
