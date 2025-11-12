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

## Checklist antes de publicar
- [ ] Revisado por al menos una persona de producto o soporte.
- [ ] Enlazado en el pull request o ticket de release.
- [ ] Menciona tareas de seguimiento o métricas que se monitorearán post-release.
- [ ] Traducción reflejada en el changelog en inglés si aplica.

Trata los changelogs como dispositivos de narración: enseñan a futuras lectoras y lectores por qué se tomaron decisiones y cómo el sistema continúa honrando su identidad Esencial.
