# Changelog — theorem-tree-tutorial

Versions follow [`docs/skill-versioning.md`](../../docs/skill-versioning.md):
`1.0.0` means "as verified at release"; **MAJOR** = the skill was wrong (re-do
work done under the old text), **MINOR** = a statement changed or grew (re-read
it), **PATCH** = nothing semantic.

Entries are **version-anchored, not per-commit**: one entry per version this
skill has held. Everything before 2026-09-14 was reconstructed on 2026-09-14
from git history and `docs/skill-versioning.md`, so it records the version
history rather than every change. The full record is

    git log -- skills/theorem-tree-tutorial/

## 1.1.0 — 2026-09-22

**MINOR.** The shared contract. `docs/capsule-tutorial-contract.md` now holds the
document skeleton, the lead, the block vocabulary and the eight workflow steps
that this skill and `formula-tree-tutorial` had been keeping in two copies.

Measured before deciding: **8/8 workflow steps identical by name and order, 4/4
SKILL.md sections identical, 3/3 reference filenames identical** — against only
**22.5%** literal text overlap. The method was shared; the prose was duplicated,
and it had drifted in both directions. The lead paragraph was in the math
skeleton and not the physics one (five tutorials shipped without one). The Lean
beat is prescribed in the math skill only, yet physics and chemistry tutorials
carry **23 `lean_` blocks to mathematics' 16** — invented by their authors,
unprescribed.

The skills stay two: their check vocabularies genuinely differ, and 24
tutorials carry provenance naming the skill that generated them. What changed is
that the shared part is single-source. `references/document-structure.md` is now
only this skill's domain deltas, and `verification/check_contract.py` fails if
either skill stops deferring to the contract or re-declares a section it owns.

No behaviour change for an author of a math tutorial: every beat this skill
prescribed it still prescribes. What moved is where the shared half is written
down. Step 3 now states the lead requirement explicitly rather than leaving it
in the skeleton, and the description gained the boundary the
`skill-authoring` scope gate wanted (closing its row in the ratchet, 33 → 32).

Tutorials from this skill are checked by
`skills/formula-tree-tutorial/verification/check_beats.py`, which covers both
skills' output. The harness is not duplicated, for the same reason the
skeleton no longer is.

## 1.0.0 — 2026-09-06

First release, verified at release. (`8fd1252`)
