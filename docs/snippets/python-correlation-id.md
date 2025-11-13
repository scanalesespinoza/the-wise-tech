# Snippet: Correlation-ID en Python

Usa este snippet para instrumentar logs con `correlation-id` y mantener trazas consistentes entre servicios.

```python
import logging
from contextlib import contextmanager
from typing import Iterator

LOG = logging.getLogger("payments")

@contextmanager
def log_with_correlation_id(correlation_id: str) -> Iterator[logging.LoggerAdapter]:
    adapter = logging.LoggerAdapter(LOG, {"correlation_id": correlation_id})
    try:
        adapter.debug("starting scoped operation")
        yield adapter
    finally:
        adapter.info("correlation-id released")
```

## Cómo aplicarlo
- Inserta el contexto alrededor de llamadas a APIs externas o handlers de eventos.
- Propaga el `correlation-id` desde el entrypoint (por ejemplo, `refund-request.json`).
- Añade asserts en pruebas de `scenarios/payments/tests/` para garantizar el log estructurado.

---

# Snippet: Correlation-ID in Python (EN)

Use this snippet to instrument logs with a `correlation-id` and keep traces consistent across services.

```python
import logging
from contextlib import contextmanager
from typing import Iterator

LOG = logging.getLogger("payments")

@contextmanager
def log_with_correlation_id(correlation_id: str) -> Iterator[logging.LoggerAdapter]:
    adapter = logging.LoggerAdapter(LOG, {"correlation_id": correlation_id})
    try:
        adapter.debug("starting scoped operation")
        yield adapter
    finally:
        adapter.info("correlation-id released")
```

## How to apply
- Wrap external API calls or event handlers with the context manager.
- Propagate the `correlation-id` from the entrypoint (for example, `refund-request.json`).
- Add assertions inside `scenarios/payments/tests/` to guarantee structured logging.

## See also / Ver también
- [Developer Playbook](../playbooks/developer-playbook.md)
- [Payments overview](../scenarios/payments-overview.md)
- [Contribution guide](../guides/contribution-guide.md)
