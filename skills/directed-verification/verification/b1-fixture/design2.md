# Fixturing behaviour 1 — run 2

Run 1 produced no result. `RESULT.md` records why. This is the rerun, with the
three recorded fixes applied and one more the failure itself suggested.

## What changed

**1. The subject is verified correct before it is used.** Run 1 assumed it;
the assumption was false, and a good harness failing on a buggy subject scored
`BROKEN`. `subject2/rounding.py` takes two integers, so the arithmetic is
exact and correctness is decidable — checked against an independent
`Fraction`-based oracle over **28,824 cases, zero mismatches**. `score2.sh`
re-asserts this as a **precondition** and refuses to score if it ever fails.

**2. The plant has headroom.** Run 1 planted half-even, which differs at
*every* tie — any tie-aware suite catches it, leaving no room for the
instruction to matter. Run 2 plants *ties toward +infinity*, which differs at
**negative ties and nowhere else**: 931 of 28,824 cases, all `neg-tie`,
verified. `5/2 -> 3` under both; `-5/2` is `-3` correct, `-2` planted. Catching
it requires testing a negative tie — the discipline step a competent suite can
skip.

**3. Spawn order is interleaved.** Run 1 spawned all of arm A then all of arm
B; the session limit killed four of five arm-B agents and left arm B at n=1.
Run 2 interleaves A1 B1 A2 B2 … so a truncation costs both arms roughly
equally instead of destroying the comparison.

## The contamination confound, analysed rather than waved at

Subjects run outside the repository directory, but they are spawned from a
session in it, and the corpus's 52 skills — including `test-writing`, whose
behaviours run 1's subjects mirrored closely — may be available to them.

**This cannot be eliminated, and it does not bias Δ.** Both arms have identical
access, so priming raises both arms equally. What it threatens is a **ceiling
effect**: if primed subjects all reach `CATCHES`, there is no headroom and the
comparison is uninformative rather than wrong. Fix 2 exists to preserve that
headroom.

So a **null result remains ambiguous** — no difference, or no room for one —
while a **positive result is still interpretable**, because contamination
cannot manufacture an asymmetry between identically-primed arms.

## Pre-registered interpretation

Unchanged from run 1. Δ = (B catches) − (A catches), out of 5 each.

| Δ | Meaning |
|---|---|
| **≥ +3** | claim supported; behaviour 1 earns its place |
| **+1 or +2** | weakly supported; soften to "tends to", state n=5 |
| **0** | **refuted**; strike behaviour 1 rather than reword it |
| **negative** | refuted, and stranger; investigate before believing |

**Ceiling rule:** if arm A scores 5/5 `CATCHES`, report *no headroom* rather
than *refuted* — the design could not have detected a difference, which is a
statement about this fixture and not about the claim.

**Attrition rule:** if either arm finishes with fewer than 4 scored subjects,
report incomplete rather than compute Δ. Run 1's mistake was not having this
written down.

## Still true from run 1

This remains `claim-fixture`'s first plausible **positive**, and that method
still has two refutations and no confirmations to its name.
