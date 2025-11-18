---
title: "Patrón: métricas y eventos"
tags: ["patterns", "observability", "data", "pcc"]
---

# Patrón: métricas y eventos

Este patrón operacionaliza el pilar de Datos y Observabilidad. Describe cómo instrumentar señales que soportan decisiones de negocio y validan las [especificaciones de datos/observabilidad](../specs/data-and-observability-requirements.md).

## Objetivos
- Saber en qué estado de carga opera la componente.
- Comunicar sobredemanda y degradaciones con contexto de negocio.
- Capturar evidencia reutilizable para aprendizaje y tuning.

## Pasos
1. **Inventariar decisiones.** Lista qué preguntas de negocio debes responder (p. ej., ¿estamos en overload?). Cada pregunta necesita al menos una métrica y/o evento.
2. **Diseñar contratos de telemetría.** Normaliza nombres, unidades y etiquetas. Documenta cada elemento en `observability.metrics_exposed` y `observability.events_emitted`.
3. **Definir señales principales.** Completa `observability.overload_signal` y `degradation_signal` con canal, frecuencia y responsables.
4. **Acoplar Zero Trust.** Protege pipelines de datos describiendo validaciones y autenticación en `zero_trust.*`.
5. **Cerrar el loop.** Guarda los tableros o consultas en el contrato (links en descripciones) y agrégales contexto en la checklist de observabilidad.

## Buenas prácticas
- Etiqueta cada métrica con `mode=in-service|degraded`.
- Incluye identificadores de cliente o segmento cuando la privacidad lo permita.
- Registra acciones correctivas como eventos separados (`action_taken`).

## Evidencia
- Ejemplo: [`examples/service-observability`](../../examples/service-observability/README.md).
- Contrato PCC y checklist [`audit/checklists/component-observability.md`](../../audit/checklists/component-observability.md).
- Scripts de validación: `make -f operations/Makefile telemetry-smoke`.

## Validación
1. Ejecuta el linter para verificar campos obligatorios.
2. Corre `operations/scripts/check-links.py` cuando documentes dashboards para evitar referencias rotas.
3. Adjunta capturas o métricas exportadas en `audit/` si el análisis alimenta decisiones de tuning.
