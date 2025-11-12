# Makefile - The Wise Tech
.PHONY: help install test parity docs docs-build docs-knowledge policies-check links ci fmt lint

help:
	@echo "Available targets:"
	@echo "  make install        # Install runtime + dev dependencies"
	@echo "  make test           # Run automated scenario tests"
	@echo "  make parity         # Ensure bilingual documentation parity"
	@echo "  make lint           # Run static analysis with Ruff"
	@echo "  make fmt            # Format Python code with Ruff"
	@echo "  make links          # Validate internal documentation links"
	@echo "  make docs           # Serve MkDocs locally"
	@echo "  make docs-build     # Build the MkDocs site"
	@echo "  make docs-knowledge # Validate knowledge assets and build docs"
	@echo "  make policies-check # Validate resilience policies definitions"
	@echo "  make ci             # Run the local quality gate"

TEST_CMD = python -m unittest discover scenarios/payments/tests
PARITY_CMD = python scripts/check_bilingual_parity.py --check-scenarios
DOCS_BUILD_CMD = mkdocs build
DOCS_SERVE_CMD = mkdocs serve
POLICIES_CMD = python scripts/validate_resilience_policies.py
LINKS_CMD = python scripts/check-links.py --strict
FORMAT_CMD = ruff format .
LINT_CMD = ruff check .

install:
	@echo "Installing development dependencies"
	@python -m pip install --upgrade pip
	@python -m pip install -r requirements.txt -r requirements-dev.txt || true
test:
	@echo "Running payment scenario tests"
	@$(TEST_CMD)

parity:
	@echo "Checking bilingual parity"
	@$(PARITY_CMD)

links:
	@echo "Validating documentation links"
	@$(LINKS_CMD)

docs:
	@echo "Serving documentation (http://127.0.0.1:8000)"
	@$(DOCS_SERVE_CMD)

docs-build:
	@echo "Building documentation"
	@$(DOCS_BUILD_CMD)

docs-knowledge:
	@echo "Validating knowledge base"
	@python scripts/validate-knowledge.py
	@echo "Building documentation"
	@$(DOCS_BUILD_CMD)

policies-check:
	@echo "Validating resilience policies"
	@$(POLICIES_CMD)

fmt:
	@echo "Formatting code"
	@$(FORMAT_CMD)

lint:
	@echo "Linting code"
	@$(LINT_CMD)

ci: install lint fmt test parity
	@echo "Local quality gate complete ✅"
