.PHONY: translate-batch translation-qa

translate-batch:
	@python scripts/translate-batch.py $(BATCH)

translation-qa:
	@mkdocs build --strict
	@if [ -f scripts/check-links.py ]; then python scripts/check-links.py --strict; fi
	@if [ -f scripts/validate-content-metadata.py ]; then python scripts/validate-content-metadata.py; fi

# Uso local:
#  make translate-batch BATCH=w1-b1
#  make translation-qa
