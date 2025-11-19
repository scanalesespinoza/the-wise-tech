---
title: "Pilar: Performance"
tags: ["developers", "performance", "principles"]
---

# Pilar: Performance

> Mantener el rendimiento significa garantizar que las promesas de negocio se cumplen dentro de límites conocidos y auditablemente justificados. Este pilar traduce la visión de Wise Tech (responsabilidad + calidad) en presupuestos explícitos y respuestas claras cuando se exceden.

## Expectativas clave
Cada componente **MUST** declarar qué recursos usa, cuáles son sus límites y cómo se comporta cuando la demanda excede esos límites.

### Límites predefinidos
- **MUST** definirse máximos de hilos o *workers*, consumo de CPU/memoria y conexiones activas.
- **MUST** declararse máximos de peticiones entrantes por unidad de tiempo y máximos de clientes conectados.
- **SHOULD** relacionar cada límite con el objetivo de negocio (por ejemplo, "checkout completo en < 2 s").
- **MAY** publicarse límites diferenciados por región o tipo de cliente cuando existan acuerdos específicos.

### Mecanismos de contención
- **MUST** existir estrategias documentadas de cola, rechazo controlado o *throttling* para cada punto de entrada.
- **MUST** emitir códigos de error claros y mensajes de negocio cuando se rechace una petición por sobredemanda.
- **SHOULD** incluir backpressure hacia dependencias para no propagar la saturación.
- **MAY** activar rutas alternativas más simples (por ejemplo, modo *read-only*) cuando el negocio prefiera degradarse antes que fallar.

### Señales de capacidad
- **MUST** monitorearse los límites declarados (hilos, peticiones, clientes, recursos) y exponerlos como métricas.
- **MUST** etiquetar las métricas con el modo operativo (`in-service`, `degraded`, etc.) para correlacionar saturación con experiencia.
- **SHOULD** definir umbrales de alerta que anticipen la sobredemanda (por ejemplo, 80% del límite) y publiquen recomendaciones de acción.
- **MAY** alimentar experimentos de *auto-tuning* siempre que existan guardrails documentados.

### Zero Trust transversal
- **MUST** garantizar que la contención no deshabilita controles de autenticación/autorización ni mezcla sesiones de clientes.
- **SHOULD** validar entradas aún cuando provengan de servicios "internos" para evitar abuso en escenarios de sobredemanda.
- **MAY** usar señales de riesgo para adaptar límites dinámicamente (cliente confiable vs. desconocido) sin sacrificar trazabilidad.

## Evidencia mínima
1. Sección `performance` del contrato con límites máximos, estrategia de overflow y mensajes para negocio.
2. Ejemplo funcional como [`service-performance-limits`](https://github.com/scanalesespinoza/the-wise-tech/tree/main/examples/service-performance-limits#readme) que muestre el rechazo controlado.
3. Checklist [`audit/checklists/component-performance.md`](https://github.com/scanalesespinoza/the-wise-tech/blob/main/audit/checklists/component-performance.md) completado con vínculos a paneles o scripts de carga.

## Referencias
- [Guía del contrato de comportamiento](../guides/component-behavior-contract.md)
- [Patrón: backpressure y colas](../patterns/pattern-backpressure-and-queues.md)
- [Patrón: modos degradados](../patterns/pattern-degraded-mode.md)
