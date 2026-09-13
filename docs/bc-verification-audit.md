# Audit: the `bc` verification pattern across every skill

**Date:** 2026-09-13. **Trigger:** building `math-linear-algebra` surfaced that
a harness that checks only `bc`'s exit status passes a run whose assertions
failed — `bc` reports *interpreter* errors, never a false claim. This audit
re-checks every skill using the pattern.

**Scope:** 24 `.bc` files across 20 skills, plus `templates/verification/`.

## Status: REMEDIATED (2026-09-13)

All 24 harnesses now assert their claims and fail the run on a wrong value.
Every one was negative-contrast tested — corrupt a value, confirm a nonzero
exit, revert — and all 24 verified green afterwards. The findings below are
kept as the record of what was wrong and how it was demonstrated.

Fixed in three passes: the 6 methodology skills (`7b7a3e3`), the 4 math
capsules whose oracles were already present (`d863651`), and the remaining 5
capsules plus the 4 that had no build script at all.

### Defects found by writing the assertions

Seven, beyond the missing checks themselves:

1. **`statistics`** — two CRLB checks were **vacuous**: `crlbbern` and
   `varbern` were the *same expression*, and the Poisson line was literally
   `(lam/n)/(lam/n)`. Both printed the expected `1` by construction. Now routed
   through the Fisher information.
2. **`visualization-design`** — the zero-baseline lie-factor check was vacuous
   the same way (`shownc` and `datac` identical).
3. **`control-systems`** — the file computed a sampling ceiling of `2/wn_cl =
   1.0 s` and its own comment called `Ts = 0.8 s` "far outside" it. `0.8 < 1.0`.
   The Python section's divergence at 0.8 s comes from the PID loop's higher
   bandwidth, not from this bound.
4. **`physics-thermodynamics`** and the three other dimensional-check files —
   the `d5`/`d6`/`p4`/`d3` helpers **printed** the exponent difference and
   returned nothing, with the result sunk into a throwaway variable. A
   dimensionally inconsistent formula printed and passed.
5. **`chemistry-foundations`** and **`chemistry-electrochemistry`** — the `.bc`
   files had **no trailing `quit`**, so running them exactly as their READMEs
   documented left `bc` reading stdin and **hung** on an interactive terminal.
   Very likely why they were never automated.
6. **A bare `grep -q FAIL` gives false positives.** `visualization-design`
   legitimately prints `(claim: < 3 -> FAILS as a standalone cue)`, which made
   a naive grep fail a *passing* run. The marker is now `*** FAIL`.
7. **Tolerances were guessed, not derived.** In `physics-newtonian` the
   small-angle checks initially failed against tolerances tighter than the next
   Taylor term (`x^4/24 = 4.2e-6`) and the `scale = 6` truncation floor. Each
   tolerance is now justified in a comment against the actual error term.

### Structural changes

- The 4 capsules with no build script (`chemistry-foundations`,
  `chemistry-electrochemistry`, `physics-newtonian`,
  `physics-thermoacoustics`) now have a `build/all.sh` on the sibling pattern,
  and their READMEs lead with it.
- Every runner greps for `*** FAIL` **and** a pass banner, and redirects
  `< /dev/null` so a missing `quit` cannot hang a build.
- `templates/verification/` was rewritten first, since it was the source
  propagating the weakness.

## Original findings

| category | count | what it means |
|---|---|---|
| **OK — a wrong result fails the run** | 4 | `.bc` emits `FAIL` lines; the runner captures the output and greps for them |
| **BROKEN — verdicts computed and ignored** | 1 | `.bc` emits `FAIL` lines that no one reads; run reports success |
| **UNASSERTED — eyeball only** | 15 | `.bc` prints numbers with a prose annotation (`(want >= 4.5)`, `(match)`); nothing compares them |
| **NOT AUTOMATED** | 4 | the `.bc` is documented in the README but no script ever runs it |

