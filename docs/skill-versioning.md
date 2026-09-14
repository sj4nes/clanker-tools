# Versioning a skill

Every `SKILL.md` carries a `version:` in its frontmatter. This document says
what the three numbers mean, when each moves, and what the field is *for*.

It exists because the field was decorative. On 2026-09-13 both copies of the
`bc` skill — the repo's and a fork in `~/.claude/skills` that had drifted 29
lines, including a correctness fix the repo's verification had forced — read
`version: 1.0.0`, with byte-identical descriptions. Nothing distinguished the
copy that taught a broken idiom from the copy that taught the fixed one. See
[`bc-verification-audit.md`](bc-verification-audit.md).

---

## 1. What the number is for

**To let a reader — human or agent — tell whether the text in front of them is
the current text, and how much it matters if it isn't.**

That is a different job from semver's "did the API break". A skill is an
instruction document, so the question is not *will my code still compile* but
**what do I have to do about the difference**:

| | Level | What changed | What the reader must do |
|---|---|---|---|
| `MAJOR` | **the skill was wrong** | it prescribed something that does not work, or that produces an incorrect result | **re-do work done under the old text.** It may be wrong. |
| `MINOR` | **a statement changed or grew** | guidance reworded to ask for something different, a behaviour or section added, another skill absorbed, a threshold moved | **re-read before relying on it.** Nothing to re-do. |
| `PATCH` | **nothing semantic** | spelling, punctuation, formatting, a repaired link, a typo in prose | **nothing.** |

So `MAJOR − 1` is the number of times this skill has been **wrong** since
release. That is a signal worth being able to read at a glance, and a number
worth being reluctant to increment.

## 2. When each one moves

**MAJOR** — the skill prescribed something that **does not work**, or that
**produces an incorrect result**. Both limbs count, and the difference between
them is worth naming because it is tempting to bump only the first:

- *silently wrong* — you get an answer, it is wrong, and nothing tells you
  (`bc`'s rounding, `tsort`'s cycle check, `math-number-systems`' truncated
  `meaning`). The dangerous kind.
- *loudly broken* — the recipe errors or hangs, so you never build on a wrong
  result (`csplit`'s GNU-only flags, the four capsule READMEs that hung).

A loud break is still MAJOR: the reader was told to do something that does not
work and has to change their approach. "Loud or silent" is also a judgement
call that would produce inconsistent bumps, where "did the prescribed thing
work?" is checkable.

Real examples from this repo:

- `bc` prescribed `((x * f + 0.5) / 1) / f` for rounding. `x / 1` does not
  truncate on the `bc` that ships with macOS, so the idiom silently returned
  the unrounded value. Anyone who used it has wrong numbers.
- `tsort` said to check the exit status for a cycle. BSD `tsort` **exits 0** on
  a cycle. Any pipeline built on that guidance had no cycle detection at all.
- `csplit`'s transactional template used `{*}`, `-b` and `--suppress-matched`,
  none of which exist on BSD `csplit`. The recipe did not run.
- `math-probability`'s `proof-checks.lean` named `Prob.markov_finite` in its
  header while the theorem body was missing — a claim of machine-verification
  for something no longer verified.

**MINOR** — the guidance is different, but the old text was not false:

- `test-writing` gained two behaviours (run the check against code you believe
  correct; report the branch-coverage number) and absorbed the
  `test-oracle-design` candidate. Someone following the old text did *less*
  than the skill now asks — but nothing they did was wrong.
- `ptx` gained `-W '[A-Za-z0-9_]+'` for whole-identifier indexing and `ptx -A`
  for `file:line:` provenance. Additions; the existing caveat was confirmed
  correct, not corrected.

**PATCH** — no reader behaviour changes. Prose typos, a broken relative link,
table alignment, a rewrapped paragraph.

### Which files count

The version tracks the skill's **instruction content**: `SKILL.md`,
`references/`, `templates/`. For a capsule skill it also covers `nodes/`,
`results/`, `validation/`, **and the capsule's own `README.md`** — a wrong
formula check, a missing Lean theorem body, a silently truncated `meaning`
field, or a documented command that does not run are all wrong claims, and
claims are the deliverable. (The capsule README is how a reader runs the
capsule; it earns its place on this list because four capsules documented a
`bc` invocation that **hung**, waiting on stdin.)

A change to `verification/` alone does **not** move the version. The harness is
how we find out whether the instruction content is right; it is not the
content. (When a harness fix *reveals* that the content was wrong, the content
change is what bumps the number.)

### The test is whether a reader could already have been holding the old text

The first formulation of this rule was "release-verification fixes do not
count", and adjudicating the corpus on 2026-09-13 showed that to be the wrong
cut. It is not *when in the process* the fix happened, it is **whether the wrong
text was ever published**:

> A correction bumps `MAJOR` if there was a published state carrying the error —
> a commit a reader could have read, copied, or been served. A fix applied to
> text that never left the authoring session is how the skill reached `1.0.0`.

The worked example is `bc`, and the margin is six minutes:

    13:38  9dd8165  bc, csplit, tsort, ptx, ed committed
    13:44           copied into ~/.claude/skills   <-- a reader now holds it
    14:10  ffc32ff  bc / csplit / tsort portability bugs fixed
    15:10  6fa714f  ptx keyword-regex behaviour corrected and extended

Those look like a release verification pass, and by intent they were one. But
the text had already been published and copied, and the copy went on serving
`bc`'s broken rounding idiom for a week. So they are `MAJOR` (and `ptx`'s
additions are `MINOR`). Meanwhile the capsules whose verification ran *inside*
their release commit — `physics-thermodynamics`, `math-real-analysis`,
`math-sets-functions-cardinality` and the rest — never exposed a wrong state,
and stay at `1.0.0` no matter how much was fixed on the way in.

