# Makefile - The Wise Tech
.PHONY: help install test parity docs docs-serve policies-check links ci

help:
	@echo "Available targets:"
	@echo "  make install        # Install local development dependencies"
	@echo "  make test            # Run automated scenario tests"
	@echo "  make parity          # Ensure bilingual documentation parity"
	@echo "  make links           # Validate internal documentation links"
	@echo "  make docs            # Build the MkDocs site"
	@echo "  make docs-knowledge  # Validate knowledge assets and build docs"
	@echo "  make docs-serve      # Serve the documentation locally"
	@echo "  make policies-check  # Validate resilience policies definitions"
	@echo "  make ci              # Run the local quality gate (test+checks)"

TEST_CMD = python -m unittest discover scenarios/payments/tests
PARITY_CMD = python scripts/check_bilingual_parity.py --check-scenarios
DOCS_BUILD_CMD = mkdocs build
DOCS_SERVE_CMD = mkdocs serve
POLICIES_CMD = python scripts/validate_resilience_policies.py
LINKS_CMD = python scripts/check-links.py --strict

install:
	@echo "Installing development dependencies"
	@python -m pip install --upgrade pip
	@python -m pip install -r requirements-dev.txt
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
	@echo "Building documentation"
	@$(DOCS_BUILD_CMD)

docs-knowledge:
	@echo "Validating knowledge base"
	@python scripts/validate-knowledge.py
	@echo "Building documentation"
	@$(DOCS_BUILD_CMD)

docs-serve:
	@echo "Serving documentation (Ctrl+C to stop)"
	@$(DOCS_SERVE_CMD)

policies-check:
	@echo "Validating resilience policies"
	@$(POLICIES_CMD)

ci: install test parity links policies-check docs
	@echo "Local quality gate complete ✅"
