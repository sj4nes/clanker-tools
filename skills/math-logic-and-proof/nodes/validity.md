# validity

## Type
definition  (epistemic status: `definition`; `constructive_grade: n/a`)

## Statement
A first-order wff `φ` is **valid** (logically true, `⊨ φ`) iff `𝔄 ⊨ φ [s]` for
**every** structure `𝔄` and **every** assignment `s`. For sentences: true in
every model. The first-order analogue of `tautology`.

## Symbols
- `⊨ φ`: "`φ` is valid" (no left operand).

## Prerequisites (tsort edges into this node)
`tarski_satisfaction`, `model`.

## Content
By `godel_completeness_theorem`, `⊨ φ ⟺ ⊢ φ` — valid = provable. But unlike
`tautology`, validity is **not decidable** (`undecidability_fol_validity`,
Church/Turing) — only **semidecidable** (enumerate proofs). Valid sentences
include all substitution instances of propositional tautologies plus the
genuinely first-order ones: `∀x φ → φ[t/x]` (`t` free for `x`),
`φ[t/x] → ∃x φ`, `∀x (φ → ψ) → (∀x φ → ∀x ψ)`, `∀x (x = x)`, and the
`quantifier_negation` / `quantifier_distribution` laws.

## Constructive grade
`n/a` — quantifies over the proper class of all structures.

## Lean status
`lean_status: cited`. Mathlib: `φ.IsValid` / `⊨ φ`. The propositional analogue
`Wff.Taut` is in `validation/proof-checks.lean`.

## Type / well-formedness check
`well_formed`. `⊨ φ` = "true in **all** structures under **all** assignments" —
a `Π`-statement over a proper class. For an **open** `φ`, `⊨ φ` iff its
universal closure is valid. `⊨ φ` is a metastatement, not a wff.

## Specialization / boundary cases
- **propositional tautology instances**: every substitution instance of a
  tautology is valid.
- `⊨ ∃x (x = x)` — valid (nonempty domain); **not** valid in free logic.
- `⊨ ∀x φ → ∃x φ` — valid (nonempty domain).
- `⊨ (∃x∀y φ) → (∀y∃x φ)` — valid; the converse is **not** (`quantifier_order`).
- **monadic** fragment, **BSR** (`∃*∀*`) fragment: validity **is** decidable
  there — the boundary in `undecidability_fol_validity`.

## Hypothesis-dropped counterexamples
- **check "many" structures**: `∀x P(x) → P(c)` is valid, but
  `∃x P(x) → ∀x P(x)` is **not** (a 2-element structure where `P` holds of one
  element) — a finite check of some structures is not a validity proof.
- **empty domain**: `∃x (x = x)` and `∀x φ → ∃x φ` fail.
- **confuse with satisfiable**: `P(c)` is satisfiable, not valid.

## Common misuse
Confusing valid with satisfiable; checking finitely many structures; assuming
validity is decidable (it is only semidecidable); free-logic instincts (empty
domain); swapping `∀∃`/`∃∀`.

## Related nodes (non-prerequisite)
- `analogue`: `tautology` (propositional).
- `equivalent_to` (via completeness): `⊢ φ`.
- `contrast_with`: `tautology_decidable` (propositional validity IS decidable);
  `undecidability_fol_validity`.
- `related`: decidable fragments (monadic, BSR, guarded).

## Sources
[enderton_logic_2e] §2.2, §2.5; [chiswell_hodges] ch. 5; [vandalen_5e] §3.1.
