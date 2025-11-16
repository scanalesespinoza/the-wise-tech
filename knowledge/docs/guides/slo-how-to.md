---
title: "SLOs & Error Budget — Cómo usarlos"
tags: ["platform-engineers", "slo", "resilience"]
---
## Propósito
Enmarca cómo SLOs & Error Budget — Cómo usarlos ayuda a mantener decisiones alineadas con The Wise Tech.

## Audiencia
Personas y equipos que necesitan una guía rápida sobre SLOs & Error Budget — Cómo usarlos.

## Cuándo usarlo
Consúltalo cuando requieras referencias inmediatas para SLOs & Error Budget — Cómo usarlos o debas compartir el enfoque con otros equipos.

> **Propósito:** Dar contexto accionable sobre SLOs & Error Budget — Cómo usarlos dentro de The Wise Tech.
> **Audiencia:** Equipos y perfiles interesados en las bases de conocimiento y lineamientos del programa.
> **Uso recomendado:** Consulta este documento cuando necesites aplicar o compartir detalles de SLOs & Error Budget — Cómo usarlos.
> **Estado:** Activo.


## Tabla de navegación

- [Flujo recomendado (mínimo)](#flujo-recomendado-mnimo)
- [Señales y acciones](#seales-y-acciones)
- [Próximos pasos](#prximos-pasos)
- [See also](#see-also)

# SLOs & Error Budget — Cómo usarlos
Los SLOs definen expectativas operativas medibles; el presupuesto de error marca cuánto “fallo” es tolerable en la ventana (p. ej., 30 días).
## Flujo recomendado (mínimo)
1) Edita `experience/scenarios/payments/slo/slo-spec.yml` con objetivos realistas (availability, p95).
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
---
Última modificación: 2025-11-16

🗳️ **¿Te fue útil este documento?**
- [ ] Sí, resolvió mi duda
- [ ] Más o menos
- [ ] No me ayudó

💬 [Deja tu feedback](https://github.com/scanalesespinoza/the-wise-tech/issues/new?template=feedback.yml)

---

