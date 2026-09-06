# Proof checks — what Lean verified vs. what is cited

Run: `lean validation/proof-checks.lean` (exit 0, no `sorry`).

**Environment:** Lean 4.33.1, **no Mathlib**. The set-level constructions
(cuts, the field laws, `lub_property`) are not formalised here — they rest on
the cited sources. Lean checks the **arithmetic and logical cores**.

| Lean item | Kind | Universal? | Supports (nodes) | What stays cited |
|---|---|---|---|---|
| `z_rel_trans` | `omega` | **yes, over ℤ** | `integer_relation_equivalence` | that ℕ (not ℤ) is the base — the ℕ version is the same identity |
| `z_add_well_defined` | `omega` | **yes, over ℤ** | `integer_operations_well_defined` | reflexivity/symmetry (immediate); the multiplication case (§7) |
| `z_le_well_defined` | `omega` | **yes, over ℤ** | `integer_order` | that the ℕ-level `≤` lifts (same inequality) |
| `NatCore.add_comm'` (+ `zero_add'`, `succ_add'`) | induction on the recursive def | **yes, over ℕ** | `nat_semiring_laws` (the pattern for all of them) | associativity, distributivity, the multiplication laws (same method, cited) |
| `nat_div_rem` | core `Nat` lemmas | **yes, over ℕ** | `nat_division_with_remainder` | uniqueness (a short `omega` argument with an explicit `Nat.mul_succ`, cited) |
| `cantor` | diagonal, plain Lean | **yes, any type** | `cantor_theorem`, `real_uncountable` (abstract core), `cantor_diagonal_argument` | the decimal-digit bookkeeping and the `0.999…` handling |
| ℤ-mult respects `∼`, `a,b,… = 5,2,8,5,4,1` | `decide` | **instance** | `integer_operations_well_defined` | the universal bilinear identity (Mathlib `ring`) |
| ℚ-relation transitivity chain | `decide` | **instance** | `rational_relation_equivalence` | the universal `ad=bc ∧ cf=de ⇒ af=be` with `d ≠ 0` cancellation |
| √2 irrational, `q < 50` | `decide` | **instance** | `sqrt2_irrational` | the parity / infinite-descent argument |
| Cantor pairing injective, `8×8` | `decide` | **instance** | `nat_pairing_bijection`, `countable_union_countable` | bijectivity for all of ℕ×ℕ (an induction) |

## Node-by-node bookkeeping

- Nodes whose standard proof is fully classical and cited carry the epistemic
  label on the strength of [landau] / [rudin_principles] / [enderton], **not**
  this file. `lean_status` in each `results/*.yaml` is one of `core-arith` (an
  `omega`/induction universal core), `instance` (a `decide` sample), `cited`
  (no Lean here — the statement is set-level), or `none`.
- **`constructive_result`** nodes (`integer`, `rational_number`, `real_number`,
  `real_is_ordered_field`, `lub_property`, `nth_root_exists`): the objects are
  *exhibited* (a specific quotient / a specific cut / a specific union) and no
  choice is used. `lub_property` in particular is the sharpest contrast with
  `math-real-analysis`, where the same statement is an axiom and its downstream
  consequences are `nonconstructive_result`.
- **`countable_union_countable`** is the one node with `uses_choice: true`
  (countable choice, one enumeration per index). The edge to `countable_choice`
  is in the graph; dropping it is consistent with ZF (Feferman–Levy).
- **`real_uniqueness`** and the extension step of `real_uncountable` rest on a
  cited back-and-forth / diagonal argument; `real_uniqueness` is
  `constructive: false` (a sup at every point).
