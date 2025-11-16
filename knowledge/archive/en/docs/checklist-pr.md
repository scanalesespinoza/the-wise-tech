<!-- metadata
para_quien: Equipos y contribuidores que consultan "Pull Request Checklist (Essential + Operational)" en The Wise Tech.
objetivo: Proporcionar un contexto accionable sobre pull request checklist (essential + operational).
cuando_usar: Recurre a este documento cuando necesites aplicar o compartir detalles de pull request checklist (essential + operational).
estado: active
-->

# Pull Request Checklist (Essential + Operational)

Use this living checklist to validate every change before requesting a review. Pair it with the PR template in `.github/PULL_REQUEST_TEMPLATE.md`.

## Essential Alignment
- [ ] Linked to at least one [Essential Principle](principles-essential.md) in the description.
- [ ] Boundaries respected (no cross-domain leaks, explicit contracts updated).
- [ ] Telemetry added or confirmed (structured logs, metrics, traces).
- [ ] Failure modes handled (timeouts, retries, graceful degradation).
- [ ] Secrets and personal data protected (no hard-coded credentials, secure storage confirmed).

## Operational Quality
- [ ] Tests updated (unit, integration, contract as applicable) with clear evidence.
- [ ] Observability signals include correlation identifiers for troubleshooting.
- [ ] Security checks (SAST/SCA) pass locally or include justification for follow-up.
- [ ] Performance impact reviewed for critical paths (latency, resource usage).
- [ ] Documentation updated (recipes, onboarding, glossary) or confirmed not needed.

## Impact and Knowledge Sharing
- [ ] Added changelog/narrative note explaining value delivered.
- [ ] Tagged mentors or subject matter experts for critical domains.
- [ ] Provided onboarding hints (files to read, commands to run) in the PR description.
- [ ] Captured any new patterns or anti-patterns in the [recipe catalog](recipes/README.md).

Keep the checklist short enough to remain actionable. When the team learns about new recurring issues, evolve the checklist collaboratively and document the rationale.

---

🗳️ **¿Te fue útil este documento?**
- [ ] Sí, resolvió mi duda
- [ ] Más o menos, necesito más contexto
- [ ] No me ayudó

📢 [Abre un feedback aquí](https://github.com/scanalesespinoza/the-wise-tech/issues/new?template=feedback.yml)

---
