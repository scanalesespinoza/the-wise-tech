# Contributing Guide (English)

Thank you for investing in The Wise Tech knowledge base. This repository mirrors every artifact in English and Spanish, so please keep both versions aligned.

## Workflow Overview
1. Update the English document or asset first.
2. Reflect the change in the Spanish counterpart with equivalent structure and intent.
3. Run `.github/scripts/generate_module_readmes.py` when you add recipes or onboarding guides.
4. Open a pull request using the template and complete the checklist.
5. Tag mentors or subject matter experts for Essential principle updates.

## Translation Expectations
- Preserve headings, callouts, and links so the navigation stays symmetrical.
- Prefer neutral Spanish that is inclusive and accessible to Latin America and Spain.
- Document idioms or terminology in `en/docs/glossary.md` and `es/docs/glossary.md`.

## Documentation Types
- **Essential:** [`en/docs/principles-essential.md`](en/docs/principles-essential.md)
- **Checklists:** [`en/docs/checklist-pr.md`](en/docs/checklist-pr.md)
- **Recipes:** `en/docs/recipes/*.md`
- **Onboarding:** `en/docs/onboarding/*.md`
- **Narrative changelog:** [`en/docs/changelog-guidelines.md`](en/docs/changelog-guidelines.md)

## Automation
- GitHub Actions enforce the presence of the checklist template and prepare PR summaries when a webhook is configured.
- `Doc Generation` workflow keeps recipe/onboarding catalogs up to date.
- Reference the workflow files under `.github/workflows/` to adapt automations to your organization.

## Review Criteria
- Essential principles referenced in the PR description and respected in the diff.
- Tests, observability, and security implications addressed or justified.
- Documentation updated or explicitly deferred with an issue link.
- Spanish translation reviewed by a bilingual peer when possible.

Please also read the [Código de Contribución en Español](CONTRIBUTING.es.md) if you prefer guidance in Spanish.
