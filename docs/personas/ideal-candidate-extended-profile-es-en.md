# Ideal Candidate — Extended Profile (ES/EN)

## Español

### Contexto y motivaciones
- Quiere **acelerar entregas** sin sacrificar calidad.
- Prefiere **pasos reproducibles** (Makefile/justfile), documentación breve y ejemplos.
- Valora la **resiliencia observable** (tests/CI, paridad, SLOs) y el **feedback humano**.

### Habilidades y comportamientos
- **Simplicidad**: propone rutas cortas (Quickstart, First Win).
- **Resiliencia**: añade tests, valida paridad bilingüe, sugiere políticas de tiempo/reintentos.
- **Capitalización del conocimiento**: documenta decisiones (ADR), añade snippets reutilizables.
- **Propósito humano**: escribe para personas (guías claras), cuida el tono y la inclusión.
- **Conexión humana**: usa plantillas de feedback (Issues/PR), referenciando aprendizajes de usuarios/soporte.

### Anti-patrones a evitar
- Cambios grandes y no revisables; tooling excesivo.
- Documentación larga sin ejemplos; ignorar señales (tests rojos, paridad rota).
- Mezclar roles sin aclarar impacto (Dev ↔ Platform ↔ Consumer).

### Entregables típicos del candidato ideal
- 1 **PR pequeño** con: test(s) + doc(s) + snippet + nota/ADR.
- 1 mejora de **DX/Operabilidad** (comando único, check de enlaces, runbook).
- 1 aportación a **navegación/one-page** (mapa ASCII o “Recommended by interest”).

### 30–60–90 días (ejemplo)
- **30**: 2–3 PRs pequeños; Quickstart y Makefile maduros; links verificados.
- **60**: playbooks por rol con **first wins** y **KPIs**; CI quality + links en verde.
- **90**: SLOs y resiliencia básicos operativos; postmortems y checklist de PR consolidados.

### Métricas de éxito
- TTFC y lead time a la baja; tasa de merges estable.
- Disminución de enlaces rotos/errores de paridad.
- Aumento de contribuciones con snippet+doc+test.

---

## English

### Context & drivers
- Wants to **speed up delivery** without losing quality.
- Prefers **reproducible steps** (Makefile/justfile), short docs, and examples.
- Values **observable resilience** (tests/CI, parity, SLOs) and **human feedback**.

### Skills & behaviors
- **Simplicity**: creates short paths (Quickstart, First Win).
- **Resilience**: adds tests, enforces bilingual parity, suggests timeouts/retries.
- **Knowledge capitalization**: documents decisions (ADR), shares reusable snippets.
- **Human purpose**: writes for people (clear guides), inclusive tone.
- **Human connection**: uses feedback templates (Issues/PR) referencing user/support learnings.

### Anti-patterns to avoid
- Big-bang changes; excessive tooling.
- Long docs without examples; ignoring signals (failing tests/parity).
- Blurring roles without clarifying impact (Dev ↔ Platform ↔ Consumer).

### Typical deliverables
- 1 **small PR**: test(s) + doc(s) + snippet + note/ADR.
- 1 **DX/Operability** improvement (one-liner, link checker, runbook).
- 1 **navigation/one-page** enhancement (ASCII map or “Recommended by interest”).

### 30–60–90 days (sample)
- **30**: 2–3 small PRs; improved Quickstart & Makefile; links verified.
- **60**: role playbooks with **first wins** and **KPIs**; CI quality + links green.
- **90**: basic SLOs & resilience in place; postmortems and PR checklist embedded.

### Success metrics
- Lower TTFC and lead time; healthy merge rate.
- Fewer broken links/parity errors.
- More contributions including snippet+doc+test.
