# Quickstart (≤15 líneas)

1. `make install` — deja listo Python, MkDocs y Ruff.
2. `make test` — ejecuta `python -m unittest` sobre `scenarios/payments/tests`.
3. `make parity` — verifica paridad bilingüe y bloquea desvíos tempranos.
4. `make docs` — sirve MkDocs en `http://127.0.0.1:8000`.
5. `python -m unittest scenarios/payments/tests/test_service_errors.py -v` para enfocarte en el flujo principal.
6. `make ci` (opcional) — cadena local idéntica a la del workflow `quality`.
7. Documenta aprendizajes en `docs/playbooks/developer-playbook.md` o en un ADR.
