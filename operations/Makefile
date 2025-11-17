.PHONY: install fmt lint test parity docs verify-links content-meta ci resilience-check resilience-sample slos check-error-budget telemetry-smoke lab-01 lab-02 lab-03 lab-run-all security-scan docs-live dev-up dev-down dev-logs dev-status audit language-audit translate-status translate-status-check translate-batch translate-verify

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
# Adjust the requirements if they already exist; tolerates absence without failing
	- test -f $(REQUIREMENTS_DIR)/requirements.txt && pip install -r $(REQUIREMENTS_DIR)/requirements.txt || true
	- test -f $(REQUIREMENTS_DIR)/requirements-dev.txt && pip install -r $(REQUIREMENTS_DIR)/requirements-dev.txt || true
# Recommended tools
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

translate-status:
	@echo "Generating translation status report"
	python $(SCRIPTS_DIR)/translation_status.py --output audit/translation-status.md

translate-status-check:
	@python $(SCRIPTS_DIR)/translation_status.py --skip-write --fail-on MISSING_ES OUTDATED_ES

translate-batch:
	@if [ -z "$(BATCH)" ]; then \
	echo "Usage: make -f operations/Makefile translate-batch BATCH=<batch-id> [DRY_RUN=1]"; \
	exit 1; \
	fi
	@echo "Processing translation batch $(BATCH)"
	python $(SCRIPTS_DIR)/translate_batch.py --batch $(BATCH) $(if $(DRY_RUN),--dry-run,)

translate-verify: parity translate-status-check

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
	@echo "Validating front matter (tags) and 'See also' links"
	python $(SCRIPTS_DIR)/validate-content-metadata.py

verify-links:
	@echo "Checking internal Markdown links"
	python $(SCRIPTS_DIR)/check-links.py

language-audit:
	@echo "Checking that content is written in English"
	python $(SCRIPTS_DIR)/language_audit.py

ci: install fmt lint test parity docs verify-links content-meta slos
	@echo "CI (local) complete ✅"

audit:
	@python $(SCRIPTS_DIR)/audit-evaluator.py

resilience-check:
	@echo "Validating resilience policies…"
	@python $(SCRIPTS_DIR)/validate-resilience.py $(SCENARIO_DIR)/policies/resilience.yml

resilience-sample:
	@echo "Showing example and supported fields"
	@echo "See: $(SCENARIO_DIR)/policies/resilience.yml and $(SCRIPTS_DIR)/validate-resilience.py"

slos:
	@echo "Validating SLOs…"
	@python $(SCRIPTS_DIR)/validate-slos.py $(SCENARIO_DIR)/slo/slo-spec.yml

check-error-budget:
	@echo "Checking error budget (mock/local)…"
	@python $(SCRIPTS_DIR)/check-error-budget.py $(SCENARIO_DIR)/slo/slo-spec.yml

telemetry-smoke:
	@echo "Running telemetry smoke (structured logs + simulated p95)…"
	python $(SCRIPTS_DIR)/telemetry-smoke.py

lab-01:
	@echo "Lab 01 — Resilience Basics"
	$(MAKE_CMD) resilience-check || true
	$(MAKE_CMD) check-error-budget || true
	@echo "Complete the template: knowledge/docs/templates/labs/evidence-lab-01.md"

lab-02:
	@echo "Lab 02 — Observability Minimum"
	$(MAKE_CMD) telemetry-smoke || python $(SCRIPTS_DIR)/telemetry-smoke.py
	@echo "Complete the template: knowledge/docs/templates/labs/evidence-lab-02.md"

lab-03:
	@echo "Lab 03 — aDevelopment Loop"
	@echo "Create a small test/doc, run $(MAKE_CMD) test, and record KPIs."
	@echo "Complete the template: knowledge/docs/templates/labs/evidence-lab-03.md"

lab-run-all: lab-01 lab-02 lab-03
	@echo "Labs completed (remember to upload evidence in the PR)."

security-scan:
	@bash $(SCRIPTS_DIR)/security-scan.sh || true
