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
	python $(SCRIPTS_DIR)/lint_i18n_strings.py
