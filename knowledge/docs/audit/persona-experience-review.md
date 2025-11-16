---
title: "Persona Experience Review"
tags: ["personas", "ux-research", "continuous-improvement"]
---
## Propósito
Enmarca cómo Persona Experience Review ayuda a mantener decisiones alineadas con The Wise Tech.

## Audiencia
Personas y equipos que necesitan una guía rápida sobre Persona Experience Review.

## Cuándo usarlo
Consúltalo cuando requieras referencias inmediatas para Persona Experience Review o debas compartir el enfoque con otros equipos.

> **Propósito:** Dar contexto accionable sobre Persona Experience Review dentro de The Wise Tech.
> **Audiencia:** Equipos y perfiles interesados en las bases de conocimiento y lineamientos del programa.
> **Uso recomendado:** Consulta este documento cuando necesites aplicar o compartir detalles de Persona Experience Review.
> **Estado:** Activo.


## Tabla de navegación

- [Resumen ejecutivo](#resumen-ejecutivo)
- [Personas, necesidades y mejoras](#personas-necesidades-y-mejoras)
- [Ventajas actuales y cómo potenciarlas](#ventajas-actuales-y-cmo-potenciarlas)
- [Cambios concretos sugeridos](#cambios-concretos-sugeridos)
- [Matriz rápida “Repo vs Personas”](#matriz-rpida-repo-vs-personas)
- [Checklist de validación continua](#checklist-de-validacin-continua)
- [Seguimiento y mejora continua](#seguimiento-y-mejora-continua)
- [Referencias rápidas](#referencias-rpidas)

# Persona Experience Review

Esta revisión actualiza la evaluación del repositorio **The Wise Tech** con base en diez personas realistas (20–50 años) que representan estudiantes, profesionales y entusiastas de la tecnología. Para cada persona se describen objetivos, tareas en el repositorio, dificultades, elementos que hoy funcionan, mejoras accionables alineadas con los principios Wise Tech (Simplicity, Continuous Improvement, Resilience, Knowledge Capitalization, Human Connection) y métricas de éxito que permiten validar la mejora.

## Resumen ejecutivo

- **Orientación inmediata:** la navegación inicial necesita un ancla inequívoca de “empieza aquí” que reduzca la fricción para quienes buscan un primer logro en <60 minutos.
- **Confianza operativa:** quienes ya contribuyen requieren guías rápidas para validar resiliencia, idempotencia y contratos de tests con ejemplos listos para reusar.
- **Capitalización del conocimiento:** plantillas, métricas y casos de estudio deben exponerse con rutas claras para que cada rol repliquen y compartan aprendizajes.
- **Conexión humana:** visibilizar historias de impacto, métricas de adopción y kits de mentoría refuerza la motivación comunitaria.
- **Mejora continua:** mantener listas de tareas “siempre vigentes” y checklists prescriptivas permite canalizar contribuciones incrementales.

## Personas, necesidades y mejoras

| Persona | Edad | Perfil | Objetivo | Qué intenta hacer en el repo | Dificultades | Qué ya funciona | Mejoras accionables (Principio) | Métrica de éxito |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Sofía | 22 | Estudiante de Ing. Informática | Aprender buenas prácticas “de cero a útil” | Seguir README, elegir ruta por rol y correr un lab | Exceso de rutas; duda por dónde empezar; miedo a romper algo | “Quickstart 5 pasos”, mapa ASCII y Labs 01–03 | Botón/anchor “Empieza aquí (30 min)” al inicio del README (Simplicity). Checklist “no te puedes equivocar” junto al Lab 01 (Human Connection). | Completa un lab en <60 min sin pedir ayuda |
| Benjamín | 24 | Bootcamp Full-Stack Jr. | Incorporar hábitos de CI/Docs y ganar confianza en PRs | `make -f operations/Makefile ci`, corregir enlaces, abrir PR pequeño | No identifica un “first win” claro | Checks de links/CI y secciones “Ops Signals” del template de PR | Lista fija “PR Ideas” con 10 mini-tareas vigentes (Continuous Improvement). Vista “Good first issue” permanente en README (Knowledge Capitalization). | Primer PR mergeado en <48 h |
| Camila | 27 | QA / Automation | Entender cómo testear escenarios (payments) y validar resiliencia | Ejecutar tests, `make resilience-check`, `make check-error-budget` | No ubica rápido los tests de contrato | Scripts de validación simples y targets Make claros | Carpeta `docs/testing/` con “Tipos de test: unit/contract/resilience” y ejemplos (Resilience). Matriz “qué test corre cada Make target” (Simplicity). | Añade 1 test de contrato y lo ve en CI |
| Diego | 30 | Dev Backend (Python/Node) | Acelerar entregas con patrones listos | Copiar snippet `correlation-id`, correr `make -f operations/Makefile telemetry-smoke` | Falta snippet de idempotency-key y retry útil | Snippet Python actual y guía de Telemetry mínima | `docs/snippets/*-idempotency-key.md` + ejemplo de retry/backoff (Resilience). “Before/After” breve para cada snippet (Knowledge Capitalization). | Integra 2 snippets en <30 min y mide p95 local |
| Valentina | 33 | Platform Engineer | Estandarizar checks de resiliencia/SLO en CI | `make slos`, `make resilience-check`, leer playbook de plataforma | Quiere matrices de fallo “qué pasa si falla X” | YAMLs de políticas y SLO con validadores | “Resilience matrices” (tabla mínima) + runbook de ejemplo (Resilience). Workflow opcional `platform-quality` con paths filtrados (Simplicity). | Un PR que modifica políticas falla si el YAML queda inconsistente |
| Rodrigo | 36 | SRE / On-call | Relacionar señales (p95, error-rate) con acciones | Ejecutar `make check-error-budget` (mock) y guías de SLO | Desea outputs prescriptivos “si fast-burn ⇒ freeze” | Políticas con acciones sugeridas | `operations/scripts/check-error-budget.py` imprime “acciones a ejecutar ahora” (Resilience). Plantilla de postmortem auto-linkeada al SLO modificado (Knowledge Capitalization). | Playbook de respuesta claro en <1 scroll |
| Andrea | 29 | PM técnica | Entender impacto humano y medición de valor | Leer Principles y “Feedback loops”, navegar Labs y Paths 30/60/90 | Métrica de adopción poco visible | Sección “Feedback Loops” y plantilla de issues | Página `docs/metrics/adoption-and-impact.md` con % PRs con feedback, TTFC, labs completados (Human Connection). “Caso de estudio 1 página” con antes/después (Knowledge Capitalization). | Prepara un pitch interno con datos en 15 min |
| Gabriel | 40 | Líder de comunidad / Mentor | Guiar a juniors en prácticas repetibles | Recomendar “Paths 30/60/90” + Labs | Falta kit de mentor para arranque grupal | Paths + labs con KPIs y plantillas | `docs/mentoring/group-kit.md`: agenda 90 min, roles, metas, checklist (Human Connection). Issue template “Cohort Progress” para seguimiento mensual (Continuous Improvement). | 5 mentees completan Lab 01 y comparten evidencia |
| Natalia | 45 | Arquitecta / Tech Lead | Estandarizar decisiones (ADRs) y documentar trade-offs | Buscar ejemplo de ADR corto ligado a principios | No hay plantilla ADR visible | Enfoque en principios y guía editorial | `docs/templates/adr-short.md` (1 página) + link en README (Knowledge Capitalization). “Árbol de decisiones” en `docs/architecture/` (Simplicity). | 1 ADR por cambio estructural |
| Mauro | 50 | Tech Enthusiast / Autodidacta | Aprender sin montar stack complejo | Leer enfoque, correr 1–2 comandos, ver resultados | Teme a Docker/OTEL y prefiere “sin instalar mucho” | `make -f operations/Makefile telemetry-smoke` y docs locales | “Modo ligero” (sin Docker): bloque con 3 comandos y qué ver (Simplicity). GIFs/short clips paso a paso (Human Connection). | Obtiene valor en 10–15 min sin contenedores |

## Ventajas actuales y cómo potenciarlas

- **Quickstart y Make targets claros.** Potenciar con un banner “Start here (30 min)” que ofrezca tres caminos: Solo lectura, Modo ligero, Stack completo (Principio: Simplicity).
- **Políticas + SLO como contrato.** Potenciar añadiendo “resilience matrices” y sugerencias automáticas en CLI (Principios: Resilience, Knowledge Capitalization).
- **Labs con KPIs y plantillas de evidencia.** Potenciar mediante un tablero “Labs completados” y una placa “MVP Labs finisher” (Principio: Continuous Improvement).
- **Feedback humano institucionalizado.** Potenciar con sección “Historias de usuarios” (casos 1 página) y KPI en `docs/metrics` (Principios: Human Connection, Knowledge Capitalization).

## Cambios concretos sugeridos

1. **README (parte superior).** Añadir botón/anchor “Empieza aquí (30 min)” que apunte a un bloque con las tres rutas de inicio (Simplicity).
2. **Nuevo contenido `docs/guides/getting-started-modes.md`.** Describir Modo ligero (sin Docker), Modo estándar (Make) y Modo stack (compose).
3. **Snippets nuevos.** Publicar `docs/snippets/<lang>-idempotency-key.md` con retry/backoff y comparativa Before/After.
4. **Guía de testing.** Crear `docs/testing/types-of-tests.md` con ejemplos unit/contract/resilience y matriz de Make targets.
5. **Métricas visibles.** Agregar `docs/metrics/adoption-and-impact.md` con KPIs: % PRs con feedback, TTFC, labs completados, errores de links/mes.
6. **Mentoría estructurada.** Incorporar `docs/mentoring/group-kit.md` y issue template “Cohort Progress”.
7. **Plantillas de decisiones.** Añadir `docs/templates/adr-short.md` y listado “árbol de decisiones” en `docs/architecture/`.
8. **CLI prescriptivo.** Actualizar `operations/scripts/check-error-budget.py` para imprimir acciones recomendadas inmediatas.
9. **Recorrido ligero.** Documentar bloque “Modo ligero” sin contenedores y acompañarlo con GIFs o clips cortos.

## Matriz rápida “Repo vs Personas”

| Persona | Tarea de validación | Resultado esperado |
| --- | --- | --- |
| Sofía | Seguir “Empieza aquí (30 min)” y completar Lab 01 | ✅ Evidencia en plantilla + 0 errores en `make resilience-check` |
| Benjamín | Ejecutar `make -f operations/Makefile ci` y abrir PR “PR Ideas #1” | ✅ PR mergeado con pequeño cambio en doc/test |
| Camila | Añadir 1 test de contrato y verlo en CI | ✅ `make -f operations/Makefile test` y workflow pasan |
| Diego | Integrar snippet de idempotency + retry | ✅ p95 estable y doc “Before/After” |
| Valentina | Cambiar un valor en resiliencia y validar fallo/éxito | ✅ CI bloquea YAML inválido |
| Rodrigo | Correr `make check-error-budget` y seguir acciones | ✅ Lista de acciones recomendadas impresa |
| Andrea | Construir “Adoption & Impact” en 15 min | ✅ Métricas visibles en docs |
| Gabriel | Coordinar sesión de mentoring con el “group-kit” | ✅ 5 evidencias de Lab 01 subidas |
| Natalia | Crear un ADR corto para un cambio de política | ✅ ADR registrado y enlazado en índice |
| Mauro | “Modo ligero”: ver valor sin Docker | ✅ Confianza ganada en 10–15 min |

## Checklist de validación continua

1. **Descubribilidad inicial.** ¿El README muestra “Empieza aquí (30 min)” de forma prominente? ¿Las tres rutas (ligero/estándar/stack) están claras?
2. **Primer éxito en <60 min.** Sofía y Mauro: ¿pueden completar un lab o smoke test sin bloqueos ni dependencias extra?
3. **Contribución guiada.** Benjamín y Camila: ¿existen “PR Ideas” y guía de tipos de test accesible desde el README?
4. **Operabilidad con contratos.** Valentina y Rodrigo: ¿los workflows fallan con políticas/SLO inválidos y recomiendan acciones prescriptivas?
5. **Aprendizaje capitalizado.** Andrea: ¿se generan y visualizan métricas de adopción en `docs/metrics`?
6. **Decisiones explícitas.** Natalia: ¿plantilla ADR y listado de ADRs están disponibles en `docs/architecture/`?
7. **Mentoría y comunidad.** Gabriel: ¿existe “group-kit” y issue template para seguimiento de cohortes?

## Seguimiento y mejora continua

- Crear issues etiquetados por principio para gestionar estas acciones y medir avances en tableros de adopción.
- Re-evaluar la experiencia cada trimestre, incorporando evidencia de métricas y feedback directo de contribuyentes.
- Comunicar resultados mediante historias de usuarios y casos de estudio de una página para reforzar la Conexión humana.

## Referencias rápidas

- [Wise Tech Principles](../principles/wise-tech-principles.md)
- [Quickstart Guide](../guides/quickstart.md)
- [Playbooks](../playbooks/)
- [Personas overview](../personas/_index.md)
---
Última modificación: 2025-11-16

🗳️ **¿Te fue útil este documento?**
- [ ] Sí, resolvió mi duda
- [ ] Más o menos
- [ ] No me ayudó

💬 [Deja tu feedback](https://github.com/scanalesespinoza/the-wise-tech/issues/new?template=feedback.yml)

---

