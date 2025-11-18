# Component Behavior Contract Guide

El contrato PCC describe cómo una componente cumple los pilares de Resiliencia, Performance y Datos/Observabilidad con lenguaje tipo RFC (MUST/SHOULD/MAY). Este documento acompaña a `docs/specs/component-behavior-contract.schema.md` y a los ejemplos en `examples/`.

## Cuándo crear o actualizar un contrato
1. Nuevo servicio o cambio mayor de arquitectura.
2. Ajuste de límites (hilos, peticiones, clientes) o estrategias de degradación.
3. Incidentes que revelan brechas en manejo de errores, limpieza o telemetría.

## Estructura del contrato
```
version: 1.1.0
component:            # Identidad básica
  name:
  domain:
  description:
ownership:
  team:
  service_slack:
  escalation:
runtime:
  tier:
  language:
  deployment:
resilience:
  error_handling_strategy:
    expected_errors:
    boundary_cases:
    detection_channels:
  cleanup_strategy:
    steps:
      - description:
        automation:
  states_implemented:
    - in-service
    - degraded
    - out-of-service-controlled
  recovery:
    fallback_paths:
      - name:
        trigger:
        impact:
    degraded_mode_playbook:
performance:
  max_threads:
  max_requests_per_second:
  max_clients_per_minute:
  resource_budgets:
    cpu_percent:
    memory_percent:
  overflow_strategy: queue|reject|throttle
  overflow_messaging:
    code:
    business_message:
observability:
  metrics_exposed:
    - name:
      type:
      description:
  events_emitted:
    - name:
      when:
      payload_contract:
  overload_signal:
    channel:
    description:
  degradation_signal:
    channel:
    description:
zero_trust:
  input_validation:
    - interface:
      rules:
  dependency_assumptions:
    - dependency:
      verification:
audit:
  last_review:
  reviewers:
    - name:
```

### Cómo rellenar cada sección
- **component / ownership / runtime.** Identidad, dominio, tier y dónde contactar al equipo. Se usa para enrutar auditorías y escalamientos.
- **resilience.** Detalla qué errores se esperan, cómo se detectan y qué pasos de limpieza se ejecutan antes de volver al modo seguro. `states_implemented` **MUST** enumerar al menos los tres modos obligatorios.
- **performance.** Define los límites máximos y la estrategia `overflow_strategy` (cola, rechazo o throttling). `overflow_messaging` describe el código y el mensaje visible para negocio.
- **observability.** Lista métricas y eventos disponibles, especificando cómo se señalan la sobredemanda y la degradación.
- **zero_trust.** Documenta validaciones de entrada y suposiciones sobre dependencias; sirve para revisar que los modos degradados no omiten controles.
- **audit.** Fecha y responsables de la última revisión para cruzar con `audit/checklists/`.

## Buenas prácticas
- Versionar el contrato junto al código. Los linters comparan los campos con las listas de verificación.
- Enlazar evidencia (dashboards, runbooks, scripts) desde cada arreglo (`steps`, `fallback_paths`, `events`).
- Reutilizar el template de `audit/component-contract.yaml` para mantener consistencia.

## Ejemplos
Cada carpeta en `examples/` incluye un `behavior-contract.yaml` ya validado:
- `service-resilience-basic`: estados operativos y limpieza.
- `service-performance-limits`: límites explícitos y mensajes de rechazo.
- `service-observability`: métricas/eventos que señalan sobredemanda.

Úsalo como punto de partida y adapta los valores a tu contexto.
