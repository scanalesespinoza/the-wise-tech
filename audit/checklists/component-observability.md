# Lista de verificación de datos y observabilidad

1. **Cobertura de métricas.**
   - `observability.metrics_exposed` incluye métricas que cubren carga, estados operativos y límites de recursos.
   - Cada métrica describe unidad y propósito.
2. **Eventos estructurados.**
   - `observability.events_emitted` documenta eventos para sobredemanda (`overload`) y degradación.
   - Los eventos contienen contratos de payload reutilizables por UX/negocio.
3. **Señales obligatorias.**
   - `observability.overload_signal` y `degradation_signal` especifican canales, impacto y acción esperada.
4. **Aprendizaje y revisión.**
   - Se enlazan tableros o reportes que usan estas señales para ajustar límites o priorizar mejoras.
5. **Zero Trust.**
   - `zero_trust.input_validation` cubre la ingesta de telemetría externa.
   - `zero_trust.dependency_assumptions` incluye verificaciones para pipelines compartidos (por ejemplo, data lake, buses de eventos).
