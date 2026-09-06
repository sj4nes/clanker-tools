# Proof checks — Lean, kernel-verified vs cited

Run: `lean validation/proof-checks.lean` (exit 0, no `sorry`, no errors, no warnings).

**No Mathlib.** No `ℝ`, `ℚ`, no real analysis. Lean 4.33's core `grind` and
`omega` discharge the finitary algebra; probabilities are carried as integer
counts "k out of N" and every quotient is written cross-multiplied. A
finite-support law is a `List (Int × Int)` of (weight, value) pairs.

## What the kernel verified — GENUINE, universal (holds for all inputs)

| Lean name | Statement | Behind node(s) |
|---|---|---|
| `sq_nonneg'` | `0 ≤ z·z` over ℤ (sign cases) | support lemma |
| `union_bound` | `P(A)+P(B)−P(A∩B) ≤ P(A)+P(B)` | `boole_inequality`, `measure_monotonicity`, `borel_cantelli_first` |
| `incl_excl_2`, `incl_excl_3` | 2- and 3-event inclusion–exclusion identities | `inclusion_exclusion`, `finite_additivity`, `complement_rule` |
| `bayes_denominator` | denominator `= P(A)` via total probability | `bayes_theorem`, `law_of_total_probability`, `multiplication_rule` |
| `ind_and`, `ind_or`, `ind_compl` | `1_{A∩B}=1_A·1_B`, `1_{A∪B}=1_A+1_B−1_A1_B`, `1_{Aᶜ}=1−1_A` | `indicator_rv` |
| `wsum_const` | `Σ pᵢ·c = c·Σ pᵢ` (list induction) | `expectation` (E[c]=c), `expectation_monotonicity` |
| `expectation_linearity` | `Σ pᵢ(a xᵢ + b yᵢ) = a Σpᵢxᵢ + b Σpᵢyᵢ`, universal in a,b (list induction + `grind`) | `expectation_linearity`, `variance`, `covariance` |
| `centid` | `Σ pᵢ(xᵢ−m)² = Σ pᵢxᵢ² − 2m Σpᵢxᵢ + m² Σpᵢ` (list induction + `grind`) | `variance_computational`, `law_of_total_variance` |
| `var_affine` | `n·[a²sxx + 2ab·sx + b²n] − (a·sx + nb)² = a²(n·sxx − sx²)` | `variance_affine` |
| `markov_finite` | `a·(tail mass) ≤ Σ pᵢxᵢ` for nonneg integer weights/values, `a ≥ 1` (list induction) | `markov_inequality`, `chernoff_bound` |
| `chebyshev_reduction_fwd` | `(k ≤ y ∨ y ≤ −k) ⇒ k² ≤ y²` for `k ≥ 0` (the direction Chebyshev uses) | `chebyshev_inequality` |
| `jensen_sq` | `(t x + (n−t) y)² ≤ n(t x² + (n−t) y²)`, universal in t,x,y,n with `0 ≤ t ≤ n`; via the factorization `= t(n−t)(x−y)²` | `jensen_inequality`, `moment_ladder` |
| `cov_bilinear_raw` | `(a·exy + ezy) − (a·ex + ez)·ey = a(exy − ex·ey) + (ezy − ez·ey)` | `covariance_bilinear` |
| `var_of_sum_raw` | `(exx + 2exy + eyy) − (ex+ey)² = (exx−ex²) + (eyy−ey²) + 2(exy−ex·ey)` | `variance_of_sum` |
| `corr_bound_iff` | `|ρ| ≤ 1 ⟺ Cov² ≤ VarX·VarY` (unfold ρ; the content is CS) | `correlation` |

## What the kernel checked as an INSTANCE (`decide` — a closed integer proposition, not universal)

| Instance | Behind node |
|---|---|
| disease-test posterior `99·6 = 99 + 495`, `594 = 6·99` | `bayes_theorem` |
| Chebyshev grid `(2 ≤ y ∨ y ≤ −2) ⟺ 4 ≤ y²` over `y ∈ [−4,4]` | `chebyshev_inequality` |
| 2-point CS/Jensen grid `(a+b)² ≤ 2(a²+b²)` over a 4-point law | `cauchy_schwarz_expectation`, `correlation` |
| Binomial(4, ½): mean `= 2`, variance `= 1` (cross-multiplied) | `binomial_distribution` |
| Bernoulli(3/10): `E·N² = 30`, `Var·N² = 21` | `bernoulli_distribution` |
| Geometric(½): partial sum `Σ_{k≤4} k·2^{4−k} = 26`, gap to `E·2⁴ = 32` is the tail | `geometric_distribution`, `memorylessness` |
| Poisson-limit ratio `2·8⁹ / 10⁹ ≈ 0.268` vs `2e⁻² ≈ 0.271` | `poisson_limit_theorem` |

Numerical distribution checks (Bernoulli / binomial / Poisson / exponential /
normal moments, the Poisson limit, memorylessness, and the standardized-binomial
→ Φ(1) CLT trend) are in `validation/instance-checks.bc`.

## What is CITED (not formalized here — deep analytic results)

The abstract Lebesgue integral and `MCT / DCT / Fatou / Fubini–Tonelli /
Radon–Nikodym`; `lebesgue_measure_caratheodory`; the general scalar linearity /
monotonicity of `E`; `dynkin_pi_lambda`; `mgf_moments`, `mgf_uniqueness`,
`cf_properties`; `levy_continuity_theorem`; `weak_law_large_numbers`,
`strong_law_large_numbers`, `central_limit_theorem`, `lindeberg_clt`,
`delta_method`; `continuous_mapping_theorem`, `slutsky_theorem`,
`portmanteau_theorem`; `conditional_expectation_existence`, `tower_property`
(the defining-property chase is elementary but not formalized), the boundary
nodes. Sources: Billingsley *Probability and Measure* 3e; Durrett *PTE* 5e;
Williams *Probability with Martingales*; Folland *Real Analysis* 2e. Each such
result's YAML carries `lean_status: cited` with a theorem number.
