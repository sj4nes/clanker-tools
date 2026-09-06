# Factorial, fractional factorial, screening, and response-surface designs

## Factorial designs

A factorial experiment varies multiple factors simultaneously. For `k` two-level
factors a full factorial has `2^k` treatment combinations.

For two factors A and B:

```
Y = β0 + βA·A + βB·B + βAB·(A×B) + ε
```

- `βA` — main effect of A, averaged over the levels of B.
- `βB` — main effect of B, averaged over the levels of A.
- `βAB` — interaction: the effect of A depends on the level of B.

Factorials beat one-factor-at-a-time testing whenever factors may interact: each
run informs several effects, and interactions are estimable. Use them for
process development, configuration optimization, simulation studies, and
multi-component product interventions.

**Do not interpret a main effect in isolation when a strong interaction
dominates** — report the conditional effects instead.

Add **center points** (all factors at their mid-level) to a two-level factorial
to test for curvature; if curvature is significant, a two-level design cannot
model it and you need a response-surface design.

## Fractional factorial designs

When `k` is large, run a `2^{k−p}` fraction. Balanced and orthogonal fractions
exist, but the economy comes from **aliasing**: some effects cannot be separated.

Every fractional design proposal must state:

- the fraction, e.g. `2^{6−2}` (16 of 64 runs);
- the **generators**, e.g. `E = ABC`, `F = BCD`;
- the **defining relation**, e.g. `I = ABCE = BCDF = ADEF`;
- the **resolution** (length of the shortest word in the defining relation);
- the **full alias structure** — for each estimable effect, what it is
  confounded with (e.g. `A = BCE = ... `);
- the assumption being relied on (usually: three-factor and higher interactions
  are negligible);
- the **foldover / augmentation path** to de-alias if screening flags an
  ambiguous effect.

Resolution guide:

| Resolution | Main effects aliased with | Use |
|---|---|---|
| III | two-factor interactions | Early screening of main effects only; cheap |
| IV | other main effects clear; 2FIs aliased with 2FIs | Screening when some interactions may matter; fold over to resolve |
| V | 2FIs clear of main effects and other 2FIs | Interactions of interest; near response-surface quality |

Never recommend a fractional design without the alias structure. "Economical" is
not a justification — the reviewer must see exactly what is given up.

## Screening designs

Screening finds a small influential subset from many candidates. It is **not
confirmation** — estimates are provisional.

- Resolution III / IV fractional factorials.
- **Plackett–Burman** — `n` a multiple of 4; estimates `n−1` main effects;
  complex partial aliasing of interactions with main effects.
- **Definitive screening designs** — three levels; main effects clear of each
  other and of two-factor interactions; can detect curvature; efficient.
- **Supersaturated designs** — more factors than runs; only with a strong
  sparsity assumption and disciplined follow-up.
- **Sequential elimination / racing** — drop clearly inferior settings early.
- **Morris elementary-effects screening** — for computational / simulation
  models with many inputs.

Workflow: `screen → de-alias / confirm → model curvature → optimize → validate`.

## Response-surface and optimization designs

Two-level factors cannot estimate curvature. A quadratic response-surface model:

```
Y = β0 + Σ βi·xi + Σ βii·xi² + Σ_{i<j} βij·xi·xj + ε
```

Designs:

- **Central composite (CCD)** — factorial / fractional core + axial (star)
  points + center points; supports the full quadratic model; choose the axial
  distance for rotatability or for face-centered (when levels are bounded).
- **Box–Behnken** — three levels, no corner (extreme) runs; good when extreme
  combinations are infeasible or unsafe.
- **Optimal designs** — D-optimal (parameter precision), I-optimal (prediction
  variance over the region), A-optimal, G-optimal; for constrained regions or
  fixed run budgets.
- **Mixture designs** — simplex-lattice / simplex-centroid / Scheffé models when
  component proportions sum to a constant.
- **Bayesian optimization / sequential model-based optimization** — expensive
  black-box responses; report the acquisition rule.
- **Multi-objective optimization** — report the Pareto front, not a single
  weighted score.

Distinguish three things when reporting an optimum:

1. settings that optimize the *estimated model*;
2. settings that are *robust* under parameter / noise uncertainty;
3. settings *experimentally confirmed* to hit the target with fresh runs.

Only (3) is a result. Always run a confirmation experiment at the recommended
settings with new randomization.
