<!-- metadata
para_quien: Equipos y contribuidores que consultan "The Hadron Pattern for Microservices" en The Wise Tech.
objetivo: Proporcionar un contexto accionable sobre the hadron pattern for microservices.
cuando_usar: Recurre a este documento cuando necesites aplicar o compartir detalles de the hadron pattern for microservices.
estado: active
-->

# The Hadron Pattern for Microservices
**Source:** https://sergio-canales-e.medium.com/the-hadron-pattern-for-microservices-5f03fcb890fa  
**Author:** Sergio Canales Espinoza  
**Date:** 2023-12-27  
**Extraction:** structured-summary (faithful representation, no full copy)

## Central idea
The author uses a particle-physics analogy to describe a microservices pattern organized into quarks, hadrons, mesons, and baryons. Each category represents a specific role: individual services, collaborative clusters, coordinators, and interfaces. The goal is to visualize how to coordinate microservices to keep resilience and responsibility clear.

## Key points (bullet list)
- “Quarks” are individual microservices across deployment and functional layers.
- “Hadrons” group microservices that collaborate for higher-level goals.
- “Mesons” act as coordinators orchestrating discovery, recovery, and healing.
- “Baryons” expose or consume capabilities, offering clear interfaces.
- Understanding the analogy helps design modular, resilient architectures.

## Argument structure
1. Introduces the cosmic analogy and defines each layer of the pattern.
2. Explains the role of hadrons, mesons, and baryons across deployment and functionality.
3. Invites deeper conversation about microservice coordination.

## Relevant data/examples
- Referenced diagrams showing relationships among the elements.
- Emphasis on coordination services that detect, recover, and heal components.

## Limitations/scope
- Conceptual; needs complementary technical guides and tooling.
- Does not cover migration scenarios from monoliths or other topologies.

## Practical conclusion (≤120 words)
Adopting the pattern means distinguishing which services are building blocks, which coordinate, and which expose capabilities. Mapping responsibilities with the analogy improves resilience and operational clarity.

---

🗳️ **¿Te fue útil este documento?**
- [ ] Sí, resolvió mi duda
- [ ] Más o menos, necesito más contexto
- [ ] No me ayudó

📢 [Abre un feedback aquí](https://github.com/scanalesespinoza/the-wise-tech/issues/new?template=feedback.yml)

---
