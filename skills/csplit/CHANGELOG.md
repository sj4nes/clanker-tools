# Changelog — csplit

Versions follow [`docs/skill-versioning.md`](../../docs/skill-versioning.md):
`1.0.0` means "as verified at release"; **MAJOR** = the skill was wrong (re-do
work done under the old text), **MINOR** = a statement changed or grew (re-read
it), **PATCH** = nothing semantic.

Entries are **version-anchored, not per-commit**: one entry per version this
skill has held. Everything before 2026-09-14 was reconstructed on 2026-09-14
from git history and `docs/skill-versioning.md`, so it records the version
history rather than every change. The full record is

    git log -- skills/csplit/

## 2.0.0 — 2026-09-13

**MAJOR.** The transactional template used `{*}`, `-b` and
`--suppress-matched`, none of which exist on BSD `csplit`. The recipe did not
run. Recorded in the version re-base (`0fbb03c`, adjudicated `f921886`); see
[`docs/skill-versioning.md` §3](../../docs/skill-versioning.md). (`0fbb03c`)

## 1.0.0 — 2026-09-05

First release, verified at release. (`9dd8165`)
