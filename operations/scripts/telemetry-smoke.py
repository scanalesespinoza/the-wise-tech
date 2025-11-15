#!/usr/bin/env python3
"""Ejecuta una simulación local:

- Genera/propaga x-correlation-id
- Emite logs estructurados
- Mide latencia (ms) y deriva un p95 simple
- Muestra contadores de requests/errores
"""

import json
import random
import statistics
import time
import uuid

SERVICE = "wise-tech-smoke"
ROUTE = "/payments/charge"


def log(event, **kw):
    rec = {
        "timestamp": int(time.time() * 1000),
        "level": "INFO",
        "service": SERVICE,
        "event": event,
        "route": ROUTE,
        "correlation_id": kw.pop("correlation_id", None),
    }
    rec.update(kw)
    print(json.dumps(rec))


def simulate_request():
    cid = str(uuid.uuid4())
    t0 = time.time()
    # 5% error artificial
    is_err = random.random() < 0.05
    # lat aleatoria 80–500ms
    time.sleep(random.uniform(0.08, 0.5))
    elapsed = int((time.time() - t0) * 1000)
    log(
        "request.end",
        correlation_id=cid,
        latency_ms=elapsed,
        status=500 if is_err else 200,
        error=is_err,
    )
    return elapsed, is_err


def main(n: int = 50):
    lats = []
    errors = 0
    for _ in range(n):
        lat, err = simulate_request()
        lats.append(lat)
        errors += 1 if err else 0
    p95 = int(statistics.quantiles(lats, n=20)[18]) if len(lats) >= 20 else max(lats)
    print(
        json.dumps(
            {
                "summary": {
                    "requests_total": len(lats),
                    "errors": errors,
                    "error_rate": round(errors / max(1, len(lats)), 3),
                    "latency_p95_ms": p95,
                }
            }
        )
    )


if __name__ == "__main__":
    main()
