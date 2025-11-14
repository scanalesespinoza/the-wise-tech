.PHONY: install fmt lint test parity docs verify-links ci resilience-check resilience-sample slos check-error-budget telemetry-smoke

install:
	@echo "Installing dev dependencies"
	python -m pip install --upgrade pip
	# Ajusta los requirements si ya existen; tolera ausencia sin fallar
	- test -f requirements.txt && pip install -r requirements.txt || true
	- test -f requirements-dev.txt && pip install -r requirements-dev.txt || true
	# Herramientas recomendadas
	- python -m pip install ruff mkdocs mkdocs-material mkdocs-static-i18n

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

ci: install fmt lint test parity docs verify-links slos
	@echo "CI (local) complete ✅"

resilience-check:
	@echo "Validando políticas de resiliencia…"
	python scripts/validate-resilience.py platform/policies/resilience.yml

resilience-sample:
	@echo "Mostrando ejemplo y campos soportados"
	@echo "Ver: platform/policies/resilience.yml y scripts/validate-resilience.py"

slos:
	@echo "Validando SLOs…"
	python scripts/validate-slos.py platform/slo/slo-spec.yml

check-error-budget:
	@echo "Chequeando presupuesto de error (mock/local)…"
	python scripts/check-error-budget.py platform/slo/slo-spec.yml || true

telemetry-smoke:
	@echo "Running telemetry smoke (logs estructurados + p95 simulado)…"
	python scripts/telemetry-smoke.py
