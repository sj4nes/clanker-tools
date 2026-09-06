# mean_value_theorem

## Type
theorem  (epistemic status: `nonconstructive_result`)

## Statement
If `f` is continuous on `[a,b]` and differentiable on `(a,b)`, then
`f'(c) = (f(b) − f(a))/(b − a)` for some `c ∈ (a,b)`.

## Symbols
- `f`: a real function, continuous on `[a,b]`, differentiable on `(a,b)`
- `c`: the mean-value point, `c ∈ (a,b)` (open interval)

## Prerequisites (tsort edges into this node)
`rolles_theorem`
(transitively: `interior_extremum_theorem`, `extreme_value_theorem`,
`differentiable_implies_continuous`, and everything under those — the MVT sits
deep in the graph because Rolle needs the EVT which needs Heine–Borel which
needs the nested-interval theorem which needs `lub_axiom`).

## Hypotheses
Continuity on the **closed** `[a,b]`; differentiability on the **open** `(a,b)`
only. The asymmetry is essential (see counterexamples).

## Proof sketch
Apply `rolles_theorem` to `h(x) = f(x) − f(a) − s·(x − a)` with slope
`s = (f(b) − f(a))/(b − a)`. Then `h(a) = h(b) = 0`, `h` inherits the
continuity/differentiability of `f`, so `h'(c) = 0` for some `c ∈ (a,b)`, i.e.
`f'(c) = s`.

**Checked with Lean:** `validation/proof-checks.lean` §9 — the endpoint identity
`h(a) = h(b) = 0` (instance `f(a)=2, f(b)=8, a=1, b=4, s=2`). Rolle itself
(EVT + Fermat) is cited, not formalized here.

## Type / well-formedness check
`well_formed` (`validation/type-checks.md#mean_value_theorem`). Forced explicit:
the two different domains (closed for continuity, open for differentiability);
`b − a ≠ 0`.

## Specialization / boundary cases
- `f(a) = f(b)` ⇒ Rolle (`f'(c) = 0`).
- `f(x) = x²` on `[1,3]`: secant slope `4`, `f'(c) = 2c = 4` ⇒ `c = 2`
  (`validation/instance-checks.bc`).
- `g(x) = x` in the Cauchy MVT ⇒ this theorem.

## Hypothesis-dropped counterexamples
- **drop continuity at an endpoint:** `f(x) = x` on `(0,1]`, `f(0) := 1`. No `c`
  with `f'(c) = (f(1) − f(0))/1 = 0`.
- **drop differentiability on `(a,b)`:** `f(x) = |x|` on `[−1,1]`. Secant slope
  `0`, but `f' = ±1` wherever it exists.
- **vector-valued `f`:** `f(t) = (cos t, sin t)` on `[0, 2π]` — `f(0) = f(2π)`
  but `|f'(t)| = 1 ≠ 0` everywhere. The MVT is a real-scalar theorem.

## Common misuse
Assuming `c` is unique or can be solved for in closed form; using the *equality*
`f(b) − f(a) = f'(c)(b − a)` as if `c` were known; applying to complex- or
vector-valued functions.

## Related nodes (non-prerequisite)
- `special_case_of`: `cauchy_mean_value_theorem`
- `generalized_by`: `taylor_theorem` (MVT is `n = 1`)
- feeds: `monotonicity_from_derivative`, `ftc_part2`, `l'hopital_rule`,
  `uniform_convergence_derivative`, `taylor_theorem`

## Sources
[rudin_principles_3e] Theorem 5.10; [spivak_calculus_4e] ch. 11;
[bartle_sherbert_4e] Theorem 6.2.4.
