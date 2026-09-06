# Conventions and foundational choices — Release 0.1

## Notation conventions (each is or links to a `notation_convention` node where it affects a statement)

| Convention | Choice for this release | Node |
|---|---|---|
| Sample space | `Omega` is an arbitrary nonempty set; outcomes `omega in Omega`. No assumption that `Omega` is countable or a product. | `probability_space` |
| Events | `F` (script F) is a **sigma-algebra** on `Omega`; only `F`-members have a probability. `sigma(C)` is the generated sigma-algebra. | `sigma_algebra` |
| `P` | a **countably additive** probability measure: `P >= 0`, `P(Omega) = 1`, `P(disjoint countable union) = sum P`. Finite additivity is derived, never assumed separately. | `kolmogorov_axioms` |
| "almost surely" / "a.s." | holds on an event of probability 1, i.e. off a `P`-null set. "a.e." is the same notion for a general measure. | `almost_sure`, `null_set` |
| Random variable | a **measurable** map `X: (Omega, F) -> (R, B(R))`, or into `(R^d, B(R^d))`; `B` is the Borel sigma-algebra. `{X <= x} := X^{-1}((-inf, x])`. | `random_variable`, `borel_sigma_algebra` |
| Law / distribution | `P_X := P o X^{-1}`, the pushforward, a probability measure on `(R, B(R))`. "`X ~ mu`" means `P_X = mu`. | `distribution_pushforward` |
| CDF | `F_X(x) := P(X <= x)` — **right-continuous**, nondecreasing, limits 0 and 1. (Left-continuous `P(X < x)` is not used.) | `cdf` |
| pmf / pdf | `p_X(x) = P(X = x)` (discrete); `f_X = dP_X/dLebesgue` (absolutely continuous). A "density" always means w.r.t. Lebesgue measure unless stated. | `pmf`, `pdf` |
| `E[X]` | `integral_Omega X dP`; defined when `E[|X|] < inf`, or unconditionally in `[0, inf]` when `X >= 0`. `E[X]` **may fail to exist** (Cauchy). | `expectation` |
| `Var`, `sd`, `Cov`, `rho` | `Var(X) = E[(X - E X)^2]`; `sd(X) = sqrt(Var(X))`; `Cov(X,Y) = E[XY] - E[X]E[Y]`; `rho = Cov/(sd sd)`. All require the relevant second moments finite. | `variance`, `covariance`, `correlation` |
| MGF / CF | `M_X(t) = E[e^{tX}]` (may be `+inf` or finite only at 0); `phi_X(t) = E[e^{itX}]` (**always** exists, `|phi_X| <= 1`). | `mgf`, `characteristic_function` |
| Independence | events/`sigma`-algebras/r.v.s are independent iff the **product rule holds over every finite subfamily** (mutual independence). Pairwise is strictly weaker. Defined **without conditioning**. | `independence_events` |
| `A_n i.o.` | `limsup_n A_n = intersection_N union_{n >= N} A_n` = "`omega` in infinitely many `A_n`". | `limsup_liminf` |
| Normal | `N(mu, sigma^2)` is parameterised by **variance** `sigma^2` (not `sigma`); `N(0,1)` is standard. | `normal_distribution` |
| Convergence modes | `-->^{a.s.}`, `-->^{p}`, `-->^{L^p}`, `-->^{d}`. Every limit-theorem node is **tagged with the mode it delivers**. | `convergence_almost_sure`, `convergence_in_probability`, `convergence_in_lp`, `convergence_in_distribution` |
| `log`, `exp` | natural base. `C(n,k)` is the binomial coefficient. Empty sum `= 0`, empty product `= 1`. | — |

## The convergence-mode tag (the `choice_grade` analogue)

The sibling capsules tag each result with a **choice grade**
(`choice_free` / `needs_countable_choice` / `needs_full_AC`). Here the analogous
per-result tag is the **mode of convergence** a limit theorem delivers, because
*that is the hypothesis-sensitive fact a downstream user gets wrong*:

