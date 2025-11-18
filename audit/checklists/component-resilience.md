# Lista de verificación de resiliencia de componentes

Esta lista vincula los campos del contrato del componente con los criterios utilizados
por el equipo de auditoría. Cada punto debe ser respaldado con evidencia documentada
y valores actualizados dentro de `component-contract.yaml`.

## 1. SLO de disponibilidad y criticidad
- `resilience.availability_slo` define el objetivo porcentual vigente para el
  componente y coincide con la severidad descrita en `component.lifecycle.tier`.
- `component.lifecycle.data_classification` justifica cualquier excepción o
  endurecimiento del objetivo.

## 2. Análisis de modos de falla y mitigación
- `resilience.failure_modes` describe los escenarios de caída por dependencias,
  saturación y errores de configuración, cada uno con impacto cuantificado.
- `resilience.recovery_runbooks` incluye vínculos a runbooks probados para cada
  modo de falla crítico.
- `resilience.chaos_validation.frequency` indica la cadencia con la que se
  ejecutan pruebas de caos u otros ejercicios de resiliencia.

## 3. Dependencias protegidas
- `component.dependencies.runtime` enumera las dependencias en tiempo de
  ejecución con responsables y contratos acordados.
- Cada dependencia crítica documenta la estrategia de "fallback" o degradación
  controlada dentro de `resilience.fallbacks`.

## 4. Preparación operativa
- `component.owner.escalation` define horarios y canales de contacto 24/7.
- `resilience.backup_and_restore` especifica medios, ventanas y resultados de la
  última restauración probada.

## 5. Evidencias de revisión
- `evidence.resilience_checklist` referencia la ubicación de las últimas
  evidencias adjuntas (por ejemplo, tickets, capturas o reportes de ejercicios).
- `evidence.last_reviewed` indica la fecha en que el equipo firmó la revisión de
  resiliencia.
