# Wise Tech: Enfoque Incremental para Consistencia y Resiliencia

La plataforma de Wise Tech evoluciona en iteraciones cortas que priorizan el aprendizaje sistemático. Este anexo resume cómo institucionalizamos perfiles de consistencia, estrategias de réplica y controles de resiliencia inspirados en prácticas de sistemas distribuidos sin perder los principios de progreso incremental, anticipación de pitfalls, capitalización de conocimiento y resiliencia operativa.

## Perfiles de Consistencia & Estrategias de Réplica

| Perfil / Estrategia | Garantías Principales | Estrategias de Réplica Compatibles | Cuándo Usarlo | Riesgos a Vigilar |
| --- | --- | --- | --- | --- |
| **Strict** | Aislamiento cercano a serializable, lecturas linealizables, escritura determinista | Primary-Backup, Quórums | Flujos financieros, pedidos, cambios de inventario global | Contención de latencia, riesgo de split-brain si la membresía falla |
| **Causal** | Respeta dependencias causales, lecturas monotónicas, read-your-writes mediante vector de sesión | Active Replication, Quórums | Experiencias colaborativas, seguimiento de actividad del usuario | Complejidad en clocks y reconciliación si se pierden metadatos de sesión |
| **Eventual** | Convergencia con reconciliación basada en políticas, latencia mínima | Active Replication, Fan-out con cachés TTL | Catálogos, contenidos, métricas agregadas | Divergencias visibles, requiere idempotencia y reconciliación explícita |

### Guías clave

1. **Consistencia declarativa**: Cada servicio declara su perfil en `platform/policies/consistency.yml` y la plataforma valida compatibilidad con su patrón de acceso y estrategia de réplica durante CI.
2. **Garantías client-centric**: Middleware de sesión incluye cabeceras con vector lógico para read-your-writes y lecturas monotónicas en clientes móviles/web.
3. **Coherence vs. Consistency**: Definir políticas por ítem (coherence) y por dataset (consistency). Las cachés deben respetar TTL alineadas al perfil seleccionado.
4. **Migraciones controladas**: Las ADRs documentan trade-offs para migrar de eventual a causal o strict sin interrupciones, usando despliegues blue/green por partición.

## Estrategias de Resiliencia Operacional

- **Catálogo de réplicas**: Primary-backup, active replication y quórums disponibles como políticas ejecutables con validaciones de idempotencia y estado compartido.
- **Fallos parciales en CI**: Los escenarios definidos en `ci/causality-test` y `ci/resilience-lint` simulan nodos lentos, pérdida de miembros y reintentos para prevenir sorpresas en producción.
- **Gestión de membresía**: El `platform-playbook` explica protocolos de heartbeats, timeouts y ordenación de eventos de grupo para minimizar ventanas de inconsistencia.

## Instrumentación de Orden y Tiempo

- **Vector clocks en eventos**: Cada mensaje lleva un encabezado con reloj vectorial para trazabilidad y reconciliación eventual/causal.
- **Orden total selectivo**: Solo se fuerza en servicios con réplica activa tipo máquina de estado; el costo y límites quedan descritos en la ADR correspondiente.

## Quality Gates en CI/CD

- **Checks automáticos**: `ci/consistency-check` asegura compatibilidad de perfiles y estrategias. `ci/resilience-lint` verifica configuraciones de timeouts, quórums y circuit breakers. `ci/causality-test` ejecuta simulaciones de ordenamiento e idempotencia.
- **Idempotencia por contrato**: Los handlers que usan réplica activa deben declarar claves de idempotencia verificables.

## Plataforma con Feedback Humano

- **Session vectors en soporte y UX**: Antes de responder al usuario tras moverse de réplica, el backend sincroniza el timestamp de sesión para mantener continuidad.
- **Plantillas enriquecidas**: Issues y PRs incluyen secciones para decisiones de consistencia, estrategia de réplica y lecciones aprendidas del usuario para reforzar memoria organizacional.

## Roadmap Incremental

1. **Semanas 1–2**: Publicar perfiles de consistencia, ADRs y linters mínimos.
2. **Semanas 3–4**: Añadir políticas de réplica y pruebas de fallos parciales.
3. **Semanas 5–6**: Instrumentar clocks lógicos/vectoriales y trazas.
4. **Semanas 7–8**: Pilotear réplica activa en un microservicio idempotente y medir orden total vs. causal.

Este anexo sirve como punto de referencia para que Wise Tech tome decisiones informadas y trazables en su evolución de plataforma.
