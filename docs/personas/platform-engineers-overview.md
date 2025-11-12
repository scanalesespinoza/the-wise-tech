# Platform Engineers Overview

## Operabilidad y observabilidad mínimas
- Instrumenta servicios con métricas de latencia, tasa de errores y capacidad en cada despliegue.
- Exige tableros compartidos y alertas claras antes de considerar un servicio listo para producción.
- Documenta runbooks resilientes en el [platform playbook](../playbooks/platform-playbook.md).

## Políticas y perfiles
- Aplica políticas de acceso mínimo y consistencia de despliegues descritas en `infra/`.
- Define perfiles de servicio (bronze/silver/gold) y enlázalos al [roadmap](../roadmap/roadmap.md) para priorizar mejoras.
- Refuerza acuerdos de confiabilidad en el [developer playbook](../playbooks/developer-playbook.md).

## Flujo de feedback
- Coordina weekly reviews con Developers para revisar telemetría y deuda operativa.
- Captura hallazgos en `adr/` y anuncia decisiones en el [contribution guide](../guides/contribution-guide.md).
- Solicita feedback de usuarios finales vía el [consumers overview](consumers-overview.md) y comparte resultados.

## See also
- [Wise Tech principles](../principles/wise-tech-principles.md)
- [Quickstart](../guides/quickstart.md)
- [Platform playbook](../playbooks/platform-playbook.md)
- [Roadmap](../roadmap/roadmap.md)
- [FAQ](../../README.md#faq)
