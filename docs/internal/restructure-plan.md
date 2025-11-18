# Internal Restructure Plan

## Context
The current documentation and governance layout has grown organically, which makes it difficult for teams to align their work with the Wise Tech philosophy of pragmatic innovation, transparency, and sustainable velocity. This plan captures the "why" behind the upcoming restructuring so stakeholders can understand how it reinforces our core beliefs and gives us a shared frame of reference.

## Why Restructure
1. **Clarity of intent.** By mapping every artifact to a Principle–Capability–Control (PCC) taxonomy we make it obvious how day-to-day decisions connect to company principles such as customer empathy, security-first thinking, and responsible automation.
2. **Faster onboarding and audits.** Streamlined navigation means engineers, auditors, and operations can find authoritative sources in minutes instead of hours, reducing duplication and audit churn.
3. **Sustainable governance.** A predictable structure lets us evolve controls without rewriting entire playbooks, preserving Wise Tech's preference for small, iterative adjustments rather than large yearly overhauls.
4. **Embedded feedback loops.** The new layout will bake in checkpoints for product, security, and compliance reviews so we can keep learning while we build—mirroring the Wise Tech belief that every system should improve with usage.

## PCC Taxonomy and Sub-Pillars
- **Principles (P).** Immutable statements that express what Wise Tech stands for (e.g., Pragmatic Security, Empathetic Automation, Operational Excellence).
- **Capabilities (C).** Cross-functional competencies that turn principles into practice (e.g., Secure Delivery, Human-Centered Insights, Platform Reliability).
- **Controls (C).** Concrete guardrails and processes owned by specific teams (e.g., Deployment Reviews, Telemetry Quality Gates, Disaster Recovery Drills).

Each capability MAY declare sub-pillars to capture nuances without fragmenting the top-level taxonomy. Examples:
- Secure Delivery → *Pipeline Hygiene*, *Runtime Observability*, *Zero Trust Enforcement*.
- Human-Centered Insights → *Research Ops*, *Accessibility Signals*, *Voice-of-Customer Feedback*.

## Requirements Language
To keep expectations unambiguous, requirements tied to controls will use RFC 2119 style keywords:
- **MUST** for non-negotiable actions tied to regulatory or existential risks.
- **SHOULD** for strong recommendations where deviations require documented rationale.
- **MAY** for optional practices that teams can adopt when capacity or context allows.

This shared vocabulary ensures teams interpret intent consistently across product, security, and compliance reviews.

## Zero Trust as a Transversal Principle
Stakeholders agreed that Zero Trust is not a standalone control but a transversal principle influencing every PCC layer:
- Principles: Pragmatic Security explicitly references continuous verification.
- Capabilities: Secure Delivery and Platform Reliability incorporate identity-aware pipelines and just-in-time access.
- Controls: Every control that deals with access, data movement, or service connectivity MUST document how Zero Trust assumptions are enforced.

This approach guarantees that Zero Trust remains visible in executive reviews while staying actionable for implementers.

## Next Steps
1. Socialize this summary with product, security, compliance, and operations leads to confirm shared understanding.
2. Update navigation artifacts (e.g., `docs/navigation.md`) to reflect the PCC taxonomy once sign-off occurs.
3. Apply the MUST/SHOULD/MAY language when rewriting individual control documents.
4. Schedule quarterly retrospectives to ensure the restructure continues to embody Wise Tech's philosophy of transparent, iterative governance.
