.PHONY: install fmt lint test parity docs verify-links content-meta ci resilience-check resilience-sample slos check-error-budget telemetry-smoke lab-01 lab-02 lab-03 lab-run-all security-scan docs-live dev-up dev-down dev-logs dev-status audit

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

docs-live:
	@echo "Iniciando MkDocs con live reload en :8000…"
	@bash scripts/run-docs-live.sh

dev-up:
	@echo "Levantando dev stack (otel-collector, jaeger, docs opcional)…"
	@docker compose -f dev/docker-compose.dev.yml up -d

dev-down:
	@echo "Deteniendo dev stack…"
	@docker compose -f dev/docker-compose.dev.yml down -v

dev-logs:
	@docker compose -f dev/docker-compose.dev.yml logs -f --tail=200

dev-status:
	@docker compose -f dev/docker-compose.dev.yml ps

content-meta:
	@echo "Validando front-matter (tags) y 'See also'…"
	python scripts/validate-content-metadata.py

verify-links:
	@echo "Checking internal Markdown links"
	python scripts/check-links.py

ci: install fmt lint test parity docs verify-links content-meta slos
	@echo "CI (local) complete ✅"

audit:
	@python scripts/audit-evaluator.py

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

lab-01:
	@echo "Lab 01 — Resilience Basics"
	make resilience-check || true
	make check-error-budget || true
	@echo "Completa la plantilla: docs/labs/evidence-templates/evidence-lab-01.md"

lab-02:
	@echo "Lab 02 — Observability Minimum"
	make telemetry-smoke || python scripts/telemetry-smoke.py
	@echo "Completa la plantilla: docs/labs/evidence-templates/evidence-lab-02.md"

lab-03:
	@echo "Lab 03 — aDevelopment Loop"
	@echo "Genera un test/doc pequeño, ejecuta make test, y registra KPIs."
	@echo "Completa la plantilla: docs/labs/evidence-templates/evidence-lab-03.md"

lab-run-all: lab-01 lab-02 lab-03
	@echo "Labs completados (recuerda subir evidencia en PR)."

security-scan:
	@bash scripts/security-scan.sh || true
