<!-- metadata
para_quien: Equipos y contribuidores que consultan "Recipe: Resilient Service Patterns" en The Wise Tech.
objetivo: Proporcionar un contexto accionable sobre recipe: resilient service patterns.
cuando_usar: Recurre a este documento cuando necesites aplicar o compartir detalles de recipe: resilient service patterns.
estado: active
-->

# Recipe: Resilient Service Patterns

**Purpose.** Maintain availability and predictable degradation under stress or dependency failure.

**Applies when.** You integrate with third-party services, add network calls, or modify infrastructure resiliency settings.

**Do this.**
1. Identify critical dependencies and categorize them (tolerate vs. fail fast vs. bulkhead isolation).
2. Configure timeouts, retries with backoff, and circuit breakers per dependency.
3. Provide fallbacks that deliver minimal viable value (cached data, queued work, partial responses).
4. Load test failure scenarios and capture evidence in the PR description.
5. Document recovery procedures and ensure observability signals cover the new protections.

**Avoid this.**
- Infinite retries or large retry bursts that amplify outages.
- Treating all dependencies with the same resiliency policy.
- Shipping without validating how clients react to degraded behavior.

**Local example.** Examine `systems/infra/resilience/policies.yml` for baseline timeout and retry configurations per dependency tier.

**Related principles.** [Design for graceful failure](../principles-essential.md), [Protect human data and trust](../principles-essential.md).

---

🗳️ **¿Te fue útil este documento?**
- [ ] Sí, resolvió mi duda
- [ ] Más o menos, necesito más contexto
- [ ] No me ayudó

📢 [Abre un feedback aquí](https://github.com/scanalesespinoza/the-wise-tech/issues/new?template=feedback.yml)

---
