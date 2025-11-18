---
title: "Specs: performance PCC"
tags: ["specs", "performance", "pcc"]
---

# Especificación de performance (PCC-P)

## Propósito
Transformar el pilar de rendimiento en límites verificables y evidencia cuantitativa.

## Alcance
- Aplica a componentes síncronas, batch y de streaming.
- Complementa los SLO/SLA definidos en `experience/scenarios`.

## Requisitos MUST
1. **Presupuestos explícitos.** Completar `performance.max_threads`, `max_requests_per_second`, `max_clients_per_minute` y `resource_budgets.cpu_percent|memory_percent` con números rastreables a pruebas de carga.
2. **Estrategia de contención.** `performance.overflow_strategy` usa únicamente `queue`, `reject` o `throttle` e incluye descripción del algoritmo en la guía del equipo.
3. **Mensajes de negocio.** `performance.overflow_messaging.code` y `business_message` deben explicar la condición para clientes y soporte.
4. **Backpressure documentado.** Cuando se afecten dependencias, describirlo en `resilience.recovery.fallback_paths` y registrar eventos.
5. **Telemetría vinculada.** `observability.metrics_exposed` incluye métricas de capacidad (RPS actual vs. máximo, profundidad de cola, uso de CPU/memoria).

## Requisitos SHOULD
- Asociar cada límite a un objetivo de negocio (ej., tiempo de checkout) dentro de las descripciones del contrato.
- Definir umbrales tempranos (70–80% del límite) y alertas derivadas.
- Publicar dashboards con los límites y enlazarlos desde la checklist de performance.

## Requisitos MAY
- Diferenciar límites por segmento/región cuando exista justificación comercial.
- Automatizar ajustes siempre que se documenten guardrails.

## Validación y evidencia
- Checklist [`audit/checklists/component-performance.md`](../../audit/checklists/component-performance.md).
- Ejemplo [`examples/service-performance-limits`](../../examples/service-performance-limits/README.md).
- `make -f operations/Makefile telemetry-smoke` para validar señales básicas.

## Referencias cruzadas
- Patrones: [backpressure y colas](../patterns/pattern-backpressure-and-queues.md) y [modos degradados](../patterns/pattern-degraded-mode.md).
- Contrato: [`docs/specs/component-behavior-contract.schema.md`](./component-behavior-contract.schema.md).
- Pilar: [performance](../pillars/performance.md).