| Result | Mode delivered | Note |
|---|---|---|
| `weak_law_large_numbers` | `p` (in probability) | finite mean suffices; finite-variance route via Chebyshev |
| `strong_law_large_numbers` | `a.s.` | finite mean suffices (Etemadi); strictly stronger than WLLN |
| `central_limit_theorem` | `d` (in distribution) | **not** a.s. or in probability; needs finite, nonzero variance |
| `lindeberg_clt` | `d` | non-i.i.d.; the Lindeberg condition replaces "identical" |
| `poisson_limit_theorem` | `d` | parameter regime `np -> lambda` |
| `continuous_mapping_theorem` | preserves the input mode | a.s./p/d each map through |
| `slutsky_theorem` | `d` | requires one sequence `-->^{p}` a **constant** |
| `glivenko_cantelli` (excluded) | `a.s.` uniform | noted for a future release |

`convergence_implications` records the lattice: `a.s. => p`, `L^p => p`,
`p => d`, `p => a.s. along a subsequence`, `d`-to-a-constant `=> p`; **no other
implication holds in general**, and `convergence_implications`'s
`counterexamples_when_dropped` carries the separating examples.

## Foundational choices (per the method, step 3)

- **The abstract integral is the floor — cited, not built.** `abstract_integral`,
  `monotone_convergence_theorem`, `dominated_convergence_theorem`,
  `fatou_lemma`, `fubini_tonelli`, `radon_nikodym`, and
  `lebesgue_measure_caratheodory` are `bridge` nodes with
  `lean_status: cited` and a source section (Billingsley / Folland). This
  capsule *develops the probability that sits on top*; a future
  `math-measure-and-integration` capsule is the natural floor below.
  Consequence: `expectation` is **defined as** `integral X dP`, so
  "linearity / monotonicity / MCT for `E`" are the integral's properties
  specialised — the edges point `abstract_integral -> expectation -> ...`, never
  the reverse.
- **Kolmogorov's third axiom is countable additivity.** `finite_additivity` is a
  derived `proposition`. `continuity_of_probability`, both Borel–Cantelli
  lemmas, `cdf_properties`, and every limit theorem use the countable form —
  edged to `kolmogorov_axioms` (or to `measure_continuity`) accordingly.
- **Independence is defined by factorization, not by conditioning.**
  `independence_events` requires only `probability_measure` and
  `finite_additivity`; `conditional_probability` requires `complement_rule`
  (for the `P(B) > 0` precondition). This is the deliberate cut that breaks the
  independence ↔ conditional-probability would-be cycle (see
  [`edges/cycles.md`](edges/cycles.md)). `P(A|B) = P(A)` is then a *theorem*
  (a `relations.tsv` `equivalent_to` note on `independence_events`), available
  only where `P(B) > 0`.
- **Classical logic**, inherited from the capsules below. Every "not a.s.
  convergent", "uncorrelated but not independent", "no convergent subsequence"
  is a `¬∀` resolved by `quantifier_negation` in `math-sets`.
- **The Axiom of Choice** is not used in any probabilistic proof in this
  release. It enters only through the cited existence of Lebesgue measure
  (Carathéodory) and the standard construction of non-measurable sets (merely
  *mentioned*, as the reason `F` cannot be `2^Omega` for `Omega = [0,1]`). The
  SLLN route taken (Etemadi / fourth-moment truncation + BC1) is choice-free.
- **`E[X|G]` exists by a cited theorem.** `conditional_expectation_existence`
  is `lean_status: cited` (Radon–Nikodym, or the `L^2` projection then
  monotone-class extension). `tower_property`, `law_of_total_variance`, and the
  `L^2`-projection characterization are then proved from the defining property.

## Cycle resolutions

See [`edges/cycles.md`](edges/cycles.md). Summary: (1) independence ↔ conditional
probability — resolved by defining independence via factorization; (2)
expectation ↔ integral — resolved by taking the integral as the cited primitive
and `E` as its specialisation; (3) `conditional_probability` ↔
`multiplication_rule` and `cdf` ↔ `distribution_pushforward` — modelling slips
(both directions encoded); kept the definitional direction only.
