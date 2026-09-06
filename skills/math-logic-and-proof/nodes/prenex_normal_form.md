# prenex_normal_form

## Type
theorem  (epistemic status: `proved_theorem`; `constructive_grade: needs_LEM` —
via the classical quantifier-movement laws)

## Statement
Every first-order wff is logically equivalent to one in **prenex normal form**:
`Q₁x₁ … Qₙxₙ M` where each `Qᵢ ∈ {∀, ∃}` and the **matrix** `M` is
quantifier-free.

## Symbols
- `Q₁x₁ … Qₙxₙ`: the **prefix**; `M`: the quantifier-free **matrix**.

## Prerequisites (tsort edges into this node)
`first_order_wff`, `alpha_equivalence`, `quantifier_negation`, `free_for`.

## Proof / algorithm
1. eliminate `↔`, `→` (`biconditional_as_conjunction`, `implication_as_disjunction`);
2. drive `¬` inward past quantifiers (`quantifier_negation`:
   `¬∀x φ ↝ ∃x ¬φ`, `¬∃x φ ↝ ∀x ¬φ`) and connectives (De Morgan) — matrix
   reaches NNF;
3. pull quantifiers outward using
   `(∀x φ) ∧ ψ ≡ ∀x (φ ∧ ψ)`, `(∃x φ) ∨ ψ ≡ ∃x (φ ∨ ψ)`, etc.,
   **α-renaming** (`alpha_equivalence`) the bound `x` to a fresh variable when
   `x ∈ FV(ψ)` so no capture occurs.
Each rewrite preserves `≡` (needs `free_for` / renaming).

## Constructive grade
`needs_LEM` — steps 1–2 use the classical directions of `implication_as_disjunction`,
`de_morgan_prop`, and `quantifier_negation` (`¬∀ ↝ ∃¬` is `needs_LEM`).
Intuitionistically there is **no full prenex form** (`¬∀x φ` cannot be moved to
a prenex `∃`).

## Lean status
`lean_status: cited`. The quantifier-movement equivalences are the FOL analogues
of the `prop_laws` lemmas; not built as a `prenex : Wff → Wff` function in
`validation/proof-checks.lean`. Mathlib has prenex-form infrastructure.

## Type / well-formedness check
`well_formed`. **Not unique** — the prefix order depends on the extraction
order, and `(∀x φ) ∧ (∃y ψ)` can become `∀x ∃y (φ ∧ ψ)` **or**
`∃y ∀x (φ ∧ ψ)` (both valid here since `x`, `y` are distinct and the
sub-formulas do not share them) — but **never** swap a `∀∃` that came from a
genuine dependency (`quantifier_order`). α-renaming is required before pulling a
quantifier past a formula containing its variable.

## Specialization / boundary cases
- already prenex: identity.
- **Skolem normal form**: prenex + drop `∃`s by introducing Skolem functions —
  *equisatisfiable*, not equivalent; the basis of resolution/Herbrand
  (out of scope).
- **∀-prefix (universal) sentences**: preserved under substructures; **∃-prefix**
  preserved under extensions — the syntactic side of preservation theorems.
- the **quantifier prefix** `∀∃∀∃…` measures logical complexity (the
  arithmetical hierarchy `Σₙ`/`Πₙ` when the matrix is arithmetic).

## Hypothesis-dropped counterexamples
- **pull a quantifier past a formula sharing its variable without renaming**:
  `(∀x P(x)) ∧ Q(x) ↝ ∀x (P(x) ∧ Q(x))` **captures** the free `x` of `Q(x)` —
  non-equivalent.
- **swap `∀∃` that encodes a dependency**: `∀x ∃y φ ↝ ∃y ∀x φ` is **not** valid
  (`quantifier_order`).
- **intuitionistic logic**: `¬∀x φ` has no prenex equivalent.

## Common misuse
Skipping α-renaming (capture); swapping dependent `∀∃`; treating prenex form as
unique; confusing prenex (equivalent) with Skolem (equisatisfiable);
prenexing an intuitionistic proof obligation.

## Related nodes (non-prerequisite)
- `uses`: `alpha_equivalence`, `quantifier_negation`, `implication_as_disjunction`,
  `de_morgan_prop`, `free_for`.
- `analogue`: `negation_normal_form` (the quantifier-free part).
- `related`: Skolem / Herbrand normal forms, the arithmetical hierarchy,
  ∀/∃-preservation theorems.

## Sources
[enderton_logic_2e] §2.3; [chiswell_hodges] ch. 7; [vandalen_5e] §3.1.
