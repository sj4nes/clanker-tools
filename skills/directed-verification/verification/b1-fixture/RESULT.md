# Result: INVALID. The fixture was broken, and arm B did not run.

Run 2026-09-15. **No verdict is reported, and none should be inferred.**

## Reason 1: the subject was not correct

The design assumed `subject/money.py` was correct, so that a harness failing on
it could only mean the harness was wrong. It was not correct. It carries **two
real defects** I did not intend:

```
  -5 x 0.5    returns -2,  spec requires -3
 -25 x 0.1    returns -2,  spec requires -3
```

`int()` truncates toward zero, so `remainder` is negative for every negative
product and the `remainder < 0.5` branch swallows all of them — negatives are
never rounded at all, and the documented `.5` branch is unreachable for them.
Separately, `remainder == 0.5` almost never fires for non-dyadic rates
(`90 * 0.35` is `31.499999999999996`), so the tie branch the docstring makes a
point of is dead for most rates a human would write.

**Consequence: a good harness fails on the clean subject, and `score.sh` calls
that `BROKEN`.** All five arm-A subjects scored `BROKEN` — for doing the job
correctly. The measurement inverts quality for exactly the subjects who do best.

## Reason 2: arm B has n=1

Four of five arm-B agents terminated on an API session limit mid-run (B1, B2,
B4, B5). Only B3 completed. Even with a sound fixture there would be nothing to
compare.

## What was observed, and what that is worth

Stated as observation, not measurement, because the instrument was broken:

All six completed subjects — **five from arm A, which was never told to make
the tests able to fail** — found both defects, built independent oracles
(`decimal.ROUND_HALF_UP`, `fractions.Fraction`, hand re-derivation from the spec
sentence), used metamorphic relations needing no expected value, reported
branch-coverage fractions for their generators, asserted their fixtures'
asymmetry rather than assuming it, and ran their checks against a
believed-correct reference to confirm the checks were not failing on everything.
Two reported catching bugs in **their own tests** before shipping.

That is what arm B's extra sentence was supposed to cause. Arm A did it
unprompted. **This is suggestive of refutation and is not evidence of it**,
because the scoring instrument could not distinguish arms.

## A confound that would have mattered anyway

The subjects ran inside this repository, where all 52 skills — including
`test-writing`, whose six behaviours their reports mirror closely — are wired
into `.claude/skills` and available to them. Their behaviour may reflect the
corpus's own skills being loaded rather than any default.

A rerun must place subjects outside the repo. Neither earlier fixture was
affected: both were scored on an unforgeable artifact, and priming could not
manufacture a stderr string or a passing patch. Here, where the measure is the
*quality* of produced tests, priming is a live alternative explanation.

## To rerun

1. **Fix the subject**, or better, invert the design: make the subject
   deliberately correct-but-subtle and verify that by an independent oracle
   *before* any subject sees it. The scorer's `clean=0` precondition was an
   assumption and should be an asserted precondition.
2. **Run subjects outside the repository**, with no skills available.
3. **Keep the arms matched** and re-run both, n >= 5 each.

## What this cost, and what it is worth

Ten agents, no result, and a day's claim still unmeasured. Against that: the
fixture's own defect was found by the subjects rather than by me, which is the
fourth occasion in this corpus's history where **the test was wrong and the
subject was fine** — the behaviour this very skill's chapter 3 is about,
happening to the experiment built to test its chapter 1.
