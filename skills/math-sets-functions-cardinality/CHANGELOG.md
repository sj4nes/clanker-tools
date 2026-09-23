# Changelog — math-sets-functions-cardinality

Versions follow [`docs/skill-versioning.md`](../../docs/skill-versioning.md):
`1.0.0` means "as verified at release"; **MAJOR** = the skill was wrong (re-do
work done under the old text), **MINOR** = a statement changed or grew (re-read
it), **PATCH** = nothing semantic.

Entries are **version-anchored, not per-commit**: one entry per version this
skill has held. Everything before 2026-09-14 was reconstructed on 2026-09-14
from git history and `docs/skill-versioning.md`, so it records the version
history rather than every change. The full record is

    git log -- skills/math-sets-functions-cardinality/

## 3.1.0 — 2026-09-22

**MINOR.** "How to use this capsule" step 1 pointed at `indexes/topic-index.md`, which this capsule has never had — six
other capsules do. The dead link was found by the new corpus link
gate (`tools/check-links.py`, `docs/verifying-skills.md` §7a).

Step 1 now names `symbol-index.md` and `status-index.md`, which exist, and says the topic index is missing rather than advertising
a file that is not there. MINOR because a reader is sent somewhere
different, not merely because a path was repaired. Building the
index is filed in `BACKLOG.md`; no node, edge or result changed.

## 3.0.0 — 2026-09-14

**MAJOR.** `countable_closure_properties` carried `lean_status: instance`
whose only evidence was `validation/instance-checks.bc` — bc arithmetic, not
Lean. (`abb9d0f`)

## 2.0.0 — 2026-09-14

**MAJOR.** **5 prerequisite edges the node text uses were missing from the
graph.** `build/check-edge-evidence.py` (new) reads each node's declared
dependencies and proof prose — written independently of the edge list — and
found results the text cites that the graph did not carry. A prerequisite
chain queried before this commit was incomplete, silently, which is what makes
this MAJOR: the capsule offers "the minimum prerequisite chain" as a headline
use. Separately, **3 `results/*.yaml` did not parse at all** (an unescaped
apostrophe, unquoted flow mappings); this capsule had no
`check-consistency.py`, so nothing had ever loaded them. Also new:
`validation/mutation-check.sh`, which plants five graph defects per build and
asserts each is caught — hygiene checks pass a deleted *or* an invented edge.
(`904ea6a`)

## 1.0.0 — 2026-09-06

First release, verified at release. (`c98dcf4`)
