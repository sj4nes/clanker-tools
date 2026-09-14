# Changelog — agent-automation

Versions follow [`docs/skill-versioning.md`](../../docs/skill-versioning.md):
`1.0.0` means "as verified at release"; **MAJOR** = the skill was wrong (re-do
work done under the old text), **MINOR** = a statement changed or grew (re-read
it), **PATCH** = nothing semantic.

Entries are **version-anchored, not per-commit**: one entry per version this
skill has held. Everything before 2026-09-14 was reconstructed on 2026-09-14
from git history and `docs/skill-versioning.md`, so it records the version
history rather than every change. The full record is

    git log -- skills/agent-automation/

## 1.2.0 — 2026-09-09

**MINOR.** The self-revision gate sharpened with borrowings from the SkillAdam
paper: paired same-case evaluation, a target-threshold plus
protected-metric-boundary acceptance rule, and a rejected-candidate log. Shipped
as `v0.3.0` at the time; renumbered in the version re-base (`0fbb03c`,
adjudicated `f921886`), which preserved both post-release revisions as minors —
see [`docs/skill-versioning.md` §3](../../docs/skill-versioning.md). (`9bcc715`)

## 1.1.0 — 2026-09-09

**MINOR.** Borrowings folded in from the Procedural Graphs paper: a compact
versioned procedure and an environment-drift review, read once. Shipped as
`v0.2.0` at the time; renumbered in the re-base. (`cc04a43`)

## 1.0.0 — 2026-09-09

First release, verified at release. (`feaa806`)
