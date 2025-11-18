# Component Behavior Contract Schema

The component behavior contract is a lightweight YAML document that codifies how a
service satisfies the resilience, performance, and observability pillars. Each
contract must follow the schema below so that tooling can validate the
information and automation can rely on the structure.

## Required top-level fields

| Field | Description |
| --- | --- |
| `version` | Semantic version for the schema understood by tooling. Use `1.0.0` for the current draft. |
| `component` | Basic identity for the service (name, domain, and a short description). |
| `ownership` | Contact information (team name, Slack channel, escalation path). |
| `environment` | Runtime and deployment metadata that helps correlate telemetry (tier, region, runtime, entrypoints). |
| `behavior` | Pillar-specific objectives, controls, and validation evidence. Must include `resilience`, `performance`, and `observability`. |
| `dependencies` | Optional list describing upstream services (name, dependency_type, criticality, integration contract). |

### `component`

```yaml
component:
  name: payments-core
  domain: checkout
  description: Stateless API that orchestrates payment processor calls.
```

### `ownership`

```yaml
ownership:
  team: pay-velocity
  service_slack: "#pay-velocity-alerts"
  oncall_schedule: "https://pagerduty.com/schedules/PAY-VELOCITY"
```

### `environment`

```yaml
environment:
  tier: tier-1
  runtime: python-3.12
  regions:
    - us-east-1
  entrypoints:
    - https://api.example.com/payments
```

### `behavior`

Each pillar contains an `objectives` array, a `controls` array, and a
`validation` block.

```yaml
behavior:
  resilience:
    objectives:
      - type: availability
        target: ">= 99.90% monthly"
        rationale: "Meets checkout OKRs"
    controls:
      - name: dependency-timeouts
        description: "Circuit breaker after 800 ms"
        automated: true
    validation:
      cadence: weekly
      last_run: 2024-05-01
      artifacts:
        - https://grafana.example.com/d/abc123
```

Use the same structure for `performance` (latency/throughput limits) and
`observability` (telemetry coverage and alerting). Additional optional keys such
as `open_questions` or `todo` can be nested inside each pillar but **must not
remove** `objectives`, `controls`, or `validation`.

### `dependencies`

```yaml
dependencies:
  - name: fraud-screener
    dependency_type: asynchronous
    criticality: high
    contract: https://git.example.com/contracts/fraud-screener
```

## YAML template

Use the following template when drafting a new contract:

```yaml
version: 1.0.0
component:
  name: <service name>
  domain: <capability area>
  description: <1-2 sentence summary>
ownership:
  team: <team name>
  service_slack: <#channel>
  oncall_schedule: <link>
environment:
  tier: <tier-1|tier-2|tier-3>
  runtime: <language/runtime>
  regions:
    - <primary region>
  entrypoints:
    - <public or internal endpoint>
behavior:
  resilience:
    objectives:
      - type: availability
        target: <target>
        rationale: <business reason>
    controls:
      - name: <control>
        description: <what enforces the objective>
        automated: <true|false>
    validation:
      cadence: <weekly|monthly|per-release>
      last_run: <YYYY-MM-DD>
      artifacts:
        - <dashboard or evidence link>
  performance:
    objectives: []
    controls: []
    validation:
      cadence: <cadence>
      last_run: <YYYY-MM-DD>
      artifacts: []
  observability:
    objectives: []
    controls: []
    validation:
      cadence: <cadence>
      last_run: <YYYY-MM-DD>
      artifacts: []
dependencies: []
```

Save the contract next to the service source (for example, inside the
repository's `docs/` or `runbooks/` folder) so reviewers can find it during
architecture reviews.
