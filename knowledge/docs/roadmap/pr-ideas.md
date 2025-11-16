---
title: "PR ideas"
tags: ["developers", "knowledge-capitalization"]
---
# PR ideas

Small tasks to practice the contribution flow:

1. **Document site metrics**
   - Update `docs/metrics/site-metrics.md` with the latest CI run.
   - Add a short note to the README inside "Learning outcomes" if the primary indicator changes.
2. **Improve "See also" links**
   - Pick a guide in `docs/guides/` that does not yet have a "See also" section.
   - Add relevant cross-references and validate them with `make content-meta`.
3. **Translate a snippet**
   - Create the missing English or Spanish version in `docs/snippets/`.
   - Run `make -f operations/Makefile parity` to confirm the routes between languages stay aligned.

Each idea must include a note in the PR explaining which guide, snippet, or metric you changed.

## See also
- [Roadmap](roadmap.md)
- [Contribution guide](../guides/contribution-guide.md)
