> **Propósito:** Dar contexto accionable sobre Evaluation scenarios dentro de The Wise Tech.
> **Audiencia:** Equipos y perfiles interesados en los escenarios y rutas de experiencia práctica.
> **Uso recomendado:** Consulta este documento cuando necesites aplicar o compartir detalles de Evaluation scenarios.
> **Estado:** Activo.

# Evaluation scenarios

## Scenario A — Documentation coherence
1. Review `README.md` and confirm that every referenced path points to an existing file.
2. Cross-check the README navigation with the MkDocs index (`operations/mkdocs.yml`).
3. Use `operations/scripts/validate-content-metadata.py` to confirm that guides declare complete metadata.
4. Report broken links or outdated sections based on the results of `make -f operations/Makefile docs`.

### Key signals
- Recent changes under `knowledge/docs/` related to navigation paths and guides.
- Presence of `TODO (parity)` notes indicating remaining translation work.

## Scenario B — Payments scenario quality
1. Read `experience/scenarios/payments/README.md` to understand the end-to-end flow.
2. Inspect `experience/scenarios/payments/contracts/` and `experience/scenarios/payments/systems/tests/` to validate case coverage.
3. Cross-reference lessons with the developer and platform playbooks (`knowledge/docs/playbooks/`).
4. Evaluate whether the KPIs defined in `knowledge/docs/labs/lab-01-resilience-basics.md` are reflected in the scenario scripts.

### Key signals
- Existence of reproducible scripts and simulated data.
- Examples that match the associated runbooks.

## Scenario C — Contribution experience
1. Follow `knowledge/docs/guides/contribution-guide.md` and `knowledge/docs/guides/editorial-workflow.md` to simulate a first contribution.
2. Validate that the templates in `.github/` capture both human feedback and operational signals.
3. Confirm that `make -f operations/Makefile ci` covers the same steps described in `README.md` and the GitHub Actions workflows.
4. Evaluate whether automation (`justfile`, `Makefile`) helps maintain consistency across the documentation set.

### Key signals
- Previous PR documentation in `knowledge/archive/` or `knowledge/adr/` to compare standards.
- Adoption metrics highlighted in `knowledge/docs/playbooks/developer-playbook.md`.

---

---
¿Te fue útil este documento?
[ ] Sí  [ ] Algo  [ ] No
Deja feedback [aquí](https://github.com/scanalesespinoza/the-wise-tech/issues/new?template=feedback.yml)
---
