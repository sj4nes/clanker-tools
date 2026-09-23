# Changelog — math-number-systems

Versions follow [`docs/skill-versioning.md`](../../docs/skill-versioning.md):
`1.0.0` means "as verified at release"; **MAJOR** = the skill was wrong (re-do
work done under the old text), **MINOR** = a statement changed or grew (re-read
it), **PATCH** = nothing semantic.

Entries are **version-anchored, not per-commit**: one entry per version this
skill has held. Everything before 2026-09-14 was reconstructed on 2026-09-14
from git history and `docs/skill-versioning.md`, so it records the version
history rather than every change. The full record is

    git log -- skills/math-number-systems/

## 4.1.0 — 2026-09-22

**MINOR.** "How to use this capsule" step 1 pointed at `indexes/topic-index.md`, which this capsule has never had — six
other capsules do. The dead link was found by the new corpus link
gate (`tools/check-links.py`, `docs/verifying-skills.md` §7a).

Step 1 now names `symbol-index.md` and `status-index.md`, which exist, and says the topic index is missing rather than advertising
a file that is not there. MINOR because a reader is sent somewhere
different, not merely because a path was repaired. Building the
index is filed in `BACKLOG.md`; no node, edge or result changed.

## 4.0.0 — 2026-09-14

**MAJOR.** Two nodes carried `lean_status: instance` whose only evidence was
`validation/instance-checks.bc` — bc arithmetic, not Lean. `integer`'s
`core-arith` label, outside any vocabulary, became `partial`. (`abb9d0f`)

## 3.0.0 — 2026-09-14

**MAJOR.** **3 prerequisite edges the node text uses were missing from the
graph.** `build/check-edge-evidence.py` (new) reads each node's declared
dependencies and proof prose — written independently of the edge list — and
found results the text cites that the graph did not carry. A prerequisite
chain queried before this commit was incomplete, silently, which is what makes
this MAJOR: the capsule offers "the minimum prerequisite chain" as a headline
use. Also new: `validation/mutation-check.sh`, which plants five graph defects
per build and asserts each is caught — hygiene checks pass a deleted *or* an
invented edge. (`904ea6a`)

## 2.0.0 — 2026-09-13

**MAJOR.** An unquoted comma in a `{ … }` flow scalar **silently truncated**
the `meaning` field in three `results/*.yaml` (`integer`, `rational_number`,
`lub_property`) for two days. Recorded in the version re-base (`0fbb03c`,
adjudicated `f921886`); see [`docs/skill-versioning.md`
§3](../../docs/skill-versioning.md). (`0fbb03c`)

## 1.0.0 — 2026-09-06

First release, verified at release. (`8e99a16`)
