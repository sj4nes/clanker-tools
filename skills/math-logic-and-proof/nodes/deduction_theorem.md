# deduction_theorem

## Type
theorem  (epistemic status: `proved_theorem`; `constructive_grade: intuitionistic`)

## Statement
In the Hilbert calculus: `Γ ∪ {φ} ⊢ ψ` **if and only if** `Γ ⊢ φ → ψ`.
(In natural deduction the "⟸" is `→E` and the "⟹" is the `→I` rule itself —
so the theorem is only substantive for Hilbert systems.)

## Symbols
- `Γ`: a set of wffs; `φ`, `ψ`: wffs.

## Prerequisites (tsort edges into this node)
`hilbert_derivation`, `modus_ponens`, `metatheoretic_induction`.

## Proof
**⟸**: from `Γ ⊢ φ → ψ` and `Γ, φ ⊢ φ` (assumption), one `modus_ponens` gives
`Γ, φ ⊢ ψ`.
**⟹**: induction on the **length** of the Hilbert derivation of `ψ` from
`Γ ∪ {φ}` (`metatheoretic_induction`). For each line `χ`:
- `χ` an axiom or `χ ∈ Γ`: `χ → (φ → χ)` is axiom 1, then MP gives `Γ ⊢ φ → χ`;
- `χ = φ`: use the derivation of `⊢ φ → φ` (`H.self`);
- `χ` by MP from earlier `θ` and `θ → χ`: IH gives `Γ ⊢ φ → θ` and
  `Γ ⊢ φ → (θ → χ)`; **axiom 2** (`(φ → (θ → χ)) → ((φ → θ) → (φ → χ))`) + MP
  twice gives `Γ ⊢ φ → χ`.

## Constructive grade
`intuitionistic` — the proof uses only Hilbert axioms 1 and 2 (the classical
axiom 3 is not needed) and modus ponens.

## Lean status
`lean_status: core`. `validation/proof-checks.lean`:
`theorem deduction {Γ p q} (h : H (p :: Γ) q) : H Γ (Wff.impl p q) := by
induction h with …` — genuine, universal, `#print axioms deduction` →
`[propext]`. `H.self` supplies the `χ = φ` case; the `mp` case uses `H.s`.

## Type / well-formedness check
`well_formed` (propositional). **First-order caveat**: the deduction theorem
needs "`φ` is closed, **or** no application of **generalisation** in the
sub-derivation is on a variable free in `φ`" — otherwise it fails (see
counterexample). No eigenvariable issue propositionally.

## Specialization / boundary cases
- `Γ = ∅`: `φ ⊢ ψ ⟺ ⊢ φ → ψ`.
- iterated: `Γ, φ₁, …, φₙ ⊢ ψ ⟺ Γ ⊢ φ₁ → … → φₙ → ψ`.
- it **is** the `→I` rule of `nd_derivation` — which is why it is the substantive
  ingredient of `nd_hilbert_equivalence` (`ND ⇒ H`).
- semantic analogue: `Γ ⊨ ψ` from `Γ, φ ⊨ ψ` iff `Γ ⊨ φ → ψ` (finite `Γ`).

## Hypothesis-dropped counterexamples
- **drop Hilbert axiom 2**: the MP case of the induction has no route — a
  Hilbert system with only `φ → (ψ → φ)` and MP does **not** admit the deduction
  theorem.
- **first-order, drop the free-variable side condition**: `{P(x)} ⊢ ∀x P(x)`
  (by generalisation), but `⊬ P(x) → ∀x P(x)` (false in a structure where `P`
  holds of some but not all elements).

## Common misuse
Using it in first-order logic without the free-variable condition; thinking it
is trivial (⟸ is; ⟹ is the theorem); confusing `Γ ⊢ φ → ψ` (the object `→`)
with `Γ, φ ⊨ ψ` (the metastatement); assuming a Hilbert system automatically has
it (it needs axioms 1 and 2).

## Related nodes (non-prerequisite)
- `equivalent_to`: the `→I` rule of `nd_derivation` / `assumption_discharge`.
- `enables`: `nd_hilbert_equivalence`, `derived_rules`, practical Hilbert
  proofs.
- `first_order`: same statement with the free-variable side condition
  (`derivability_fol`).

## Sources
[mendelson_6e] ch. 1 (Deduction Theorem); [enderton_logic_2e] §2.4;
[shoenfield] ch. 3.
