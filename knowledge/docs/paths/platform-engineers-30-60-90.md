---
title: "Platform Engineers — 30/60/90"
tags: ["platform-engineers", "paths", "resilience"]
---
> **Propósito:** Dar contexto accionable sobre Platform Engineers — 30/60/90 dentro de The Wise Tech.
> **Audiencia:** Equipos y perfiles interesados en las bases de conocimiento y lineamientos del programa.
> **Uso recomendado:** Consulta este documento cuando necesites aplicar o compartir detalles de Platform Engineers — 30/60/90.
> **Estado:** Activo.

# Platform Engineers — 30/60/90

## 30 min
- Ejecuta `make -f operations/Makefile install && make -f operations/Makefile parity && make -f operations/Makefile docs` para comprobar el setup base.
- Revisa `experience/scenarios/payments/policies/` y `experience/scenarios/payments/slo/` para entender los contratos actuales.

## 60 min (first win)
- Habilita o verifica la ejecución de `make -f operations/Makefile verify-links` en CI (workflow docs-and-links).
- Documenta cómo correrlo en local y en CI para nuevos contribuidores.

## 90 min (operabilidad)
- Propón o valida timeouts/retries o un check de resiliencia adicional.
- Añade una nota en el playbook o runbook correspondiente con el hallazgo.

**KPIs**
- 0 enlaces rotos en la PR.
- Políticas válidas en PRs que toquen `experience/scenarios/payments/**`.
- CI verde garantizado.

---

# Platform Engineers — 30/60/90 (EN)

## 30 min
- Run `make -f operations/Makefile install && make -f operations/Makefile parity && make -f operations/Makefile docs` to confirm the baseline setup.
- Review `experience/scenarios/payments/policies/` and `experience/scenarios/payments/slo/` to understand current contracts.

## 60 min (first win)
- Enable or verify `make -f operations/Makefile verify-links` in CI (docs-and-links workflow).
- Document how to run it locally and in CI for new contributors.

## 90 min (operability)
- Propose or validate timeouts/retries or an additional resilience check.
- Add a note in the relevant playbook or runbook capturing the finding.

**KPIs**
- Zero broken links in the PR.
- Policies validated on PRs touching `experience/scenarios/payments/**`.
- CI remains green.

## See also / Ver también
- [Platform playbook](../playbooks/platform-playbook.md)
- [Platform engineers overview](../personas/platform-engineers-overview.md)
- [Payments overview](../scenarios/payments-overview.md)
- [Roadmap](../roadmap/roadmap.md)

---

---
¿Te fue útil este documento?
[ ] Sí  [ ] Algo  [ ] No
Deja feedback [aquí](https://github.com/scanalesespinoza/the-wise-tech/issues/new?template=feedback.yml)
---