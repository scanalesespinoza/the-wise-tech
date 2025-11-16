---
title: "Platform Engineers Fast Track"
tags: ["platform", "paths", "fast-track"]
---
## Propósito
Enmarca cómo Fast Track — Platform Engineers ayuda a mantener decisiones alineadas con The Wise Tech.

## Audiencia
Personas y equipos que necesitan una guía rápida sobre Fast Track — Platform Engineers.

## Cuándo usarlo
Consúltalo cuando requieras referencias inmediatas para Fast Track — Platform Engineers o debas compartir el enfoque con otros equipos.

> **Propósito:** Dar contexto accionable sobre Platform Engineers Fast Track dentro de The Wise Tech.
> **Audiencia:** Equipos y perfiles interesados en las bases de conocimiento y lineamientos del programa.
> **Uso recomendado:** Consulta este documento cuando necesites aplicar o compartir detalles de Platform Engineers Fast Track.
> **Estado:** Activo.

# Fast Track — Platform Engineers

Atajo diseñado para probar la plataforma mínima antes de continuar con [Platform Engineers 30/60/90](../platform-engineers-30-60-90.md).

**KPI exprés:** En 10 min deberías haber ajustado una política, corrido una verificación y documentado el hallazgo en un issue.

## Tabla de navegación

- [⚡ Paso rápido](#⚡-paso-rápido)
- [🔗 Más información](#🔗-más-información)
- [📌 Dependencias](#📌-dependencias)

## ⚡ Paso rápido

1. **⚙️ Ajusta una política (3 min).** Revisa `experience/scenarios/payments/policies/resilience.yml` y modifica un control puntual (p. ej. *timeout* o *circuit-breaker*).
2. **🛡️ Valida resiliencia (4 min).** Ejecuta `make -f operations/Makefile resilience-check` y guarda la salida junto con el diff aplicado.
> ℹ️ Consejo: Ajusta el comando a tu entorno antes de ejecutarlo.
3. **📘 Publica el runbook (3 min).** Documenta el aprendizaje en `knowledge/docs/playbooks/platform-playbook.md` (sección experimentos) y abre un issue para el próximo control a automatizar.

## 🔗 Más información

- [Platform Engineers — 30/60/90](../platform-engineers-30-60-90.md)
- [Platform Playbook](../../playbooks/platform-playbook.md)
- [Resilience policies guide](../../guides/resilience-policies.md)

## 📌 Dependencias

- `make`, `git` y acceso local a los scripts de operaciones.
- Permisos para editar políticas dentro del repositorio.
- Plantilla de issues para documentar experimentos de plataforma.

## See also / Ver también

- [Platform Engineers — 30/60/90](../platform-engineers-30-60-90.md)
- [Platform Playbook](../../playbooks/platform-playbook.md)
- [Resilience policies guide](../../guides/resilience-policies.md)
- [Content style guide](../../guides/content-style-guide.md)
---
Última modificación: 2025-11-16

🗳️ **¿Te fue útil este documento?**
- [ ] Sí, resolvió mi duda
- [ ] Más o menos
- [ ] No me ayudó

💬 [Deja tu feedback](https://github.com/scanalesespinoza/the-wise-tech/issues/new?template=feedback.yml)

---

