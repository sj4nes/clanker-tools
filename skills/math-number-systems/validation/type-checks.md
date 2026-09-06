# Type / well-formedness checks — headline nodes

The construction analog of a dimensional check. The dominant question is
**"does this operation respect the quotient it is defined on?"** (objects.md
rule 1). A well-typed construction can still fail to be a *field* (that is the
downstream theorem) — this pass rules out ill-formed definitions.

## `peano_axioms`
- `0 : nat`, `S : ℕ → ℕ`, induction quantifies over `X ⊆ ℕ`. ✓
- The induction clause is **second-order** (any subset), deliberately — this is
  what makes `natural_number` categorical. Recorded.
- **Status: well_formed.**

## `recursion_theorem`
- `X` an arbitrary `set`; `a : X`; `g : ℕ × X → X`; conclusion `∃! f : ℕ → X`.
- No arithmetic symbol appears — the theorem is stated purely in `peano_axioms`
  + `function` (objects.md, cycle 2). ✓
- **Status: well_formed.**

## `integer`
- `∼_ℤ` on `ℕ × ℕ`: `(a,b) ∼ (c,d) :⟺ a + d = b + c` — uses `+` **only** (no
  subtraction, which does not exist yet). ✓
- Transitivity is a genuine clause, not automatic (objects.md rule 2); it needs
  additive cancellation in ℕ. Checked in Lean §1 (`omega`, universal).
- `ℤ := (ℕ×ℕ)/∼_ℤ` is well-formed **only after** `integer_relation_equivalence`. ✓
- **Status: well_formed.**

## `rational_number`
- `∼_ℚ` on `ℤ × ℤ*`: second coordinate is **nonzero** (objects.md rule 8). ✓
- `(a,b) ∼ (c,d) :⟺ ad = bc` — transitivity needs ℤ a domain (cancel a nonzero
  common factor). Recorded; Lean §8 (instance).
- `ℚ := (ℤ×ℤ*)/∼_ℚ` well-formed after `rational_relation_equivalence`. ✓
- **Status: well_formed.**

## `integer_is_ordered_integral_domain` / `rational_is_ordered_field`
- Every axiom is checked on **representatives** and separately shown independent
  of the choice of representative (the operations are already known
  well-defined). ✓
- "ordered" means the order is **total** (trichotomy, lifted from ℕ) and
  **compatible** with `+` and with `·`-by-positives. The totality clause is not
  free — it is `nat_order_trichotomy` pushed through the quotient. ✓
- **Status: well_formed.**

## `dedekind_cut`
- A cut is a **set** `A ⊆ ℚ`; the "type" is the conjunction of the four clauses
  (nonempty, proper, downward closed, no greatest element). ✓
- "No greatest element" is meaningful only because `rational_order` is **dense**
  — recorded as a dependency. In a discrete order the clause would exclude the
  rationals themselves. ✓
- **Status: well_formed.**

## `real_number`
- `ℝ := { A ⊆ ℚ : A is a cut }` — a set of sets of rationals. `A ≤ B :⟺ A ⊆ B`.
- Totality of `≤` is a theorem (`real_order`), not part of the definition —
  flagged so a reader does not assume it. ✓
- **Status: well_formed.**

## `real_is_ordered_field`
- `real_addition`: `A + B := { a + b : a ∈ A, b ∈ B }` — must be shown to be a
  cut (objects.md rule 3): nonempty ✓, proper ✓ (bounded by `supA + supB`
  informally), downward closed ✓, no greatest ✓.
- `real_multiplication`: defined for `A, B > 0*` then extended **by sign cases**
  — the naive `{ab}` is *not* a cut when a cut contains arbitrarily negative
  rationals. This is the one genuinely fiddly well-formedness obligation in the
  capsule; recorded prominently.
- `−A` uses "upper bound of `A` but not the least one" precisely to land on a
  cut with no greatest element. ✓
- **Status: well_formed.**

## `lub_property`
- Inputs: `S ⊆ ℝ` (a set of cuts), nonempty, bounded above by some cut `B`.
- Output: `⋃ S`. The **entire content** is that `⋃ S` is again a cut (rule 3):
  nonempty (some `A ∈ S` nonempty), proper (`⋃ S ⊆ B ≠ ℚ`), downward closed
  (union of downward-closed sets), no greatest (a greatest `q ∈ ⋃ S` would be
  greatest in some `A ∈ S`). Each clause is one line. ✓
- Contrast: in `math-real-analysis` this is `lub_axiom` and `sup S` is a real
  "by axiom"; here `sup S` is the *exhibited set* `⋃ S`. ✓
- **Status: well_formed.**

## `nth_root_exists`
- `E := { t ∈ ℝ : t > 0 ∧ t^n < x }`; `t^n` for `n : ℕ` is defined by recursion
  on the exponent using `real_multiplication` (needs `recursion_theorem`). ✓
- `y := sup E` is a `real` because `E` is nonempty and bounded above
  (`lub_property`, rule 4). ✓
- **Status: well_formed.**

## `cantor_diagonal_argument`
- Input: any `x : ℕ → ℝ` with values in `[0,1]`. Output: an **explicit** `d`.
- The digit rule must land in `{1,…,8}` so that `d` has a unique decimal
  expansion and the digitwise difference from each `x_k` is a genuine
  inequality of reals (objects.md rule 7). This is the one real subtlety and it
  is a *type* issue: `0.4999… = 0.5000…` as reals. ✓
- **Status: well_formed.**

## `countable_union_countable`
- "`I` countable", "each `A_i` countable" = injections into ℕ.
- The proof **chooses** one enumeration `e_i` per `i` — `countable_choice`, one
  choice per index. `uses_choice: true` and the edge to `countable_choice` make
  this visible in the graph (objects.md rule 7 + scope.md). ✓
- **Status: well_formed.**

## Summary

All 14 headline nodes: **well_formed**. Recurring obligations this pass forced
into the entries: (1) the defining relation is a genuine equivalence *before*
the quotient is formed — `integer`, `rational_number`; (2) every quotient
operation carries a "respects `∼`" clause — `*_operations_well_defined`;
(3) every ℝ operation must output a *cut* — `real_addition`,
`real_multiplication`, `lub_property`; (4) sign cases are mandatory in
`real_multiplication`; (5) `cantor_diagonal_argument` must avoid the
`0.999… = 1.000…` ambiguity; (6) `countable_union_countable`'s choice use is
edged, not hidden.
