---
title: "Specs: datos y observabilidad PCC"
tags: ["specs", "observability", "data", "pcc"]
---

# Especificación de datos y observabilidad (PCC-O)

## Propósito
Dar trazabilidad total sobre el estado de carga, la comunicación de sobredemanda y la captura de datos para aprendizaje.

## Alcance
- Instrumentación de métricas, logs y eventos.
- Integraciones con tableros, analítica y automatización.

## Requisitos MUST
1. **Estado de carga.** `observability.metrics_exposed` incluye métricas que permitan distinguir `normal-load` de `overload` (ej., throughput, latencia p95, clientes concurrentes).
2. **Señales de sobredemanda.** `observability.overload_signal` y `degradation_signal` describen canal, formato y responsables.
3. **Eventos narrativos.** Cada acción relevante (fallback, rechazo, cleanup) se registra en `observability.events_emitted` con `payload_contract` que incluya estado, impacto y acción recomendada.
4. **Estandarización.** Los nombres/etiquetas declarados siguen la convención `domain.component.metric` o `event.domain.action`.
5. **Zero Trust aplicado.** Los campos `zero_trust.*` documentan cómo se autentican productores/consumidores de telemetría y cómo se valida el esquema.

## Requisitos SHOULD
- Adjuntar enlaces a dashboards o consultas dentro de las descripciones del contrato.
- Publicar métricas derivadas (errores por modo, saturación vs. presupuesto) para acelerar el diagnóstico.
- Integrar las señales con canales de negocio (Slack, CRM) cuando la degradación impacte usuarios finales.

## Requisitos MAY
- Añadir etiquetas que indiquen experimentos o hipótesis activas.
- Automatizar el análisis (por ejemplo, detección de anomalías) siempre que existan alertas manuales como respaldo.

## Validación y evidencia
- Checklist [`audit/checklists/component-observability.md`](../../audit/checklists/component-observability.md).
- Ejemplo [`examples/service-observability`](../../examples/service-observability/README.md).
- Scripts: `make -f operations/Makefile telemetry-smoke` para generar señales mínimas.

## Referencias cruzadas
- Patrones: [métricas y eventos](../patterns/pattern-metrics-and-events.md) y [modos degradados](../patterns/pattern-degraded-mode.md).
- Pilar: [datos y observabilidad](../pillars/data-and-observability.md).
- Contrato: [`docs/specs/component-behavior-contract.schema.md`](./component-behavior-contract.schema.md).
