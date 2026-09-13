# Audit: the `bc` verification pattern across every skill

**Date:** 2026-09-13. **Trigger:** building `math-linear-algebra` surfaced that
`bc`'s `quit` **always exits 0**, so a harness that checks only the exit status
passes a run whose assertions failed. This audit re-checks every skill using the
pattern.

**Scope:** 24 `.bc` files across 20 skills, plus `templates/verification/`.

## Result

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

1. **`quit` always exits 0.** There is no way to make `bc` signal failure
   through its exit status. The runner must inspect the **output**. This is why
   `set -e` gives no protection at all in these harnesses.
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
