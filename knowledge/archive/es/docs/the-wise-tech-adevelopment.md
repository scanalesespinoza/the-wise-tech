# The Wise Tech + aDevelopment

## Capitalizar experiencia desde el código, acelerar con IA y recuperar la mentoría

**Objetivo:** no volver a empezar de cero. Construir con ventaja desde lo aprendido, usando el repositorio como fuente de verdad y la IA como acelerador del aprendizaje y la calidad.

## 1. Contexto y propósito

En equipos modernos, la rotación y la escasez de mentoría dificultan capturar y transmitir el conocimiento crítico. The Wise Tech propone una práctica para acumular, curar y operacionalizar la experiencia técnica; aDevelopment (AI-Augmented Development) la potencia transformando el código y su histórico en *insights* accionables.

**Propósito**

- Convertir experiencia + tecnología en una base ventajosa.
- Hacer viable la transferencia de conocimiento en la realidad actual (onboarding ágil, *handovers* claros, menos fricción).
- Acelerar la maduración y la maestría al ritmo que la organización requiere.

## 2. Los tres contextos de The Wise Tech

### 2.1 Esencial (Identidad del sistema)
Principios y comportamientos no negociables que definen cómo debe existir el sistema (p. ej., idempotencia, consistencia eventual, límites de dominio, políticas de resiliencia).

### 2.2 Operativo (Evolución con calidad)
Prácticas, automatizaciones y estándares que permiten crecer sin degradar (p. ej., revisión de PR, *contract testing*, SLOs, observabilidad, seguridad).

### 2.3 Impacto (Personas y resultados)
Cómo lo construido reduce fricción, habilita a los equipos y mejora resultados (p. ej., *onboarding* guiado, *handover* sin trauma, retroalimentación continua).

### IA en los tres contextos

- Detecta violaciones a principios (Esencial) desde el PR.
- Genera documentos, ejemplos y *checklists* desde el código (Operativo).
- Ofrece “mentoring aumentado” y guías contextuales (Impacto).

## 3. aDevelopment: del repositorio al aprendizaje activo

### El código como fuente de verdad

Patrones, decisiones, *trade-offs* y convenciones viven en los repositorios, *commits*, *issues* y PR.

La IA ayuda a minar patrones y generar conocimiento reusable (resúmenes, guías, *recipes*).

### Mentoría aumentada (*on-demand*)

- *Pairing* virtual: preguntas contextuales sobre el archivo/PR.
- Revisiones consistentes: *bots* que enseñan y corrigen con ejemplos del propio repositorio.
- *Onboarding* guiado: recorridos autoexplicativos (tour de módulos, *endpoints*, diagramas).

### Sistemas que aprenden

- Cada sprint deja huella: se promueven patrones efectivos y se retiran antipatrones.
- El conocimiento permanece aunque cambien las personas.

## 4. Prácticas recomendadas (aplicables hoy)

### 4.1 “Knowledge Mining” del repositorio

