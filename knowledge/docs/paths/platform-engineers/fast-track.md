---
title: "Platform Engineers Fast Track"
tags: ["platform", "paths", "fast-track"]
---
<!-- metadata
para_quien: Equipos y contribuidores que consultan "Fast Track — Platform Engineers" en The Wise Tech.
objetivo: Proporcionar un contexto accionable sobre fast track — platform engineers.
cuando_usar: Recurre a este documento cuando necesites aplicar o compartir detalles de fast track — platform engineers.
estado: active
-->

# Fast Track — Platform Engineers

Atajo diseñado para probar la plataforma mínima antes de continuar con [Platform Engineers 30/60/90](../platform-engineers-30-60-90.md).

1. **Carga las políticas (10 min).** Revisa `experience/scenarios/payments/policies/resilience.yml` y ajusta un solo control (por ejemplo, *circuit-breaker* o *timeouts*).
2. **Valida resiliencia (15 min).** Ejecuta `make -f operations/Makefile resilience-check` y captura el resultado junto con el cambio aplicado.
3. **Publica el runbook (20 min).** Documenta el aprendizaje en `knowledge/docs/playbooks/platform-playbook.md` (sección de experimentos) y abre un issue para el siguiente control a automatizar.

➡️ Una vez completado, expande tu cobertura en [Platform Engineers — 30/60/90](../platform-engineers-30-60-90.md).

## See also / Ver también
- [Platform Engineers — 30/60/90](../platform-engineers-30-60-90.md)
- [Platform Playbook](../../playbooks/platform-playbook.md)
- [Resilience policies guide](../../guides/resilience-policies.md)

---

🗳️ **¿Te fue útil este documento?**
- [ ] Sí, resolvió mi duda
- [ ] Más o menos, necesito más contexto
- [ ] No me ayudó

📢 [Abre un feedback aquí](https://github.com/scanalesespinoza/the-wise-tech/issues/new?template=feedback.yml)

---
