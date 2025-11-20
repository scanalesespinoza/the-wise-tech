.PHONY: translate-batch docs-qa

translate-batch:
	@python scripts/translate-batch.py $(BATCH)

docs-qa:
	@mkdocs build --strict
	@python scripts/check-links.py --root docs --strict
	@python scripts/validate-content-metadata.py
	@python scripts/validate-spanish-quality.py

# Uso local:
#  make translate-batch BATCH=w1-b1
#  make docs-qa
