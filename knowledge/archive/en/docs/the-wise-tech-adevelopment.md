# The Wise Tech + aDevelopment

## Capitalize on experience in code, accelerate with AI, and revive mentorship

**Objective:** Never start from zero again. Build with an advantage by using the repository as the source of truth and AI as the accelerator for learning and quality.

## 1. Context and purpose

Modern teams face turnover and limited mentorship, making it hard to capture and transmit critical knowledge. The Wise Tech practice promotes accumulating, curating, and operationalizing technical experience; aDevelopment (AI-Augmented Development) supercharges that knowledge by transforming code history into actionable insights.

**Purpose**

- Turn experience + technology into a long-term advantage.
- Make knowledge transfer viable in today’s reality (fast onboarding, clear handovers, less friction).
- Accelerate maturity and mastery at the pace the organization requires.

## 2. The three contexts of The Wise Tech

### 2.1 Essential (System identity)
Non-negotiable principles and behaviors that define how the system must exist (e.g., idempotency, eventual consistency, domain boundaries, resilience policies).

### 2.2 Operational (Evolve with quality)
Practices, automation, and standards that enable growth without degradation (e.g., PR review, contract testing, SLOs, observability, security).

### 2.3 Impact (People and outcomes)
How the system reduces friction, empowers teams, and improves results (e.g., guided onboarding, smooth handovers, continuous feedback).

### AI across the three contexts

- Detects principle violations (Essential) directly from the PR.
- Generates documents, examples, and checklists from the code base (Operational).
- Offers “augmented mentoring” and contextual guides (Impact).

## 3. aDevelopment: from repository to active learning

### Code as the source of truth

Patterns, decisions, trade-offs, and conventions live inside repositories, commits, issues, and PRs.

AI helps mine these patterns and generate reusable knowledge (summaries, guides, recipes).

### Augmented mentorship (on-demand)

- Virtual pairing: contextual questions about the file/PR.
- Consistent reviews: bots that teach and correct using examples from the repository.
- Guided onboarding: self-serve walkthroughs (module tours, endpoints, diagrams).

### Systems that learn

- Every sprint leaves a trace: promote effective patterns and retire anti-patterns.
- Knowledge remains even when people change.

## 4. Recommended practices (start today)

### 4.1 Repository “knowledge mining”

- PR summaries with context (what, why, risks, compatibility).
- Catalog of patterns/recipes (by language, module, layer).
- Narrative changelog per release (go beyond technical lists and include impact).
- Extract decisions (ADR) from PR and issue discussions.

#### Base prompt for PRs (template)

- **Role:** Technical mentor/reviewer.
- **Input:** PR diff + title + description + labels.
- **Tasks:**
  1. Explain the change in 5–7 bullets (what/why).
  2. Identify risks and compatibility (breaking/non-breaking).
  3. Highlight applied patterns and detected anti-patterns (link to local recipes).
  4. Tests and observability: what is missing? What evidence is recommended?
  5. Short onboarding guide to understand this change (key files and flow).
- **Output:** Markdown ready to comment on the PR.

### 4.2 Living checklists in PRs (Essential + Operational)

Anchor your reviews with the [Pull Request Checklist](checklist-pr.md) so Essential, operational, and impact considerations stay visible for every change.

- Essential principles (idempotency, domain boundaries, handled errors).
- Security (secrets, dependencies, SCA scanning).
- Observability (logs, metrics, traces with correlation ID).
- Tests (unit, contract, end-to-end if applicable).
- Performance and resilience (circuit breakers, timeouts).

#### Checklist example (excerpt)

- [ ] Explicit error handling—no generic catch-all.
- [ ] Defined timeouts and retries for external calls.
- [ ] Structured logs + correlation ID.
- [ ] Unit tests for happy path and relevant edge cases.
- [ ] Contract tests for modified public APIs.
- [ ] No secrets in code (see SCA scan).

### 4.3 Documentation from code (DocOps)

Use the automation script under `.github/scripts/generate_module_readmes.py` to keep the [Recipe Catalog](recipes/README.md) and [Onboarding Assets](onboarding/README.md) synchronized with new material.

- Auto-generate module READMEs.
- Build a living technical glossary from comments/docstrings.
- Publish diagrams (e.g., PlantUML/Mermaid) derived from the repository.

## 5. Recommended workflow

1. Lightweight design guided by the Essential context (key decisions + boundaries).
2. Implementation with recipes and catalog examples.
3. PR with checklist, AI summary, and mentoring hints.
4. Continuous integration (build, tests, security, documentation generation).
5. Release with narrative changelog (value delivered, migration guidance).
6. Retrospective and mining: promote effective patterns to the catalog.

## 6. Maturity metrics (KPIs)

- Onboarding Lead Time: days from arrival to first accepted PR.
- % of PRs with checklist completed and essential violations detected.
- Coverage of recipes/patterns referenced per PR.
- Review time and rework per PR.
- Post-release incidents tied to undocumented decisions.
- Handover time between teams/shifts.

## 7. Adoption roadmap (4 weeks)

### Week 1 – Foundations

- Define Essential principles (5–8 max).
- Create PR checklist and a `knowledge/docs/recipes/` folder.
- Enable baseline GitHub Actions (build, test, SCA).

### Week 2 – AI in PRs and DocOps

