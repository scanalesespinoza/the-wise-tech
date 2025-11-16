---
title: "Taxonomy — Tags permitidos"
tags: ["developers", "knowledge-capitalization", "paths"]
---
<!-- metadata
para_quien: Equipos y contribuidores que consultan "Taxonomy — Tags permitidos" en The Wise Tech.
objetivo: Proporcionar un contexto accionable sobre taxonomy — tags permitidos.
cuando_usar: Recurre a este documento cuando necesites aplicar o compartir detalles de taxonomy — tags permitidos.
estado: active
-->

# Taxonomy — Tags permitidos

## Por-qué-importa
Una taxonomía consistente hace que las rutas de aprendizaje y playbooks sean fáciles de filtrar y descubrir.

## Qué-harás
1. Elegir tags de roles y temas permitidos en cada página nueva.
2. Mantener "See also" con enlaces que refuercen la narrativa.
3. Automatizar validaciones mínimas desde el repositorio.

## Tags-permitidos
**Roles**: `consumers`, `developers`, `platform-engineers`  
**Temas**: `simplicity`, `resilience`, `knowledge-capitalization`, `human-connection`, `aDevelopment`, `observability`, `slo`, `playbooks`, `paths`, `labs`, `quickstart`, `principles`, `business-logic`, `distributed-systems`, `microservices`

### Principios-mandatorios para sistemas distribuidos
- **Límites claros de responsabilidad** → cada artefacto debe documentar cuál parte de la lógica de negocio protege y cómo se coordinan los límites del dominio.
- **Idempotencia y manejo de fallos** → describe reintentos, tolerancia a particiones y mecanismos de contención para evitar efectos colaterales.
- **Contratos verificables** → enlaza a pruebas o escenarios que reafirman cómo se cumplen los contratos entre servicios.
- **Observabilidad end-to-end** → exige tags que permitan rastrear trazas, métricas y logs desde la experiencia del usuario hasta la plataforma.
- **Backpressure y desacoplo** → documenta colas, políticas de carga y estrategias de degradación segura.

### Referencia microservicios
- Reusa los tags `distributed-systems` y `microservices` cuando conectes páginas con patrones como [The Hadron Pattern for Microservices — resumen EN](../knowledge/articles/the-hadron-pattern-for-microservices/the-hadron-pattern-for-microservices-summary-en.md) / [ES](../knowledge/articles/the-hadron-pattern-for-microservices/the-hadron-pattern-for-microservices-summary-es.md).
- Incluye en "See also" enlaces a laboratorios o escenarios que demuestren cómo esos principios aterrizan en microservicios y cargas de trabajo críticas.

## Front-matter-ejemplo
```yaml
---
title: "Page title"
tags: ["developers", "resilience"]
---
```

## Reglas-de-uso
- Incluye al menos un tag de roles o temas por página.
- Evita tags libres fuera del listado; solicita ampliaciones vía issue.
- Replica tags en traducciones espejo (`es/` y `en/`).

## See-also
- [Content-Style-Guide — Wise Tech](content-style-guide.md)
- [Editorial-Workflow — Propuesta→Draft→Review→Publish](editorial-workflow.md)
- [Versioning-Docs — Semver básico](versioning-docs.md)
- [Front-Matter Example](../snippets/front-matter-example.md)

---

🗳️ **¿Te fue útil este documento?**
- [ ] Sí, resolvió mi duda
- [ ] Más o menos, necesito más contexto
- [ ] No me ayudó

📢 [Abre un feedback aquí](https://github.com/scanalesespinoza/the-wise-tech/issues/new?template=feedback.yml)

---
