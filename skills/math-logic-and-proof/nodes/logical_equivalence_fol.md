# logical_equivalence_fol

## Type
definition  (epistemic status: `definition`; `constructive_grade: n/a` as a
definition)

## Statement
Two first-order wffs `φ`, `ψ` are **logically equivalent**, `φ ≡ ψ`, iff
`𝔄 ⊨ φ [s] ⟺ 𝔄 ⊨ ψ [s]` for every structure `𝔄` and assignment `s` —
equivalently `φ ⊨ ψ` and `ψ ⊨ φ` (`semantic_consequence_fol`), equivalently
`⊨ (φ ↔ ψ)` (`validity`).

## Symbols
- `φ ≡ ψ`: the equivalence relation on first-order wffs.

## Prerequisites (tsort edges into this node)
`tarski_satisfaction`, `semantic_consequence_fol`.

## Content
The first-order analogue of `logical_equivalence`. It is a **congruence** for
the connectives *and* the quantifiers (`φ ≡ φ'` ⟹ `∀x φ ≡ ∀x φ'`), so
substitution of equivalents extends to the first-order case — with the caveat
that you may not substitute inside a quantifier in a way that changes binding.
The quantifier-law nodes (`quantifier_negation`, `quantifier_distribution`,
`quantifier_order`, `exists_forall_duality`, `vacuous_quantification`,
`prenex_normal_form`) are instances or one-directional relatives.

## Constructive grade
`n/a` as a definition; specific equivalences split (`quantifier_negation` is
`needs_LEM`, `exists_forall_duality` uses `double_negation`).

## Lean status
`lean_status: cited`. Mathlib: `φ.Iff ψ` at the `BoundedFormula` level. The
propositional analogue `Wff.Equiv` + congruences is in
`validation/proof-checks.lean`.

## Type / well-formedness check
`well_formed`. `∀`-quantify over structures *and* assignments — so `≡` holds for
**open** formulas too (evaluated pointwise). `φ ≡ ψ` is a metastatement.
α-equivalent formulas are logically equivalent (`≡_α ⊊ ≡`). Substitution of
equivalents into a formula is safe (no intensional contexts in FOL), but must
respect binding.

## Specialization / boundary cases
- `φ ≡ φ`; α-variants are `≡`.
- all valid sentences are `≡` (to `⊤`); all unsatisfiable ones `≡` (to `⊥`).
- **prenex form**: `φ ≡` its prenex normal form (`prenex_normal_form`).
- `∀x φ ≡ φ` when `x ∉ FV(φ)` (`vacuous_quantification`).
- the Lindenbaum–Tarski algebra `Wff / ≡` is a Boolean algebra with operators
  (`∀x`, `∃x` as modal-like operators) — a **cylindric / polyadic algebra**.

## Hypothesis-dropped counterexamples
- **check some structures**: `∀x P(x) ≡ ∃x P(x)`? — holds in every
  **one-element** structure, fails in general; a partial check misleads.
- **substitute inside a quantifier changing binding**: `∀x φ` with `φ` replaced
  by an equivalent `φ'` that has different free variables.
- **confuse `≡` with `↔`**: `φ ↔ ψ` is a wff (true in some structures, false in
  others); `φ ≡ ψ` says `φ ↔ ψ` is **valid**.

## Common misuse
Treating `≡` as the object `↔`; checking finitely many structures; substituting
an equivalent that changes binding; assuming the *quantifier* laws are all
two-directional (`quantifier_distribution` is not).

## Related nodes (non-prerequisite)
- `is`: an equivalence relation + congruence on first-order wffs.
- `instances`: `quantifier_negation`, `exists_forall_duality`,
  `vacuous_quantification`, `prenex_normal_form`.
- `propositional`: `logical_equivalence`.
- `algebra`: cylindric / polyadic algebras.

## Sources
[enderton_logic_2e] §2.2; [chiswell_hodges] ch. 5; [vandalen_5e] §3.1.
