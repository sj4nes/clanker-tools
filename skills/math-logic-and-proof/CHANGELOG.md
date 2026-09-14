# Changelog — math-logic-and-proof

Versions follow [`docs/skill-versioning.md`](../../docs/skill-versioning.md):
`1.0.0` means "as verified at release"; **MAJOR** = the skill was wrong (re-do
work done under the old text), **MINOR** = a statement changed or grew (re-read
it), **PATCH** = nothing semantic.

Entries are **version-anchored, not per-commit**: one entry per version this
skill has held. Everything before 2026-09-14 was reconstructed on 2026-09-14
from git history and `docs/skill-versioning.md`, so it records the version
history rather than every change. The full record is

    git log -- skills/math-logic-and-proof/

## 2.1.0 — 2026-09-14

**MINOR.** Five `core` refs described the proof technique in prose instead of
naming the declaration. The declarations were all there exactly as claimed, so
nobody was misled; the refs simply could not be resolved by machine. They now
name `deduction`, `soundness`, `conj_injective`, `nand`, `strong_of_weak` and
friends. (`abb9d0f`)

## 2.0.0 — 2026-09-14

**MAJOR.** **4 prerequisite edges the node text uses were missing from the
graph.** `build/check-edge-evidence.py` (new) reads each node's declared
dependencies and proof prose — written independently of the edge list — and
found results the text cites that the graph did not carry. A prerequisite
chain queried before this commit was incomplete, silently, which is what makes
this MAJOR: the capsule offers "the minimum prerequisite chain" as a headline
use. Also new: `validation/mutation-check.sh`, which plants five graph defects
per build and asserts each is caught — hygiene checks pass a deleted *or* an
invented edge. (`904ea6a`)

## 1.0.0 — 2026-09-06

First release, verified at release. (`e25ed3c`)