Only **4 of 24** `bc` harnesses would catch a wrong number.

## The table

| skill | file | category |
|---|---|---|
| `causal-sandbox` | `verification/checks.bc` | OK |
| `skill-evolution` | `verification/checks.bc` | OK |
| `temporal-data-modeling` | `verification/checks.bc` | OK |
| `math-linear-algebra` | `validation/instance-checks.bc` | OK |
| **`hypergraph-reasoning`** | `verification/checks.bc` | **BROKEN** |
| `control-systems` | `verification/checks.bc` | unasserted |
| `design-of-experiments` | `verification/checks.bc` | unasserted |
| `simulation` | `verification/checks.bc` | unasserted |
| `statistics` | `verification/checks.bc` | unasserted |
| `unknown-discovery` | `verification/checks.bc` | unasserted |
| `visualization-design` | `verification/checks.bc` | unasserted |
| `bayes-bridge` | `validation/instance-checks.bc` | unasserted |
| `math-logic-and-proof` | `validation/instance-checks.bc` | unasserted |
| `math-number-systems` | `validation/instance-checks.bc` | unasserted |
| `math-probability` | `validation/instance-checks.bc` | unasserted |
| `math-real-analysis` | `validation/instance-checks.bc` | unasserted |
| `math-sets-functions-cardinality` | `validation/instance-checks.bc` | unasserted |
| `math-statistics` | `validation/instance-checks.bc` | unasserted |
| `physics-acoustics` | `validation/instance-checks.bc` | unasserted |
| `physics-thermodynamics` | `validation/dimensional-checks.bc` | unasserted |
| `templates/verification` | `checks.bc` | unasserted (and therefore propagates) |
| `chemistry-electrochemistry` | `validation/dimensional-checks.bc` | not automated |
| `chemistry-foundations` | `validation/dimensional-checks.bc` | not automated |
| `physics-newtonian` | `validation/dimensional-checks.bc` | not automated |
| `physics-thermoacoustics` | `validation/dimensional-checks.bc` | not automated |

## Reproductions

Each was demonstrated by corrupting a value and confirming the harness still
reported success. All corruptions were reverted and every harness re-verified
green afterwards.

**`hypergraph-reasoning` (BROKEN).** Its `checks.bc` genuinely computes verdicts
— `if (scorey > scorex) print "PASS..."` / `if (scorey <= scorex) print "FAIL"`.
Forcing the `FAIL` branch:

```
run.sh EXIT = 0
FAIL lines printed: 1
ALL CHECKS PASS
```

The `FAIL` is printed and the run reports success. `run.sh` has `set -e`, which
does nothing here because `bc` exits 0 regardless.

**`visualization-design` (unasserted).** Corrupting the WCAG contrast formula
(`+ 0.05` → `+ 0.95`):

```
black on white = 2.05263157  (want >= 4.5)
ALL CHECKS PASS      (exit 0)
```

The output states the want, violates it by more than 2×, and passes.

**`design-of-experiments` (unasserted).** Forcing the sample size to a nonsense
value prints `n per arm (raw) = 99999` and exits 0.

**`math-probability` (unasserted).** This one is the most instructive. Its
`.bc` already computes an **independent oracle** — `va` from the closed form
`p(1-p)`, and `vs` by direct summation over the support — which is exactly the
right verification design. Corrupting the closed form to `p(1+p)` makes the two
disagree (.39 vs .21), and the printed line still reads `(match)`:

```
math-probability build/all.sh  →  ALL OK   (exit 0)
```

The oracle is there. It is simply never compared.

## Why "unasserted" is the interesting category, not a technicality

The pattern in all 15 is the same: compute a number, print it next to a prose
claim about what it should be, and rely on a reader noticing. That is a
**documented example**, not a check. It has two specific failure modes:

1. **Regression is invisible.** Nothing fails when a formula drifts, so these
   files cannot protect the capsules they belong to.
