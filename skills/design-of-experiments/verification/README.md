# `design-of-experiments` skill — verification run

The `design-of-experiments` skill is methodology-only (no bespoke CLI), so
verification means: exercise the prescribed steps on tractable cases with
known-correct answers, and confirm each prescribed check behaves as the SKILL
claims.

## Run

```
sh skills/design-of-experiments/verification/run.sh
```

Tooling: `bc` 7.0.3, Python 3.14 (stdlib only), macOS. ~15 s wall.

## What each step demonstrates (SKILL workflow step → result)

| Step | Prescribed check | Result |
|---|---|---|
| 6 sample size — `references/power-and-sample-size.md` | `bc` computes `n ≈ 2(z_{1−α/2}+z_{1−β})²σ²/δ²` for σ=20, δ=5; halving δ must quadruple n | `n = 252/arm` (504 total); δ→δ/2 ratio `4.0000000000` — **pass** |
| 6 sample size — adjustments | `bc` computes design effect `DE = 1+(m−1)ρ`, the 2:1 allocation penalty `(1+r)²/4r`, and the ANCOVA factor `1−R²` | `DE = 3.45`, penalty `1.125`, ANCOVA factor `0.64` — **pass** |
| 6 sample size — realized power | Monte Carlo: 10 000 two-arm experiments at the prescribed `n = 252`; realized power must hit the 0.80 target | realized power `0.804` — **pass** (the formula's n delivers the stated power) |
| 6 clustering — design effect | Monte Carlo: `Var(cluster-randomized arm mean) / Var(iid mean)` for m=50, ρ=0.05 must equal `1+(m−1)ρ` | empirical `≈ 3.4` vs analytic `3.45` — **pass** |
| guardrail — pseudoreplication | Monte Carlo of a **null** cluster-randomized trial (m=50, ρ=0.05): analyze at the observation level (wrong unit) vs the cluster level (the SKILL's prescribed unit); measure the false-positive rate | obs-level FPR `≈ 0.29` (∼6× the nominal 5%); cluster-level FPR `≈ 0.06` — **pass** (this is the SKILL's central "the independent unit is the cluster, not the observation" guardrail, quantified) |
| 6 covariate adjustment | Monte Carlo: ANCOVA-adjusted vs unadjusted treatment-effect SE, covariate with `R² = 0.36`; ratio must be `√(1−R²)` | empirical `0.806` vs `√0.64 = 0.800` — **pass** |
| 5 design — fractional factorial | `references/factorial-and-screening.md` requires the alias structure. Derive it for the 2^(4−1) design (`D = ABC`) two independent ways — word algebra on `I = ABCD`, and column-equality in the built 8-run matrix — and require agreement + resolution IV (no main effect aliased with another main effect or with a 2-factor interaction) | both methods give `A=BCD, B=ACD, C=ABD, D=ABC, AB=CD, AC=BD, AD=BC`; partitions identical; resolution IV confirmed — **pass** |

## Findings folded back into the skill

- The `bc` sample-size snippet in `references/power-and-sample-size.md` was
  corrected from "503 total" to "504" (252 per arm × 2). The formula itself and
  every adjustment reproduce their reference values.
- Gavin Howard `bc` 7.x identifier rules (no `_`, no single uppercase letters)
  were already reflected in the SKILL's `bc` guidance; `checks.bc` follows them
  (`nraw`, `de`, `rsq`, …) and runs clean.
- No correctness fix was needed in the SKILL body or the other reference files:
  the prescribed formulas, the design-effect adjustment, the pseudoreplication
  guardrail, the ANCOVA variance-reduction factor, and the alias-structure
  requirement all produce the right numbers and the right conclusions.

## Files

- `run.sh` — orchestrates all six checks.
- `checks.bc` — the sample-size and adjustment arithmetic.
- `doe_sim.py` — pure-stdlib Monte Carlo: `power_two_arm`, `design_effect_empirical`,
  `cluster_fpr`, `ancova_se_ratio`.
- `alias.py` — 2^(4−1) alias structure by algebra and by design-matrix columns.