This is what keeps `MAJOR` readable. Without it, every skill would start at
`2.0.0` or `3.0.0` purely from drafting, and the number would record how messy
the authoring was rather than how often a reader was misled. The README's
Verification table is where release-pass findings live; that is their record,
not the version.

## 2b. The 2026-09-14 graph-evidence round

Eleven capsules went `MAJOR` in one commit, which is worth explaining rather
than leaving as an unexplained cluster.

`build/check-edge-evidence.py` (see
[`verifying-skills.md` §5a](verifying-skills.md)) checks the dependency graph
against the node text, which was written independently of it. It found **36
prerequisite edges the node text uses and the graph did not carry**, spread over
eleven capsules, plus **7 `results/*.yaml` in two capsules that did not parse at
all**.

A missing edge is `MAJOR` under §2's silently-wrong limb. Every capsule's
`SKILL.md` offers "the minimum prerequisite chain for a result" as a headline
use; a chain with a required result missing is an **incorrect answer** presented
as complete, and nothing told the reader. The published state carried it, so the
published-state test is met too.

Two changes in the same commit are deliberately **not** `MAJOR`:

- `physics-newtonian` → `2.1.0`. One formula entry had no `Prereqs:` line at
  all. The *graph* was right, so a prerequisite query answered correctly; the
  human-facing entry merely omitted the list. Missing information the graph
  still holds is `MINOR`.
- `physics-acoustics` and `physics-thermodynamics` → **unchanged**. Their only
  diffs are harness wiring and a regenerated `tsort` order that is a different
  but equally valid linearisation. Nothing a reader relied on was wrong.

`math-theorem-tree` and `physics-formula-tree` went `1.1.0`: they now prescribe
two checks they did not before. What they prescribed previously was not false —
the hygiene checks did exactly what they claimed, they just never claimed to
catch a wrong edge.

---

## 2c. The 2026-09-14 Lean-core round

The same day's second audit, same shape. `lean file.lean && echo ok` exits **0**
on a `sorry`, on an `axiom` (which makes `3 = 4` provable), and on a "core"
that is a closed numeral identity — so nothing in any capsule build had ever
tested a `lean_status` claim. `check-lean-cores.py` found **41 problems in six
capsules**, including **19 nodes claiming `lean_status: core` with an empty
`lean_ref`**.

`MAJOR` where the claim was **false**: a node asserting `core` is asserting
*this capsule's `.lean` file proves the general statement*, and a reader who
trusted it skipped verification they would otherwise have done. That is the
same failure the 2026-09-13 re-base already charged `math-probability` `2.0.0`
for — "`Prob.markov_finite`'s body was missing behind a header that claimed
it" — now found at scale. So `math-probability` → `4.0.0`,
`math-statistics` → `3.0.0`, and `math-number-systems` / `math-sets-functions-
cardinality` → `4.0.0` / `3.0.0` for statuses whose only evidence was a **bc**
check.

`MINOR` where the claim was **true but unverifiable by machine**:
`math-logic-and-proof`'s five `core` refs described the proof technique in prose
instead of naming the declaration — and the declarations were all there, exactly
as claimed. Nobody was misled; the refs just could not be checked. Likewise
`math-real-analysis`'s four `core-arith` labels, a vocabulary outside the
documented set pointing at real, existing sections.

