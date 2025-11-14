# Personas para auditoría LLM

## 1. Maintainer estratega
- **Contexto**: Responsable de mantener la coherencia de la filosofía Wise Tech y priorizar mejoras.
- **Objetivos**:
  - Identificar brechas entre principios estratégicos y la implementación en docs, escenarios y código.
  - Detectar riesgos que afecten la narrativa bilingüe o la experiencia de contribución descrita en `docs/guides/editorial-workflow.md`.
- **Preguntas frecuentes**:
  - ¿El roadmap documentado en `docs/roadmap/roadmap.md` se refleja en los assets técnicos (por ejemplo `platform/` y `scenarios/`)?
  - ¿Los recursos críticos están actualizados y referenciados desde el README principal?

## 2. Contribuidor externo
- **Contexto**: Persona que llega desde la comunidad y quiere aportar a escenarios o guías sin contexto previo.
- **Objetivos**:
  - Evaluar si la guía de contribución (`docs/guides/contribution-guide.md`) entrega pasos accionables para la primera PR.
  - Verificar que existan ejemplos claros en `docs/labs/` y `docs/playbooks/` que faciliten el onboarding.
- **Preguntas frecuentes**:
  - ¿La estructura de navegación descrita en `README.md` coincide con el árbol real de archivos?
  - ¿Los enlaces críticos pasan los chequeos automáticos (`make docs`, `scripts/check-links.py`)?

## 3. Ingeniera de plataforma enfocada en resiliencia
- **Contexto**: Necesita validar que los artefactos de plataforma (SLOs, políticas, runbooks) son accionables.
- **Objetivos**:
  - Revisar la cobertura de resiliencia en `platform/policies/resilience.yml` y la alineación con `docs/guides/resilience-policies.md`.
  - Confirmar que los escenarios de pagos (`scenarios/payments/`) tienen contratos y pruebas listas para ejecutarse.
- **Preguntas frecuentes**:
  - ¿Los runbooks bilingües reflejan los KPIs descritos en `docs/playbooks/platform-playbook.md`?
  - ¿Hay instrucciones claras para reproducir incidentes simulados y medir MTTR?

## 4. Analista de experiencia de aprendizaje
- **Contexto**: Evalúa si las rutas 30/60/90 y laboratorios generan impacto en adopción.
- **Objetivos**:
  - Corroborar que cada persona (`docs/personas/`) esté conectada con rutas y KPIs pertinentes.
  - Revisar que los labs (`docs/labs/`) especifiquen métricas y entregables accionables.
- **Preguntas frecuentes**:
  - ¿Las rutas incluyen "Primeros 60 minutos" y métricas de seguimiento claras?
  - ¿Existen gaps entre la versión en inglés y español (`en/` vs `es/`) que afecten la experiencia?
