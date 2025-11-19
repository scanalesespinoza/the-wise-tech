---
title: "Patrón: modos degradados"
tags: ["patterns", "resilience", "performance", "pcc"]
---

# Patrón: modos degradados

El patrón de modos degradados define cómo una componente mantiene control del impacto cuando pierde funcionalidades. Complementa la [especificación de resiliencia](../specs/resilience-requirements.md) y los límites descritos en [performance](../pillars/performance.md).

## Objetivo
Asegurar que siempre exista un estado conocido (`in-service`, `degraded`, `out-of-service-controlled`) respaldado por criterios explícitos y mensajes para el negocio.

## Pasos clave
1. **Mapa de capacidades.** Documenta qué funciones son esenciales, degradables o prescindibles. Usa este mapa para justificar los `fallback_paths` del contrato.
2. **Criterios de transición.** Define umbrales técnicos (por ejemplo, porcentaje de errores, disponibilidad de dependencias) y asócialos a cada modo operativo.
3. **Playbooks accionables.** Para cada transición, enlaza el runbook más reciente en `resilience.recovery.degraded_mode_playbook` y describe qué equipo lo ejecuta.
4. **Mensajería alineada.** Llena `performance.overflow_messaging` y `observability.degradation_signal` con mensajes que los canales de soporte puedan reutilizar.
5. **Estados auditables.** Emite eventos o métricas etiquetadas con el modo actual para que SRE y negocio vean el cambio en dashboards.

## Herramientas y evidencias
- Contrato PCC actualizado (`resilience.states_implemented`, `resilience.recovery.*`).
- Eventos en `observability.events_emitted` que describen la transición.
- Ejemplo: [`examples/service-resilience-basic`](https://github.com/scanalesespinoza/the-wise-tech/tree/main/examples/service-resilience-basic#readme) y [`examples/service-performance-limits`](https://github.com/scanalesespinoza/the-wise-tech/tree/main/examples/service-performance-limits#readme).

## Checklist rápido
- [ ] Los tres modos obligatorios aparecen en `states_implemented` y están respaldados por métricas.
- [ ] Existe un mensaje aprobado por UX/negocio para cada degradación.
- [ ] Se describen límites máximos antes de pasar a `out-of-service-controlled`.

## Validación automática
Ejecuta `python tools/wise-tech-linter/wise_tech_linter.py <ruta del contrato>` para garantizar que los modos y mensajes estén presentes. Complementa con la checklist [`audit/checklists/component-resilience.md`](https://github.com/scanalesespinoza/the-wise-tech/blob/main/audit/checklists/component-resilience.md) y la de performance.
