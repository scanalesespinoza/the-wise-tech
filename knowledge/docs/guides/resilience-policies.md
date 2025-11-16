---
title: "Resilience Policies — Cómo usarlas"
tags: ["developers", "resilience", "playbooks"]
---
## Propósito
Enmarca cómo Resilience Policies — Cómo usarlas ayuda a mantener decisiones alineadas con The Wise Tech.

## Audiencia
Personas y equipos que necesitan una guía rápida sobre Resilience Policies — Cómo usarlas.

## Cuándo usarlo
Consúltalo cuando requieras referencias inmediatas para Resilience Policies — Cómo usarlas o debas compartir el enfoque con otros equipos.

> **Propósito:** Dar contexto accionable sobre Resilience Policies — Cómo usarlas dentro de The Wise Tech.
> **Audiencia:** Equipos y perfiles interesados en las bases de conocimiento y lineamientos del programa.
> **Uso recomendado:** Consulta este documento cuando necesites aplicar o compartir detalles de Resilience Policies — Cómo usarlas.
> **Estado:** Activo.


## Tabla de navegación

- [Flujo recomendado](#flujo-recomendado)
- [Ejemplo](#ejemplo)
- [Próximos pasos](#prximos-pasos)
- [See also](#see-also)

# Resilience Policies — Cómo usarlas
Las políticas definen **contratos operativos** por servicio/escenario:
- **timeouts_ms**: límites por cliente/infra (1–120000 ms)
- **retries**: on/off, intentos (1–10), backoff (fixed|linear|exponential), base_ms (10–60000)
- **circuit_breaker**: on/off, failure_threshold (0–1), min_samples, reset_timeout_ms
- **bulkhead**: on/off, max_concurrent
- **cache**: on/off, ttl_s
## Flujo recomendado
1) Edita `experience/scenarios/payments/policies/resilience.yml` con valores iniciales realistas.
2) Ejecuta `make resilience-check` en local.
3) Sube PR; CI validará automáticamente la política.
4) Documenta cualquier ajuste y su “por qué” en el PR.
## Ejemplo
Ver `experience/scenarios/payments/policies/resilience.yml` (payments).
## Próximos pasos
- Integrar SLOs y presupuestos de error (Iteración 6).
- Añadir snippets de instrumentación (telemetría) y runbooks.

## See also
- [SLOs & Error Budget](slo-how-to.md)
- [Telemetry (Minimum)](telemetry-minima.md)
- [Platform playbook](../playbooks/platform-playbook.md)
- [Platform Engineers — 30/60/90](../paths/platform-engineers-30-60-90.md)
---
Última modificación: 2025-11-16

🗳️ **¿Te fue útil este documento?**
- [ ] Sí, resolvió mi duda
- [ ] Más o menos
- [ ] No me ayudó

💬 [Deja tu feedback](https://github.com/scanalesespinoza/the-wise-tech/issues/new?template=feedback.yml)

---

