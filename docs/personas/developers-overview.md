# Developers — Quickstart

## Primeros 10 minutos
1. `make install` — instala dependencias runtime y de documentación.
2. `make test` — ejecuta todos los tests del escenario de pagos.
3. `make parity` — asegura paridad bilingüe antes de abrir PR.
4. `make docs` — navega la experiencia local en `http://127.0.0.1:8000`.
5. `make ci` — reproduce el mismo pipeline que corre en el workflow `quality`.

## Escenario de pagos: primeros pasos
- Datos de prueba en `scenarios/payments/tests/fixtures/` (`valid-charge.json` y `refund-request.json`).
- Ejecuta pruebas focalizadas:
  ```bash
  python -m unittest scenarios/payments/tests/test_payments_flow.py -v
  ```
- Si necesitas depurar traducciones o errores, revisa `scenarios/payments/service/errors.py` y registra aprendizajes en `adr/`.

## Prácticas compartidas (mínimas)
- **Idempotencia**: usa `idempotency_key` en tus handlers críticos y verifica reintentos con los fixtures.
- **Trazabilidad**: añade un `correlation_id` a tus logs (ver snippet en el [Developer Playbook](../playbooks/developer-playbook.md#trazabilidad-con-correlation-id)).
- **Capitalización**: cada entrega debe apuntar al principio reforzado de Wise Tech y documentar decisiones en el tablero de ADRs.
