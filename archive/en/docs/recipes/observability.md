# Recipe: Observable Services by Default

**Purpose.** Guarantee that every change leaves a trace that accelerates detection, triage, and learning.

**Applies when.** Adding new functionality, touching infrastructure, or adjusting logging/metrics/tracing configurations.

**Do this.**
1. Define success, warning, and failure signals before implementing the change.
2. Emit structured logs with consistent keys (service name, operation, correlation ID, user context).
3. Publish metrics with clear naming (`team.domain.metric`) and attach SLO/SLA thresholds.
4. Instrument distributed traces and propagate correlation headers across services.
5. Create or update dashboards and alerts that surface the new signals.

**Avoid this.**
- Writing ad-hoc print/debug statements that never reach centralized logging.
- Emitting high-cardinality labels without justification.
- Adding telemetry without updating runbooks or alert routing.

**Local example.** Review `infra/observability/telemetry.json` for the canonical field names and logging format.

**Related principles.** [Embrace observable behaviors](../principles-essential.md), [Automate repeatable learning](../principles-essential.md).
