## Propósito
Enmarca cómo Guías para Changelog Narrativo ayuda a mantener decisiones alineadas con The Wise Tech.

## Audiencia
Personas y equipos que necesitan una guía rápida sobre Guías para Changelog Narrativo.

## Cuándo usarlo
Consúltalo cuando requieras referencias inmediatas para Guías para Changelog Narrativo o debas compartir el enfoque con otros equipos.

> **Propósito:** Dar contexto accionable sobre Guías para Changelog Narrativo dentro de The Wise Tech.
> **Audiencia:** Equipos y perfiles interesados en las bases de conocimiento y lineamientos del programa.
> **Uso recomendado:** Consulta este documento cuando necesites aplicar o compartir detalles de Guías para Changelog Narrativo.
> **Estado:** Activo.


## Tabla de navegación

- [Estructura](#estructura)
- [Prácticas](#prcticas)
- [Orquestación por fases](#orquestacin-por-fases)
- [Checklist antes de publicar](#checklist-antes-de-publicar)

# Guías para Changelog Narrativo

Una entrada de changelog debe explicar más que el diff de código. Usa esta guía para redactar actualizaciones comprensibles para personas ingenieras, stakeholders y equipos de soporte.

## Estructura
1. **Título** – Resume el valor entregado en lenguaje sencillo.
2. **Qué cambió** – 3–5 viñetas que referencien módulos, APIs o infraestructura impactada.
3. **Por qué importa** – Describe el resultado para personas usuarias o negocio y qué [Principios Esenciales](principles-essential.md) se reforzaron.
4. **Riesgos/Mitigaciones** – Anota cambios disruptivos, pasos de migración, feature flags o planes de monitoreo.
5. **Evidencia** – Enlaza pruebas, tableros o seguimientos de incidentes que demuestren preparación.
6. **Próximos pasos** – Señala trabajo pendiente o ciclos de aprendizaje activados por este release.

## Prácticas
- Mantén las entradas cortas pero con contexto (200–300 palabras máximo).
- Haz cross-link con [recetas](recipes/README.md), recursos de onboarding o ADR relevantes.
- Usa etiquetas consistentes (p. ej. `#observabilidad`, `#resiliencia`) para mejorar la búsqueda.
- Pide a asistentes de IA que redacten el borrador inicial y luego refínalo por precisión y tono.
- Guarda el changelog junto a los artefactos del release para que sea parte de la evidencia operativa.

## Orquestación por fases
- Publica el changelog en inglés y español por cada fase (alpha, beta, GA) para que el mensaje sea consistente en todos los puntos de contacto.
- Coordina con soporte y customer success la actualización de FAQs y macros; registra responsables y fecha de despliegue para cada ajuste.
- Recoge feedback de personas beta en español (encuestas, sesiones guiadas) y usa los hallazgos para ajustar el glosario y el tono editorial.

## Checklist antes de publicar
- [ ] Revisado por al menos una persona de producto o soporte.
- [ ] Enlazado en el pull request o ticket de release.
- [ ] Menciona tareas de seguimiento o métricas que se monitorearán post-release.
- [ ] Traducción reflejada en el changelog en inglés si aplica.
- [ ] Changelog bilingüe publicado por fase (alpha/beta/GA) con equivalencias revisadas.
- [ ] FAQs y macros de soporte/CS actualizadas según el mensaje del release.
- [ ] Feedback beta en español incorporado y ajustes documentados en glosario/estilo.

Trata los changelogs como dispositivos de narración: enseñan a futuras lectoras y lectores por qué se tomaron decisiones y cómo el sistema continúa honrando su identidad Esencial.
---
Última modificación: 2025-11-17

🗳️ **¿Te fue útil este documento?**
- [ ] Sí, resolvió mi duda
- [ ] Más o menos
- [ ] No me ayudó

💬 [Deja tu feedback](https://github.com/scanalesespinoza/the-wise-tech/issues/new?template=feedback.yml)

---

