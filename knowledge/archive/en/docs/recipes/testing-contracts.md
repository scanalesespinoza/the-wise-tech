> **Propósito:** Dar contexto accionable sobre Recipe: Contract Testing for Stable Integrations dentro de The Wise Tech.
> **Audiencia:** Equipos y perfiles interesados en las bases de conocimiento y lineamientos del programa.
> **Uso recomendado:** Consulta este documento cuando necesites aplicar o compartir detalles de Recipe: Contract Testing for Stable Integrations.
> **Estado:** Activo.

# Recipe: Contract Testing for Stable Integrations

**Purpose.** Prevent regressions across service boundaries by codifying expectations between producers and consumers.

**Applies when.** Building or modifying APIs, message schemas, or event streams consumed by other teams or systems.

**Do this.**
1. Document the contract (fields, types, optionality, semantic meaning) and link it from the PR.
2. Implement consumer-driven contract tests that run in CI and validate provider changes.
3. Version contracts explicitly and describe migration paths for breaking changes.
4. Automate schema publication (e.g., upload to registry, share via package) as part of the release pipeline.
5. Monitor contract usage to detect unused endpoints and stale consumers.

**Avoid this.**
- Relying only on integration environments to catch breaking changes.
- Deploying without notifying consumers about required updates.
- Allowing multiple undocumented contract variants to coexist.

**Local example.** Inspect `experience/scenarios/payments/contracts/payments/v2` for Pact files and the README that explains expected behaviors.

**Related principles.** [Respect the domain contract](../principles-essential.md), [Bias toward maintainable simplicity](../principles-essential.md).

---

---
¿Te fue útil este documento?
[ ] Sí  [ ] Algo  [ ] No
Deja feedback [aquí](https://github.com/scanalesespinoza/the-wise-tech/issues/new?template=feedback.yml)
---
