# Proof checks — what Lean verified vs. what is cited

Run: `lean validation/proof-checks.lean` (exit 0, no `sorry`).

**Environment:** Lean 4.33.1, **no Mathlib**. So there is no `ring` / `nlinarith`
/ real-analysis library, and *none* of the analytic theorems in this capsule can
be stated over ℝ here. The Lean file checks the **algebraic and arithmetic
cores** that the informal proofs rest on. Everything else — the ε-δ logic, limit
constructions, `lub_axiom`, compactness, quantification over real functions —
rests on the cited sources.

| Lean item | Kind | Universal? | Supports (nodes) | What stays cited |
|---|---|---|---|---|
| `tri` : `|a+b| ≤ |a|+|b|` | `omega` | **yes, over ℤ** | `algebra_of_limits`, `cauchy_sequence`, `abs_convergence_implies_convergence`, `uniform_cauchy_criterion` | that the reals form an ordered field where this holds (immediate); the ε-manipulation around it |
| `rev_tri` : `|a|−|b| ≤ |a−b|` | `omega` | **yes, over ℤ** | `differentiable_implies_continuous`, `limit_uniqueness` | as above |
| `squeeze_core` | `omega` | **yes, over ℤ** | `squeeze_theorem`, the 3-ε step in `uniform_limit_continuous` | that `a_n, b_n → L` (the hypothesis being squeezed) |
| `telescope` : `∑(g(i+1)−g(i)) = g(n)−g(0)` | induction | **yes, over ℤ** | `ftc_part2`, `interval_additivity` | that `G` is an antiderivative and that the MVT applies on each subinterval |
| `ratio_bound` : `aₙ ≤ cⁿ a₀` from `aₙ₊₁ ≤ c aₙ` | induction | **yes, over ℕ** | `ratio_test`, `root_test`, `comparison_test` (geometric majorant) | that the ratio/root limsup is `< 1` so such a `c` exists; convergence of `∑ cⁿ` |
| geometric partial sum, `r=3, n=4` | `decide` | **instance** | `geometric_series` | the universal identity (Mathlib `geom_sum`); the limit `rⁿ⁺¹ → 0` for `|r|<1` |
| Taylor 2nd order, `f=x², x=5` | `decide` | **instance** | `taylor_theorem` | the universal remainder formula; existence of `ξ` (needs iterated Rolle) |
| AM–GM, `a=5, b=3` | `decide` | **instance** | `monotone_convergence_theorem` (the √2 example) | that the recursion is monotone and bounded for all real `x_0 > 0` |
| MVT auxiliary endpoints, `f(a)=2,f(b)=8` | `decide` | **instance** | `rolles_theorem` ⇒ `mean_value_theorem` | Rolle itself (needs EVT + Fermat); that `h` is continuous/differentiable |

## Node-by-node epistemic bookkeeping

- Every node labelled `proved_theorem` / `proved_lemma` / `proposition` in
  `nodes/nodes.tsv` carries that label on the strength of a **cited, standard,
  checked textbook proof** (`sources/bibliography.md`), *not* on the strength of
  this Lean file. `lean_status` in each `results/*.yaml` records separately what
  this file actually verified: one of `core-arith` (an `omega`/induction
  universal core), `instance` (a `decide` sample), or `none`.
- `nonconstructive_result` nodes (`monotone_convergence_theorem`,
  `bolzano_weierstrass`, `heine_borel`, `extreme_value_theorem`,
  `intermediate_value_theorem`, `riemann_integral`, `continuous_implies_integrable`,
  and everything downstream of `lub_axiom` used non-constructively): the standard
  proof invokes `lub_axiom` in a way that does not exhibit the object
  algorithmically (the `sup` is not computed). The ℝ¹ Bolzano–Weierstrass
  *bisection* proof is choice-free and *is* constructive given a modulus of
  boundedness — noted on that node.
- `countable_choice` nodes (`sequential_criterion_limit`, `sequential_continuity`,
  `closed_iff_seq_closed`): the `(⇐)` direction builds a sequence by choosing one
  point per `n`. A choice-free route exists for `sequential_continuity` in ℝ
  (the domain is second-countable) and is noted; the capsule keeps the edge to
  `countable_choice` because the *standard textbook proof* uses it.