- Resumen de PR con contexto (qué, por qué, riesgos, compatibilidad).
- Catálogo de patrones/*recipes* (por lenguaje, módulo, capa).
- *Changelog* narrativo por *release* (evitar solo listas técnicas, incluir impacto).
- Extracto de decisiones (ADR) desde discusiones de PR e *issues*.

#### Prompt base para PR (plantilla)

- **Rol:** Revisor técnico-mentoring.
- **Entrada:** *Diff* del PR + título + descripción + etiquetas.
- **Tareas:**
  1. Explica el cambio en 5-7 viñetas (qué/por qué).
  2. Riesgos y compatibilidad (rompiente/no rompiente).
  3. Patrones aplicados y antipatrones detectados (con enlaces locales a *recipes*).
  4. Tests y observabilidad: ¿qué falta? ¿qué evidencia recomienda?
  5. Breve guía de *onboarding* para entender este cambio (archivos clave y flujo).
- **Salida:** Markdown listo para comentar en el PR.

### 4.2 *Checklists* vivos en PR (Esencial + Operativo)

Ancla las revisiones con la [Checklist de Pull Request](checklist-pr.md) para mantener visibles las preocupaciones esenciales, operativas y de impacto en cada cambio.

- Principios esenciales (idempotencia, límites de dominio, errores manejados).
- Seguridad (secretos, dependencias, escaneo SCA).
- Observabilidad (logs, métricas, trazas con *correlation id*).
- Tests (unidad, contrato, *e2e* si aplica).
- *Performance* y resiliencia (*circuit breakers*, *timeouts*).

#### Ejemplo de *checklist* (fragmento)

- [ ] Manejo de errores explícito y no genérico.
- [ ] *Timeouts* y reintentos definidos en llamadas externas.
- [ ] Logs estructurados + *correlation id*.
- [ ] Tests unitarios para casos felices y bordes relevantes.
- [ ] *Contract tests* para APIs públicas modificadas.
- [ ] Sin secretos en código (ver escaneo SCA).

### 4.3 Documentación desde el código (*DocOps*)

Usa el script `.github/scripts/generate_module_readmes.py` para mantener sincronizados el [Catálogo de Recetas](recipes/README.md) y los [Recursos de Onboarding](onboarding/README.md) cuando agregues nuevo contenido.

- Generar README por módulo automáticamente.
- Construir glosario técnico vivo a partir de comentarios/*docstrings*.
- Publicar diagramas (p. ej., PlantUML/Mermaid) derivados del repositorio.

## 5. Flujo de trabajo recomendado

1. Diseño ligero guiado por Esencial (decisiones clave + límites).
2. Implementación con *recipes* y ejemplos del catálogo.
3. PR con *checklist*, resumen IA y *mentoring hints*.
4. Integración continua (build, tests, seguridad, generación de documentación).
5. *Release* con *changelog* narrativo (qué aporta, cómo migrar).
6. *Retro* y *mining*: promover patrones efectivos al catálogo.

## 6. Métricas (KPIs) para maduración

- *Onboarding Lead Time*: días desde ingreso hasta primer PR aceptado.
- % PR con *checklist* completo y violaciones esenciales detectadas.
- Cobertura de *recipes*/patrones referenciados por PR.
- Tiempo de revisión y retrabajo por PR.
- Incidentes post-*release* relacionados a decisiones no documentadas.
- Tiempo de *handover* entre equipos/turnos.

## 7. *Roadmap* de adopción (4 semanas)

### Semana 1 – Fundaciones

- Definir principios Esenciales (5-8 máx.).
- Crear *checklist* de PR y carpeta `knowledge/docs/recipes/`.
- Habilitar GitHub Actions básicos (build, test, SCA).

### Semana 2 – IA en PR y *DocOps*

- *Bot* de resumen de PR + *mentoring hints*.
- Generación de README por módulo y glosario.
- Primeras *recipes* (errores, observabilidad, pruebas).

### Semana 3 – Calidad y patrones

- *Enforce* de *checklists* (fallar si falta lo crítico).
- *Contract tests* y evidencia de SLOs/errores.
- “*Mining*” del histórico para descubrir patrones.

### Semana 4 – Operacionalización

- *Changelog* narrativo automático.
- *Onboarding tour* (docs + enlaces + rutas de aprendizaje).
- Retrospectiva y promoción de patrones al catálogo.

## 8. Ejemplos de automatización (GitHub Actions)

> Ajusta nombres/paths según el repositorio.

### 8.1 Resumen de PR con *hints* (ejemplo simplificado)

`.github/workflows/pr-summarizer.yml`

```yaml
name: PR Summarizer
on:
  pull_request:
    types: [opened, synchronize, reopened]
permissions:
  contents: read
  pull-requests: write
jobs:
  summarize:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Get PR diff
        id: diff
        run: |
          git fetch origin ${{ github.base_ref }} --depth=1
          git diff origin/${{ github.base_ref }}...HEAD > pr.diff || true
          echo "diff<<EOF" >> $GITHUB_OUTPUT
          sed -e 's/`/`/g' pr.diff >> $GITHUB_OUTPUT
          echo "EOF" >> $GITHUB_OUTPUT
      - name: Generate summary (LLM)
        id: ai
        env:
          PR_TITLE: ${{ github.event.pull_request.title }}
          PR_BODY:  ${{ github.event.pull_request.body }}
          DIFF:     ${{ steps.diff.outputs.diff }}
        run: |
          python - << 'PY'
# Aquí invoca tu proveedor de IA (ej. API interna) con el prompt base del repo.
# Imprime el Markdown final en stdout para que el siguiente paso lo comente.
print("# Resumen del PR\n\n- Qué/por qué...\n- Riesgos...\n- Patrones...\n- Tests/Observabilidad...")
PY
      - name: Comment summary
        uses: marocchino/sticky-pull-request-comment@v2
        with:
          header: pr-summary
          message: ${{ steps.ai.outputs.stdout || 'Resumen no disponible' }}
```

