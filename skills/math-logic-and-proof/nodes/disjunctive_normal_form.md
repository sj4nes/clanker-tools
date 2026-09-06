# disjunctive_normal_form

## Type
theorem  (epistemic status: `proved_theorem`; `constructive_grade: needs_LEM` —
via `negation_normal_form`)

## Statement
Every wff is logically equivalent to one in **disjunctive normal form (DNF)**: a
**disjunction of terms**, each term a **conjunction of literals**:

    ⋁ᵢ ( ⋀ⱼ ℓᵢⱼ ).

## Symbols
- `φ`: any wff; `dnf(φ)`: an equivalent DNF wff.
- term (implicant): `ℓ₁ ∧ … ∧ ℓₖ`. Empty term `= ⊤`; empty disjunction `= ⊥`.

## Prerequisites (tsort edges into this node)
`negation_normal_form`, `distributivity_prop`.

## Proof / algorithm
Two routes:
1. **from NNF**: `negation_normal_form`, then distribute `∧` **over** `∨`:
   `φ ∧ (ψ ∨ χ) ↝ (φ ∧ ψ) ∨ (φ ∧ χ)` (`distributivity_prop`) until the formula
   is a disjunction of terms;
2. **from the truth table** (`dnf_from_truth_table`): one term per row where
   `φ` is `T` — the conjunction of `p` (if `v(p) = T`) / `¬p` (if `v(p) = F`).
   This is the **canonical (full) DNF** — every term mentions every atom.

## Constructive grade
`needs_LEM` — via `negation_normal_form` (route 1) or via the truth table
(route 2 uses a completed table, i.e. `LEM` at each atom). Distribution itself is
`intuitionistic`.

## Lean status
`lean_status: core` (at the Boolean-function level). `validation/proof-checks.lean`:
`binary_dnf` proves **every** `f : Bool → Bool → Bool` equals its full DNF
```
f a b = (f tt tt && (a && b)) || (f tt ff && (a && !b)) || … || (f ff ff && (!a && !b))
```
(all 4 cases, `by cases a <;> cases b <;> simp`). The Wff-level `dnf : Wff → Wff`
function is cited.

## Type / well-formedness check
`well_formed`. **Not unique** in general; the **full/canonical DNF** (from the
truth table) *is* unique up to order. DNF is the **dual** of CNF (swap `∧`/`∨`).
Satisfiability of a DNF is **trivial** (check each term for a literal and its
negation) — but the *conversion to* DNF is the hard part, so DNF does not make
SAT easy.

## Specialization / boundary cases
- a single term: `φ` is a conjunction of literals.
- `⊥` = empty disjunction; `⊤` = a term that is empty (or `p ∨ ¬p`).
- **canonical DNF from the truth table**: `dnf_from_truth_table` — the explicit
  witness that `{¬, ∧, ∨}` is `functional_completeness`.
- **Karnaugh maps / Quine–McCluskey**: minimise a DNF by merging adjacent terms
  (`absorption`, `distributivity_prop`).
- **tautology check via DNF**: `φ` is a tautology iff its DNF covers all `2ⁿ`
  rows — as expensive as the table.

## Hypothesis-dropped counterexamples
- **distribute `∨` over `∧`** (the CNF direction): produces CNF, not DNF.
- **stop early**: `p ∧ (q ∨ r)` is not DNF.
- **assume DNF makes SAT tractable**: the conversion is the exponential step;
  DNF-SAT is trivial only *after* you pay that cost.
- **assume uniqueness** of non-canonical DNF.

## Common misuse
Distributing the wrong way (getting CNF); thinking DNF trivialises SAT for the
original formula; stopping before full distribution; assuming a unique DNF;
confusing the canonical (full) DNF with an arbitrary one.

## Related nodes (non-prerequisite)
- `uses`: `negation_normal_form`, `distributivity_prop`.
- `dual_of`: `conjunctive_normal_form`.
- `canonical_form_via`: `dnf_from_truth_table`.
- `witnesses`: `functional_completeness`.
- `related`: Karnaugh / Quine–McCluskey minimisation.

## Sources
[enderton_logic_2e] §1.5; [chiswell_hodges] ch. 3; [vandalen_5e] §1.3.
