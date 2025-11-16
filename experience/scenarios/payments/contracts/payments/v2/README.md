> **Propósito:** Dar contexto accionable sobre Payments API Contract v2 / Contrato API de Pagos v2 dentro de The Wise Tech.
> **Audiencia:** Equipos y perfiles interesados en los escenarios y rutas de experiencia práctica.
> **Uso recomendado:** Consulta este documento cuando necesites aplicar o compartir detalles de Payments API Contract v2 / Contrato API de Pagos v2.
> **Estado:** Activo.

# Payments API Contract v2 / Contrato API de Pagos v2

This directory stores the canonical contract used in the recipe for
consumer-driven contract testing. The document is intentionally bilingual
so reviewers and stakeholders can reason about the same artifact.

## Overview / Descripción
- **Producer / Productor:** `payments` service
- **Consumer / Consumidor:** `checkout-ui`
- **Format:** JSON over HTTPS
- **Version:** 2.0.0

## Schema (English)
```json
{
  "type": "object",
  "required": ["payment_id", "status", "amount", "currency"],
  "properties": {
    "payment_id": {"type": "string", "description": "Opaque identifier"},
    "status": {"type": "string", "enum": ["AUTHORIZED", "DECLINED", "PENDING"]},
    "amount": {"type": "number", "minimum": 0},
    "currency": {"type": "string", "pattern": "^[A-Z]{3}$"},
    "retry_after_seconds": {"type": "integer", "minimum": 0}
  }
}
```

## Esquema (Español)
```json
{
  "type": "object",
  "required": ["payment_id", "status", "amount", "currency"],
  "properties": {
    "payment_id": {"type": "string", "description": "Identificador opaco"},
    "status": {"type": "string", "enum": ["AUTHORIZED", "DECLINED", "PENDING"]},
    "amount": {"type": "number", "minimum": 0},
    "currency": {"type": "string", "pattern": "^[A-Z]{3}$"},
    "retry_after_seconds": {"type": "integer", "minimum": 0}
  }
}
```

## Contract Test Notes / Notas de pruebas de contrato
- Providers must set `retry_after_seconds` when `status` is `PENDING`.
- Consumers ignore unknown fields but log them for analysis.
- Pact files live alongside this README under `pacts/` (add them as you
  evolve scenarios) / Los archivos Pact viven junto a este README en
  `pacts/` (agrégalos conforme evoluciones los escenarios).
- Automated verification lives in
  `experience/scenarios/payments/systems/tests/test_contract_pact.py` to detect schema drift
  during CI runs. / La verificación automática vive en
  `experience/scenarios/payments/systems/tests/test_contract_pact.py` para detectar desvíos
  de esquema durante las ejecuciones de CI.

---

---
¿Te fue útil este documento?
[ ] Sí  [ ] Algo  [ ] No
Deja feedback [aquí](https://github.com/scanalesespinoza/the-wise-tech/issues/new?template=feedback.yml)
---
