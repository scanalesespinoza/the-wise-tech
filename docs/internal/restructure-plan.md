# Internal Restructure Plan

## Context
The current documentation and governance layout has grown organically, which makes it difficult for teams to align their work with the Wise Tech philosophy of pragmatic innovation, transparency, and sustainable velocity. This plan captures the "why" behind the upcoming restructuring so stakeholders can understand how it reinforces our core beliefs and gives us a shared frame of reference.

## Target Information Architecture
```
docs/
├── overview/
│   ├── vision.md            # Versión publicada del manifiesto
│   └── principles.md        # Referencia rápida a Wise Tech Principles
├── pillars/
│   ├── resilience.md
│   ├── performance.md
│   ├── data-and-observability.md
│   └── zero-trust.md        # Pilar transversal
├── guides/
│   ├── component-behavior-contract.md
│   ├── designing-resilient-components.md
│   ├── designing-for-performance.md
│   └── instrumenting-components.md
├── patterns/
│   ├── pattern-error-handling-and-cleanup.md
│   ├── pattern-degraded-mode.md
│   ├── pattern-backpressure-and-queues.md
│   └── pattern-metrics-and-events.md
├── specs/
│   ├── component-behavior-contract.schema.md
│   ├── resilience-requirements.md
│   ├── performance-requirements.md
│   └── data-and-observability-requirements.md
├── examples/
│   ├── service-resilience-basic/
│   ├── service-performance-limits/
│   └── service-observability/
├── tools/
│   └── wise-tech-linter/
└── audit/
    ├── checklists/
    ├── personas/
    ├── scenarios/
    ├── impacts/
    └── component-contract.yaml
```
- `docs/overview` conserva la experiencia de aterrizaje y enlaza a la visión sin romper URLs existentes.
- `docs/pillars` se transforma en la referencia oficial de PCC, incluyendo Zero Trust como principio transversal.
- `docs/guides` y `docs/patterns` sirven para bajar los pilares a pasos accionables y plantillas reutilizables.
- `docs/specs` concentra requisitos formales y contratos; será la fuente para linters y automatizaciones.
- `examples/` y `tools/` muestran cómo se implementan y validan los pilares en código.
- `audit/` mantiene checklists, contratos y reportes necesarios para revisiones regulatorias.

## Archivo actual → destino futuro → comentarios
| Archivo/directorio actual | Destino futuro | Comentarios |
| --- | --- | --- |
| `docs/index.md` | `docs/overview/vision.md` (include desde la raíz) | Mantiene la URL pública y apunta al manifiesto actualizado. |
| `README.md#vision-and-purpose` | `docs/overview/vision.md` | El README referencia la nueva ubicación, manteniendo anclas existentes. |
| `docs/navigation.md` | `docs/guides/component-behavior-contract.md` + `docs/pillars/*.md` | El contenido conceptual migra a pilares/guías; `navigation.md` queda como redirección. |
| `docs/onboarding-landing.md` | `docs/guides/designing-resilient-components.md` | La experiencia de onboarding arranca desde la guía PCC enlazando patrones y ejemplos. |
| `docs/ux-redesign-preview.md` | `docs/examples/ux-redesign.md` | Caso de estudio conectado desde `docs/patterns/pattern-metrics-and-events.md`. |
| `operations/` y `governance/` notas clave | `docs/specs/*.md` | Los requisitos se reescriben con lenguaje MUST/SHOULD/MAY y alimentan linters/auditorías. |
| `audit-report.*` | `audit/` (rutas estables) | Se mantiene fuera de `docs/` para preservar integraciones automáticas. |


## Rutas estables y redirecciones
- `docs/index.md` y `docs/es/index.md` **deben** permanecer como páginas raíz publicadas en GitHub Pages para evitar enlaces rotos. El contenido se incluirá desde `docs/overview/vision.md` y `docs/overview/principles.md` sin cambiar las rutas públicas.
- `docs/navigation.md` se convierte en un alias hacia `docs/pillars/resilience.md` y `docs/guides/component-behavior-contract.md`; `mkdocs.yml` deberá exponer ambas rutas para que el menú legacy no se rompa.
- `docs/onboarding-landing.md` redirigirá a `docs/guides/designing-resilient-components.md` y mantendrá alias `onboarding/landing/` en `mkdocs.yml`.
- Los casos de estudio como `docs/ux-redesign-preview.md` mantendrán alias (`visual-nav/`, `ux-preview/`) cuando migren a `docs/examples/`.
- `audit-report.md` y `audit-report.json` seguirán publicándose bajo `/audit/` usando rutas estables `audit/report.md` y `audit/report.json` para asegurar compatibilidad con integraciones automáticas.

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

## Execution Checklist
Use this living checklist to confirm the restructure is complete before requesting final approval:

- [ ] **Pilares documentados.** Cada principio, capacidad y control cuenta con una página actualizada en `docs/pillars/` enlazando al resto del árbol.
- [ ] **Guía del contrato.** Existe una guía explícita que describe acuerdos de entrega y expectativas entre equipos en `docs/guides/`.
- [ ] **Especificación formal.** Los requisitos de gobernanza migran a `docs/specs/` con numeración PCC y lenguaje MUST/SHOULD/MAY.
- [ ] **Ejemplos vivos.** Se publican casos prácticos en `docs/examples/` y se integran con las guías correspondientes.
- [ ] **Navegación actualizada.** `docs/navigation.md`, `mkdocs.yml` y cualquier índice relacionado reflejan la nueva arquitectura.
- [ ] **Experiencia legacy intacta.** Se mantienen alias/redirecciones y verificaciones manuales para garantizar que los flujos existentes de usuarios o integraciones no se rompan.

## Joint Review Before Merge
- Convocar una revisión conjunta entre responsables de producto, seguridad, cumplimiento y operaciones **antes del merge**.
- Usar la checklist anterior como agenda, marcando cada ítem solo cuando exista evidencia vinculada (enlaces o capturas de navegación).
- Registrar hallazgos o deudas en `docs/internal/restructure-plan.md` para que sirvan como insumo de la siguiente iteración.

## Próxima Iteración
1. **Automatizar validaciones.** Instrumentar scripts o jobs que verifiquen la checklist (p. ej., lint de enlaces, verificación de alias y presencia de PCC IDs) dentro de `scripts/` o `tools/`.
2. **Integrar en CI.** Conectar las validaciones anteriores al pipeline principal para bloquear merges que no cumplan con los criterios mínimos.
3. **Monitoreo continuo.** Añadir reportes recurrentes (mensuales) en `audit/` que muestren el estado del cumplimiento y cualquier desviación detectada automáticamente.
