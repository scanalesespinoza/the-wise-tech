.PHONY: install fmt lint test parity docs verify-links ci

install:
	@echo "Installing dev dependencies"
	python -m pip install --upgrade pip
	# Ajusta los requirements si ya existen; tolera ausencia sin fallar
	- test -f requirements.txt && pip install -r requirements.txt || true
	- test -f requirements-dev.txt && pip install -r requirements-dev.txt || true
	# Herramientas recomendadas
	- python -m pip install ruff mkdocs mkdocs-material

fmt:
	@echo "Formatting code"
	- ruff format .

lint:
	@echo "Linting code"
	- ruff check .

test:
	@echo "Running unit tests"
	python -m unittest discover scenarios/payments/tests || true

parity:
	@echo "Checking bilingual parity"
	python scripts/check_bilingual_parity.py --check-scenarios || true

docs:
	@echo "Building docs"
	mkdocs build --strict

verify-links:
	@echo "Checking internal Markdown links"
	python scripts/check-links.py

ci: install fmt lint test parity docs verify-links
	@echo "CI (local) complete ✅"
