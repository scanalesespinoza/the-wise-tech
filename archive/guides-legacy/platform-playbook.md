# Platform Playbook: Membresía, Quórums y Degradación Controlada

## Operar la gestión de membresía

1. **Heartbeats**: cada nodo emite heartbeats cada `timeouts.heartbeat_interval_ms` definido en `resilience.yml`.
2. **Detección de fallos**: marca un nodo como sospechoso tras `failure_detection_ms`. Propaga el evento con orden consistente (usa secuencias monotonically increasing).
3. **Join/Leave**: al ingresar un nodo, aplica warmup controlado replicando el estado desde la réplica primaria/quórum antes de aceptar tráfico. Para salidas planificadas, drena solicitudes y publica un evento `leave` con el último vector conocido.

## Estrategias de réplica

- **Primary-Backup**: garantizar que solo el primario procese escrituras. En degradación, enruta lecturas al backup y habilita failover manual/automático según SLAs.
- **Active Replication**: requiere orden determinista (state-machine). Documenta handlers idempotentes y utiliza relojes vectoriales para confirmar convergencia después de replays.
- **Quórums**: asegura que `read + write > total_nodes`. Ajusta dinámicamente quórums durante fallos parciales, priorizando disponibilidad sin violar consistencia.

## Procedimientos ante fallos parciales

1. **Nodo lento**: detecta latencia anómala, replica backlog en paralelo y considera disminuir el quórum de lectura temporalmente.
2. **Pérdida de miembro**: ejecuta `ci/resilience-lint` para validar que los parámetros permitirán degradación aceptable antes del despliegue. Durante la incidencia, comunica el cambio de topología a los servicios consumidores.
3. **Cortes intermitentes**: usa circuit breakers para aislar la réplica afectada; aplica reintentos con claves de idempotencia.

## Quality Gates en la plataforma

- Asegura que `ci/consistency-check`, `ci/resilience-lint` y `ci/causality-test` se ejecuten en cada PR.
- Mantén actualizadas las plantillas de Issues/PR con secciones de "decisión de consistencia", "estrategia de réplica" y "lecciones del usuario".

## Trazabilidad y feedback humano

- Propaga el vector de sesión al equipo de soporte para reproducir estados.
- Documenta degradaciones planificadas o incidentes en una bitácora centralizada, enlazando las ADRs relevantes.
