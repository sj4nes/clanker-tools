# Changelog — experience-library

Versions follow [`docs/skill-versioning.md`](../../docs/skill-versioning.md):
`1.0.0` means "as verified at release"; **MAJOR** = the skill was wrong (re-do
work done under the old text), **MINOR** = a statement changed or grew (re-read
it), **PATCH** = nothing semantic.

Entries are **version-anchored, not per-commit**: one entry per version this
skill has held. The full record is

    git log -- skills/experience-library/

## 1.0.0 — 2026-09-14

First release, verified at release. Six behaviours mined from Duan, Liu, Tang,
Chen, Zhou et al., *The Last AI Built by Humans: Toward Genuine Recursive
Self-Improvement*, arXiv:2609.11873v1 (§3.5.1, §3.5.3, §6) and built
fixture-first: `verification/` models a library whose true value is a
parameter of the fixture, and shows each default failing — inspection-based
admission cannot distinguish a useless candidate from a real one, unbounded
growth falls below a tiny library, over-retirement is worse than no policy,
and three different pathologies produce identical task scores. Displacement
table: 5 covered, 4 judgement, 4 gaps (logged in `BACKLOG.md`).
