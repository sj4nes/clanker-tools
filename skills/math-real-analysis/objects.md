# Type vocabulary and well-formedness rules — Release 0.1

The analog of the physics capsule's dimensional basis. Every result's
`type_check_status` is decided against these. A well-typed statement can still
be false — the check is necessary, not sufficient.

## Object kinds

| Kind | What it is | Formed from | Typical predicates |
|---|---|---|---|
| `real` | an element of ℝ | primitive | `= , < , ≤`, sign |
| `nat` | an element of ℕ | primitive | `= , <`, divisibility |
| `subset_R` | a subset `A ⊆ ℝ` | comprehension over `real` | `open, closed, bounded, compact, connected, nonempty` |
| `interval` | a `subset_R` of the form `[a,b] , (a,b) , [a,b) , (a,b] , (-∞,b] , …` | two `real` endpoints (or ±∞) | all `subset_R` predicates |
| `sequence` | a function `ℕ → ℝ` | `nat → real` | `bounded, monotone, convergent, Cauchy` |
| `series` | a formal sum `Σ a_n` with `(a_n)` a `sequence`; its **sum** is a `real` when convergent | a `sequence` | `convergent, absolutely convergent` |
| `function` | `f : D → ℝ` with `D : subset_R` | `subset_R → real` | `continuous (at c / on D), uniformly continuous, differentiable, integrable, monotone, bounded` |
| `partition` | a finite increasing tuple `a = t_0 < … < t_n = b` | finitely many `real` in an `interval` | `refinement of` |
| `function_sequence` | a sequence `(f_n)` of `function`s on a common `D` | `nat → function` | `pointwise / uniformly convergent` |
| `open_cover` | a family `{U_α}` of `open` `subset_R` with `A ⊆ ⋃ U_α` | indexed `subset_R` | `has a finite subcover` |

## Well-formedness rules (checked in `validation/type-checks.md`)

1. **Domain of a limit.** `lim_{x→c} f(x)` is well-formed only if `c` is a
   **limit point of `D = dom f`** (so the approach is non-vacuous). Recorded on
   every node mentioning a function limit.
2. **Domain of continuity.** `f` continuous at `c` requires `c ∈ dom f`. No
   limit-point condition (isolated points are vacuously points of continuity).
3. **Derivative.** `f'(c)` requires `c` a limit point of `dom f` *and*
   `c ∈ dom f`; the difference quotient `(f(x)−f(c))/(x−c)` is a `function` on
   `dom f ∖ {c}`, and `f'(c)` is its limit as `x → c`.
4. **Integral.** `∫_a^b f` is formed only for `f` a **bounded** `function` on
   the **compact interval** `[a,b]` (Darboux sums need `sup`/`inf` of `f` on
   each subinterval to be `real`). Unbounded `f` or non-compact domain ⇒ not a
   Riemann integral in this release (improper integrals are out of scope).
5. **Series sum.** `Σ a_n` may be written as a `real` only inside a context that
   has asserted or hypothesised convergence; otherwise it is the formal
   `series` object or the `sequence` `(s_n)` of partial sums.
6. **Quantifier order.** ε–δ / ε–N statements fix the order `∀ε ∃δ`
   (`∀ε ∃N`). `uniform_continuity` and `uniform_convergence` differ from their
   pointwise cousins **only** by moving a `∀x` to the left of `∃δ` / `∃N`; the
   type check records exactly which quantifier moved.
7. **`sup`/`inf` existence.** Writing `sup A` as a `real` asserts `A` is
   nonempty and bounded above; this is discharged by `lub_axiom` and must be
   cited at the point of use.
8. **Composition domain.** `f ∘ g` is a `function` on `{x ∈ dom g : g(x) ∈ dom
   f}`; a statement about `f ∘ g` on a set `D` carries the implicit hypothesis
   `g(D) ⊆ dom f`.

## The `[real, nat, subset_R, function]` "signature check"

For a quick pass, tag each symbol in a statement with one kind above and verify:
every arithmetic operation has `real` (or `nat`) operands; every set operation
has `subset_R` operands; every "`f` is continuous/…" has a `function` subject;
every `∈` has `element : real/nat` on the left and `subset_R` on the right;
every `sup/inf/∫/lim/Σ` has produced a `real` only under its rule above. This is
the row-by-row analog of "sum the dimension exponents and check LHS = RHS".
