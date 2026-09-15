# Changelog — evaluator-integrity

Versions follow [`docs/skill-versioning.md`](../../docs/skill-versioning.md):
`1.0.0` means "as verified at release"; **MAJOR** = the skill was wrong (re-do
work done under the old text), **MINOR** = a statement changed or grew (re-read
it), **PATCH** = nothing semantic.

Entries are **version-anchored, not per-commit**: one entry per version this
skill has held. The full record is

    git log -- skills/evaluator-integrity/

## 1.0.0 — 2026-09-14

First release, verified at release. Six behaviours mined from Duan, Liu, Tang,
Chen, Zhou et al., *The Last AI Built by Humans: Toward Genuine Recursive
Self-Improvement*, arXiv:2609.11873v1 (§1.3, §2.1, §3.6.2, §6) and built
fixture-first: `verification/` constructs five measurement setups whose true
ability is fixed by the fixture, and shows the default reading reporting an
improvement that did not happen in each. Displacement table: 5 covered,
4 judgement, 5 gaps (logged in `BACKLOG.md`).