No proof anywhere was wrong: every `.lean` file compiled clean before and after,
and the repo contains no `sorry` and no `axiom`. What was wrong was the index.
That distinction is what keeps these bumps meaningful — `MAJOR` is for a reader
who was told something false, not for a repository that tightened its own gates.

`math-linear-algebra` had **zero** findings and takes a `PATCH` for a changelog
note. It already carried the guard (`leanmap.py` + `check-lean-refs.py`); the
audit generalised it to its six siblings.

---

## 3. The 2026-09-13 re-base

Before this document, the leading digit encoded **kind**, not maturity: all ten
CLI-primitive skills read `1.0.0`, twenty-eight methodology and capsule skills
read `0.1.0`, four had **no `version:` field at all**, and four carried ad-hoc
minor bumps. None of it was comparable across skills.

Every skill was re-based to **`1.0.0` = "as verified at release"**, then the
rules above applied to what is documented to have happened *since*:

| Skill | Was | Now | Why |
|---|---|---|---|
| `bc` | 1.0.0 | **2.0.0** | the `x / 1` truncation idiom was wrong on macOS |
| `tsort` | 1.0.0 | **2.0.0** | cycle detection by exit status does not work on BSD |
| `csplit` | 1.0.0 | **2.0.0** | the transactional template used GNU-only flags |
| `math-probability` | 0.1.0 | **2.0.0** | `Prob.markov_finite`'s body was missing behind a header that claimed it |
| `math-number-systems` | 0.1.0 | **2.0.0** | an unquoted comma in a `{ … }` flow scalar **silently truncated** `meaning` in three `results/*.yaml` (`integer`, `rational_number`, `lub_property`) for two days |
| `physics-newtonian`, `physics-thermoacoustics`, `chemistry-foundations`, `chemistry-electrochemistry` | 0.1.0 | **2.0.0** | each README documented `bc -q -l validation/…bc` with no stdin redirect, so the capsule's own validation command **hung** when run as written — for 8 days |
| `ptx` | 1.0.0 | **1.1.0** | `-W` and `-A` added post-release |
| `test-writing` | 0.1.0 | **1.1.0** | behaviours 5–6 and fixture subject F added post-release |
| `simulation`, `unattended-automation`, `temporal-data-modeling` | 0.2.0 | **1.1.0** | one recorded post-release revision each, preserved as a minor |
| `agent-automation` | 0.3.0 | **1.2.0** | two recorded post-release revisions, preserved as minors |
| `bayes-bridge`, `physics-acoustics`, `math-linear-algebra`, `physics-formula-atlas` | *(none)* | **1.0.0** | field was missing entirely |
| everything else | 0.1.0 / 1.0.0 | **1.0.0** | verified at release; no documented post-release change |

Nine skills carry a `2.0.0`. Fourteen are marked "verified, **fixed**" in the
README Verification table, and the two sets overlap only partly — the marker
records *that something was fixed*, not whether a reader was ever exposed to the
broken text, which is the question this field answers. `ed` was the one
installed copy that had not drifted at all, and stays `1.0.0`.

**The first pass under-counted and was corrected.** Four skills were left at
`1.0.0` because the README's prose did not make clear whether the *instruction
content* or the *harness* had been wrong. Adjudicating them against git history
on 2026-09-13 moved five skills to `2.0.0` and confirmed `ptx` at `1.1.0`, and
it changed two of this document's own rules — the published-state test above
replaced "release-verification fixes do not count", and the capsule `README.md`
joined the list of files that count. The lesson: **a version backfill is a
git-history question, not a changelog-prose question.** Prose records what the
author noticed; history records what a reader could have been holding.

Still, prefer under-counting when the history is genuinely ambiguous. An
inflated `MAJOR` is a false claim about the skill's past, and this field exists
to stop false claims, not to make new ones.

## 4. Mechanics

- Bump in the same commit as the change. A version that lags is worse than no
  version, because it actively asserts something false.
- One bump per commit, at the highest level the commit reaches: a commit that
  fixes a bug *and* a typo is a `MAJOR`.
- Never re-use or decrement a number.
- `sh tools/check-skills.sh` asserts every skill has a parseable
  `MAJOR.MINOR.PATCH` and that every `.claude/skills` symlink resolves. It is a
  gate, not a reminder — see [`verifying-skills.md`](verifying-skills.md) §8.

## 5. What this does not solve

A version tells a reader that two texts differ and how much to care. It does
**not** tell them *which* text they are holding — that needs the two copies not
to exist, which is why `~/.claude/skills` now symlinks into this repo instead of
copying from it. Versioning is the backstop for when a copy escapes anyway.
