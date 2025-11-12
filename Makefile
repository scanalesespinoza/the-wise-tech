# Makefile - The Wise Tech
.PHONY: help test parity docs docs-serve policies-check ci

help:
	@echo "Available targets:"
	@echo "  make test            # Run automated scenario tests"
	@echo "  make parity          # Ensure bilingual documentation parity"
	@echo "  make docs            # Build the MkDocs site"
	@echo "  make docs-serve      # Serve the documentation locally"
	@echo "  make policies-check  # Validate resilience policies definitions"
	@echo "  make ci              # Run the local quality gate (test+checks)"

TEST_CMD = python -m unittest discover scenarios/payments/tests
PARITY_CMD = python scripts/check_bilingual_parity.py --check-scenarios
DOCS_BUILD_CMD = mkdocs build
DOCS_SERVE_CMD = mkdocs serve
POLICIES_CMD = python scripts/validate_resilience_policies.py
test:
	@echo "Running payment scenario tests"
	@$(TEST_CMD)

parity:
	@echo "Checking bilingual parity"
	@$(PARITY_CMD)

docs:
	@echo "Building documentation"
	@$(DOCS_BUILD_CMD)

docs-serve:
	@echo "Serving documentation (Ctrl+C to stop)"
	@$(DOCS_SERVE_CMD)

policies-check:
	@echo "Validating resilience policies"
	@$(POLICIES_CMD)

ci: test parity policies-check docs
	@echo "Local quality gate complete ✅"
