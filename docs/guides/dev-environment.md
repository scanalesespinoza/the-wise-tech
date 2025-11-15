---
title: "Dev environment — devcontainer, pre-commit y just"
tags: ["quickstart","developers","platform-engineers","dx"]
---
# Dev environment — rápido
## Opciones
- **Codespaces/containers**: abre en GitHub Codespaces o `Dev Containers` en VS Code.
- **Local**: `pip install pre-commit ruff` y `pre-commit install`.

## Componentes del entorno
- [`dev/`](https://github.com/scanalesespinoza/the-wise-tech/tree/main/dev) — docker compose para OTEL collector, Jaeger y servicios auxiliares.
- [`.devcontainer/`](https://github.com/scanalesespinoza/the-wise-tech/tree/main/.devcontainer) — definición de contenedor para Codespaces o VS Code.
- [`scripts/`](https://github.com/scanalesespinoza/the-wise-tech/tree/main/scripts) — utilidades para validaciones (`validate-resilience.py`, `check-links.py`, etc.).
- [`justfile`](https://github.com/scanalesespinoza/the-wise-tech/blob/main/justfile) / [`Makefile`](https://github.com/scanalesespinoza/the-wise-tech/blob/main/Makefile) — comandos espejo para flujos rápidos.

## Primeros 5 minutos
1) `just install` o `make install`
2) `pre-commit install`
3) `just docs` y abre `http://127.0.0.1:8000`
4) `just ci` (equivalente a `make ci`)

## Hooks incluidos
- `ruff` (lint/format), `markdownlint`, `yamllint`
- Verificador de **enlaces internos** y **front-matter/See also** en docs

## Consejos
- Commits pequeños; ejecuta `just fmt && just lint`.
- Si usas Codespaces, ya viene todo preinstalado.

## See also
- [Quickstart](./quickstart.md)
- [Content Style Guide](./content-style-guide.md)
- [Telemetry (Minimum)](./telemetry-minima.md)