### 8.2 *Enforce* de *checklist* esencial

`.github/workflows/pr-checklist.yml`

```yaml
name: PR Checklist Enforcer
on:
  pull_request:
    types: [opened, synchronize, reopened, edited]
jobs:
  enforce:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Ensure checklist is present
        run: |
          FILE=".github/PULL_REQUEST_TEMPLATE.md"
          if [ ! -f "$FILE" ]; then
            echo "Falta PULL_REQUEST_TEMPLATE.md con checklist esencial." >&2
            exit 1
          fi
          echo "Checklist esencial presente."
```

### 8.3 Generación de documentación desde código

`.github/workflows/doc-gen.yml`

```yaml
name: DocGen
on:
  push:
    branches: [ main ]
jobs:
  generate-docs:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Build module READMEs
        run: |
          python .github/scripts/generate_module_readmes.py
      - name: Commit docs
        uses: stefanzweifel/git-auto-commit-action@v5
        with:
          commit_message: "docs: actualizar READMEs de módulos y glosario"
          file_pattern: "knowledge/docs/** README.md **/README.md"
```

## 9. Estructura sugerida en `knowledge/docs/`

```text
knowledge/docs/
  the-wise-tech-adevelopment.md   # este documento
  principles-essential.md         # 5-8 principios no negociables (ver ejemplo en el repo)
  checklist-pr.md                 # checklist vivo de PR (ver ejemplo en el repo)
  recipes/
    errors-handling.md            # ejemplo poblado
    observability.md              # ejemplo poblado
    testing-contracts.md          # ejemplo poblado
    resiliency.md                 # ejemplo poblado
  onboarding/
    tour.md                       # ejemplo poblado
    learning-paths.md             # ejemplo poblado
  glossary.md                     # ejemplo poblado
  changelog-guidelines.md         # ejemplo poblado
```

## 10. Roles y responsabilidades

- **Arquitectura/Tech Leads:** custodiar el Esencial, promover patrones y revisar métricas.
- **Equipo de Plataforma:** automatización, CI/CD, seguridad, generación de documentación.
- **Equipos de Producto:** aplicar *recipes*, enriquecer catálogo, mejorar *checklists*.
- **Mentores (o mentores aumentados):** curar ejemplos, responder dudas codificándolas.

## 11. Antipatrones comunes

- *Checklist* por cumplir: marcar sin verificar evidencias.
- Documentación paralela al código que se desincroniza.
- *Bots* de IA que no referencian el repositorio local (respuestas genéricas).
- Cambiar principios esenciales con frecuencia (pérdida de identidad).
- *Recipes* sin ejemplos reales del repositorio.

## 12. FAQ

**¿Necesitamos mucho *tooling* nuevo?**

No. Comienza con GitHub Actions y scripts simples. La clave es proceso + curaduría.

**¿Qué pasa si la IA se equivoca?**

Diseña el flujo como asistencia, no autoridad. Las personas deciden; la IA acelera.

**¿Cómo medimos el avance?**

Con KPIs de *onboarding*, revisión, cobertura de *recipes*, violaciones esenciales y retrabajo post-*release*.

## 13. Licencia y contribución

- Sigue las guías de contribución del repositorio.
- Toda *recipe* debe incluir: propósito, cuándo usar, cuándo no, pasos, ejemplo local y enlaces internos.
- Las propuestas de cambio al Esencial se tratan como ADR (*Architecture Decision Record*).

## 14. Próximos pasos

- Publicar `principles-essential.md` (5-8 reglas claras).
- Activar PR Summarizer y Checklist Enforcer.
- Crear 3-4 *recipes* semilla con ejemplos reales.
- Habilitar `onboarding/tour.md` y enlazar desde el README.
- Cerrar el primer ciclo con métricas y *retro* para promover patrones.

---

Con **The Wise Tech + aDevelopment**, cada cambio enseña. El conocimiento deja de ser efímero y se convierte en ventaja compuesta.
