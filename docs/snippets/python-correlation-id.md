---
title: "Python Correlation-ID Snippet"
tags: ["developers", "observability", "quickstart"]
---
# Python Correlation-ID Snippet

```python
import uuid, time, json, logging
from contextvars import ContextVar
from functools import wraps

CORR_ID = ContextVar("correlation_id", default=None)
SERVICE = "wise-tech-example"

def ensure_correlation_id(headers: dict) -> str:
    cid = headers.get("x-correlation-id") or str(uuid.uuid4())
    CORR_ID.set(cid)
    return cid

def log_struct(level, event, **kw):
    rec = {
        "timestamp": int(time.time() * 1000),
        "level": level.upper(),
        "service": SERVICE,
        "event": event,
        "correlation_id": CORR_ID.get(),
    }
    rec.update(kw)
    print(json.dumps(rec))

def traced(fn):
    @wraps(fn)
    def _w(*args, **kwargs):
        start = time.time()
        try:
            return fn(*args, **kwargs)
        finally:
            elapsed_ms = int((time.time() - start) * 1000)
            log_struct("info", "span.end", fn=fn.__name__, latency_ms=elapsed_ms)
    return _w

# Ejemplo de uso:
# headers = {"x-correlation-id": "..."}  # si no viene, se creará
# ensure_correlation_id(headers)
# log_struct("info", "payment.start", route="/payments/charge")
# @traced
# def do_work(): ...
```

(Nota: si prefieres Node.js, crear también docs/snippets/nodejs-correlation-id.md con middleware Express equivalente — opcional en esta iteración.)

## See also
- [Telemetría mínima (Dev & Platform)](../guides/telemetry-minima.md)
- [Content-Style-Guide — Wise Tech](../guides/content-style-guide.md)
- [Editorial-Workflow — Propuesta→Draft→Review→Publish](../guides/editorial-workflow.md)
