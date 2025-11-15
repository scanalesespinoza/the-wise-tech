# The Wise Tech Approach: A Contrast with Traditional Complex Software Practices

## Traditional Complex Approach: CICD + DevOps + DevSecOps as Disconnected Chains

### CICD (Continuous Integration/Continuous Deployment)
- **Primary focus:** Automate how code is integrated, tested, and deployed.
- **Key challenges:**
  - Operates narrowly on pipeline mechanics without deep alignment to security, operations, or user experience.
  - Encourages rapid releases that may overlook broader organizational context.
  - Provides limited feedback loops for understanding quality or impact.

### DevOps
- **Primary focus:** Improve collaboration between development and operations to increase delivery speed.
- **Key challenges:**
  - Can devolve into another silo where speed is prioritized over sustainable quality.
  - Security and user feedback often arrive late, resulting in reactive fire-fighting.
  - Toolchain complexity raises cognitive load for engineers and increases friction.

### DevSecOps
- **Primary focus:** Embed security practices into DevOps workflows.
- **Key challenges:**
  - Frequently bolted onto existing processes, leading to fragmented responsibilities.
  - Security becomes a compliance checkbox instead of a shared mindset.
  - Disconnects between development, operations, and security produce blind spots and inefficiencies.

## The Wise Tech Approach: Integrated and End-to-End

### End-to-End Developer Process
- **Primary focus:** Developers own the lifecycle from design to deployment while championing quality, security, and user impact.
- **Key principles:**
  - **Process Improvement:** Apply lessons from previous work to continuously refine how we build and release.
  - **Knowledge Capitalization:** Partner with security, operations, and product to build collective intelligence instead of reinforcing silos.
  - **Resilience Behavior:** Engineer for graceful degradation, recovery paths, and long-term maintainability.

### End-to-End Platform Process
- **Primary focus:** Platform engineers craft resilient, scalable, user-aware systems.
- **Key principles:**
  - **System Resilience:** Design for failure, monitor continuously, and invest in proactive improvements.
  - **Scalability and Efficiency:** Grow with demand without sacrificing performance or environmental sustainability.
  - **User-Centric Design:** Ensure services and architecture enhance reliability, accessibility, and simplicity.

### Feedback Process Wrapped Around Technology Consumers
- **Primary focus:** Close the loop with the people who use the software and let their experiences guide evolution.
- **Key principles:**
  - **Purposeful Technology:** Validate that every change improves outcomes instead of complicating lives.
  - **Human Connection:** Measure how technology supports relationships and community well-being.
  - **Simplicity:** Reduce friction, eliminate unnecessary complexity, and clarify user journeys.

## Why It Matters
The Wise Tech approach replaces fragmented chains with a symbiotic system. Developers, platform engineers, and technology consumers share responsibility for quality, resilience, and human impact. When feedback flows freely, we build products that stay relevant, trustworthy, and genuinely helpful.

## Annex: Consistency Profiles & Replication Strategies

This annex translates distributed-system guardrails into Wise Tech’s incremental playbook. Each service declares its preferred **consistency profile** and **replication strategy** so that automation can verify the combination before code is merged or deployed.

### Decision Matrix

| Profile / Strategy | Primary guarantees | Compatible replication strategies | When to choose it | Watch-outs |
| --- | --- | --- | --- | --- |
| **Strict** | Near-serializable isolation, linearizable reads, deterministic writes | Primary-backup, Quorums | Financial flows, orders, global inventory updates | Latency contention, split-brain risk if membership falters |
| **Causal** | Preserves causal dependencies, monotonic reads, read-your-writes with session vectors | Active replication, Quorums | Collaborative experiences, user activity timelines | Clock management complexity when metadata is lost |
| **Eventual** | Convergence through policy-driven reconciliation and minimal latency | Active replication, Fan-out caches with TTL | Catalogs, content, aggregated metrics | Visible divergence without explicit idempotency and reconciliation |

### Implementation Guidelines

1. **Declarative consistency:** Services record their profile in `systems/platform/policies/consistency.yml`. The CI check in `systems/ci/consistency-check` matches the profile with access patterns and the declared replication approach.
2. **Client-centric guarantees:** Session middleware attaches vector-clock headers so mobile and web clients observe read-your-writes and monotonic reads even across replicas.
3. **Consistency vs. coherence:** Policies distinguish between dataset-level rules (consistency) and item-level caching (coherence). Cache TTLs must align with the selected profile to avoid stale reads.
4. **Controlled migrations:** Architectural Decision Records describe how to shift between profiles—e.g., from eventual to causal—using partition-aware blue/green rollouts and observability checkpoints.

### Operational Resilience Hooks

- **Replica catalog:** Primary-backup, active replication, and quorum-based policies are expressed in `experience/scenarios/payments/policies/resilience.yml`, each with automated validation for idempotency and shared state expectations.
- **Partial-failure drills:** CI scenarios within `systems/ci/resilience-lint` and `systems/ci/causality-test` simulate slow nodes, member loss, and retry storms to set expectations for graceful degradation.
- **Membership management:** The `guides/platform-playbook.md` walkthrough keeps heartbeats, timeouts, and group-event ordering in sync with the declared replication strategy.

### Quality Gates & Human Feedback

- **Automated checks:** Pull requests trigger consistency, resilience, and causality validations so that incompatible configurations are caught early.
- **Idempotency by contract:** Services opting into active replication must expose idempotency keys or verifiable side effects to survive retries.
- **Session continuity:** Support and UX flows read session vectors before responding when a user switches replicas, ensuring continuity.
- **Knowledge capture:** Issue and PR templates prompt teams to log consistency and replication decisions alongside user lessons, reinforcing organizational memory.
