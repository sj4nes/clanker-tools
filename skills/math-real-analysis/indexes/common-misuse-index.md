# Common-misuse index — Release 0.1

The recurring errors, and the node whose statement or hypotheses rule them out.
Drawn from the `common_misuse` / `counterexamples_when_dropped` fields of the
result entries and `edges/relations.tsv` `commonly_confused_with` rows.

## Confusing two nearby notions
| Confusion | Separating example | Node |
|---|---|---|
| convergent vs Cauchy | `(1,1.4,1.41,…)` in ℚ: Cauchy, not convergent | `cauchy_convergence_criterion` |
| pointwise vs uniform convergence | `x^n` on `[0,1]`: pointwise to a discontinuous limit, `sup|f_n−f|=1` | `uniform_convergence` |
| continuous vs uniformly continuous | `1/x` on `(0,1)`: continuous, not uniformly | `uniform_continuity` |
| limit point vs point of closure | an isolated point of `A`: in `Ā`, not a limit point | `closure`, `limit_point` |
| absolute vs conditional convergence | `Σ(−1)^n/n`: converges, not absolutely | `absolute_convergence` |
| `x_{n+1}−x_n → 0` vs Cauchy | harmonic partial sums: differences → 0, not Cauchy | `cauchy_sequence` |

## Dropping a hypothesis silently
| Misuse | What breaks | Node |
|---|---|---|
| "closed and bounded ⇒ compact" in a general space | closed unit ball of `ℓ²` | `heine_borel` |
| MVT with `f` not differentiable on all of `(a,b)` | `|x|` on `[−1,1]` | `mean_value_theorem` |
| EVT on a non-closed / unbounded interval | `x` on `(0,1)`; `arctan` on ℝ | `extreme_value_theorem` |
| IVT for a discontinuous `f` | step function skips a value | `intermediate_value_theorem` |
| Riemann integral of an unbounded `f` | `1/√x` on `(0,1]` | `riemann_integral` |
| "every bounded `f` is integrable" | Dirichlet `1_ℚ` | `riemann_integral` |
| "every derivative is integrable" (FTC II) | Volterra's function | `ftc_part2` |
| geometric-series closed form outside `|r|<1` | `r = 2` | `geometric_series` |
| M-test failure ⇒ non-uniform convergence | `Σ(−1)^n x^n/n` on `[0,1]` | `weierstrass_m_test` |
| interchanging `lim` and `∫` without uniformity | `n·1_{(0,1/n)}` → 0, `∫ = 1` | `uniform_convergence_integral` |
| Taylor **series** vs Taylor **theorem** (finite + remainder) | `e^{−1/x²}` | `taylor_theorem` |
| `sup S ∈ S` | `S = {1 − 1/n}` | `lub_axiom`, `supremum` |

## Over-claiming
| Misuse | Correct statement | Node |
|---|---|---|
| "the MVT point `c` is unique / computable" | pure existence | `mean_value_theorem` |
| "BW: the whole sequence converges" | only a subsequence | `bolzano_weierstrass` |
| "IVT gives a unique root" | at least one | `intermediate_value_theorem` |
| "continuity is necessary for integrability" | sufficient only | `continuous_implies_integrable` |
| "`limsup` is a limit" | it is `inf_N sup_{n≥N}` | `limsup_liminf` |