- PR summary bot + mentoring hints.
- Generate module READMEs and glossary.
- Seed recipes (errors, observability, testing).

### Week 3 – Quality and patterns

- Enforce checklists (fail if critical items missing).
- Contract tests and evidence for SLOs/incidents.
- “Mine” history to uncover patterns.

### Week 4 – Operationalization

- Automated narrative changelog.
- Onboarding tour (docs + links + learning paths).
- Retrospective and pattern promotion into the catalog.

## 8. Automation examples (GitHub Actions)

> Adjust names/paths to fit your repository.

### 8.1 PR summary with hints (simplified example)

`.github/workflows/pr-summarizer.yml`

```yaml
name: PR Summarizer
on:
  pull_request:
    types: [opened, synchronize, reopened]
permissions:
  contents: read
  pull-requests: write
jobs:
  summarize:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Get PR diff
        id: diff
        run: |
          git fetch origin ${{ github.base_ref }} --depth=1
          git diff origin/${{ github.base_ref }}...HEAD > pr.diff || true
          echo "diff<<EOF" >> $GITHUB_OUTPUT
          sed -e 's/`/`/g' pr.diff >> $GITHUB_OUTPUT
          echo "EOF" >> $GITHUB_OUTPUT
      - name: Generate summary (LLM)
        id: ai
        env:
          PR_TITLE: ${{ github.event.pull_request.title }}
          PR_BODY:  ${{ github.event.pull_request.body }}
          DIFF:     ${{ steps.diff.outputs.diff }}
        run: |
          python - << 'PY'
# Call your AI provider here (e.g., internal API) with the repository prompt template.
# Print the final Markdown to stdout so the next step can comment with it.
print("# PR Summary\n\n- What/why...\n- Risks...\n- Patterns...\n- Tests/Observability...")
PY
      - name: Comment summary
        uses: marocchino/sticky-pull-request-comment@v2
        with:
          header: pr-summary
          message: ${{ steps.ai.outputs.stdout || 'Summary not available' }}
```

### 8.2 Enforce essential checklist

`.github/workflows/pr-checklist.yml`

```yaml
name: PR Checklist Enforcer
on:
  pull_request:
    types: [opened, synchronize, reopened, edited]
jobs:
  enforce:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Ensure checklist is present
        run: |
          FILE=".github/PULL_REQUEST_TEMPLATE.md"
          if [ ! -f "$FILE" ]; then
            echo "Missing PULL_REQUEST_TEMPLATE.md with essential checklist." >&2
            exit 1
          fi
          echo "Essential checklist present."
```

### 8.3 Documentation generated from code

`.github/workflows/doc-gen.yml`

```yaml
name: DocGen
on:
  push:
    branches: [ main ]
jobs:
  generate-docs:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Build module READMEs
        run: |
          python .github/scripts/generate_module_readmes.py
      - name: Commit docs
        uses: stefanzweifel/git-auto-commit-action@v5
        with:
          commit_message: "docs: update module READMEs and glossary"
          file_pattern: "knowledge/docs/** README.md **/README.md"
```

## 9. Suggested structure in `knowledge/docs/`

```text
knowledge/docs/
  the-wise-tech-adevelopment.md   # this document
  principles-essential.md         # 5–8 non-negotiable principles (see repository seed)
  checklist-pr.md                 # living PR checklist (see repository seed)
  recipes/
    errors-handling.md            # populated example
    observability.md              # populated example
    testing-contracts.md          # populated example
    resiliency.md                 # populated example
  onboarding/
    tour.md                       # populated example
    learning-paths.md             # populated example
  glossary.md                     # populated example
  changelog-guidelines.md         # populated example
```

## 10. Roles and responsibilities

- **Architecture/Tech Leads:** Guard the Essential, promote patterns, and review metrics.
- **Platform Team:** Automation, CI/CD, security, documentation generation.
- **Product Teams:** Apply recipes, enrich the catalog, improve checklists.
- **Mentors (or augmented mentors):** Curate examples and answer questions by codifying responses.

## 11. Common anti-patterns

- Checklist performed just to comply: checking boxes without verifying evidence.
- Documentation that drifts away from code.
- AI bots that ignore the local repository (generic answers).
- Changing Essential principles too frequently (loss of identity).
- Recipes without real examples from the repository.

## 12. FAQ

**Do we need significant new tooling?**

No. Start with GitHub Actions and simple scripts. The key is process + curation.

**What if the AI makes mistakes?**

Treat the flow as assistance, not authority. People decide; AI accelerates.

**How do we measure progress?**

Track onboarding, review efficiency, recipe coverage, Essential violations, and post-release rework.

## 13. Licensing and contribution

- Follow the repository contribution guidelines.
- Every recipe must include: purpose, when to use, when not to use, steps, local example, and internal links.
- Proposed changes to the Essential are handled as Architecture Decision Records (ADR).

## 14. Next steps

- Publish `principles-essential.md` (5–8 clear rules).
- Activate PR Summarizer and Checklist Enforcer.
- Create 3–4 seed recipes with real examples.
- Enable `onboarding/tour.md` and link it from the README.
- Close the first cycle with metrics and a retrospective to promote patterns.

---

With **The Wise Tech + aDevelopment**, every change teaches. Knowledge stops being ephemeral and becomes a compound advantage.