2. **It reads as verification.** Every one of these skills' README carries a
   "Verification" row citing the `.bc` file, and `docs/verifying-skills.md`
   presents the pattern as the shared contract. The claim is stronger than the
   mechanism.

The fix is mechanical wherever an oracle is already computed (as in
`math-probability`): compare the two numbers and print `FAIL` on mismatch, then
have the runner grep for it.

## The two `bc` facts behind this

1. **The exit status reports interpreter errors, not false claims.**
   *(Corrected 2026-09-13 — the first version of this document overstated
   this as "there is no failure exit status", which is wrong.)*

   `bc` has a documented, well-populated exit vocabulary (`man bc`, EXIT
   STATUS): **0** no error, **1** math error (divide by zero, sqrt of a
   negative), **2** syntax/parse error, **3** undefined function, **4** file
   not found. Verified empirically on bc 7.0.3.

   What it cannot report is that your arithmetic **claim was false** — to a
   calculator that is a *value*, not an error — and `quit` takes no status
   argument (`quit 1` exits 0).

   The consequence is sharper than "no protection": `set -e` catches a
   **broken** file (typo, missing file, bad function) and never a **wrong**
   one. Partial protection that reads as full protection is exactly why this
   survived in 20 of 24 harnesses.

   A deliberate `1/0` is an available escape hatch (`if (fails > 0) { zz = 1/0 }`
   → exit 1). **`templates/verification/` now ships both signals**: the grep
   names *which* claim failed, and the forced nonzero exit backstops a runner
   that forgets to grep. Verified — a naive `set -e; bc checks.bc` against the
   updated template now catches a false claim, where before it passed.

   A third, independent trap: **a pipe replaces `bc`'s status with the last
   command's**. `bc f.bc | tail` reports success even when `bc` died parsing.
   This document's own author hit that while measuring the problem.
2. **`abs` is a reserved name in macOS `bc`.** `define abs(x)` fails with
   "bad function definition" even without `-l`. Use another name (`aval`).

Both are now recorded in `docs/verifying-skills.md`.

## The working pattern

From `math-linear-algebra/validation/instance-checks.bc` — note that BSD `bc`
functions take **numeric arguments only**, so the message is printed at the call
site rather than passed to the helper:

```bc
define aval(x) {
  if (x < 0) { return (-x) }
  return (x)
}
define chk(claim, tol) {          /* 1 on FAILURE, else 0 */
  if (aval(claim) <= tol) { return (0) }
  return (1)
}
fails = 0
bad = 0

bad = chk(detc - deta*detb, 0); if (bad) { print "*** FAIL: det(AB) = det(A)det(B)\n" }
fails += bad

/* ... */
if (fails == 0) { print " ALL INSTANCE CHECKS PASSED.\n" } else {
  print " *** ", fails, " CHECK(S) FAILED\n"
}
```

and in the runner:

```sh
bc -q -l validation/instance-checks.bc > build/instance-checks.out 2>&1
if grep -q "ALL INSTANCE CHECKS PASSED" build/instance-checks.out \
   && ! grep -q '\*\*\* FAIL' build/instance-checks.out; then
  echo "bc: ok"
else
  echo "bc: FAILED" >&2; grep '\*\*\* FAIL' build/instance-checks.out >&2; exit 1
fi
```

Both conditions are needed: the pass banner alone would be satisfied by a file
that never ran its later sections, and the absence of a failure marker alone
would be satisfied by a file that crashed before printing anything.

**Grep for the marker `*** FAIL`, never bare `FAIL`.** Descriptive text
legitimately contains the word — `visualization-design` prints
`(claim: < 3 -> FAILS as a standalone cue)`, which made a bare `grep -q FAIL`
fail a *passing* run during this remediation.

**Every harness written to this pattern must be negative-contrast tested** —
corrupt one value, confirm the run fails, revert. An assertion that has never
been seen to fail is not known to be an assertion.
