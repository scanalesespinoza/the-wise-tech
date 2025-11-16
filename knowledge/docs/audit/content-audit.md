<!-- metadata
para_quien: Equipos y contribuidores que consultan "Content Audit" en The Wise Tech.
objetivo: Proporcionar un contexto accionable sobre content audit.
cuando_usar: Recurre a este documento cuando necesites aplicar o compartir detalles de content audit.
estado: active
-->

# Content Audit

## Repository Snapshot (pre-restructure)
- Top-level bilingual trees under `en/` and `es/` mirror each other partially but have diverged.
- Legacy knowledge bases located in `guides/`, `systems/platform/`, `experience/scenarios/`, and `docs/wise-tech/teams/` without a unifying index.
- Multiple contribution guides (`governance/CONTRIBUTING.md`, `governance/CONTRIBUTING.es.md`, duplicates under `knowledge/docs/`).
- Automation scripts exist under `operations/scripts/`, but there is no documentation lint to validate Markdown links.

## Duplicates and Redundancies
- English and Spanish folders contain duplicated guides (e.g., `en/docs/principles-essential.md` and `es/docs/principles-essential.md`).
- Contribution guides duplicated at root and under `docs/`.
- Scenario documentation duplicated between `experience/scenarios/payments/README.md` and language folders.

**Action:** Consolidate the bilingual content into a single neutral information architecture inside `knowledge/docs/`, with language-specific assets archived. Replace redundant contribution guides with a single navigable source under `governance/`.

## Dispersed or Orphaned Content
- ASCII diagrams (`extracted-architecting-open-source-teams.md`, `wise-tech-readme-addendum-teams.md`) live at repo root without category placement.
- ADRs exist under `knowledge/adr/` but lack a central pointer from navigation.
- `systems/infra/`, `systems/platform/`, and `experience/scenarios/` folders contain valuable practices but are hard to discover from README.

**Action:** Create thematic sections (`principles/`, `personas/`, `guides/`, `playbooks/`, `experience/scenarios/`, `diagrams/`) with `_index.md` entry points that link to these assets or summarize migration plans.

## Broken or Risky Relative Links
- Root `README.md` references `en/README.md` and `es/README.md`; the upcoming restructure will invalidate them.
- Several documents inside `en/docs` link to `../glossary.md` style paths that will break once files are relocated.

**Action:** After moving files, update every relative link to point to the new structure and provide redirects where necessary.

## Naming and Structure Gaps
- Mixed casing and underscores across filenames (`operations/mkdocs.yml`, `wise-tech-alignment-architecting-teams.md`).
- Section directories lack `_index.md` or `README.md` summaries.

**Action:** Enforce hyphenated filenames and add section indexes with quick navigation plus "See also" references.

## Automation and Validation
- No automated check for Markdown link validity or filename conventions in CI.

**Action:** Introduce `operations/scripts/check-links.py` and una acción `docs-and-links` en GitHub. Optionally add a lints job to guard filename rules.

## Next Steps
1. Migrate valuable content into the new `docs/` structure.
2. Archive bilingual tree remnants with clear signposts.
3. Rewrite root `README.md` as a one-page navigation surface with role-based journeys.
4. Update contribution templates and CHANGELOG to reflect the restructure.

## Post-restructure Notes
- Contenido bilingüe legado movido a `knowledge/archive/` para referencia histórica.
- Diagramas y configuraciones previas agrupados en `knowledge/archive/legacy-diagrams/` y `knowledge/archive/config/`.
- Los nuevos índices dentro de `docs/` orientan la navegación y reemplazan referencias anteriores.
- Puentes heredados viven en `docs/en/` y `docs/es/` para mantener enlaces estables durante la transición.

---

🗳️ **¿Te fue útil este documento?**
- [ ] Sí, resolvió mi duda
- [ ] Más o menos, necesito más contexto
- [ ] No me ayudó

📢 [Abre un feedback aquí](https://github.com/scanalesespinoza/the-wise-tech/issues/new?template=feedback.yml)

---
