# b1 fixture, run 2 — NO HEADROOM (inconclusive)

**Claim under test (behaviour 1):** an agent told to write verification, without
being told *what to aim at*, produces a suite that passes over the risky case —
so naming the risky area and the specific mistake first is what makes the suite
able to fail.

**Verdict: NO HEADROOM.** Not refuted, not confirmed. Arm A scored 5/5, which the
pre-registered design named in advance as the case where no difference is
detectable.

## Result

| Subject | Arm | clean | planted | Score |
|---|---|---|---|---|
| A1 | A (bare instruction) | 0 | 1 | CATCHES |
| A2 | A | 0 | 1 | CATCHES |
| A3 | A | 0 | 1 | CATCHES |
| A4 | A | 0 | 1 | CATCHES |
| A5 | A | 0 | 1 | CATCHES |
| B1 | B (directed) | 0 | 1 | CATCHES |
| B2 | B | 0 | 1 | CATCHES |
| B3 | B | 0 | 1 | CATCHES |
| B4 | B | 0 | 1 | CATCHES |
| B5 | B | 0 | 1 | CATCHES |

**Δ = (B catches) − (A catches) = 5 − 5 = 0.**

`clean=0` means the suite passes on the correct implementation; `planted=1` means
it fails on the planted defect. Both are required to score `CATCHES` — a suite
that fails on everything scores `BROKEN`, not a catch.

## Why this is not a third refutation

From [`design2.md`](design2.md), committed as `e3e8498` **before any subject ran**:

> **Ceiling rule:** if arm A scores 5/5 `CATCHES`, report *no headroom* rather
> than *refuted* — the design could not have detected a difference, which is a
> statement about this fixture and not about the claim.

Arm A is at the ceiling. Arm B had nowhere to go. A design in which the treatment
cannot possibly score higher than the control has not tested the treatment, and
reading Δ = 0 as "direction does not help" would be reading a measurement the
apparatus could not have made. The rule was written down in advance precisely so
that this outcome could not be retold as a finding.

The attrition rule was satisfied (both arms scored 5/5, above the floor of 4), so
the run is **complete**. It is the ceiling, not attrition or infrastructure, that
blocks a verdict.

## Where the headroom went

The plant was designed to have headroom. `plant.py` inserts

```python
if negative and 2 * rest == denominator: whole -= 1
```

which differs from the correct implementation **only at negative ties** —
931 of 28,824 enumerated cases, every one of them a negative tie. Catching it
therefore *requires* exercising a negative tie. The design's assumption was that
an undirected agent would build a positives-only fixture table and miss it.

That assumption was wrong, and the subjects say why in their own words. Every
arm-A agent identified the tie-and-sign interaction unprompted, and several named
the exact discrimination the plant exploits before writing a line of test code:

- **A2:** "the mistake I aimed at is half-**up** (toward +inf) masquerading as
  half-**away-from-zero**: the two are identical on every positive input and
  differ by 1 on every negative tie, so a positives-only fixture table cannot
  see it."
- **A5:** tabulated `-5/2` across half-away / half-up / truncate to show the
  three readings "only diverge" on the negative side.
- **A1:** "All five agree with the implementation on `4/2` and `6/3`, so those
  are deliberately not the fixtures."

The headroom was in the *defect*. It was not in the *population*: the behaviour
the fixture was built to elicit by instruction turned out to be the undirected
default. All ten subjects also independently wrote a mutation harness or an
in-file mutant set, which neither arm was asked for.

One subject (A4, an **arm A** agent) went further and caught a defect in its own
harness: Python keys its bytecode cache on source mtime at 1-second resolution
plus file size, so single-byte mutants written within the same second silently
reused each other's stale `.pyc`, and one mutant scored `SURVIVED` on 2 of 3
runs. It fixed this with `PYTHONDONTWRITEBYTECODE=1` and made a failing baseline
abort rather than score mutants — because a module that fails to import marks
every mutant "killed". That is `directed-verification`'s own subject matter (a
check that cannot fail is not a check) arrived at unprompted, and it is further
evidence that this task did not separate the arms.

## What this does and does not license

- **It does not refute behaviour 1.** A ceiling is an absence of measurement.
- **It does not support behaviour 1 either.** Two runs, no evidence.
- **It does say something on its own:** on a small, well-specified function with
  a docstring that states the rule, the undirected default already tests the
  discriminating case, 5/5. That is a statement about *this* task's difficulty,
  not about direction.

Consistent with, but not evidence for, the pattern from the two `role-deck`
premise fixtures: claims of the form "an unprompted agent will skip the careful
step" keep failing to reproduce on bounded tasks.

## What a run 3 would need

The fixture's job is to create headroom, and this design could not. A third
attempt needs a defect a competent undirected suite genuinely misses — which
means moving away from a self-contained pure function whose docstring names the
rule. Candidates: a defect in an interaction between modules, one reachable only
through a state sequence, or one in code whose intended behaviour is not
recoverable from the code under test. Until such a plant exists and is shown to
survive arm A, behaviour 1 stays **unmeasured**.

Run 1 is at [`RESULT.md`](RESULT.md) — invalid for a different reason (the subject
itself was buggy, so arm-A agents scored `BROKEN` for correct work).

## Provenance

- Design pre-registered: `e3e8498`, 2026-09-15 22:31:13 −0500, before any subject ran.
- Subject `rounding.py` md5 `127904733d75847a47bd1499913a6692`, verified identical
  in all ten working directories after the run — no subject modified the code it
  was testing.
- Scoring by `score2.sh`, which asserts its 28,824-case `Fraction` precondition
  (clean code correct, planted code wrong only at negative ties) before scoring.
