# `evaluator-integrity` skill — verification run

`evaluator-integrity` is a *nudge away from known measurement failure modes*,
not a tutorial. So verification cannot mean "re-solve a case with a closed
form". It means the thing the skill is actually claiming:

> **build a measurement setup whose true answer is fixed by construction, run
> the default reading over it, and confirm the default reports an improvement
> that did not happen — while the prescribed reading recovers the truth.**

Every "the score rose" number quoted in [`SKILL.md`](../SKILL.md) is a score
that rose over an ability the fixture holds constant or drives *downward*. That
is what makes the six behaviours falsifiable rather than advice.

**Fixture-first.** This directory was built before `SKILL.md`, so the prose
quotes the harness rather than the harness illustrating the prose.

## Run

```
sh skills/evaluator-integrity/verification/run.sh
```

Tooling: `bc` 7.x (`-lq`), Python 3 (stdlib only), macOS `/bin/sh`. ~1 s wall.
Monte Carlo sections use 200 000 draws (pass@k, leniency), 20 000 (judge swap)
and 400 runs × up to 100 candidates (selection). Every RNG stream is seeded
from an argument; re-running reproduces the numbers below exactly.

## Model / case, and why these

Each section is a system where **true ability is a parameter of the fixture**,
so "did it improve?" has an answer independent of any score:

| Section | Setup | True answer, by construction |
|---|---|---|
| bc §1 / sim §1 | one solver, per-attempt success `p = 0.35`, scored at k = 1 then k = 4 | ability **unchanged** |
| sim §2 | N candidates, **all** with true ability 0.60, scored on a shared 100-item set | every candidate **identical**; no candidate is better |
| sim §3 | six rounds, ability 0.60 → 0.45, judge v1 (t = 0.55) for rounds 1–3, v2 (t = 0.35) for 4–6 | ability **declined 15 points** |
| bc §5 / sim §4 | judges at threshold t, candidate quality ~ U(0,1), anchor truth at 0.50 | the judge at **t = 0.50** is the correct one |
| bc §2–4 | two benchmarks at different saturation; a source pool containing a self-report; two families at different coverage | arithmetic, exact |

They were chosen because each isolates **one** mechanism. A realistic eval
confounds all five at once, which is precisely why the default reading survives
in practice.

## What each step demonstrates

| `SKILL.md` step | Prescribed check | Result |
|---|---|---|
| b2 matched budgets | compare only at equal k | pass@1 = 0.3514, pass@4 = 0.8225 at **identical** p. Apparent gain **+47.1 pts**; the real 15-pt ability improvement it would sit beside is smaller. Re-run at matched k = 4: **0.04 pts**, noise. |
| b3 steer ≠ report | hold out a protected set; log the look count | best-of-N on the chosen-on set: **0.6002 / 0.6580 / 0.6922 / 0.7214** at 1 / 5 / 20 / 100 looks. Held-out: **0.6023 / 0.5974 / 0.6034 / 0.6024** — flat at truth. Gap **−0.2 → +11.9 pts**, monotone in looks. |
| b4 freeze + re-score | re-score every round under one evaluator | as-reported table **+8.3 pts** over a run whose ability fell 15. Re-scored under v1: **−23.9 pts**. The readings disagree in **sign**. |
| b5 anchor-validate | accept on anchor agreement, not on score | score at t = 0.50/0.35/0.20/0.00 = **0.4999 / 0.6498 / 0.8003 / 1.0000** (monotone, no interior optimum); agreement = **1.0000 / 0.8514 / 0.7000 / 0.4975**. Score-selection picks t = 0 — agreement **0.4975, a coin flip**. Anchor-selection picks t = 0.50. |
| b6 headroom | report remaining headroom; weight before pooling | two **identical** +4 raw deltas close 50% vs 6.67% of remaining headroom — **7.5×**. Weighted consensus **82** vs naive mean **85**. `sqrt(n)` domain **66** vs naive **75** (thin family moves it **9 pts**); linear-`n` would give 61.8. |
| b6 HCI formula | Eq. 2 against hand values | H = 84 → 92 (benchmark a), 33.33 → 37.78 (benchmark b). |

The Monte Carlo sections are also **independent oracles** for the closed forms
in `checks.bc`: §1 draws `pass@k` rather than computing `1-(1-p)^k`, and §4
draws the leniency curves rather than integrating them. Agreement is within
0.005 on 200 000 draws in every case. Restating a formula and comparing it to
itself would certify nothing — the point `docs/verifying-skills.md` §3 makes
about `bc` harnesses generally.

## Negative-contrast testing

Run end to end, and **each `bc` signal in isolation** — the omission that let a
dead `grep -q '*** FAIL'` clause hide in 8 of 9 harnesses repo-wide:

| Planted defect | Signal that should catch it | `run.sh` exit |
|---|---|---|
| a false claim (`passat4` asserted against 0.99) | all three | **1** ✓ (3 FAIL lines) |
| `*** FAIL` marker only, `fails` counter untouched — banner still printed, `bc` exits **0** | `grep -qF '*** FAIL'` **alone** | **1** ✓ |
| syntax error mid-file (`bc` status 2) | exit-status clause | **1** ✓ |
| undefined function (`bc` status 3) | exit-status clause | **1** ✓ |
| `checks.bc` removed (`bc` status 4) | exit-status clause | **1** ✓ |
| banner condition falsified, nothing else | missing-banner clause | **1** ✓ |
| `abilities` no longer monotonically declining | python assertions | **1** ✓ (3 FAIL lines) |

