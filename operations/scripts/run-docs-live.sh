#!/usr/bin/env bash
set -euo pipefail
python -m pip install --upgrade pip
pip install mkdocs mkdocs-material mkdocs-static-i18n
mkdocs serve -f operations/mkdocs.yml -a 0.0.0.0:8000
