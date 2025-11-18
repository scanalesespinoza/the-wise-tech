---
title: "Patrón: backpressure y colas"
tags: ["patterns", "performance", "pcc"]
---

# Patrón: backpressure y colas

Este patrón explica cómo contener la sobredemanda sin perder trazabilidad. Complementa la [especificación de performance](../specs/performance-requirements.md) y los modos degradados.

## Problema
Sin límites explícitos, los componentes consumen recursos hasta saturar dependencias. El patrón introduce mecanismos reproducibles para absorber picos, rechazar con intención o desviar tráfico.

## Implementación paso a paso
1. **Definir presupuestos.** Poblá `performance.max_threads`, `max_requests_per_second`, `max_clients_per_minute` y `resource_budgets.*`.
2. **Seleccionar estrategia.** Documenta en `performance.overflow_strategy` si usarás `queue`, `reject` o `throttle` y describe el algoritmo.
3. **Configurar colas.** Cuando uses `queue`, establece límites de tamaño y tiempos máximos, y publícalos como métricas (`observability.metrics_exposed`).
4. **Aplicar backpressure a dependencias.** Cuando el componente se sature, reduce o pausan llamadas downstream; registra la acción como evento.
5. **Mensajes claros.** Usa `performance.overflow_messaging` para entregar códigos y explicaciones útiles al negocio y soporte.

## Métricas mínimas
- Profundidad de la cola y edad máxima.
- Rechazos por minuto y causa.
- Uso del presupuesto de CPU/memoria mientras la contención está activa.

## Evidencia
- Ejemplo: [`examples/service-performance-limits`](../../examples/service-performance-limits/README.md).
- Checklist [`audit/checklists/component-performance.md`](../../audit/checklists/component-performance.md).
- Señales descritas en `observability.overload_signal`.

## Validación
- `python tools/wise-tech-linter/wise_tech_linter.py <contrato>` asegura que los campos obligatorios existen.
- Simula carga y documenta resultados en `examples/` o `audit/` para soportar las métricas declaradas.
