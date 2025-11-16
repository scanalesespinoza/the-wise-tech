<!-- metadata
para_quien: Equipos y contribuidores que consultan "Lab 01 — Resilience Basics (≤ 60–90 min)" en The Wise Tech.
objetivo: Proporcionar un contexto accionable sobre lab 01 — resilience basics (≤ 60–90 min).
cuando_usar: Recurre a este documento cuando necesites aplicar o compartir detalles de lab 01 — resilience basics (≤ 60–90 min).
estado: active
-->

# Lab 01 — Resilience Basics (≤ 60–90 min)
**Objetivo:** ejercitar políticas de resiliencia y su validación automática.

## Prerrequisitos
- Iteración 5 (políticas) y 6 (SLOs) aplicadas.
- `python3`, `make`.

## Pasos
1) Explora la política: `experience/scenarios/payments/policies/resilience.yml`.
2) Valida: `make resilience-check`.
3) Ajusta `timeouts_ms.http_client_default` y `retries.base_ms` con valores seguros.
4) Revalida y anota los cambios (por qué, qué esperas mejorar).
5) Simula presupuesto de error: `make check-error-budget` (mock) y registra el resultado.

## KPIs (anota en la plantilla de evidencia)
- `resilience_check_pass`: true/false.
- `policy_diff_lines`: Nº de líneas cambiadas (bajo es mejor: cambios mínimos).
- `error_budget_spent_% (mock)`: antes/después.

## Evidencia
- Usa `docs/templates/labs/evidence-lab-01.md`.

## What’s next
- Relaciona cambios con un PR real y explica impacto en SLO (latencia p95).

---

🗳️ **¿Te fue útil este documento?**
- [ ] Sí, resolvió mi duda
- [ ] Más o menos, necesito más contexto
- [ ] No me ayudó

📢 [Abre un feedback aquí](https://github.com/scanalesespinoza/the-wise-tech/issues/new?template=feedback.yml)

---
