# Personas for LLM audits

## 1. Strategic maintainer
- **Context**: Responsible for keeping the Wise Tech philosophy coherent and prioritizing improvements.
- **Goals**:
  - Identify gaps between strategic principles and their implementation across docs, scenarios, and code.
  - Detect risks that could affect the contribution experience described in `knowledge/docs/guides/editorial-workflow.md`.
- **Frequently asked questions**:
  - Does the roadmap captured in `knowledge/docs/roadmap/roadmap.md` match the technical assets (for example `systems/platform/` and `experience/scenarios/`)?
  - Are critical resources updated and referenced from the main README?

## 2. External contributor
- **Context**: Arrives from the community and wants to contribute to scenarios or guides without prior background.
- **Goals**:
  - Evaluate whether the contribution guide (`knowledge/docs/guides/contribution-guide.md`) provides actionable steps for the first PR.
  - Verify that `knowledge/docs/labs/` and `knowledge/docs/playbooks/` offer clear examples that accelerate onboarding.
- **Frequently asked questions**:
  - Does the navigation structure described in `README.md` match the actual file tree?
  - Do the critical links pass the automated checks (`make -f operations/Makefile docs`, `operations/scripts/check-links.py`)?

## 3. Platform engineer focused on resilience
- **Context**: Needs to validate that platform artifacts (SLOs, policies, runbooks) are actionable.
- **Goals**:
  - Review the resilience coverage in `experience/scenarios/payments/policies/resilience.yml` and confirm alignment with `knowledge/docs/guides/resilience-policies.md`.
  - Confirm that the payments scenarios (`experience/scenarios/payments/`) have contracts and tests ready to run.
- **Frequently asked questions**:
  - Do the runbooks reflect the KPIs described in `knowledge/docs/playbooks/platform-playbook.md`?
  - Are there clear instructions to reproduce simulated incidents and measure MTTR?

## 4. Learning experience analyst
- **Context**: Evaluates whether the 30/60/90 paths and labs drive adoption.
- **Goals**:
  - Confirm that each persona (`knowledge/docs/personas/`) connects with the right paths and KPIs.
  - Ensure that labs (`knowledge/docs/labs/`) define actionable metrics and deliverables.
- **Frequently asked questions**:
  - Do the paths include "First 60 minutes" guidance and clear follow-up metrics?
  - Are there gaps between historical English and Spanish versions (`en/` vs `es/`) that affect the experience?
