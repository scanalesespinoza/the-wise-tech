<!-- metadata
para_quien: Equipos y contribuidores que consultan "Lab 02 — Observability Minimum (≤ 60–90 min)" en The Wise Tech.
objetivo: Proporcionar un contexto accionable sobre lab 02 — observability minimum (≤ 60–90 min).
cuando_usar: Recurre a este documento cuando necesites aplicar o compartir detalles de lab 02 — observability minimum (≤ 60–90 min).
estado: active
-->

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

🗳️ **¿Te fue útil este documento?**
- [ ] Sí, resolvió mi duda
- [ ] Más o menos, necesito más contexto
- [ ] No me ayudó

📢 [Abre un feedback aquí](https://github.com/scanalesespinoza/the-wise-tech/issues/new?template=feedback.yml)

---
