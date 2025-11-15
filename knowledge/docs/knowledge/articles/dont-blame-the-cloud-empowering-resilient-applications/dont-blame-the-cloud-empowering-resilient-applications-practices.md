# Practices — Don't Blame the Cloud: Empowering Resilient Applications

## Quick checklist (≤10 ítems)
- [ ] Definir objetivos de resiliencia por servicio (SLO, MTTR, error budget).
- [ ] Implementar monitoreo, logging y alertas accionables.
- [ ] Diseñar estrategias de degradación y failover documentadas.
- [ ] Automatizar restart, scaling y rollback con guardrails.
- [ ] Practicar pruebas de estrés y caos periódicas.
- [ ] Revisar eficiencia de recursos y límites de consumo.
- [ ] Crear runbooks compartidos entre desarrollo y operaciones.
- [ ] Participar en comunidades o foros para compartir incidentes y aprendizajes.

## How-to (pasos accionables)
1) Catalogar capacidades mínimas por servicio (observabilidad, recuperación, seguridad) y asignar responsables de implementación.  
2) Integrar pipelines que ejecuten pruebas de resiliencia (chaos scripts, load tests) antes de promover a producción y registren resultados.  
3) Establecer rituales de revisión post-incidente donde se actualicen runbooks, automatizaciones y métricas compartidas con toda la organización.

## KPIs / Leading indicators
- MTTR y tiempo de detección (MTTD).
- Cobertura de monitoreo por servicio crítico.
- Número de ejercicios de resiliencia ejecutados por trimestre.
- Porcentaje de incidentes con acciones preventivas documentadas.
