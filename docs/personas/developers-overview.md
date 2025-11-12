# Developers Overview

## Onboarding rápido
- Configura el IDE con extensiones de linting y IA recomendadas en `scripts/` (ver README).
- Ejecuta `make install` para dependencias locales y revisa `scripts/check-links.py` antes de abrir PRs.
- Usa los ejemplos del [escenario de pagos](../scenarios/payments-overview.md) para practicar flujos end-to-end.

## Calidad y resiliencia
- Ejecuta las suites de pruebas descritas en `ci/` y mantén la idempotencia en pipelines.
- Revisa el [platform playbook](../playbooks/platform-playbook.md) para conocer expectativas de observabilidad.
- Documenta supuestos y límites en el [developer playbook](../playbooks/developer-playbook.md).

## Knowledge capitalization
- Registra decisiones estratégicas en `adr/` y enlázalas desde el [roadmap](../roadmap/roadmap.md).
- Actualiza el [contribution guide](../guides/contribution-guide.md) cuando cambien rituales.
- Documenta aprendizajes en el [diagrama de enfoque](../diagrams/wise-tech-approach-ascii.md) para compartir patrones.

## See also
- [Consumers overview](consumers-overview.md)
- [Platform engineers overview](platform-engineers-overview.md)
- [Quickstart](../guides/quickstart.md)
- [Developer playbook](../playbooks/developer-playbook.md)
- [FAQ](../../README.md#faq)
