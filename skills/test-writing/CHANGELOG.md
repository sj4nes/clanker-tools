# Changelog — test-writing

Versions follow [`docs/skill-versioning.md`](../../docs/skill-versioning.md):
`1.0.0` means "as verified at release"; **MAJOR** = the skill was wrong (re-do
work done under the old text), **MINOR** = a statement changed or grew (re-read
it), **PATCH** = nothing semantic.

Entries are **version-anchored, not per-commit**: one entry per version this
skill has held. Everything before 2026-09-14 was reconstructed on 2026-09-14
from git history and `docs/skill-versioning.md`, so it records the version
history rather than every change. The full record is

    git log -- skills/test-writing/

## 1.2.0 — 2026-09-17

**MINOR: the skill's stated reason was overstated; no prescription changed.**
Re-read the opening. It said agents fell back to poor default testing "across
every condition the danluu eval measured" and that tutorial-style skills
performed "worse than no skill". Read against the article (book ledger C-I-01
to C-I-04), both are too strong: the fallback was across the named techniques,
and one skill did worse than no instructions only on the runs it influenced.
The overstatement was present in the first commit that cited the eval
(`2c387db`) and was copied from `docs/verifying-skills.md` §7, corrected in the
same commit as this entry.

Behaviour 3's founding default (expected values copied from the code's output)
is still Yossi Kreinin's hypothesis, not an observation (ledger C-I-17). That
is a separate decision and is not made here.

## 1.1.0 — 2026-09-13

**MINOR.** Behaviours 5–6 and fixture subject F added post-release, and the
`test-oracle-design` candidate absorbed. Someone following the old text did
*less* than the skill now asks — but nothing they did was wrong. Recorded in
the version re-base (`0fbb03c`, adjudicated `f921886`); see
[`docs/skill-versioning.md` §3](../../docs/skill-versioning.md). (`0fbb03c`)

## 1.0.0 — 2026-09-13

First release, verified at release. (`352703c`)
