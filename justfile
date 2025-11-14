set shell := ["bash", "-uc"]

# Alias rápidos a Makefile
install:    run "make install"
fmt:        run "make fmt"
lint:       run "make lint"
test:       run "make test"
parity:     run "make parity"
docs:       run "make docs"
ci:         run "make ci"
links:      run "make verify-links"
resilience: run "make resilience-check"
slos:       run "make slos"
budget:     run "make check-error-budget"
telemetry:  run "make telemetry-smoke"
lab-01:     run "make lab-01"
lab-02:     run "make lab-02"
lab-03:     run "make lab-03"
content:    run "make content-meta"
security:   run "make security-scan"

default:
  @echo "Comandos disponibles:"
  @echo "  just install|fmt|lint|test|parity|docs|ci|links|resilience|slos|budget|telemetry|lab-01|lab-02|lab-03|content|security"
