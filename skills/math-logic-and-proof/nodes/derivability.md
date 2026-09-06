# derivability

## Type
definition  (epistemic status: `definition`; `constructive_grade: split` —
`⊢` is calculus-neutral; the classical rule/schema makes a given proof classical)

## Statement
`Γ ⊢ φ` ("`Γ` **proves** / **derives** `φ`") holds iff there is a derivation of
`φ` from `Γ`. After `nd_hilbert_equivalence`, the calculus is immaterial:
`Γ ⊢_ND φ ⟺ Γ ⊢_H φ`, so `Γ ⊢ φ` is well-defined without a subscript.

## Symbols
- `Γ`: a set of wffs; `φ`: a wff.
- `⊢`: the **syntactic** consequence relation (contrast `⊨`,
  `semantic_consequence`).

## Prerequisites (tsort edges into this node)
`nd_hilbert_equivalence`, `nd_derivation`, `hilbert_derivation`.

## Content
The abstraction that lets the metatheory speak of "provability" without fixing a
proof format. Structural properties (all provable from either calculus):
- **reflexivity**: `φ ∈ Γ ⟹ Γ ⊢ φ`;
- **monotonicity**: `Γ ⊢ φ` and `Γ ⊆ Δ ⟹ Δ ⊢ φ`;
- **cut / transitivity**: `Γ ⊢ ψ` for all `ψ ∈ Δ` and `Δ ⊢ φ ⟹ Γ ⊢ φ`;
- **finiteness (compactness of `⊢`)**: `Γ ⊢ φ ⟹` some **finite** `Γ₀ ⊆ Γ` has
  `Γ₀ ⊢ φ` — a derivation cites finitely many premises;
- **deduction theorem**: `Γ, φ ⊢ ψ ⟺ Γ ⊢ φ → ψ`.

`soundness_prop`: `⊢ ⊆ ⊨`. `post_completeness_theorem`: `⊨ ⊆ ⊢`. Together
`Γ ⊢ φ ⟺ Γ ⊨ φ` — provability = semantic consequence.

## Constructive grade
`split`. The relation `⊢` is defined by "a derivation exists"; whether that
derivation is intuitionistic depends on whether it uses `raa_rule` / schema 3.
`Γ ⊢ φ` in the **classical** calculus may hold where `Γ ⊢ᵢ φ` (intuitionistic)
does not — e.g. `⊢ p ∨ ¬p`.

## Lean status
`lean_status: partial`. `validation/proof-checks.lean` has `Deriv` (`⊢_ND`,
fragment) and `H` (`⊢_H`, `→`-fragment) as **separate** inductives, with
`soundness` over `Deriv` and `deduction` over `H`. The **`Deriv ↔ H` round
trip** that would justify a single calculus-free `⊢` is **stated, not
formalised** here (see `nd_hilbert_equivalence`). So `derivability` as
*calculus-independent* is `partial`; each calculus individually is `core`.

## Type / well-formedness check
`well_formed`. `Γ` and `φ` in one language. `Γ ⊢ φ` is a **metastatement**, not
a wff — it does not nest in connectives or get quantified (contrast the object
`→`). The classic use–mention slip is `Γ ⊢ φ` vs the wff `⋀Γ → φ` (related by
the deduction theorem, for finite `Γ`).

## Specialization / boundary cases
- `Γ = ∅`: `⊢ φ` — `φ` is a **theorem** (= tautology, by soundness+completeness).
- `φ ∈ Γ`: `Γ ⊢ φ` trivially.
- `Γ` inconsistent (`Γ ⊢ ⊥`): `Γ ⊢ φ` for **every** `φ` (`explosion_ex_falso`).
- `Γ` infinite: `Γ ⊢ φ` still reduces to a finite sub-derivation.

## Hypothesis-dropped counterexamples
- **treat `⊢` as `⊨` without soundness/completeness**: they *are* extensionally
  equal for classical propositional logic — but that is the content of two
  theorems, not a definition. For intuitionistic logic `⊢ᵢ ⊊ ⊨_classical`.
- **`⊢` as a wff**: ill-formed.
- **non-monotonic reading** ("adding premises could lose a proof"): classical
  `⊢` is monotone; default/non-monotonic logics drop this (out of scope).

## Common misuse
Writing `Γ ⊢ φ` as the wff `⋀Γ → φ`; conflating `⊢` (syntactic) with `⊨`
(semantic) — equivalent here but distinct notions, and the equivalence is
exactly `soundness_prop` + `post_completeness_theorem`; assuming a proof exists
just because the statement "feels true"; forgetting `⊢` is finite-character.

## Related nodes (non-prerequisite)
- `semantic_counterpart`: `semantic_consequence` (`⊨`).
- `abstracts`: `nd_derivation`, `hilbert_derivation`.
- `related`: `soundness_prop`, `post_completeness_theorem`, `compactness_prop`,
  `consistency`, `deduction_theorem`.
- `first_order_analogue`: `derivability_fol`.

## Sources
[enderton_logic_2e] §2.4; [vandalen_5e] §1.4; [chiswell_hodges] ch. 3–4.
