# Personas para auditoría LLM

## 1. Maintainer estratega
- **Contexto**: Responsable de mantener la coherencia de la filosofía Wise Tech y priorizar mejoras.
- **Objetivos**:
  - Identificar brechas entre principios estratégicos y la implementación en docs, escenarios y código.
  - Detectar riesgos que afecten la narrativa bilingüe o la experiencia de contribución descrita en `knowledge/docs/guides/editorial-workflow.md`.
- **Preguntas frecuentes**:
  - ¿El roadmap documentado en `knowledge/docs/roadmap/roadmap.md` se refleja en los assets técnicos (por ejemplo `systems/platform/` y `experience/scenarios/`)?
  - ¿Los recursos críticos están actualizados y referenciados desde el README principal?

## 2. Contribuidor externo
- **Contexto**: Persona que llega desde la comunidad y quiere aportar a escenarios o guías sin contexto previo.
- **Objetivos**:
  - Evaluar si la guía de contribución (`knowledge/docs/guides/contribution-guide.md`) entrega pasos accionables para la primera PR.
  - Verificar que existan ejemplos claros en `knowledge/docs/labs/` y `knowledge/docs/playbooks/` que faciliten el onboarding.
- **Preguntas frecuentes**:
  - ¿La estructura de navegación descrita en `README.md` coincide con el árbol real de archivos?
  - ¿Los enlaces críticos pasan los chequeos automáticos (`make -f operations/Makefile docs`, `operations/scripts/check-links.py`)?

## 3. Ingeniera de plataforma enfocada en resiliencia
- **Contexto**: Necesita validar que los artefactos de plataforma (SLOs, políticas, runbooks) son accionables.
- **Objetivos**:
- Revisar la cobertura de resiliencia en `experience/scenarios/payments/policies/resilience.yml` y la alineación con `knowledge/docs/guides/resilience-policies.md`.
  - Confirmar que los escenarios de pagos (`experience/scenarios/payments/`) tienen contratos y pruebas listas para ejecutarse.
- **Preguntas frecuentes**:
  - ¿Los runbooks bilingües reflejan los KPIs descritos en `knowledge/docs/playbooks/platform-playbook.md`?
  - ¿Hay instrucciones claras para reproducir incidentes simulados y medir MTTR?

## 4. Analista de experiencia de aprendizaje
- **Contexto**: Evalúa si las rutas 30/60/90 y laboratorios generan impacto en adopción.
- **Objetivos**:
  - Corroborar que cada persona (`knowledge/docs/personas/`) esté conectada con rutas y KPIs pertinentes.
  - Revisar que los labs (`knowledge/docs/labs/`) especifiquen métricas y entregables accionables.
- **Preguntas frecuentes**:
  - ¿Las rutas incluyen "Primeros 60 minutos" y métricas de seguimiento claras?
  - ¿Existen gaps entre la versión en inglés y español (`en/` vs `es/`) que afecten la experiencia?
