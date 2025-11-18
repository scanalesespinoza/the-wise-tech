---
title: "Patrón: manejo de errores y cleanup"
tags: ["patterns", "resilience", "pcc"]
---

# Patrón: manejo de errores y cleanup

Este patrón aterriza el pilar de Resiliencia en actividades concretas para capturar fallas, limpiar recursos y comunicar el estado de la componente. Sirve como puente entre [las reglas del pilar](../pillars/resilience.md) y la [especificación formal](../specs/resilience-requirements.md).

## ¿Cuándo aplicarlo?
- Lanzamiento de una componente nueva o refactor crítico.
- Después de un incidente que mostró fugas de recursos o estados corruptos.
- Cuando el contrato PCC revela campos vacíos en `resilience.*` o `zero_trust.*`.

## Flujo recomendado
1. **Inventariar fallas conocidas.** Clasifica los errores en `expected_errors` y `boundary_cases` con lenguaje de negocio. Captura el canal de detección (log, métrica, evento) para cada entrada.
2. **Encapsular cleanup como pasos idempotentes.** Modela cada acción en `resilience.cleanup_strategy.steps` indicando si está automatizada. Incluye reversión de datos, cierre de conexiones y avisos a dependencias.
3. **Definir criterios de cambio de modo.** Documenta qué condición envía a la componente a `degraded` u `out-of-service-controlled`. Relaciona cada criterio con un fallback documentado y su impacto.
4. **Alinear Zero Trust.** Para cada recuperación, especifica en `zero_trust.input_validation` cómo se evita ejecutar datos maliciosos, y en `zero_trust.dependency_assumptions` cómo verificas a terceros antes de reconectarlos.
5. **Conectar telemetría.** Registra en `observability.events_emitted` los eventos que confirman que el cleanup terminó, e incluye `overload_signal`/`degradation_signal` si la falla degrada al sistema.

## Señales esperadas
- Logs o eventos con `correlation_id` que narran error → cleanup → resultado.
- Métricas de intentos de recuperación y duración promedio.
- Referencia al runbook (`resilience.recovery.degraded_mode_playbook`).

## Evidencia en el repositorio
- `behavior-contract.yaml` actualizado (usa `tools/wise-tech-linter`).
- Ejemplo práctico: [`examples/service-resilience-basic`](../../examples/service-resilience-basic/README.md).
- Checklist [`audit/checklists/component-resilience.md`](../../audit/checklists/component-resilience.md) firmada.

## Cómo validar
1. Ejecuta `python tools/wise-tech-linter/wise_tech_linter.py examples/service-resilience-basic/behavior-contract.yaml`.
2. Corre `make -f operations/Makefile audit` si quieres validar múltiples contratos.
3. Documenta las brechas detectadas en `audit/component-contract.yaml` para dar seguimiento.
