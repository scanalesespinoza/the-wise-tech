# Component Behavior Contract Guide

The component behavior contract captures how a service upholds the resilience,
performance, and observability pillars. This guide explains when to create a
contract, how to keep it updated, and how to use the example projects.

## When to create a contract

Create (or update) a contract when:

1. Designing a new service or major capability.
2. Changing service-level objectives (SLOs) or revising a dependency strategy.
3. Responding to an incident where documentation gaps were discovered.

Contracts live next to the service code so owners can iterate on them during
normal development. The `specs/component-behavior-contract.schema.md` file
documents every required field.

## Drafting the YAML

1. Copy the template from the schema file.
2. Fill the `component`, `ownership`, and `environment` sections so stakeholders
   can contact the team quickly.
3. Define the three pillar blocks in `behavior`:
   - **Resilience** — availability targets, automated safeguards (circuit
     breakers, retries, graceful degradation), and validation cadence.
   - **Performance** — throughput limits, latency targets, and controls such as
     load-shedding or rate limiting.
   - **Observability** — telemetry coverage, alert routing, and validation steps
     (dashboards or runbooks).
4. Link evidence (dashboards, playbooks, chaos run reports) inside the
   `validation.artifacts` arrays.
5. Describe upstream dependencies and the integration contract for each entry.

## Keeping the contract useful

- Review the contract during every architecture/design review and release
  retrospective.
- Automate validation by referencing scheduled jobs (for example, `validation:
  cadence: weekly`).
- Store links to dashboards that highlight each objective; this ensures SREs can
  verify controls without digging through multiple systems.

## Example projects

The `examples/` directory contains minimal services that show how to tie real
controls to the contract:

- `service-resilience-basic` demonstrates dependency timeouts, retries, and a
  graceful fallback for a Tier-2 API.
- `service-performance-limits` showcases a sliding-window rate limiter and the
  contract entries that describe throughput guarantees.
- `service-observability` focuses on structured logging, tracing contexts, and
  alert routing metadata.

Each example ships with:

1. A `README.md` explaining the scenario, how to run the sample script, and what
   to look for in the console output.
2. A `behavior-contract.yaml` file that satisfies the schema.
3. A small Python module showing how the controls are implemented.

Use these directories as starting points when drafting a contract for your own
service. Copy the relevant sections, update the contact information, and tweak
objectives to match the new SLOs.
