---
title: "CI overview"
tags: ["ci", "automation"]
---
# CI overview

Los workflows viven en `.github/workflows/`. Usa esta tabla para saber qué valida cada uno y cuándo se ejecuta.

| Workflow | Cuándo corre | Pasos principales |
| --- | --- | --- |
| `quality` | Push y pull request a `main` | `make -f operations/Makefile ci`, `make -f operations/Makefile resilience-check`, `make -f operations/Makefile slos`, `make -f operations/Makefile check-error-budget`. |
| `docs-and-links` | Cambios en Markdown, `knowledge/docs/` u `operations/mkdocs.yml` (push/PR) | Construye MkDocs con `--strict`, valida enlaces internos y front-matter. |
| `pre-commit` | Push y PR | Ejecuta `pre-commit run --all-files` (incluye `ruff`, `markdownlint`, `yamllint`). |
| `gitleaks` | Push y PR | Escanea secretos usando `gitleaks` con la allowlist en `systems/ci/gitleaks-allowlist.toml`. |
| `audit` | Push y PR con cambios en `experience/audit/`, documentación o workflows | Corre `python operations/scripts/audit-evaluator.py` para evaluar cobertura de evidencias y métricas. |
| `knowledge-validate` | PR con cambios en `knowledge/docs/knowledge/` o la herramienta asociada | Instala dependencias de dev y ejecuta `python operations/scripts/validate-knowledge.py`. |
| `pr-feedback-check` | PR abiertos/editados | Analiza el cuerpo del PR y valida que se incluyan referencias a feedback humano. |
| `PR Checklist Enforcer` | PR abiertos/editados | Verifica que el cuerpo del PR contenga los ítems esenciales del checklist. |
| `PR Summarizer` | PR abiertos/sincronizados | Genera un resumen vía webhook (si está configurado) con contexto del diff. |
| `Doc Generation` | Push a `main` o manual (`workflow_dispatch`) | Ejecuta `.github/scripts/generate_module_readmes.py` y auto-commitea si hay cambios en `knowledge/docs/en/docs` o `knowledge/docs/es/docs`. |

## See also
- [Dev environment — devcontainer, pre-commit y just](../guides/dev-environment.md)
- [.github/workflows/](../../../.github/workflows)
- [operations/scripts/](../../../operations/scripts/)
