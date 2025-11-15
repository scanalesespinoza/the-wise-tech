---
title: "Dev stack local — live docs + OTEL/Jaeger"
tags: ["developers","platform-engineers","dx","observability"]
---
# Dev stack local — rápido
## Qué incluye
- **Docs en vivo** (MkDocs) en `http://127.0.0.1:8000`
- **Trazas**: envía OTLP a `http://127.0.0.1:4318` → **Jaeger UI** en `http://127.0.0.1:16686`

## Cómo usar
- Levanta todo: `make -f operations/Makefile dev-up`
- Estado/Logs: `make -f operations/Makefile dev-status` / `make -f operations/Makefile dev-logs`
- Detener: `make -f operations/Makefile dev-down`
- Solo docs live (sin compose): `make -f operations/Makefile docs-live`

## Probar trazas con el smoke
- Exporta OTLP (HTTP) en tu entorno:

```bash
export OTEL_EXPORTER_OTLP_TRACES_ENDPOINT=http://127.0.0.1:4318/v1/traces

export OTEL_TRACES_EXPORTER=otlp
```

- Ejecuta el smoke para generar actividad (y, si implementas spans en tu app/ejemplo, verás trazas en Jaeger):

```bash
python operations/scripts/telemetry-smoke.py
```

> El smoke actual emite logs/metrics; para trazas reales, añade el cliente OTEL en tu runtime siguiendo la guía de telemetría.

## See also
- [Telemetry (Minimum)](./telemetry-minima.md)
- [SLOs & Error Budget](./slo-how-to.md)
- [Resilience Policies](./resilience-policies.md)
