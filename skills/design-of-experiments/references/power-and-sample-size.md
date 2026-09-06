# Power, sample size, and precision

Offer **both** power-based and precision-based planning. Never recycle a generic
formula — compute from the model that matches the outcome type.

## Power-based planning

Power `1 − β` is the probability of detecting a true effect of a specified
magnitude, under a chosen test and assumptions. 80% or 90% are conventions, not
laws — justify the target against the cost of a missed effect vs a false one.

Two-arm comparison of means, equal groups, per-group `n`:

```
n ≈ 2·(z_{1−α/2} + z_{1−β})²·σ² / δ²
```

- `α` — false-positive rate (two-sided → `z_{1−α/2}`; `α = 0.05` → `1.960`)
- `1 − β` — power (`0.80` → `z = 0.842`; `0.90` → `z = 1.282`)
- `σ` — outcome standard deviation (from pilot / historical data — state the source)
- `δ` — the smallest effect worth detecting (the minimum practical effect, from
  the charter — **not** a guessed "expected" effect)

Worked (via [`bc`](../bc/SKILL.md), `scale = 4`, lowercase identifiers):

```bc
scale = 10
zalpha = 1.959964
zbeta  = 0.8416212
sigma  = 20
delta  = 5
n = 2*(zalpha + zbeta)^2 * sigma^2 / delta^2
scale = 0; (n + 0.9999)/1   /* ceil */
```

→ `n = 252` per arm (504 total). Halving `δ` quadruples `n`.

**Binary outcome**, baseline rate `p0`, target `p1`:

```
pbar = (p0 + p1)/2
n ≈ ( z_{1−α/2}·√(2·pbar·(1−pbar)) + z_{1−β}·√(p0·(1−p0) + p1·(1−p1)) )² / (p1 − p0)²
```

Use the exact / arcsine form for small `n` or rates near 0 or 1.

**Count / rate outcome** — plan on the Poisson or negative-binomial model with an
exposure offset; inflate for overdispersion (`Var = φ·μ`, multiply `n` by `φ`).

**Time-to-event** — power is driven by the *number of events*, not the number of
units; plan the event count from the hazard ratio, then back out enrollment and
follow-up from the expected event rate and censoring.

## Precision-based planning

When the decision needs an *estimate within a tolerance* ("latency improvement
within ±5 ms", "defect rate within ±1 pp"), design to a confidence / credible
interval half-width `h` rather than to significance:

```
n ≈ 2·(z_{1−α/2})²·σ² / h²      (difference of two means, per arm)
```

Report the planned interval width, not just "significant / not".

## Required adjustments

Apply every one that bites:

| Adjustment | Effect on `n` |
|---|---|
| **Clustering** | multiply by the design effect `DE = 1 + (m − 1)·ρ` (`m` = mean cluster size, `ρ` = intraclass correlation). Effective `n` = raw `n` / `DE`. With few clusters, `n` is bounded by the *number of clusters* — add clusters, not members. |
| Unequal allocation `r : 1` | multiply the balanced total by `(1 + r)² / (4r)` |
| Covariate adjustment (ANCOVA) | multiply by `1 − R²` (pre-period covariate can cut `n` substantially) |
| Repeated measures | account for the within-unit correlation; often reduces `n` |
| Multiple arms / comparisons | inflate `z_{1−α/2}` for the multiplicity correction (Bonferroni, Dunnett, hierarchical) |
| Interim analyses | spend `α` (O'Brien–Fleming, Pocock); the maximum `n` rises slightly, expected `n` falls |
| Attrition / noncompliance | divide by `(1 − attrition)²`; for ITT with partial compliance, divide by compliance² |
| Overdispersion | multiply by the dispersion parameter `φ` |
| Finite population `N` | multiply by `(N − n)/(N − 1)` |
| Time-series autocorrelation (switchback) | inflate by the effective-sample-size penalty from the autocorrelation at the switch interval |
| Variance reduction (CUPED, stratification) | multiply by `1 − ρ²` for the reduction achieved |
| Monte Carlo error (simulation) | choose replications so the MC standard error is small relative to `δ`; use common random numbers across arms to shrink the variance of the *difference* |

"More users" is not more independent information when assignment is by store,
school, region, or day — the independent count is clusters or periods.

## Sanity checks

- Recompute `n` with `σ` at the high end of its plausible range — is the design
  still feasible?
- Confirm the minimum detectable effect at the *achievable* `n` is smaller than
  the practical threshold; if not, the experiment cannot answer the question.
- For clustered designs, report both the raw observation count and the effective
  sample size.
- State every assumed input and its source in the analysis plan.
