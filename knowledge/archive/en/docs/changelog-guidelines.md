> **Propósito:** Dar contexto accionable sobre Narrative Changelog Guidelines dentro de The Wise Tech.
> **Audiencia:** Equipos y perfiles interesados en las bases de conocimiento y lineamientos del programa.
> **Uso recomendado:** Consulta este documento cuando necesites aplicar o compartir detalles de Narrative Changelog Guidelines.
> **Estado:** Activo.

# Narrative Changelog Guidelines

A changelog entry should explain more than the code diff. Use this guide to craft updates that make releases understandable to engineers, stakeholders, and support teams.

## Structure
1. **Title** – Summarize the value delivered in plain language.
2. **What changed** – 3–5 bullets referencing impacted modules, APIs, or infrastructure.
3. **Why it matters** – Describe the user or business outcome and which [Essential Principles](principles-essential.md) were reinforced.
4. **Risks/Mitigations** – Note breaking changes, migration steps, feature flags, or monitoring plans.
5. **Evidence** – Link to tests, dashboards, or incident follow-ups demonstrating readiness.
6. **Next steps** – Call out upcoming work or learning loops triggered by this release.

## Practices
- Keep entries short but rich in context (200–300 words max).
- Cross-link to relevant [recipes](recipes/README.md), onboarding assets, or ADRs.
- Use consistent tags (e.g., `#observability`, `#resilience`) to improve searchability.
- Encourage AI assistants to draft the initial summary, then refine for accuracy and tone.
- Store the changelog alongside release artifacts so it becomes part of operational evidence.

## Checklist before publishing
- [ ] Reviewed by at least one product or support stakeholder.
- [ ] Linked in the pull request or release ticket.
- [ ] Mentions follow-up tasks or metrics that will be tracked post-release.
- [ ] Translation mirrored in the Spanish changelog if applicable.

Treat changelogs as storytelling devices: they teach future readers why decisions were made and how the system continues to honor its Essential identity.

---

---
¿Te fue útil este documento?
[ ] Sí  [ ] Algo  [ ] No
Deja feedback [aquí](https://github.com/scanalesespinoza/the-wise-tech/issues/new?template=feedback.yml)
---
