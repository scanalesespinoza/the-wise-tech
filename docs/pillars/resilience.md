# Pilar: Resiliencia

> Conecta la visión de resultados confiables descrita en [Vision and purpose](../../README.md#vision-and-purpose) con los [Wise Tech Principles](../../knowledge/docs/principles/wise-tech-principles.md#resiliencia) para asegurar que cada sistema se degrade de forma controlada.

## Contexto estratégico
La resiliencia articula la capacidad de cumplir promesas de negocio incluso en presencia de fallas. Sustenta el principio de Resiliencia del marco Wise Tech y sirve como mecanismo de ejecución para Simplicity y Mejora continua: se diseña para fallar con gracia y se mejora observando señales reales.

## Requisitos esenciales
### Manejo de errores
- **MUST** capturar errores técnicos y de negocio con mensajes accionables y trazabilidad (ID de correlación, usuario afectado, carga enviada) sin exponer datos sensibles.
- **SHOULD** diferenciar errores transitorios y permanentes para activar el runbook correcto (reintentos versus revisión manual).
- **MAY** automatizar la clasificación con IA siempre que exista supervisión humana y registro auditable.

### Modos degradados
- **MUST** definir modos degradados explícitos (por ejemplo, cola manual, capacidad reducida, *read-only*) antes de desplegar cambios que toquen la lógica crítica.
- **SHOULD** incluir indicadores de entrada y salida de cada modo en los tableros operativos para validar que el comportamiento reduce daño.
- **MAY** permitir saltos controlados a un modo "manual assist" cuando los equipos de experiencia necesiten preservar la conexión humana descrita en los principios.

### Límites y contención
- **MUST** implementar *circuit breakers* o colas de aislamiento cuando una dependencia exceda el presupuesto de error definido en los SLOs.
- **SHOULD** documentar límites de throughput y almacenamiento junto con las decisiones en ADR visibles desde Knowledge Capitalization.
- **MAY** usar políticas basadas en riesgo para ajustar límites dinámicamente cuando la visión exija proteger una métrica prioritaria (por ejemplo, ingresos de pagos).

### Señales de observabilidad
- **MUST** exponer métricas de éxito funcional (transacciones comprometidas, órdenes compensadas) además de CPU o memoria.
- **SHOULD** mapear alertas directamente a runbooks del escenario correspondiente (p. ej., `experience/scenarios/payments/docs`).
- **MAY** registrar *feature flags* activos para facilitar auditorías de resiliencia retroactivas.

### Operaciones y revisión
- **MUST** ensayar los runbooks críticos con la cadencia propuesta en los laboratorios de resiliencia.
- **SHOULD** usar retrospectivas post-incidente para reforzar la captura de conocimiento (ver [Knowledge Capitalization](../../knowledge/docs/principles/wise-tech-principles.md#capitalizacin-del-conocimiento)).
- **MAY** compartir hallazgos como cápsulas reutilizables en la base de conocimiento para que otros equipos aceleren su alineación con la visión.

## Transversal — Zero Trust
- **MUST** validar identidades y permisos antes de ejecutar cualquier flujo de recuperación o bypass, evitando que el modo degradado se convierta en un vector de escalamiento.
- **SHOULD** registrar en telemetría quién habilita o deshabilita protecciones para facilitar trazabilidad y auditoría.
- **MAY** integrar señales de postura (por ejemplo, nivel de riesgo del dispositivo) como entrada para activar contención automática.
