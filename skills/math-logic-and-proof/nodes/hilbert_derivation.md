# hilbert_derivation

## Type
definition  (epistemic status: `definition`; `constructive_grade: split` —
neutral object; classicality via schema 3 of `hilbert_system_prop`)

## Statement
A **Hilbert derivation** of `φ` from `Γ` is a **finite sequence** of wffs
`ψ₁, …, ψₙ = φ` in which each `ψᵢ` is either
- an instance of an axiom schema of `hilbert_system_prop`, or
- a member of `Γ`, or
- obtained from two earlier `ψⱼ, ψₖ` (`j, k < i`) by **modus ponens**.

Written `Γ ⊢_H φ`.

## Symbols
- `Γ`: the premise set.
- the sequence: a `finite_sequence` of wffs, generated inductively
  (`inductive_definition` — closure under axioms, `Γ`, and MP).

## Prerequisites (tsort edges into this node)
`finite_sequence`, `hilbert_system_prop`, `inductive_definition`.

## Content
A **linear** proof object (contrast the **tree** of `nd_derivation`). No
assumption discharge — every premise used stays in `Γ` throughout; the
**deduction theorem** (`deduction_theorem`) is the metatheorem that recovers
conditional reasoning. Induction on the **length** `n` (`metatheoretic_induction`)
is the standard proof technique over Hilbert derivations, and it is short
because there are only three line-types.

`nd_hilbert_equivalence`: `Γ ⊢_H φ ⟺ Γ ⊢_ND φ`.

## Constructive grade
`split` — the sequence is neutral. A derivation citing only schemas 1–2 (+ the
intuitionistic extensions) is intuitionistic; one using schema 3 is classical.

## Lean status
`lean_status: core` (the `→`-fragment). `validation/proof-checks.lean`
`inductive H : Ctx → Wff → Prop` **is** `⊢_H` (constructors `ax`, `k`, `s`,
`mp`); `H.self : H Γ (φ → φ)` is a worked 3-line derivation; `deduction` is
proved by `induction h` over `H`.

## Type / well-formedness check
`well_formed`. Every line must be justified by **one** of the three clauses,
citing an axiom **instance** (not the schema) or two **earlier** lines for MP.
`Γ` fixed throughout (no discharge). Same language.

## Specialization / boundary cases
- `Γ = ∅`: `⊢_H φ` — a **theorem**; the sequence uses only axioms and MP.
- length 1: a single axiom instance, or a single member of `Γ`.
- **proof from a proof**: appending derivations / substituting a derived
  `⊢_H (φ → ψ)` — legitimate, the basis of "derived rules" like the deduction
  theorem being *used* as a rule.
- first-order: `hilbert_derivation` extends with `hilbert_quantifier_axioms` and
  the generalisation rule — a separate edge into `derivability_fol`.

## Hypothesis-dropped counterexamples
- **cite a later line for MP**: circular — the sequence order is essential.
- **cite a schema, not an instance**: not a well-formed line.
- **infinite sequence**: not a derivation (finiteness is definitional; it is
  what `compactness_prop` uses — a derivation of `⊥` from infinite `Γ` uses a
  finite `Γ₀`).
- **discharge a premise mid-sequence**: no such rule; `Γ` is monotone.

## Common misuse
Expecting assumption discharge; citing schemas instead of instances; forward
references for MP; treating the linear and tree formats as different logics
(same derivability); forgetting the deduction theorem is needed to make Hilbert
derivations practical.

## Related nodes (non-prerequisite)
- `equivalent_to`: `nd_derivation` (`nd_hilbert_equivalence`).
- `built_from`: `hilbert_system_prop`, `modus_ponens`.
- `abstracted_by`: `derivability`.
- `needs`: `deduction_theorem`.
- `contrast`: `nd_derivation` (tree, with discharge).

## Sources
[mendelson_6e] ch. 1; [enderton_logic_2e] §2.4; [shoenfield] ch. 2.
