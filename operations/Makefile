.PHONY: install fmt lint test parity docs verify-links content-meta ci resilience-check resilience-sample slos check-error-budget telemetry-smoke lab-01 lab-02 lab-03 lab-run-all security-scan docs-live dev-up dev-down dev-logs dev-status audit

THIS_MAKEFILE := $(lastword $(MAKEFILE_LIST))
MAKE_CMD := $(MAKE) -f $(THIS_MAKEFILE)

OPS_DIR := operations
DOCS_CONFIG := $(OPS_DIR)/mkdocs.yml
SCENARIO_DIR := experience/scenarios/payments
SCRIPTS_DIR := $(OPS_DIR)/scripts
DEV_DIR := systems/dev
REQUIREMENTS_DIR := $(OPS_DIR)

install:
	@echo "Installing dev dependencies"
	python -m pip install --upgrade pip
	# Ajusta los requirements si ya existen; tolera ausencia sin fallar
	- test -f $(REQUIREMENTS_DIR)/requirements.txt && pip install -r $(REQUIREMENTS_DIR)/requirements.txt || true
	- test -f $(REQUIREMENTS_DIR)/requirements-dev.txt && pip install -r $(REQUIREMENTS_DIR)/requirements-dev.txt || true
	# Herramientas recomendadas
	- python -m pip install "ruff==0.14.5" mkdocs mkdocs-material mkdocs-static-i18n

fmt:
	@echo "Formatting code"
	- ruff format .

lint:
	@echo "Linting code"
	- ruff check .

test:
	@echo "Running unit tests"
	python -m unittest discover experience/scenarios/payments/tests

parity:
	@echo "Checking bilingual parity"
	python $(SCRIPTS_DIR)/check_bilingual_parity.py --check-scenarios

docs:
	@echo "Building docs"
	mkdocs build --strict -f $(DOCS_CONFIG)

docs-live:
	@echo "Iniciando MkDocs con live reload en :8000…"
	@bash $(SCRIPTS_DIR)/run-docs-live.sh

dev-up:
	@echo "Levantando dev stack (otel-collector, jaeger, docs opcional)…"
	@docker compose -f $(DEV_DIR)/docker-compose.dev.yml up -d

dev-down:
	@echo "Deteniendo dev stack…"
	@docker compose -f $(DEV_DIR)/docker-compose.dev.yml down -v

dev-logs:
	@docker compose -f $(DEV_DIR)/docker-compose.dev.yml logs -f --tail=200

dev-status:
	@docker compose -f $(DEV_DIR)/docker-compose.dev.yml ps

content-meta:
	@echo "Validando front-matter (tags) y 'See also'…"
	python $(SCRIPTS_DIR)/validate-content-metadata.py

verify-links:
	@echo "Checking internal Markdown links"
	python $(SCRIPTS_DIR)/check-links.py

ci: install fmt lint test parity docs verify-links content-meta slos
	@echo "CI (local) complete ✅"

audit:
	@python $(SCRIPTS_DIR)/audit-evaluator.py

resilience-check:
	@echo "Validando políticas de resiliencia…"
	@python $(SCRIPTS_DIR)/validate-resilience.py $(SCENARIO_DIR)/policies/resilience.yml

resilience-sample:
	@echo "Mostrando ejemplo y campos soportados"
	@echo "Ver: $(SCENARIO_DIR)/policies/resilience.yml y $(SCRIPTS_DIR)/validate-resilience.py"

slos:
	@echo "Validando SLOs…"
	@python $(SCRIPTS_DIR)/validate-slos.py $(SCENARIO_DIR)/slo/slo-spec.yml

check-error-budget:
	@echo "Chequeando presupuesto de error (mock/local)…"
	@python $(SCRIPTS_DIR)/check-error-budget.py $(SCENARIO_DIR)/slo/slo-spec.yml

telemetry-smoke:
	@echo "Running telemetry smoke (logs estructurados + p95 simulado)…"
	python $(SCRIPTS_DIR)/telemetry-smoke.py

lab-01:
	@echo "Lab 01 — Resilience Basics"
	$(MAKE_CMD) resilience-check || true
	$(MAKE_CMD) check-error-budget || true
	@echo "Completa la plantilla: knowledge/docs/templates/labs/evidence-lab-01.md"

lab-02:
	@echo "Lab 02 — Observability Minimum"
	$(MAKE_CMD) telemetry-smoke || python $(SCRIPTS_DIR)/telemetry-smoke.py
	@echo "Completa la plantilla: knowledge/docs/templates/labs/evidence-lab-02.md"

lab-03:
	@echo "Lab 03 — aDevelopment Loop"
	@echo "Genera un test/doc pequeño, ejecuta $(MAKE_CMD) test, y registra KPIs."
	@echo "Completa la plantilla: knowledge/docs/templates/labs/evidence-lab-03.md"

lab-run-all: lab-01 lab-02 lab-03
	@echo "Labs completados (recuerda subir evidencia en PR)."

security-scan:
	@bash $(SCRIPTS_DIR)/security-scan.sh || true
