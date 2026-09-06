# `unknown-discovery` skill — verification run

The `unknown-discovery` skill is methodology-only (no bespoke CLI), so
verification means: exercise the quantitative methods the skill prescribes on
cases with known answers, and confirm each behaves as claimed.

## Run

```
sh skills/unknown-discovery/verification/run.sh
```

Tooling: `bc` 7.x (`-l`), Python 3 (stdlib only), macOS. < 1 s wall.

## What each step demonstrates (SKILL.md workflow step → result)

| Step | Prescribed check | Result |
|---|---|---|
| 6 probes — value of information | `bc` on a two-action / two-state decision: `value_now = 5`, `value_perfect = 44`, `EVPI = 39`; a probe costing `45` is `not worthwhile`; `EVPI ≥ 0` and bounded by the worse action's regret | the VoI arithmetic and the "don't probe if EVPI < cheapest probe" rule hold — **pass** |
| 7 forecast & calibrate | 40 000-event Monte Carlo: irreducible floor `mean p(1−p) = 0.167`; a **calibrated** forecaster's Brier `0.166` sits on the floor; an **overconfident** forecaster (probabilities pushed 3× toward 0/1) scores `0.203`, worse; per-bucket stated-vs-observed gap `< 0.008` | the Brier score rewards calibration and punishes overconfidence exactly as the skill claims — **pass** |
| 4 generate alternatives — diagnosticity | Bayesian update from a 50/50 prior: **non-diagnostic** evidence (`P(E\|H1) 0.90`, `P(E\|H2) 0.85`) moves the posterior to `0.514` — nothing; **diagnostic** evidence (`0.90` vs `0.20`) moves it to `0.818` | confirming evidence every hypothesis predicts is near-worthless; diagnostic evidence is where the probe budget goes — **pass** |
| 5 search for surprise — residuals | 4 000 rows from `y = 2x + ε` with a hidden `+4` in one cell (`late & category b`). OLS fit: **aggregate** mean residual `+0.000` (looks clean); the cell's mean residual is `+3.0`, `96 SE` from zero | a hidden regime shift is invisible in the aggregate and obvious once disaggregated — the "don't suppress anomalies, disaggregate" guardrail quantified — **pass** |
| 3 mine assumptions — triage score | `P = I·U·(1−R)·D` is monotone increasing in `I`, `U`, `D`, decreasing in `R`; two assumptions reach the same `P = 1.28` from different components (`I = 0.8` vs `0.4`) — so the score alone would send them to the wrong probe | confirms the skill's rule to keep the components beside the score and never treat `P` as a risk metric — **pass** |

## Findings folded back into the skill

- The overconfidence effect on the Brier score is real but modest at small
  distortion (a 1.8× push barely clears the floor); it takes a ~3× push toward
  0/1 to move the aggregate Brier decisively. This is *why* the skill prescribes
  a **bucketed** calibration review rather than a single headline Brier number —
  the per-bucket stated-vs-observed gap catches miscalibration the aggregate
  score smears out. Reflected in `references/forecasting-and-calibration.md`.
- The residual case's "everything else" cell drifts to `−1.0`: absorbing the
  hidden `+4` pulls the whole regression line up, so *every other* cell looks
  slightly negative. The missing variable distorts the baseline, not just its
  own cell — reinforcing the skill's instruction to disaggregate across *every*
  listed dimension, not only the one you suspect.

No correctness fix was needed in the skill body; the prescribed methods produced
the right calls and the right conclusions.
