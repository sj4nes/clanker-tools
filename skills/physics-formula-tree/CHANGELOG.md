# Changelog — physics-formula-tree

Versions follow [`docs/skill-versioning.md`](../../docs/skill-versioning.md):
`1.0.0` means "as verified at release"; **MAJOR** = the skill was wrong (re-do
work done under the old text), **MINOR** = a statement changed or grew (re-read
it), **PATCH** = nothing semantic.

Entries are **version-anchored, not per-commit**: one entry per version this
skill has held. Everything before 2026-09-14 was reconstructed on 2026-09-14
from git history and `docs/skill-versioning.md`, so it records the version
history rather than every change. The full record is

    git log -- skills/physics-formula-tree/

## 1.2.0 — 2026-09-14

**MINOR.** Prescribes two further checks: `build/check-lean-cores.py` and
`validation/lean-mutation-check.sh`. (`abb9d0f`)

## 1.1.0 — 2026-09-14

**MINOR.** As `math-theorem-tree`: two new prescribed checks, and
`references/package-layout.md` now points at `lib/` instead of inlining the
scripts. A `lib/` re-exporting the canonical implementation added. (`904ea6a`)

## 1.0.0 — 2026-09-05

First release, verified at release. (`e35fa60`)
