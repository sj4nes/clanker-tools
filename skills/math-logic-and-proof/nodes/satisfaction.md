# satisfaction

## Type
definition  (epistemic status: `definition`; `constructive_grade: intuitionistic`)

## Statement
A truth assignment `v` **satisfies** a wff `φ`, written `v ⊨ φ`, iff
`⟦φ⟧_v = T` (`truth_value_recursion`). `v` satisfies a set `Γ` iff it satisfies
every member. "`v` is a **model** of `φ` / `Γ`" means the same.

## Symbols
- `v`: a `truth_assignment`.
- `v ⊨ φ`: the satisfaction relation (a `Prop`).
- `Γ`: a set of wffs.

## Prerequisites (tsort edges into this node)
`truth_value_recursion`.

## Content
The one-line bridge from the recursion to a relation. Everything else in
`prop_semantics` is a quantification of `v ⊨ φ` over `v` and/or over `Γ`:
- `tautology` — `∀v, v ⊨ φ`;
- `contradiction_unsat` — `∀v, v ⊭ φ`;
- `satisfiability` — `∃v, v ⊨ φ`;
- `semantic_consequence` — `∀v, (v ⊨ Γ) → v ⊨ φ`;
- `logical_equivalence` — `∀v, (v ⊨ φ ↔ v ⊨ ψ)`.

The `⊨` symbol is overloaded (`conventions.md`): `v ⊨ φ` (this node),
`Γ ⊨ φ` (`semantic_consequence`), and in FOL `𝔄 ⊨ φ[s]`, `𝔄 ⊨ σ` — disambiguated
by the type of the left operand.

## Constructive grade
`intuitionistic` — `v ⊨ φ` is `eval v φ = true`, a decidable proposition (for
fixed `v`, `φ`). Classicality enters only under `∀v` / `∃v` over an infinite
atom set.

## Lean status
`lean_status: core`. `validation/proof-checks.lean`: `Wff.eval v φ = true` is
the satisfaction relation; `Entails Γ p := ∀ v, (∀ q ∈ Γ, eval v q = true) →
eval v p = true` builds `semantic_consequence` on it; the `soundness` theorem is
stated with it.

## Type / well-formedness check
`well_formed`. `v` must be a **total** assignment (`truth_assignment`); `φ` a
wff of the same language. `v ⊨ Γ` for infinite `Γ` is a `Π`-statement over `Γ`.
`v ⊨ φ` is **decidable** given `v`, `φ` (finitely many atoms) — contrast the FOL
`𝔄 ⊨ φ[s]`, undecidable for infinite `𝔄`.

## Specialization / boundary cases
- `Γ = ∅`: every `v` satisfies `∅` vacuously.
- `φ` a tautology: every `v` satisfies it (that *is* `tautology`).
- `φ = ⊥`: no `v` satisfies it.
- finite atom set: `v ⊨ φ` is settled by looking up one row of the
  `truth_table`.

## Hypothesis-dropped counterexamples
- **partial `v`**: `v ⊨ φ` is undefined if `φ` mentions an atom outside `dom(v)`.
- **`Γ` in a different language than `φ`**: `v ⊨ Γ` and `v ⊨ φ` use different
  atom sets — the combination `Γ ⊨ φ` is then ill-posed.

## Common misuse
Writing `⊨ φ` (tautology) when meaning `v ⊨ φ` (this specific `v` satisfies it),
or vice versa; confusing `v ⊨ φ` (semantic, about an assignment) with `⊢ φ`
(syntactic, about a derivation) — `soundness_prop` / `post_completeness_theorem`
relate them but they are different relations; treating `v ⊨ Γ` as `Γ ⊢`
something.

## Related nodes (non-prerequisite)
- `defined_from`: `truth_value_recursion`.
- `generalised_by`: `tarski_satisfaction` (FOL).
- `feeds`: every other `prop_semantics` node.
- `contrasts_with`: `derivability` (the syntactic side).

## Sources
[enderton_logic_2e] §1.2; [vandalen_5e] §1.2; [chiswell_hodges] §2.3.
