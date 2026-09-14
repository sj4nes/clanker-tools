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

**MAJOR** — the skill told you something false, and someone following it would
get a wrong result. Real examples from this repo:

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
`references/`, `templates/`. For a capsule skill it also covers `nodes/` and
`validation/` — a wrong formula check or a missing Lean theorem body is a wrong
claim, and claims are the deliverable.

A change to `verification/` alone does **not** move the version. The harness is
how we find out whether the instruction content is right; it is not the
content. (When a harness fix *reveals* that the content was wrong, the content
change is what bumps the number.)

### Release-verification fixes do not count

A skill reaches `1.0.0` when it has been verified. Everything fixed **during
that first verification pass** — the wrong constant in a reference snippet, the
`bc` identifier that does not parse, the Lean tactic that needs Mathlib — is how
it *got* to `1.0.0`. Those are not corrections to a shipped skill and they do
not bump anything.

This is what keeps `MAJOR` readable. Without it, every skill would start at
`2.0.0` or `3.0.0` purely from drafting, and the number would record how messy
the authoring was rather than how often the published text has been wrong. The
README's Verification table is where release-pass findings live; that is their
record, not the version.

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
| `ptx` | 1.0.0 | **1.1.0** | `-W` and `-A` added post-release |
| `test-writing` | 0.1.0 | **1.1.0** | behaviours 5–6 and fixture subject F added post-release |
| `simulation`, `unattended-automation`, `temporal-data-modeling` | 0.2.0 | **1.1.0** | one recorded post-release revision each, preserved as a minor |
| `agent-automation` | 0.3.0 | **1.2.0** | two recorded post-release revisions, preserved as minors |
| `bayes-bridge`, `physics-acoustics`, `math-linear-algebra`, `physics-formula-atlas` | *(none)* | **1.0.0** | field was missing entirely |
| everything else | 0.1.0 / 1.0.0 | **1.0.0** | verified at release; no documented post-release change |

Fourteen skills are marked "verified, **fixed**" in the README Verification
table. Only four of those bump, because the other ten were fixed *during* their
release verification pass — see the rule above. `ed` was the one installed copy
that had not drifted at all, and stays `1.0.0`.

**The backfill under-counts on purpose.** Where the record does not say clearly
whether the *instruction content* was wrong or the *harness* was, the skill
stays at `1.0.0`. An inflated `MAJOR` is a false claim about the skill's
history, and this field exists to stop false claims, not to make new ones.

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
