# Escenarios de evaluación

## Escenario A — Coherencia documental
1. Analiza `README.md` y verifica que todos los paths tengan archivos existentes.
2. Correlaciona la navegación del README con el índice de MkDocs (`operations/mkdocs.yml`).
3. Usa `operations/scripts/validate-content-metadata.py` para confirmar que las guías declaren metadatos completos.
4. Reporta enlaces rotos o secciones desactualizadas en función de los resultados de `make -f operations/Makefile docs`.

### Señales clave
- Últimos cambios en `knowledge/docs/` relacionados con rutas y guías.
- Presencia de notas `TODO (parity)` indicando deuda bilingüe.

## Escenario B — Calidad del escenario de pagos
1. Revisa `experience/scenarios/payments/README.md` para entender el flujo end-to-end.
2. Inspecciona `experience/scenarios/payments/contracts/` y `experience/scenarios/payments/systems/tests/` para validar cobertura de casos.
3. Cruza los aprendizajes con los playbooks de developers y platform (`knowledge/docs/playbooks/`).
4. Evalúa si los KPIs definidos en `knowledge/docs/labs/lab-01-resilience-basics.md` se reflejan en los scripts del escenario.

### Señales clave
- Existencia de scripts reproducibles y datos simulados.
- Ejemplos bilingües consistentes con los runbooks asociados.

## Escenario C — Experiencia de contribución
1. Sigue `knowledge/docs/guides/contribution-guide.md` y `knowledge/docs/guides/editorial-workflow.md` para simular la primera contribución.
2. Valida que las plantillas en `.github/` contemplen feedback humano y señales operacionales.
3. Comprueba que `make -f operations/Makefile ci` cubre los mismos pasos descritos en `README.md` y workflows de GitHub Actions.
4. Evalúa si la automatización (`justfile`, `Makefile`) ayuda a mantener paridad entre lenguajes.

### Señales clave
- Documentación de PRs previa en `knowledge/archive/` o `knowledge/adr/` para comparar estándares.
- Métricas de adopción presentes en `knowledge/docs/playbooks/developer-playbook.md`.
