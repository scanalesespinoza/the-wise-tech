---
title: "Pilar: Datos y Observabilidad"
tags: ["developers", "observability", "data"]
---

# Pilar: Datos y Observabilidad

> La visión de Wise Tech establece que la información debe transformarse en conocimiento y, finalmente, en comportamiento responsable. Este pilar asegura que cada componente conoce su estado de carga, comunica la sobredemanda y deja evidencia reutilizable para aprender.

## Reglas base
Cada componente **MUST** instrumentar señales que permitan distinguir demanda normal vs. sobredemanda, documentar degradaciones y alimentar ciclos de aprendizaje.

### Conocimiento del estado de carga
- **MUST** medirse métricas de uso alineadas a performance (latencia, throughput, clientes conectados) y declararse los valores normales/esperados.
- **MUST** comparar continuamente el estado actual con esos valores para identificar `normal-load` y `overload`.
- **SHOULD** exponer dashboards compartidos donde se vean ambos estados con claridad.
- **MAY** almacenar historiales para correlacionar picos con eventos de negocio.

### Comunicación de sobredemanda y degradación
- **MUST** emitirse señales (logs estructurados, eventos o métricas) cuando una componente detecte sobredemanda o cambie de modo operativo.
- **MUST** incluir en cada señal: estado actual, impacto estimado y acción recomendada (escalar, fallback, degradar).
- **SHOULD** integrar estos eventos en canales visibles para negocio/UX, no solo para SRE.
- **MAY** automatizar la comunicación hacia clientes internos mediante webhooks o colas.

### Datos para aprendizaje y evolución
- **MUST** estandarizar los campos de eventos y métricas (nombres, unidades, niveles) para que el análisis cruzado sea posible.
- **MUST** conservar la data necesaria para reconstruir qué acciones se tomaron durante incidentes y qué resultados tuvieron.
- **SHOULD** usar la data registrada para ajustar límites, redefinir umbrales o priorizar mejoras.
- **MAY** etiquetar los eventos con hipótesis o experimentos activos para acelerar los ciclos de aprendizaje.

### Zero Trust transversal
- **MUST** aplicarse controles de acceso y cifrado sobre pipelines de observabilidad e información de negocio.
- **SHOULD** validarse la procedencia de cada evento antes de aceptarlo (firmas, autenticación mutua) para evitar contaminación de datos.
- **MAY** incorporar verificaciones de postura antes de permitir acceso a paneles sensibles.

## Evidencia mínima
1. Sección `observability` del contrato con métricas, eventos y señales de overload/degradación.
2. Ejemplo funcional (`examples/service-observability`) que documente cómo se emiten y consumen las señales.
3. Checklist `audit/checklists/component-observability.md` completada con enlaces a tableros y catálogos de eventos.

## Referencias
- [Guía del contrato de comportamiento](../guides/component-behavior-contract.md)
- [Patrón: métricas y eventos](../patterns/pattern-metrics-and-events.md)
- [Specs: data-and-observability](../specs/data-and-observability-requirements.md)
