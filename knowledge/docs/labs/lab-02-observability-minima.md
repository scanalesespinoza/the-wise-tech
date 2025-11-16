## Propósito
Enmarca cómo Lab 02 — Observability Minimum (≤ 60–90 min) ayuda a mantener decisiones alineadas con The Wise Tech.

## Audiencia
Personas y equipos que necesitan una guía rápida sobre Lab 02 — Observability Minimum (≤ 60–90 min).

## Cuándo usarlo
Consúltalo cuando requieras referencias inmediatas para Lab 02 — Observability Minimum (≤ 60–90 min) o debas compartir el enfoque con otros equipos.

> **Propósito:** Dar contexto accionable sobre Lab 02 — Observability Minimum (≤ 60–90 min) dentro de The Wise Tech.
> **Audiencia:** Equipos y perfiles interesados en las bases de conocimiento y lineamientos del programa.
> **Uso recomendado:** Consulta este documento cuando necesites aplicar o compartir detalles de Lab 02 — Observability Minimum (≤ 60–90 min).
> **Estado:** Activo.


## Tabla de navegación

- [Prerrequisitos](#prerrequisitos)
- [Pasos](#pasos)
- [KPIs](#kpis)
- [Evidencia](#evidencia)
- [What’s next](#whats-next)

# Lab 02 — Observability Minimum (≤ 60–90 min)
**Objetivo:** demostrar correlation-id, logs estructurados y p95 medible.

## Prerrequisitos
- Iteración 7 aplicada (`operations/scripts/telemetry-smoke.py` y guía de telemetría).

## Pasos
1) Revisa la guía: `docs/guides/telemetry-minima.md`.
2) Ejecuta: `make -f operations/Makefile telemetry-smoke` (o `python operations/scripts/telemetry-smoke.py`).
3) Captura el `summary` (requests_total, error_rate, latency_p95_ms).
4) Si es posible, añade un pequeño retraso configurable y compara p95.
5) Documenta cómo se propaga `x-correlation-id` (log extract).

## KPIs
- `requests_total`: ≥ 50 (default smoke).
- `error_rate`: ≤ 0.10 (mock).
- `latency_p95_ms`: valor observado; documenta impacto de tu cambio.

## Evidencia
- Usa `docs/templates/labs/evidence-lab-02.md`.

## What’s next
- Conectar p95 con una acción de resiliencia (timeouts/retries) o con SLO p95.
---
Última modificación: 2025-11-16

🗳️ **¿Te fue útil este documento?**
- [ ] Sí, resolvió mi duda
- [ ] Más o menos
- [ ] No me ayudó

💬 [Deja tu feedback](https://github.com/scanalesespinoza/the-wise-tech/issues/new?template=feedback.yml)

---

