# ADR-0002: Estrategias de Réplica Ejecutables

- Fecha: 2024-06-14
- Estado: Propuesto

## Contexto

Los servicios distribuídos han adoptado diferentes patrones de réplica sin un catálogo unificado. Esto provoca incompatibilidades (p.ej., servicios no idempotentes intentando réplica activa) y dificulta pruebas de fallos parciales. Necesitamos políticas ejecutables que hagan explícitos los supuestos de estado e idempotencia.

## Decisión

1. El catálogo soportado incluye **Primary-Backup**, **Active Replication** (state-machine) y **Quórums** (lectura/escritura).
2. Cada servicio declara su estrategia en `systems/platform/policies/consistency.yml` y los parámetros específicos (timeouts, reintentos, quórums) en `experience/scenarios/<servicio>/policies/resilience.yml` (p.ej. `experience/scenarios/payments/policies/resilience.yml`).
3. La plataforma valida que los servicios que eligen réplica activa declaren handlers idempotentes y orden determinista; los que usan quórums especifican tamaños de lectura/escritura consistentes.
4. Se documentan guías de degradación aceptable (p.ej., primary-backup degrada a lectura, quórums ajustan tamaños dinámicamente).
5. El pipeline de CI ejecuta escenarios de fallos parciales para cada estrategia.

## Consecuencias

- **Positivas**: evita combinaciones incompatibles, habilita simulaciones repetibles de fallos y facilita la comunicación entre desarrollo y operaciones.
- **Negativas**: requiere invertir en tooling y en observabilidad (p.ej., relojes vectoriales) para soportar estrategias avanzadas.

## Migración

1. Inventariar la estrategia actual de cada servicio.
2. Definir plantillas de despliegue por estrategia con checks automáticos.
3. Migrar servicios con baja criticidad primero para validar tooling.
4. Documentar lecciones aprendidas en los playbooks y plantillas de PR.
