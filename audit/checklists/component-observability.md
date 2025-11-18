# Lista de verificación de observabilidad de componentes

Evalúa si el componente provee señales suficientes para detectar, diagnosticar y
aprender de incidentes.

## 1. Cobertura de métricas
- `observability.metrics` cataloga métricas clave con nombre, etiqueta primaria y
  propietario.
- Cada métrica indica su retención mínima y la plataforma donde reside.
- Al menos una métrica cubre el objetivo `performance.latency_slo_ms` y otra
  monitorea capacidad (`performance.capacity_plan`).

## 2. Telemetría de logs y trazas
- `observability.logs.structured` confirma uso de formato estructurado y
  `observability.logs.retention_days` cumple requisitos regulatorios.
- `observability.traces.coverage` detalla porcentaje de solicitudes críticas con
  trazabilidad distribuida.

## 3. Alertas accionables
- `observability.alerts` define condiciones, umbrales, canales y equipos
  destinatarios.
- Alertas están vinculadas a runbooks en `resilience.recovery_runbooks`.

## 4. Integridad de datos
- `observability.data_quality.validations` describe chequeos automáticos que
  aseguran integridad de las señales antes de generar alertas o reportes.
- `observability.access_controls` documenta quién puede modificar dashboards y
  canales de alerta.

## 5. Evidencias de revisión
- `evidence.observability_checklist` enlaza los artefactos revisados (dashboards,
  definiciones de alerta, consultas de logs, etc.).
- `evidence.last_reviewed` demuestra la fecha de la última auditoría conjunta con
  SRE/Observability.
