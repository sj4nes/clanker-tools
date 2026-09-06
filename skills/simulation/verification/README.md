# `simulation` skill — verification run

The `simulation` skill is methodology-only (no bespoke CLI), so verification
means: exercise the workflow the skill prescribes end-to-end on a model with a
known closed form, and confirm each prescribed check behaves as claimed.

**Model.** M/M/1 queue — a discrete-event simulation (event calendar, seeded
streams, warm-up, replications). Chosen because it has exact analytic results
(`L = ρ/(1−ρ)`, `W = 1/(μ−λ)`, Little's law `L = λW`) to validate against.

## Run

```
sh skills/simulation/verification/run.sh
```

Tooling: `bc` 7.0.3, Python 3.14 (stdlib only), macOS. ~8 s wall.

## What each step demonstrates (SKILL.md workflow step → result)

| Step | Prescribed check | Result |
|---|---|---|
| 4 formalize / units | `bc` computes the analytic benchmarks; dimensional check `dim(λ)+dim(W)=0`; Little's-law residual `L − λW` | residual `0` to scale; dim sum `0` — **pass** |
| 6 verify — analytic benchmark | simulated `L` vs closed-form `L` at ρ=0.8, 40 reps | sim `3.957 ± 0.057`, analytic `4.000` — analytic inside the 95% CI — **pass** |
| 6 verify — convergence | lengthen the horizon; CI must tighten and the estimate settle | CI half-width `0.237 → 0.087 → 0.055` over horizons 5k/20k/80k; estimate `3.95 → 3.98` — **pass** (a small residual warm-up bias is visible and is why the skill mandates a warm-up period and a convergence study rather than trusting one horizon) |
| 6 verify — degenerate case | zero arrivals → queue stays empty | `L = 0.0000 ± 0.0000` — **pass** |
| 8 uncertainty — one run ≠ evidence | spread of single unreplicated runs at ρ=0.9 (analytic `L=9`) | eight runs span `7.17 … 10.63` — a single run would mislead by ±20% — **pass** (illustrates the guardrail) |
| 9 experiment — common random numbers | paired comparison of ρ=0.7 vs ρ=0.75 with and without CRN | CRN cuts the 95% CI half-width on `ΔL` from `0.052` to `0.018` (~3×) at the same replication count; both bracket the analytic `ΔL = 0.667` — **pass** |

## Findings folded back into the skill

- **Gavin Howard `bc` 7.0.3 rejects `_` in identifiers and single uppercase
  letters as variable names** (`L`, `W`, `dim_sum` all fail with
  `bad assignment` / `bad expression`). Use lowercase, letters-and-digits-only
  names (`ll`, `ww`, `dimsum`). This matches the `bc`-name findings already
  recorded for the physics/math capsules; `references/verification-validation.md`
  and the SKILL's unit-check guidance now point at the [`bc`](../../bc/SKILL.md)
  skill explicitly for the naming rules.
- The visible warm-up bias (sim `L` sits ~1% below analytic even at long
  horizons until warm-up is generous) is a concrete instance of the skill's
  "too short a warm-up period" mistake — kept as the worked example of why
  step 6 pairs a warm-up with a convergence study.

Nothing in `SKILL.md` or the other reference files needed a correctness fix; the
prescribed workflow produced the right calls and the right conclusions.
