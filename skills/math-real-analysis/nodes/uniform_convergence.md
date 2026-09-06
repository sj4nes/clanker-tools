# uniform_convergence

## Type
definition  (the headline definition of the function-sequences chapter)

## Statement
`f_n ⇉ f` on `D` iff `sup_{x∈D} |f_n(x) − f(x)| → 0`; equivalently
`∀ε>0 ∃N ∀n≥N ∀x∈D : |f_n(x) − f(x)| < ε`.

## Symbols
- `(f_n)`: a `function_sequence` on a common domain `D ⊆ ℝ`
- `f`: the limit function, `f : D → ℝ`
- `‖g‖_∞ = sup_{x∈D} |g(x)|`: the sup-norm (a real, or `+∞`)

## Prerequisites (tsort edges into this node)
`pointwise_convergence`, `supremum`

## The one thing that matters: quantifier order
Pointwise: `∀x ∀ε ∃N ∀n≥N …` — `N` may depend on `x`.
Uniform:   `∀ε ∃N ∀x ∀n≥N …` — one `N` works for **all** `x`.
Exactly one quantifier (`∀x`) moves left of `∃N`. This is `objects.md` rule 6
and the entire content of the distinction.

## Type / well-formedness check
`well_formed` (`validation/type-checks.md#uniform_convergence`). Note: `‖f_n −
f‖_∞` is a real only when `f_n − f` is bounded on `D`; otherwise the statement is
read in the extended reals. For `f_n` continuous on a compact `D` the difference
is automatically bounded (EVT).

## Equivalent forms
- `(f_n)` is **uniformly Cauchy** (`uniform_cauchy_criterion`).
- Convergence in the metric `d(g,h) = ‖g − h‖_∞` on the bounded functions on `D`.

## Specialization / boundary cases
- `f_n` eventually equal to `f` ⇒ uniform.
- uniform on `D` ⇒ uniform on every subset of `D`.
- `f_n(x) = x^n` on `[0, 0.9]`: `sup = 0.9^n → 0`, uniform
  (`validation/instance-checks.bc`).

## Hypothesis-dropped counterexamples
- **drop uniformity (keep pointwise):** `f_n(x) = x^n` on `[0,1]` → a
  discontinuous limit; `sup_x |f_n − f| = 1` for **every** `n`
  (`validation/instance-checks.bc`). Continuity is not inherited; the integral
  need not pass to the limit (`g_n = n·1_{(0,1/n)}` → 0 pointwise,
  `∫ g_n = 1`).
- **drop bounded difference (for the sup to be real):** `f_n(x) = x/n` on `ℝ` →
  0 pointwise, `sup_x |x/n| = +∞` for every `n` — not uniform on `ℝ` (uniform on
  every bounded set).
- **locally uniform ≠ uniform:** `f_n(x) = x/n` again is uniform on each
  `[−R,R]` but not on `ℝ`.

## Common misuse
Confusing it with pointwise convergence; assuming "uniform on every compact
subset" ⇒ "uniform"; forgetting the sup-norm can be `+∞`.

## Related nodes (non-prerequisite)
- `generalizes` / `commonly_confused_with`: `pointwise_convergence`
- enables: `uniform_limit_continuous`, `uniform_convergence_integral`,
  `uniform_convergence_derivative`, `weierstrass_m_test`,
  `radius_of_convergence`

## Sources
[abbott_understanding_2e] §6.2; [rudin_principles_3e] Definition 7.7.
