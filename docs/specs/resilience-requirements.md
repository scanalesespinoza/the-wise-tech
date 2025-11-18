---
title: "Specs: resiliencia PCC"
tags: ["specs", "resilience", "pcc"]
---

# Especificación de resiliencia (PCC-R)

## Propósito
Garantizar que toda componente documente cómo previene, detecta y se recupera de fallas siguiendo el contrato PCC. Estas reglas se derivan del [pilar de resiliencia](../pillars/resilience.md) y se verifican con `tools/wise-tech-linter`.

## Alcance
- Se aplica a cualquier servicio o componente que procese eventos, solicitudes síncronas o trabajos batch.
- Extiende la cobertura a runbooks, telemetría y checklists de auditoría.

## Requisitos MUST
1. **Clasificación de errores.** `resilience.error_handling_strategy.expected_errors`, `boundary_cases` y `detection_channels` deben enumerar los fallos conocidos y cómo se detectan.
2. **Cleanup idempotente.** `resilience.cleanup_strategy.steps` define pasos numerados, con `automation` indicando si existe tooling.
3. **Modos operativos completos.** `resilience.states_implemented` incluye obligatoriamente `in-service`, `degraded` y `out-of-service-controlled`.
4. **Fallback documentado.** `resilience.recovery.fallback_paths` describe `name`, `trigger` e `impact`, y `degraded_mode_playbook` enlaza el runbook vigente.
5. **Zero Trust en recuperación.** `zero_trust.input_validation` y `zero_trust.dependency_assumptions` cubren los flujos de error (no solo la operación nominal).
6. **Mensajería a negocio.** Cada transición debe generar eventos o logs registrados en `observability.events_emitted`.

## Requisitos SHOULD
- Documentar límites de reintentos y temporizadores en las descripciones de pasos.
- Incluir referencias a tableros o paneles de control junto a los eventos de degradación.
- Coordinar con UX/soporte para aprobar los mensajes citados en el contrato.

## Requisitos MAY
- Añadir modos adicionales (por ejemplo, `manual-assist`).
- Definir automatismos de clasificación de errores mientras exista supervisión humana.

## Validación y evidencia
- `tools/wise-tech-linter` verifica campos y valores esperados.
- Checklist [`audit/checklists/component-resilience.md`](https://github.com/scanalesespinoza/the-wise-tech/blob/main/audit/checklists/component-resilience.md).
- Ejemplos vivos en [`examples/service-resilience-basic`](https://github.com/scanalesespinoza/the-wise-tech/tree/main/examples/service-resilience-basic#readme).

## Relación con otros artefactos
- Patrones: [error handling & cleanup](../patterns/pattern-error-handling-and-cleanup.md) y [modos degradados](../patterns/pattern-degraded-mode.md).
- Contrato: [`docs/specs/component-behavior-contract.schema.md`](./component-behavior-contract.schema.md).
