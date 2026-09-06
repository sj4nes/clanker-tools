# Type / well-formedness checks — headline nodes

The analog of the physics capsule's dimensional check. Decided against the type
vocabulary and rules in `objects.md`. **A well-typed statement can still be
false** — this pass only rules out category errors, quantifier-order slips, and
undefined objects.

## `bolzano_weierstrass`
- `(x_n)` : `sequence` = `nat → real`. ✓
- "bounded" : predicate on `sequence` (`∃M:real, ∀n:nat, |x_n| ≤ M`). ✓
- "subsequence `(x_{n_j})`" : needs `j ↦ n_j` **strictly increasing** `nat → nat`
  — recorded as an explicit precondition, not just "some terms". ✓
- "converges to `L ∈ ℝ`" : `∃L:real`, standard ε-N, `L` existentially quantified
  **after** the sequence is fixed. ✓
- Quantifier order: `∀ε ∃N ∀n≥N`. ✓
- **Status: well_formed.**

## `monotone_convergence_theorem`
- "monotone" and "bounded" : predicates on `sequence`. ✓
- Conclusion "converges to `sup{x_n}`" : `sup` of the **range** `{x_n : n∈ℕ}`,
  a nonempty `subset_R` bounded above — `sup` is a `real` by rule 7 (discharged
  by `lub_axiom`, cited at use). ✓
- **Status: well_formed.**

## `intermediate_value_theorem`
- `f` : `function` on `[a,b]` (`interval`, compact). ✓
- "continuous on `[a,b]`" : `function` predicate. ✓
- "`y` between `f(a)` and `f(b)`" : `real`, `min(f a, f b) ≤ y ≤ max(f a, f b)`. ✓
- Conclusion "`∃c∈[a,b], f(c)=y`" : `c` a `real` in the `interval`. ✓
- Canonical proof forms `sup{x∈[a,b] : f(x) < y}` — nonempty (`a` is in it if
  `f(a)<y`) and bounded above by `b`, so `sup` is a `real` by rule 7. ✓
- **Status: well_formed.**

## `derivative`
- Difference quotient `(f(x)−f(c))/(x−c)` : a `function` on `dom f ∖ {c}`
  (rule 3); `x−c ≠ 0` there. ✓
- `f'(c)` : the `function_limit` of that quotient as `x→c`, requires `c` a
  **limit point** of `dom f` (rule 1) **and** `c ∈ dom f`. Both recorded. ✓
- **Status: well_formed.** Note: the one-sided convention at an endpoint
  (`conventions.md`) is what makes `f'(a)` on `[a,b]` well-formed.

## `mean_value_theorem`
- Hypotheses: `f` continuous on `[a,b]`, differentiable on `(a,b)`. The two
  domains differ deliberately — differentiability is only required on the open
  interval. ✓
- Conclusion `f'(c) = (f(b)−f(a))/(b−a)`, `c ∈ (a,b)`, `b−a ≠ 0` since `a<b`. ✓
- **Status: well_formed.**

## `riemann_integral`
- `f` : `bounded` `function` on the **compact** `interval` `[a,b]` (rule 4). An
  unbounded `f` makes `M_i = sup_{[t_{i-1},t_i]} f` not a `real` — the object
  `U(f,P)` would be undefined. Recorded as a hard precondition. ✓
- `∫_a^b f` : the common value of `inf_P U(f,P)` and `sup_P L(f,P)`; each is a
  `sup`/`inf` of a nonempty bounded `subset_R` (rule 7). ✓
- Orientation `∫_b^a := −∫_a^b` is a **convention** (`conventions.md`), applied
  only after the `a<b` theory is built. ✓
- **Status: well_formed.**

## `ftc_part1`
- `F(x) := ∫_a^x f` : well-formed for each `x∈[a,b]` because `f` bounded on
  `[a,x] ⊆ [a,b]` (rule 4) and integrable (hypothesis). ✓
- `F'(x) = f(x)` : `F'` is a `derivative` (rule 3); the claim needs `f`
  continuous **at `x`** (weaker than continuous on `[a,b]`). Recorded. ✓
- **Status: well_formed.**

## `uniform_convergence`
- `(f_n)` : `function_sequence` on a common domain `D`. ✓
- `‖f_n − f‖_∞ = sup_{x∈D} |f_n(x) − f(x)|` : a `real` **only if** `f_n − f` is
  bounded on `D`; otherwise the sup is `+∞` and the statement is read in the
  extended reals. Recorded — for `f_n` continuous on a compact `D` the
  difference is automatically bounded (EVT). ✓
- Quantifier order vs `pointwise_convergence`: the `∀x` moves **left of `∃N`**.
  Exactly one quantifier moved — recorded (rule 6). ✓
- **Status: well_formed.**

## `weierstrass_m_test`
- `M_n` : `sequence` of **nonnegative** reals (`|f_n(x)| ≤ M_n`). ✓
- `Σ M_n` : a `series` of nonnegative terms; "converges" hypothesised, so its
  sum is a `real` (rule 5). ✓
- Conclusion: `Σ f_n` converges **uniformly** — the sum function is
  `D → ℝ`, and the partial sums form a `function_sequence`. ✓
- **Status: well_formed.**

## `radius_of_convergence`
- `1/R = limsup |a_n|^{1/n}` : `limsup` of a `sequence` of nonnegative reals; may
  be `0` (`R=∞`) or `+∞` (`R=0`) — `R ∈ [0,∞]`, an **extended** real, recorded. ✓
- "converges for `|x−c| < R`" : a statement about the `series` `Σ a_n (x−c)^n`
  for each such `real` `x`. ✓
- **Status: well_formed.** The `1/0` and `1/∞` cases are handled by the
  extended-value convention, not left as type errors.

## Summary
All 11 headline nodes: **well_formed**. The recurring things this pass caught and
forced into explicit preconditions: *limit-point* requirement for every
functional limit and derivative; *boundedness + compact domain* for every
Riemann integral; *strictly increasing* index map for every subsequence;
*nonempty + bounded-above* for every `sup` written as a real; the exact
quantifier that moves between a pointwise and a uniform notion.
