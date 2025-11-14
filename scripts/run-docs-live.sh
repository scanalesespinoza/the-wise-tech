#!/usr/bin/env bash
set -euo pipefail
python -m pip install --upgrade pip
pip install mkdocs mkdocs-material
mkdocs serve -a 0.0.0.0:8000
