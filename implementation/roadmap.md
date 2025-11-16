## Propósito
Enmarca cómo Implementation Roadmap ayuda a mantener decisiones alineadas con The Wise Tech.

## Audiencia
Personas y equipos que necesitan una guía rápida sobre Implementation Roadmap.

## Cuándo usarlo
Consúltalo cuando requieras referencias inmediatas para Implementation Roadmap o debas compartir el enfoque con otros equipos.

> **Propósito:** Dar contexto accionable sobre Implementation Roadmap dentro de The Wise Tech.
> **Audiencia:** Equipos y perfiles interesados en los planes y tableros de implementación.
> **Uso recomendado:** Consulta este documento cuando necesites aplicar o compartir detalles de Implementation Roadmap.
> **Estado:** Activo.


## Tabla de navegación

- [How to use this directory](#how-to-use-this-directory)
- [Current state (Release 01)](#current-state-release-01)
- [Stages to reach a consumable product](#stages-to-reach-a-consumable-product)
- [Immediate next steps](#immediate-next-steps)

# Implementation Roadmap

## How to use this directory
1. **Always read this roadmap before writing code.** It summarizes the current state of the repository and the next prioritized stage to turn it into a consumable product.
2. **Review the `implementation/releases/release-XX.md` files in chronological order.** Each release documents which part of the plan is already complete.
3. **When you finish a stage, create a new `release-XX.md` file.** Describe what changed, how it was validated, and what remains before moving on to the next phase.
4. **If the plan needs adjustments, edit this roadmap first and explain the change in the release that introduces it.** This keeps traceability for future Codex iterations.

## Current state (Release 01)
- The repository already functions as a **documentation hub** (see `README.md` and `knowledge/docs/index.md`), but there is still no packaged experience for external consumption beyond manual navigation.
- The automations (`operations/Makefile`, workflows in `.github/`) cover documentation quality and bilingual parity, which shows process maturity but not product delivery.
- There is no **release history** or executable artifacts that turn the guides into a service or demonstrator.

## Stages to reach a consumable product
### Stage 1 — "Operational discovery" (Release 01 ✅)
Objective: Document the real status of the repository, identify gaps between the documentation and a product experience, and define success criteria.
Key results:
- Inventory of existing assets (docs, scenarios, pipelines).
- Definition of the minimum backlog to package the content.
- Instructions for future iterations (this roadmap + `release-01`).

### Stage 2 — "Navigable MVP"
Objective: Turn the hub into a serviceable experience that guides the user step by step.
Approach:
- Package an initial flow (e.g., 30/60/90 Learning Path) as a demonstrative case inside `knowledge/docs/` and expose it from the landing page.
- Automate the verification of critical links (Quick start, Paths, Labs) in `operations/Makefile` to guarantee availability.
- Prepare a reproducible onboarding script (docs + script) in `operations/`.
Exit criteria:
- README and docs landing page redirect to the MVP flow.
- Single script or command that installs dependencies, serves docs, and validates priority links.
- Stage documentation in `release-02`.

### Stage 3 — "Operational experience"
Objective: Move from the documentary MVP to a product that combines documentation with automation.
Suggested workstreams:
- Integrate a practical scenario (e.g., `experience/scenarios/payments/`) with reproducible scripts.
- Add minimum telemetry (see `knowledge/docs/guides/telemetry-minima.md`) and shared dashboards.
- Publish KPI templates in `knowledge/docs/playbooks/` linked to the executable flow.
Exit criteria:
- Documented release (`release-03`).
- Operational demonstration (command or pipeline) validated in CI.

### Stage 4+ — "Open product"
Objective: Iterate on real feedback to offer an experience ready for adoption by teams.
- Version the content with semantic tags.
- Measure satisfaction/usage and adjust learning paths.
- Establish mentoring cycles documented in new releases.

## Immediate next steps
1. Prepare the Navigable MVP design (Stage 2) prioritizing the 30/60/90 flow for a single persona.
2. Define minimal automated checks that exercise that flow.
3. Open `release-02.md` when the MVP is complete and link any roadmap adjustments.
---
Última modificación: 2025-11-16

🗳️ **¿Te fue útil este documento?**
- [ ] Sí, resolvió mi duda
- [ ] Más o menos
- [ ] No me ayudó

💬 [Deja tu feedback](https://github.com/scanalesespinoza/the-wise-tech/issues/new?template=feedback.yml)

---

