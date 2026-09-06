# Cycles found and how they were resolved — Release 0.1

`build/build-tree.sh` runs `tsort` with the BSD-safe check (stderr, not just
exit status). The final graph is **acyclic**: `validation/tsort-errors.txt` is
empty and every one of the 263 edges is respected by `indexes/tsort-order.txt`.
The graph has a **single root**, `proposition_logic`, and twelve assumed
`axiom`-typed nodes (the nine ZF axioms plus AC, DC, CC).

No cycle survived into the committed graph. The would-be cycles below were
designed out via `conventions.md`.

## 1. AC ⟺ Zorn ⟺ well-ordering ⟺ cardinal comparability

**Would-be cycle:** all four are equivalent over ZF; texts prove them in a ring.

**Resolution:** `axiom_of_choice` is the canonical form (an `axiom` node,
upstream). `zorn_lemma`, `well_ordering_theorem`, and `cardinal_comparability`
each `derive_from` it one-directionally. `ac_equivalences` is a summary
`theorem` node that *requires* all of them and states the reverse implications
in prose; the reverse implications themselves are `equivalent_to` rows in
`edges/relations.tsv`, **not** graph edges. **Do not add an edge whose target
is `axiom_of_choice`.**

## 2. cardinal `≤` ⟺ injection ⟺ Cantor–Schröder–Bernstein

**Would-be cycle:** `cardinal_le` is *defined* as "an injection exists"; CSB is
a theorem about `≤`.

**Resolution:** `cardinal_le` `requires` `injection` only.
`cantor_schroeder_bernstein` `requires` `cardinal_le`. One-directional.

## 3. ordinal ⟺ well-order

**Would-be cycle:** an ordinal is a `∈`-well-ordered set; every well-order has
an order type (an ordinal).

**Resolution:** `ordinal` `requires` `well_order` (+ `axiom_foundation`,
`axiom_separation`). `order_type_theorem` `requires` both `well_order` and
`ordinal` and is the connecting theorem. No reverse edge.

## 4. ℕ ⟺ set

**Would-be cycle:** `ω` is built from `∅` via Infinity + Separation, and
`finite_set` counts with the finite ordinals — so numbers seem to presuppose
sets and vice versa.

**Resolution:** the direction is strictly `set → omega_construction →
finite_ordinal → finite_set`. `omega_construction` `requires` `set`,
`axiom_infinity`, `axiom_separation`, `empty_set`, `binary_union_intersection`.
`peano_holds_in_omega` is a theorem *about* the construction, not a prerequisite
of it.

## 5. transfinite recursion ⟺ ordinal arithmetic

**Would-be cycle:** recursion defines the aleph function and order types, which
one might use to state recursion.

**Resolution:** `transfinite_recursion` is stated abstractly (define a class
function `F` on all ordinals from a rule `G` using `F` below `α`), needing only
`ordinal` + `transfinite_induction` + `function` + `axiom_replacement`.
Downstream uses `require` it; nothing flows back. `recursion_theorem` on `ω` is
proved **directly** (not via `transfinite_recursion`) so it does not drag the
ordinal spine into the naturals — recorded as `special_case_of` in
`edges/relations.tsv`.

## 6. power set ⟺ function space

**Would-be cycle:** `𝒫(X)` and `2^X` are "the same".

**Resolution:** `power_set` (subsets) and `function_space` (`Y^X`) are defined
independently. `characteristic_function` and `powerset_iso_two_power` (the
bijection `A ↦ 1_A`) are a **theorem**, not a definitional identification.

## 7. the quotient before the relation is verified an equivalence

Same pattern as `math-number-systems` cycle 6: `equivalence_relation` (the three
properties) and `equivalence_partition_correspondence` are established for a
relation on `X` **before** `X/∼` is formed. `quotient_set` `requires`
`equivalence_class` and `equivalence_partition_correspondence`.

## Note on the completeness-style resolution

Unlike `math-number-systems` (where `lub_property` is a theorem because ℝ is
built first) and `math-real-analysis` (where it is an axiom), this capsule has
no completeness node — it stops at `ω`. Its analog is **`continuum_hypothesis`**,
which is resolved a third way: it is neither proved nor assumed but marked
`independent_of_ZFC`, with the independence proofs cited and out of scope.