The marker-only row is the one that matters: `bc` exits **0** and prints
`ALL BC CHECKS PASSED`, so only the fixed-string grep stands between that file
and a green run.

One test of my own was wrong before the harness was: appending garbage *after*
`quit` produced exit 0 and briefly looked like a hole in the status clause.
`bc` never reaches it. The defect has to be planted before `quit` — recorded
here because the same mistake will look like a finding next time.

## Findings folded back into the skill

- **No correctness fix was needed in the skill body** — `SKILL.md` was written
  after the harness and quotes it, so there was no independent claim left to
  contradict. That is a consequence of building fixture-first, not evidence
  that the prose is right; the displacement table below is where that is
  tested.
- The `sqrt(n)` weighting in behaviour 6 originally cited only the contrast
  with a naive mean. Adding the **linear-`n`** row to `checks.bc` §4 changed
  the claim: `sqrt(n)` is defensible because it is bounded on *both* sides
  (66, between 75 and 61.8), and `references/headroom-index.md` now says so
  rather than just asserting the choice.
- The selection sweep initially ran at 20 candidates only. The **look-count
  sweep** was added because a single number reads as a fixed penalty, when
  the thing worth knowing is that the gap has no ceiling — which is what makes
  "log the query count" a behaviour rather than a nicety.

## The gates are necessary, not sufficient

Everything here is a *mechanical* check on comparability. Three things stay
human, and are named in `SKILL.md`'s "What a score cannot tell you":

- **Construct validity.** No fixture tests whether the benchmark measures the
  capability, because the fixture *defines* the capability as a parameter.
  A perfectly matched, held-out, anchored measurement of the wrong thing is
  still the wrong thing.
- **Anchor quality.** Behaviour 5 moves trust from the judge to the anchor.
  The harness supplies a perfect anchor by construction; nothing here tells
  you whether yours is one.
- **Which metrics are targets and which are protected.** A decision, not a
  measurement.

## Displacement table

Per `docs/verifying-skills.md` §7 — every section names the default behaviour
it displaces, and the verification shows that default failing.

| `SKILL.md` section | Default behaviour it displaces | Where the default visibly fails |
|---|---|---|
| b1 name the optimizer and channel | treat the score as a neutral fact with no loop around it | `judgement` — the fixture supplies the loop the step is meant to find |
| b2 matched budgets | compare round-over-round scores without stating the budget | sim §1: +47.1 pts at fixed ability |
| b3 steer ≠ report, count looks | one eval set, consulted every round for both steering and reporting | sim §2: reported 0.7214 vs true 0.60; gap grows with looks, held-out never moves |
| b4 freeze evaluator, re-score on replacement | swap in a better judge and keep the old rows in the same table | sim §3: **+8.3** reported over a **−15** decline; −23.9 re-scored |
| b5 anchor-validate evaluator changes | adopt the judge that produces higher scores | sim §4: score-selection is monotone → picks agreement 0.4975 |
| b6 headroom + weighted pooling | read a raw delta as progress; average raw percentages | bc §2/§3/§4: 7.5× ratio at identical deltas; +3 pts; +9 pts |
| construct validity | assume a comparable number is a valid one | `judgement` |
| anchor quality | assume an anchor is trustworthy because it is called one | `judgement` |
| choosing what may be optimized | let the available metric decide what is a target | `judgement` |

**5 covered · 4 judgement · 5 gaps.**

### Gaps — logged in [`BACKLOG.md`](../../../BACKLOG.md)

These are claims a fixture *could* falsify and currently does not. They are the
yield of building the table:

1. **Evaluator-call budget** (b2). The budget section matches *attempts* (k),
   not evaluator queries. The skill lists "same number of evaluator calls" as
   part of matching, and nothing demonstrates a loop that wins on query count
   alone at equal compute.
2. **Early stopping on the reporting set** (b3). The sweep demonstrates
   *selection* (an argmax), not early stopping, which leaks through a
   different channel and at a different magnitude.
3. **Coupled solver + evaluator co-evolution** (b5). The judge moves alone in
   sim §4. The skill's "hold one fixed and move the other" targets the case
   where **both** move — the paper's central L5 attribution problem — and no
   section plants it.
4. **Anchor noise** (b5). The anchor is perfect by construction. A small or
   noisy anchor sample producing a *wrong accept* is the realistic failure and
   is untested.
5. **Protocol-link families** (`references/headroom-index.md` §1). The rule
   that gates whether two scores may be pooled at all has no check; `bc` §2–4
   assume linkage. This is the rule most often broken in practice and it sits
   upstream of every formula that is verified.

A green harness with five gaps is the honest state. Four of the five are
concrete enough to write as harness sections; the fifth (protocol linkage)
needs a fixture design that does not yet exist here.
