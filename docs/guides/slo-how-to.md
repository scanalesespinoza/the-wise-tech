---
title: "SLOs & Error Budget — Cómo usarlos"
tags: ["platform-engineers", "slo", "resilience"]
---
# SLOs & Error Budget — Cómo usarlos
Los SLOs definen expectativas operativas medibles; el presupuesto de error marca cuánto “fallo” es tolerable en la ventana (p. ej., 30 días).
## Flujo recomendado (mínimo)
1) Edita `scenarios/payments/slo/slo-spec.yml` con objetivos realistas (availability, p95).
2) `make slos` para validar formato y rangos.
3) `make check-error-budget` para simular consumo y ver políticas aplicables.
4) En PR, explica si algún cambio impacta SLOs o presupuesto (plantilla PR).
## Señales y acciones
- “fast burn” → acciones rápidas (freeze/hardening/rollback).
- “slow burn” → mitigación planificada.
## Próximos pasos
- Conectar métricas reales (prometheus/otlp) cuando estén disponibles.
- Integrar SLOs con resiliencia y postmortems.

## See also
- [Resilience Policies — Cómo usarlas](resilience-policies.md)
- [Telemetry (Minimum)](telemetry-minima.md)
- [Platform playbook](../playbooks/platform-playbook.md)
- [Platform Engineers — 30/60/90](../paths/platform-engineers-30-60-90.md)
