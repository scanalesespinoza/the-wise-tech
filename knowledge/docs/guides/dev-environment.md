---
title: "Dev environment — devcontainer, pre-commit y just"
tags: ["quickstart","developers","platform-engineers","dx"]
---
## Propósito
Enmarca cómo Dev environment — rápido ayuda a mantener decisiones alineadas con The Wise Tech.

## Audiencia
Personas y equipos que necesitan una guía rápida sobre Dev environment — rápido.

## Cuándo usarlo
Consúltalo cuando requieras referencias inmediatas para Dev environment — rápido o debas compartir el enfoque con otros equipos.

> **Propósito:** Dar contexto accionable sobre Dev environment — devcontainer, pre-commit y just dentro de The Wise Tech.
> **Audiencia:** Equipos y perfiles interesados en las bases de conocimiento y lineamientos del programa.
> **Uso recomendado:** Consulta este documento cuando necesites aplicar o compartir detalles de Dev environment — devcontainer, pre-commit y just.
> **Estado:** Activo.


## Tabla de navegación

- [Opciones](#opciones)
- [Componentes del entorno](#componentes-del-entorno)
- [Primeros 5 minutos](#primeros-5-minutos)
- [Hooks incluidos](#hooks-incluidos)
- [Consejos](#consejos)
- [See also](#see-also)

# Dev environment — rápido
## Opciones
- **Codespaces/containers**: abre en GitHub Codespaces o `Dev Containers` en VS Code.
- **Local**: `pip install pre-commit ruff` y `pre-commit install`.

## Componentes del entorno
- [`systems/dev/`](https://github.com/scanalesespinoza/the-wise-tech/tree/main/dev) — docker compose para OTEL collector, Jaeger y servicios auxiliares.
- [`.devcontainer/`](https://github.com/scanalesespinoza/the-wise-tech/tree/main/.devcontainer) — definición de contenedor para Codespaces o VS Code.
- [`operations/scripts/`](https://github.com/scanalesespinoza/the-wise-tech/tree/main/operations/scripts) — utilidades para validaciones (`validate-resilience.py`, `check-links.py`, etc.).
- [`operations/justfile`](https://github.com/scanalesespinoza/the-wise-tech/blob/main/operations/justfile) / [`operations/Makefile`](https://github.com/scanalesespinoza/the-wise-tech/blob/main/operations/Makefile) — comandos espejo para flujos rápidos.

## Primeros 5 minutos
1) `just --justfile operations/justfile install` o `make -f operations/Makefile install`
2) `pre-commit install`
3) `just --justfile operations/justfile docs` y abre `http://127.0.0.1:8000`
4) `just ci` (equivalente a `make -f operations/Makefile ci`)

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
---
Última modificación: 2025-11-16

🗳️ **¿Te fue útil este documento?**
- [ ] Sí, resolvió mi duda
- [ ] Más o menos
- [ ] No me ayudó

💬 [Deja tu feedback](https://github.com/scanalesespinoza/the-wise-tech/issues/new?template=feedback.yml)

---

