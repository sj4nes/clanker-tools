# Changelog — chemistry-foundations

Versions follow [`docs/skill-versioning.md`](../../docs/skill-versioning.md):
`1.0.0` means "as verified at release"; **MAJOR** = the skill was wrong (re-do
work done under the old text), **MINOR** = a statement changed or grew (re-read
it), **PATCH** = nothing semantic.

Entries are **version-anchored, not per-commit**: one entry per version this
skill has held. Everything before 2026-09-14 was reconstructed on 2026-09-14
from git history and `docs/skill-versioning.md`, so it records the version
history rather than every change. The full record is

    git log -- skills/chemistry-foundations/

## 3.0.0 — 2026-09-14

**MAJOR.** **2 prerequisite edges the node text uses were missing from the
graph.** `build/check-edge-evidence.py` (new) reads each node's declared
dependencies and proof prose — written independently of the edge list — and
found results the text cites that the graph did not carry. A prerequisite
chain queried before this commit was incomplete, silently, which is what makes
this MAJOR: the capsule offers "the minimum prerequisite chain" as a headline
use. Also new: `validation/mutation-check.sh`, which plants five graph defects
per build and asserts each is caught — hygiene checks pass a deleted *or* an
invented edge. (`904ea6a`)

## 2.0.0 — 2026-09-13

**MAJOR.** The capsule README documented `bc -q -l validation/…bc` with no
stdin redirect, so the capsule's own validation command **hung** when run as
written — for 8 days. Recorded in the version re-base (`0fbb03c`, adjudicated
`f921886`); see [`docs/skill-versioning.md`
§3](../../docs/skill-versioning.md). (`0fbb03c`)

## 1.0.0 — 2026-09-09

First release, verified at release. (`34c5e14`)
