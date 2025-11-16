---
title: "Telemetría mínima (Dev & Platform)"
tags: ["developers", "observability", "quickstart"]
---
## Propósito
Enmarca cómo Telemetría mínima (Dev & Platform) ayuda a mantener decisiones alineadas con The Wise Tech.

## Audiencia
Personas y equipos que necesitan una guía rápida sobre Telemetría mínima (Dev & Platform).

## Cuándo usarlo
Consúltalo cuando requieras referencias inmediatas para Telemetría mínima (Dev & Platform) o debas compartir el enfoque con otros equipos.

> **Propósito:** Dar contexto accionable sobre Telemetría mínima (Dev & Platform) dentro de The Wise Tech.
> **Audiencia:** Equipos y perfiles interesados en las bases de conocimiento y lineamientos del programa.
> **Uso recomendado:** Consulta este documento cuando necesites aplicar o compartir detalles de Telemetría mínima (Dev & Platform).
> **Estado:** Activo.


## Tabla de navegación

- [Cómo adoptarla (TL;DR)](#cmo-adoptarla-tldr)
- [Señales mínimas en PR (ops-signals)](#seales-mnimas-en-pr-ops-signals)
- [Próximos pasos](#prximos-pasos)
- [See also](#see-also)

# Telemetría mínima (Dev & Platform)
Esta guía define la base de observabilidad reproducible:
- **Correlation-ID**: propaga `x-correlation-id` entre servicios; genera uno si falta.
- **Logs estructurados**: incluye `timestamp, level, correlation_id, service, event, latency_ms`.
- **Métricas base**:
  - `requests_total{service,route,status}`
  - `error_rate{service,route}`
  - `latency_p95_ms{service,route}`
- **Trazas (OTEL)**: span por request y spans anidados para llamadas externas; exportador OTLP opcional.
## Cómo adoptarla (TL;DR)
1) Copia el snippet de correlation-id para tu runtime (ver “Snippets”).
2) Estandariza logs con los campos mínimos.
3) Expone/recoge métricas base (o simula local) y mide p95.
4) Si usas OTEL, añade inicialización y exportador (opcional).
5) Ejecuta `make -f operations/Makefile telemetry-smoke` para verificar.
## Señales mínimas en PR (ops-signals)
- Impacto esperado en SLO (latencia/errores): bajo/medio/alto.
- ¿Se propaga `x-correlation-id`? Sí/No (adjunta evidencia del smoke).
- ¿Logs estructurados y métrica p95 presentes? Sí/No.
## Próximos pasos
- Conectar con SLOs (iteración 6) y políticas de resiliencia (iteración 5).

## See also
- [SLOs & Error Budget — Cómo usarlos](slo-how-to.md)
- [Resilience Policies — Cómo usarlas](resilience-policies.md)
- [Python correlation-id snippet](../snippets/python-correlation-id.md)
- [Platform playbook](../playbooks/platform-playbook.md)
---
Última modificación: 2025-11-16

🗳️ **¿Te fue útil este documento?**
- [ ] Sí, resolvió mi duda
- [ ] Más o menos
- [ ] No me ayudó

💬 [Deja tu feedback](https://github.com/scanalesespinoza/the-wise-tech/issues/new?template=feedback.yml)

---

