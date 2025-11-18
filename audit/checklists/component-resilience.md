# Lista de verificación de resiliencia de componentes

Alineada con `specs/component-behavior-contract.schema.md`.

1. **Errores conocidos y detección.**
   - `resilience.error_handling_strategy.expected_errors` y `boundary_cases` están poblados con ejemplos reales.
   - `resilience.error_handling_strategy.detection_channels` incluye al menos un log, métrica o evento por error crítico.
2. **Limpieza y restauración.**
   - Cada elemento en `resilience.cleanup_strategy.steps` describe el objetivo y marca si está automatizado.
   - Los pasos cubren liberación de recursos, reversión de datos y comunicación a dependencias.
3. **Modos operativos.**
   - `resilience.states_implemented` declara `in-service`, `degraded` y `out-of-service-controlled`.
   - `resilience.recovery.degraded_mode_playbook` enlaza un runbook actualizado (< 90 días).
4. **Fallbacks y degradaciones.**
   - Cada `resilience.recovery.fallback_paths` detalla `trigger` e `impact` cuantificado.
   - Los fallbacks explican cómo se evita contagiar la falla al resto del sistema.
5. **Capa Zero Trust.**
   - `zero_trust.input_validation` cubre las interfaces de recuperación.
   - `zero_trust.dependency_assumptions` explica cómo se verifica cada dependencia crítica antes de activarla durante la recuperación.
