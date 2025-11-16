---
title: "Security Minimum"
tags: ["developers", "resilience", "playbooks"]
---
## Propósito
Enmarca cómo Seguridad mínima — Contributors ayuda a mantener decisiones alineadas con The Wise Tech.

## Audiencia
Personas y equipos que necesitan una guía rápida sobre Seguridad mínima — Contributors.

## Cuándo usarlo
Consúltalo cuando requieras referencias inmediatas para Seguridad mínima — Contributors o debas compartir el enfoque con otros equipos.

> **Propósito:** Dar contexto accionable sobre Security Minimum dentro de The Wise Tech.
> **Audiencia:** Equipos y perfiles interesados en las bases de conocimiento y lineamientos del programa.
> **Uso recomendado:** Consulta este documento cuando necesites aplicar o compartir detalles de Security Minimum.
> **Estado:** Activo.


## Tabla de navegación

- [Flujo recomendado](#flujo-recomendado)
- [Próximos pasos](#prximos-pasos)
- [See also](#see-also)

# Seguridad mínima — Contributors
Esta guía define controles prácticos y reproducibles:
- **Secretos**: nunca en el repo. Usa variables de entorno o secretos en GitHub.
- **Dependencias**: Dependabot abre PRs semanales para Actions y Python.
- **Escaneo de secretos**:
  - Local: `make security-scan` (gitleaks).
  - CI: workflow `gitleaks` se ejecuta en PR/push.
- **Datos sensibles en docs**: usa ejemplos ficticios y elimina PII.
- **PRs**: si tu cambio toca CI/scripts/deps, añade una línea “Security note” en el cuerpo del PR.

## Flujo recomendado
1) Ejecuta `make security-scan` antes del PR.
2) Revisa diffs por si quedaron credenciales o tokens.
3) Acepta PRs de Dependabot (verifica que CI pase).
4) Si detectas un riesgo, usa el canal privado de `SECURITY.md`.

## Próximos pasos
- Añadir SAST/linters específicos cuando el stack lo requiera.
- Firmado de commits y/o provenance de artefactos (release pipeline).

## See also
- [Security Policy](https://github.com/scanalesespinoza/the-wise-tech/blob/main/.github/SECURITY.md)
- [Developer playbook](../playbooks/developer-playbook.md)
- [Contribution Guide](contribution-guide.md)
---
Última modificación: 2025-11-16

🗳️ **¿Te fue útil este documento?**
- [ ] Sí, resolvió mi duda
- [ ] Más o menos
- [ ] No me ayudó

💬 [Deja tu feedback](https://github.com/scanalesespinoza/the-wise-tech/issues/new?template=feedback.yml)

---

