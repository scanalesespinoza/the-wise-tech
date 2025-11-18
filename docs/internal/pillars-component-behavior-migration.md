# Pillars Component Behavior Restructure Execution Guide

## Working Branch and Scope Guardrails
- **Branch name:** `feature/pillars-component-behavior`.
- **Purpose:** Implement the migration described in `docs/internal/restructure-plan.md` for all component-behavior artifacts (principles, capabilities, and controls) without regressing navigation or published URLs.
- **Branch hygiene:**
  1. Branch off the latest `main` after pulling upstream changes.
  2. Keep commits scoped ("create pillars routes", "move legacy navigation content", "update mkdocs nav"), which simplifies reviews and rollback.
  3. Rebase frequently to avoid drifting from other restructure work.

## Migration Steps
1. **Create/verify the new directory tree.**
   - Ensure `docs/pillars/index.md`, `docs/pillars/principles/`, `docs/pillars/capabilities/`, and `docs/pillars/controls/` exist.
   - Create placeholder index files in each directory if missing so MkDocs can render navigation nodes immediately.
2. **Define new routes in `mkdocs.yml`.**
   - Under `nav`, add a top-level entry for "Pilares PCC" that points to `pillars/index.md`.
   - Nest subsections for `Principios`, `Capacidades`, and `Controles`, referencing the corresponding directories/files.
   - Keep `Inicio: index.md` as the first entry to preserve the public landing URL.
3. **Copy or move legacy content.**
   - Move conceptual introductions from `docs/navigation.md` to `docs/guides/navigation.md`.
   - Relocate principle-focused narratives (e.g., `docs/visual-navigation.md`) to `docs/pillars/principles/` and rename them following `kebab-case`.
   - Shift onboarding-focused material from `docs/onboarding-landing.md` into `docs/guides/onboarding.md`, linking back to the relevant pillars and capabilities.
4. **Update cross-links and embeds.**
   - Within moved files, update relative links so they reference the new directory depth.
   - Audit the `docs/guides`, `docs/examples`, and `docs/specs` folders for any references to the moved pages and update them to the new routes.
5. **Adjust navigation helpers.**
   - Refresh `docs/navigation.md` so it becomes a short explainer pointing to `docs/pillars/index.md` and the reorganized guides.
   - Update any custom include or symlink that keeps `docs/index.md` aligned with `docs/pillars/index.md`.
6. **Content QA.**
   - Run `mkdocs serve` locally to verify navigation depth and breadcrumbs.
   - Confirm that Material for MkDocs search indexes the new locations.

## Preserving Key URLs and Redirect Strategy
1. **Use MkDocs Redirects plugin.**
   - Add the plugin to `mkdocs.yml`:
     ```yaml
     plugins:
       - redirects:
           redirect_maps:
             navigation.md: pillars/index.md
             onboarding-landing.md: guides/onboarding.md
             visual-navigation.md: pillars/principles/visual-navigation.md
     ```
   - This keeps legacy URLs alive for direct hits and SEO.
2. **Leverage front matter aliases for translated content.**
   - In files like `docs/es/index.md`, add:
     ```yaml
     ---
     title: Inicio
     aliases:
       - /es/onboarding/landing/
       - /es/visual-nav/
     ---
     ```
   - MkDocs Material passes these aliases to `mkdocs-redirects` when present, so they behave like permanent redirects.
3. **Stable audit endpoints.**
   - Keep `audit-report.md` and `audit-report.json` under `/audit/` by adding explicit nav entries:
     ```yaml
     nav:
       - Audit:
           - Reporte (MD): audit/audit-report.md
           - Reporte (JSON): audit/audit-report.json
     ```
4. **Documented exceptions.**
   - When a page must remain at the legacy route (e.g., `docs/index.md`), embed an include pointing to the new structure instead of moving the file. This keeps inbound links functioning while exposing the reorganized navigation.

## Pre-Merge Experience Checklist
Use this checklist before requesting review or merging `feature/pillars-component-behavior`:

- [ ] `mkdocs serve` renders without navigation errors or broken links.
- [ ] `Inicio` still loads legacy `index.md`, but its primary CTA targets `docs/pillars/index.md`.
- [ ] New `Pilares PCC` nav entry exposes Principles, Capabilities, and Controls pages with working breadcrumbs.
- [ ] Legacy URLs (`/navigation/`, `/visual-nav/`, `/onboarding/landing/`) redirect to the new destinations without 404s.
- [ ] All migrated content retains images, admonitions, and callouts (no missing assets or warnings in console output).
- [ ] Search index returns both legacy query terms and new taxonomy keywords.
- [ ] Accessibility review: headings remain sequential (no skipped levels) and navigation items have descriptive labels.
- [ ] Cross-links from Guides, Examples, and Specs resolve to the new pillar pages.
- [ ] Audit artifacts continue to be accessible under `/audit/` paths.
- [ ] README or contributor docs reference the new branch instructions if necessary.
