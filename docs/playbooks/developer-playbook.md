# Developer Playbook (mínimo)

## Idempotencia práctica
- Todas las operaciones críticas deben aceptar un `idempotency_key` (usa el fixture `refund-request.json` para replicar reintentos).
- Define claramente qué campos participan en el hash; documenta supuestos junto al handler.
- Las pruebas deben validar que dos invocaciones consecutivas no generan efectos colaterales.

## Trazabilidad con correlation-id
```python
import logging
from contextlib import contextmanager

logger = logging.getLogger("payments")

@contextmanager
def log_with_correlation_id(correlation_id: str):
    try:
        logger = logging.LoggerAdapter(logging.getLogger("payments"), {"correlation_id": correlation_id})
        yield logger
    finally:
        logger.info("correlation-id released")
```
- Inserta el `correlation_id` en cada log relevante y replica el patrón en runbooks.
- Reutiliza los IDs incluidos en `valid-charge.json` para mantener trazas consistentes.

## Diseño de pruebas escalonado
1. **Unitarias** (`python -m unittest scenarios/payments/tests/test_service_errors.py`).
2. **Flow tests** (`python -m unittest scenarios/payments/tests/test_payments_flow.py -v`).
3. **Resiliencia** (`make parity` + validaciones de enlaces).

## Ciclo local → CI
- `make ci` encadena install + lint + fmt + test + parity.
- El workflow [`quality`](../../.github/workflows/quality.yml) ejecuta exactamente los mismos comandos.
- Usa `make docs` para verificar navegación bilingüe antes de pedir revisión.

## ADR y decisiones compartidas
- Registra cada cambio estructural en `adr/` y enlaza el principio de Wise Tech reforzado.
- Añade referencias al runbook o contrato que impacta el cambio.

## Indicadores clave de experimento
- **Tiempo de ciclo**: ≤ 5 minutos desde `make test` hasta detener `make docs`.
- **Defectos prevenidos**: al menos 1 hallazgo semanal detectado por `make parity` o `python scripts/check-links.py --strict`.
- **Cobertura documental**: cada PR cita al menos un recurso en `docs/knowledge/` o `docs/playbooks/`.
