# Lab 03 — aDevelopment Loop (≤ 60–90 min)
**Objetivo:** usar IA responsable para acelerar systems/tests/docs y medir impacto.

## Prerrequisitos
- Conocer el escenario (p. ej., `experience/scenarios/payments/`).
- Tener lista una pauta de “uso responsable” (resumir en el PR qué se generó y qué se validó).

## Pasos
1) Selecciona un punto de mejora (test faltante, doc breve, ejemplo).
2) Solicita a la IA: *“Genera un test unitario mínimo y una breve doc que explique el caso; mantén estilo del repo y guiones medios en nombres.”*
3) Revisa manualmente lo generado (calidad, pertinencia, simplicidad).
4) Ejecuta: `make -f operations/Makefile test` y actualiza docs con enlaces relativos.
5) Prepara PR pequeño (explica qué principio de Wise Tech refuerza y por qué).

## KPIs
- `time_to_first_test_added`: min.
- `tests_added`: nº.
- `doc_lines_added`: nº (preferir conciso).
- `make -f operations/Makefile test` → verde.

## Evidencia
- Usa `docs/templates/labs/evidence-lab-03.md`.

## What’s next
- Encadenar con resiliencia (timeouts/retries) o con SLO (impacto percibido).
