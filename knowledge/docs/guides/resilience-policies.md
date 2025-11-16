---
title: "Resilience Policies — Cómo usarlas"
tags: ["developers", "resilience", "playbooks"]
---
<!-- metadata
para_quien: Equipos y contribuidores que consultan "Resilience Policies — Cómo usarlas" en The Wise Tech.
objetivo: Proporcionar un contexto accionable sobre resilience policies — cómo usarlas.
cuando_usar: Recurre a este documento cuando necesites aplicar o compartir detalles de resilience policies — cómo usarlas.
estado: active
-->

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

🗳️ **¿Te fue útil este documento?**
- [ ] Sí, resolvió mi duda
- [ ] Más o menos, necesito más contexto
- [ ] No me ayudó

📢 [Abre un feedback aquí](https://github.com/scanalesespinoza/the-wise-tech/issues/new?template=feedback.yml)

---
