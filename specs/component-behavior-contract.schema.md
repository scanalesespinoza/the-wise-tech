# Component Behavior Contract Schema

La especificación define el formato obligatorio para `behavior-contract.yaml`. El objetivo es que herramientas como `wise-tech-linter` puedan validar que cada componente documenta cómo cumple los pilares PCC.

## Resumen
- Formato: YAML.
- Versión actual: `1.1.0` (campo `version`).
- Palabras clave: usar `MUST`, `SHOULD`, `MAY` según RFC 2119.

## Campos obligatorios
| Ruta | Tipo | Descripción |
| --- | --- | --- |
| `version` | string | Versión del esquema adoptado (`1.1.0`). |
| `component.name` | string | Nombre único del servicio o componente. |
| `component.domain` | string | Dominio o capability que cubre. |
| `component.description` | string | Resumen de 1–2 líneas. |
| `ownership.team` | string | Equipo responsable. |
| `ownership.service_slack` | string | Canal de contacto operativo. |
| `ownership.escalation` | string | Ruta de escalamiento (PagerDuty, teléfono, etc.). |
| `runtime.tier` | string | Criticidad (`tier-1`, `tier-2`, etc.). |
| `runtime.language` | string | Lenguaje/runtime dominante. |
| `runtime.deployment` | string | Forma de despliegue (Kubernetes, serverless, batch). |
| `resilience.error_handling_strategy.expected_errors` | list(string) | Errores esperados por tipo. |
| `resilience.error_handling_strategy.boundary_cases` | list(string) | Casos de borde documentados. |
| `resilience.error_handling_strategy.detection_channels` | list(string) | Cómo se detectan (logs, métricas, eventos). |
| `resilience.cleanup_strategy.steps[].description` | string | Paso de limpieza. |
| `resilience.cleanup_strategy.steps[].automation` | bool | Indica si el paso está automatizado. |
| `resilience.states_implemented` | list(string) | Debe incluir `in-service`, `degraded`, `out-of-service-controlled`. |
| `resilience.recovery.fallback_paths[].name` | string | Nombre del fallback. |
| `resilience.recovery.fallback_paths[].trigger` | string | Evento que activa el fallback. |
| `resilience.recovery.fallback_paths[].impact` | string | Impacto en negocio/UX. |
| `resilience.recovery.degraded_mode_playbook` | string | URL o referencia del runbook. |
| `performance.max_threads` | integer | Máximo de hilos/threads o workers. |
| `performance.max_requests_per_second` | integer | Máximo de RPS aceptado. |
| `performance.max_clients_per_minute` | integer | Máximo de clientes concurrentes. |
| `performance.resource_budgets.cpu_percent` | number | Presupuesto de CPU (%). |
| `performance.resource_budgets.memory_percent` | number | Presupuesto de memoria (%). |
| `performance.overflow_strategy` | string | Estrategia (`queue`, `reject`, `throttle`). |
| `performance.overflow_messaging.code` | string | Código de error expuesto al consumidor. |
| `performance.overflow_messaging.business_message` | string | Mensaje explicando la contención. |
| `observability.metrics_exposed[].name` | string | Nombre de la métrica. |
| `observability.metrics_exposed[].type` | string | Tipo (counter, gauge, histogram). |
| `observability.metrics_exposed[].description` | string | Propósito de la métrica. |
| `observability.events_emitted[].name` | string | Nombre del evento. |
| `observability.events_emitted[].when` | string | Cuándo se emite. |
| `observability.events_emitted[].payload_contract` | string | Campos clave del evento. |
| `observability.overload_signal.channel` | string | Dónde se publica la señal de sobredemanda. |
| `observability.overload_signal.description` | string | Qué significa para el negocio. |
| `observability.degradation_signal.channel` | string | Dónde se publica el estado degradado. |
| `observability.degradation_signal.description` | string | Impacto y acción esperada. |
| `zero_trust.input_validation[].interface` | string | Interfaz protegida. |
| `zero_trust.input_validation[].rules` | string | Reglas o filtros aplicados. |
| `zero_trust.dependency_assumptions[].dependency` | string | Dependencia crítica. |
| `zero_trust.dependency_assumptions[].verification` | string | Cómo se valida la confianza. |
| `audit.last_review` | string | Fecha ISO de última revisión. |
| `audit.reviewers[].name` | string | Personas que firmaron la revisión. |

## Campos opcionales
Los equipos **MAY** añadir campos adicionales siempre que no eliminen los obligatorios. Ejemplos útiles:
- `component.links`: enlaces a ADRs o diagramas.
- `performance.resource_budgets.additional`: GPU, ancho de banda, etc.
- `observability.metrics_exposed[].dashboard`: URL al tablero principal.

## Plantilla YAML
```yaml
version: 1.1.0
component:
  name: <service name>
  domain: <capability>
  description: <summary>
ownership:
  team: <team>
  service_slack: <#channel>
  escalation: <pager/escalation>
runtime:
  tier: <tier-1|tier-2|tier-3>
  language: <language/runtime>
  deployment: <kubernetes|batch|lambda>
resilience:
  error_handling_strategy:
    expected_errors:
      - <error>
    boundary_cases:
      - <edge case>
    detection_channels:
      - <log|metric|event>
  cleanup_strategy:
    steps:
      - description: <step>
        automation: <true|false>
  states_implemented:
    - in-service
    - degraded
    - out-of-service-controlled
  recovery:
    fallback_paths:
      - name: <fallback>
        trigger: <condition>
        impact: <business impact>
    degraded_mode_playbook: <link>
performance:
  max_threads: <int>
  max_requests_per_second: <int>
  max_clients_per_minute: <int>
  resource_budgets:
    cpu_percent: <float>
    memory_percent: <float>
  overflow_strategy: <queue|reject|throttle>
  overflow_messaging:
    code: <error code>
    business_message: <explanation>
observability:
  metrics_exposed:
    - name: <metric>
      type: <counter|gauge|histogram>
      description: <what it tracks>
  events_emitted:
    - name: <event>
      when: <trigger>
      payload_contract: <fields>
  overload_signal:
    channel: <metrics|event|log>
    description: <meaning>
  degradation_signal:
    channel: <metrics|event|log>
    description: <impact>
zero_trust:
  input_validation:
    - interface: <api>
      rules: <validation summary>
  dependency_assumptions:
    - dependency: <service>
      verification: <timeout|schema|token>
audit:
  last_review: <YYYY-MM-DD>
  reviewers:
    - name: <person>
```

Respete esta estructura para habilitar validaciones automáticas y checklists consistentes.
