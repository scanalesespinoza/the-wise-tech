#!/usr/bin/env bash
set -euo pipefail
python -m pip install --upgrade pip
pip install ruff pre-commit mkdocs mkdocs-material pyyaml
# instalar deps del proyecto si existen
test -f requirements.txt && pip install -r requirements.txt || true
test -f requirements-dev.txt && pip install -r requirements-dev.txt || true
# instalar hooks
pre-commit install || true
echo "[devcontainer] ready."
