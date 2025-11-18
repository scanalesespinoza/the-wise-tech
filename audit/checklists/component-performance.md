# Lista de verificación de desempeño de componentes

Los criterios permiten validar que los parámetros de rendimiento declarados en el
contrato sean medibles, rastreables y accionables.

## 1. Perfil de carga y supuestos
- `performance.load_profile.expected_qps` define demanda promedio y picos
  estimados por ventana temporal.
- `performance.load_profile.peak_duration` explica la duración esperada de los
  picos y el origen de los datos utilizados.

## 2. SLO y métricas de experiencia
- `performance.latency_slo_ms` fija el percentil (p99 o similar) para
  solicitudes críticas.
- `performance.error_budget_policy` detalla cómo se mide el consumo del presupuesto
  de errores en relación con el SLO.
- `observability.metrics` incluye la métrica exacta que alimenta el cálculo del
  SLO de desempeño.

## 3. Capacidad instalada y plan de crecimiento
- `performance.capacity_plan.current_utilization` resume uso promedio de CPU,
  memoria y almacenamiento.
- `performance.capacity_plan.scale_strategy` describe cuándo y cómo se aumenta la
  capacidad (autoescalado, "capacity reservations", etc.).
- `performance.benchmark_evidence` enlaza resultados de pruebas de carga
  reproducibles.

## 4. Gestión de regresiones
- `performance.regression_tests` indica suites automatizadas que corren antes de
  cada despliegue.
- `component.owner.team` mantiene responsables para revisar alertas de latencia y
  saturación.

## 5. Evidencias de revisión
- `evidence.performance_checklist` enumera los documentos/tickets aprobados en la
  última revisión de desempeño.
- `evidence.last_reviewed` indica la fecha de firma por parte de arquitectura de
  rendimiento.
