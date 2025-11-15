# Recipe: Intentional Error Handling

**Purpose.** Provide consistent, user-friendly recovery paths while keeping telemetry actionable.

**Applies when.** You touch code that propagates exceptions across service boundaries or exposes messages to end users.

**Do this.**
1. Map expected failure modes and decide which ones deserve explicit handling vs. propagation.
2. Convert generic exceptions into domain-specific errors that carry remediation hints.
3. Log errors once with structured context (correlation ID, inputs, downstream dependencies) and emit metrics for alerting.
4. Return safe responses to clients (HTTP status + machine-readable code + human message).
5. Link the PR to runbooks or operational playbooks if manual intervention is required.

**Avoid this.**
- Swallowing exceptions silently or logging them without context.
- Returning stack traces or implementation details to consumers.
- Creating divergent error taxonomies across services.

**Local example.** See `experience/scenarios/payments/service/errors.py` for the canonical domain exceptions and how they map to API responses.

**Related principles.** [Respect the domain contract](../principles-essential.md), [Design for graceful failure](../principles-essential.md).
