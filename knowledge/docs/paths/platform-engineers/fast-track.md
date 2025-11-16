---
title: "Platform Engineers Fast Track"
tags: ["platform", "paths", "fast-track"]
---
> **Propósito:** Dar contexto accionable sobre Platform Engineers Fast Track dentro de The Wise Tech.
> **Audiencia:** Equipos y perfiles interesados en las bases de conocimiento y lineamientos del programa.
> **Uso recomendado:** Consulta este documento cuando necesites aplicar o compartir detalles de Platform Engineers Fast Track.
> **Estado:** Activo.

# Fast Track — Platform Engineers

Atajo diseñado para probar la plataforma mínima antes de continuar con [Platform Engineers 30/60/90](../platform-engineers-30-60-90.md).

## 🧭 3 pasos rápidos
1. **⚙️ Ajusta una política (10 min).** Revisa `experience/scenarios/payments/policies/resilience.yml` y modifica un control puntual (p. ej. *timeouts* o *circuit-breaker*).
2. **🛡️ Valida resiliencia (15 min).** Ejecuta `make -f operations/Makefile resilience-check` y guarda la salida junto con el diff aplicado.
3. **📘 Publica el runbook (20 min).** Documenta el aprendizaje en `knowledge/docs/playbooks/platform-playbook.md` (sección experimentos) y abre un issue para el próximo control a automatizar.

[➡️ Ruta completa Platform Engineers — 30/60/90](../platform-engineers-30-60-90.md)

## See also / Ver también
- [Platform Engineers — 30/60/90](../platform-engineers-30-60-90.md)
- [Platform Playbook](../../playbooks/platform-playbook.md)
- [Resilience policies guide](../../guides/resilience-policies.md)

---

---
¿Te fue útil este documento?
[ ] Sí  [ ] Algo  [ ] No
Deja feedback [aquí](https://github.com/scanalesespinoza/the-wise-tech/issues/new?template=feedback.yml)
---