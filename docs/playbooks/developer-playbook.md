# Developer Playbook

## Ciclo diario
- Revisar telemetría de servicios críticos y documentar hallazgos.
- Coordinar pairings con Platform Engineers para revisar pipelines.
- Actualizar tableros de progreso en base a métricas compartidas.

## Entregables clave
- Código instrumentado con pruebas automatizadas y reportes.
- ADRs que expliquen decisiones de arquitectura.
- Runbooks actualizados para escenarios recurrentes.

## Prácticas de resiliencia
- Ejecutar pruebas de caos controladas con soporte de Platform Engineers.
- Aplicar feature flags para desplegar de forma gradual.
- Mantener comunicación activa con soporte y personas usuarias.

## Primeros 60 minutos
- Ejecuta `make test`, `make parity` y `make links` registrando duración y salida de cada comando.
- Documenta en el changelog del escenario de pagos qué aprendizaje dejó la ronda de validaciones.
- Abre un borrador de PR enlazando el principio de Wise Tech reforzado y el KPI que impactará.

## Indicadores clave de experimento
- **Tiempo de ciclo del escenario de pagos**: objetivo inicial ≤ 5 minutos desde `make test` hasta `make docs`.
- **Defectos prevenidos**: mínimo 1 hallazgo por semana detectado antes de merge por paridad o enlaces.
- **Cobertura documental**: cada PR debe añadir o actualizar al menos un enlace hacia guías o runbooks.

## See also
- [Quickstart](../guides/quickstart.md)
- [Contribution guide](../guides/contribution-guide.md)
- [Platform playbook](platform-playbook.md)
- [Wise Tech principles](../principles/wise-tech-principles.md)
- [Roadmap](../roadmap/roadmap.md)
