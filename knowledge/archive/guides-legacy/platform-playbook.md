## Propósito
Enmarca cómo Platform Playbook: Membresía, Quórums y Degradación Controlada ayuda a mantener decisiones alineadas con The Wise Tech.

## Audiencia
Personas y equipos que necesitan una guía rápida sobre Platform Playbook: Membresía, Quórums y Degradación Controlada.

## Cuándo usarlo
Consúltalo cuando requieras referencias inmediatas para Platform Playbook: Membresía, Quórums y Degradación Controlada o debas compartir el enfoque con otros equipos.

> **Propósito:** Dar contexto accionable sobre Platform Playbook: Membresía, Quórums y Degradación Controlada dentro de The Wise Tech.
> **Audiencia:** Equipos y perfiles interesados en las bases de conocimiento y lineamientos del programa.
> **Uso recomendado:** Consulta este documento cuando necesites aplicar o compartir detalles de Platform Playbook: Membresía, Quórums y Degradación Controlada.
> **Estado:** Activo.


## Tabla de navegación

- [Operar la gestión de membresía](#operar-la-gestin-de-membresa)
- [Estrategias de réplica](#estrategias-de-rplica)
- [Procedimientos ante fallos parciales](#procedimientos-ante-fallos-parciales)
- [Quality Gates en la plataforma](#quality-gates-en-la-plataforma)
- [Trazabilidad y feedback humano](#trazabilidad-y-feedback-humano)

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
2. **Pérdida de miembro**: ejecuta `systems/ci/resilience-lint` para validar que los parámetros permitirán degradación aceptable antes del despliegue. Durante la incidencia, comunica el cambio de topología a los servicios consumidores.
3. **Cortes intermitentes**: usa circuit breakers para aislar la réplica afectada; aplica reintentos con claves de idempotencia.

## Quality Gates en la plataforma

- Asegura que `systems/ci/consistency-check`, `systems/ci/resilience-lint` y `systems/ci/causality-test` se ejecuten en cada PR.
- Mantén actualizadas las plantillas de Issues/PR con secciones de "decisión de consistencia", "estrategia de réplica" y "lecciones del usuario".

## Trazabilidad y feedback humano

- Propaga el vector de sesión al equipo de soporte para reproducir estados.
- Documenta degradaciones planificadas o incidentes en una bitácora centralizada, enlazando las ADRs relevantes.
---
Última modificación: 2025-11-16

🗳️ **¿Te fue útil este documento?**
- [ ] Sí, resolvió mi duda
- [ ] Más o menos
- [ ] No me ayudó

💬 [Deja tu feedback](https://github.com/scanalesespinoza/the-wise-tech/issues/new?template=feedback.yml)

---

