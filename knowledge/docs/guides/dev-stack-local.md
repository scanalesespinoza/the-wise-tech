---
title: "Dev stack local — live docs + OTEL/Jaeger"
tags: ["developers","platform-engineers","dx","observability"]
---
## Propósito
Enmarca cómo Dev stack local — rápido ayuda a mantener decisiones alineadas con The Wise Tech.

## Audiencia
Personas y equipos que necesitan una guía rápida sobre Dev stack local — rápido.

## Cuándo usarlo
Consúltalo cuando requieras referencias inmediatas para Dev stack local — rápido o debas compartir el enfoque con otros equipos.

> **Propósito:** Dar contexto accionable sobre Dev stack local — live docs + OTEL/Jaeger dentro de The Wise Tech.
> **Audiencia:** Equipos y perfiles interesados en las bases de conocimiento y lineamientos del programa.
> **Uso recomendado:** Consulta este documento cuando necesites aplicar o compartir detalles de Dev stack local — live docs + OTEL/Jaeger.
> **Estado:** Activo.


## Tabla de navegación

- [Qué incluye](#qu-incluye)
- [Cómo usar](#cmo-usar)
- [Probar trazas con el smoke](#probar-trazas-con-el-smoke)
- [See also](#see-also)

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
---
Última modificación: 2025-11-16

🗳️ **¿Te fue útil este documento?**
- [ ] Sí, resolvió mi duda
- [ ] Más o menos
- [ ] No me ayudó

💬 [Deja tu feedback](https://github.com/scanalesespinoza/the-wise-tech/issues/new?template=feedback.yml)

---

