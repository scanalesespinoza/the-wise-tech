# Internal Restructure Plan

## Context
The current documentation and governance layout has grown organically, which makes it difficult for teams to align their work with the Wise Tech philosophy of pragmatic innovation, transparency, and sustainable velocity. This plan captures the "why" behind the upcoming restructuring so stakeholders can understand how it reinforces our core beliefs and gives us a shared frame of reference.

## Target Information Architecture
```
docs/
├── pillars/               # Principle, Capability, Control explainers and PCC taxonomy map
│   ├── index.md
│   ├── principles/
│   ├── capabilities/
│   └── controls/
├── guides/                # End-to-end playbooks (delivery, audits, onboarding, communications)
│   └── *.md
├── patterns/              # Repeatable architecture, process, and tooling patterns
│   └── *.md
├── specs/                 # Formal specifications, requirements, and RFCs tied to PCC controls
│   └── *.md
├── examples/              # Canonical examples, walkthroughs, and worked scenarios
│   └── *.md
├── tools/                 # Automation references, CLI docs, and integration how-tos
│   └── *.md
└── audit/                 # Evidence templates, checklists, and regulator-facing briefs
    └── *.md
```
- `docs/pillars/index.md` acts as the canonical PCC landing page and should include deep links to principles, capabilities, and control catalogs.
- `docs/guides` consolidates current onboarding, operations, and governance guides under a single navigation entry, organized by lifecycle stage.
- `docs/patterns`, `docs/specs`, and `docs/examples` isolate reusable knowledge artifacts so they can evolve at different cadences without creating navigation noise.
- `docs/tools` houses references to scripts, CLIs, dashboards, and integration instructions, clarifying how automation supports PCC controls.
- `docs/audit` remains the authoritative home for regulator-facing evidence, reports, and quarterly assurance packages.

## Archivo actual → destino futuro → comentarios
| Archivo/directorio actual | Destino futuro | Comentarios |
| --- | --- | --- |
| `docs/index.md` | `docs/pillars/index.md` (symlink or include) | Mantiene la narrativa de aterrizaje, pero resalta la taxonomía PCC; se preserva la URL raíz. |
| `docs/navigation.md` | `docs/guides/navigation.md` + referencias en `mkdocs.yml` | Se migra el contenido a guías; `mkdocs.yml` debe apuntar a la nueva ruta. |
| `docs/onboarding-landing.md` | `docs/guides/onboarding.md` | Se reescribe como guía integral vinculada a ejemplos y herramientas. |
| `docs/visual-navigation.md` | `docs/pillars/principles/visual-navigation.md` | Pasa a ser un principio con visualizaciones; debe enlazar a patrones relacionados. |
| `docs/ux-redesign-preview.md` | `docs/examples/ux-redesign.md` | Queda como caso de estudio dentro de ejemplos. |
| `docs/es/` | `docs/guides/es/` + `docs/examples/es/` | Se redistribuye el contenido traducido manteniendo la jerarquía local. |
| `operations/` y `governance/` notas clave | `docs/specs/` | Las especificaciones formales se centralizan aquí con numeración PCC. |
| `audit/` (fuera de `docs/`) | `docs/audit/` | Mover reportes públicos relevantes para alinearse con MkDocs y facilitar publicación. |

## Rutas estables y redirecciones
- `docs/index.md` y `docs/es/index.md` **deben** permanecer como páginas raíz publicadas en GitHub Pages para evitar enlaces rotos externos. Usaremos includes o front matter para apuntar a `docs/pillars/index.md` y `docs/guides/es/index.md` sin cambiar las rutas públicas.
- `docs/navigation.md` recibe una redirección permanente hacia `docs/pillars/index.md` (para navegación conceptual) y una segunda redirección contextual desde `mkdocs.yml` hacia `docs/guides/navigation.md` para menús laterales.
- `docs/onboarding-landing.md` redirige a `docs/guides/onboarding.md` y conservará un alias especificado en `mkdocs.yml` (`onboarding/landing/`).
- `docs/visual-navigation.md` necesita alias `visual-nav/` porque existen referencias en comunicaciones externas.
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
