# Upstream Changes

This log helps downstream repositories understand what changed in the original [The Wise Tech](https://github.com/scanalesespinoza/the-wise-tech) template so they can decide when to sync. Each section summarizes structural updates, new labs, routing/navigation tweaks, and auditing or governance adjustments.

## How to use this file
- Review the latest version before running `sync-check.sh` or merging upstream work.
- Capture the date when your fork last integrated the upstream version.
- Reference the "Structure & navigation" and "Audits & governance" subsections to identify manual steps after pulling updates.

---

## v1.2 — 2024-06-01
**Highlights**
- Improved parity scripts and telemetry smoke tests to speed up lab verification.
- Added upstream synchronization helpers (`sync-check.sh`, scheduled GitHub Action) for template-based forks.

**Structure & navigation**
- Introduced `UPSTREAM_CHANGES.md` with curated release notes.
- README now displays a "Based on The Wise Tech" badge and a direct link to upstream changes.

**Labs & learning routes**
- Documented maintenance workflow for existing labs; no new labs shipped in this cut but all references were refreshed.
- Clarified how Learning Path 30/60/90 links map to docs after the reorganization.

**Audits & governance**
- Added optional automation to notify downstream forks about upstream releases.
- Reinforced audit trail by documenting sync expectations for forks using the template.

## v1.1 — 2024-05-15
**Highlights**
- Expanded observability labs with new telemetry exercises.
- Consolidated governance artifacts to simplify contribution review.

**Structure & navigation**
- Reworked `knowledge/docs/labs/` to include bilingual cues and cross-links in each lab file.
- Updated navigation map within `README.md` and MkDocs navigation entries to reflect renamed guides.

**Labs & learning routes**
- Lab 02 (Observability Minimum) now bundles OTLP walkthroughs and recommended dashboards.
- Learning paths gained explicit "First 60 minutes" action lists for each persona.

**Audits & governance**
- `governance/` received a refreshed decision log plus guidance for postmortems.
- Added parity checks across Spanish/English docs in the auditing scripts.

## v1.0 — 2024-04-01
**Highlights**
- Initial public release of The Wise Tech template with documentation, labs, and governance assets.

**Structure & navigation**
- Established the root layout: `knowledge/`, `experience/`, `systems/`, and `operations/`.
- Added Quick Start instructions plus Makefile/Justfile automation references.

**Labs & learning routes**
- Published Labs 01–03 with bilingual walkthroughs and KPI templates.
- Released Learning Paths (30/60/90) for Consumers, Developers, and Platform Engineers.

**Audits & governance**
- Shipped baseline auditing datasets (`audit-report`, `experience/scenarios/payments/` scripts).
- Introduced governance guardrails with contribution templates and style guides.
