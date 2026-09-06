# coincidence_lemma

## Type
proposition  (epistemic status: `proved_theorem`; `constructive_grade:
intuitionistic`)

## Statement
Satisfaction depends only on the relevant data:
- **(terms)** if `s`, `s'` agree on `var(t)`, then `s̄(t) = s̄'(t)`;
- **(formulas)** if `s`, `s'` agree on `FV(φ)`, then `𝔄 ⊨ φ [s] ⟺ 𝔄 ⊨ φ [s']`;
- **(reducts)** if `𝔄`, `𝔅` have the same domain and agree on the symbols
  occurring in `φ`, then `𝔄 ⊨ φ [s] ⟺ 𝔅 ⊨ φ [s]`.

Corollary: for a **sentence** `σ`, `𝔄 ⊨ σ [s]` is `s`-independent — write
`𝔄 ⊨ σ`.

## Symbols
- `s`, `s'`: assignments agreeing on `FV(φ)`; `𝔄`, `𝔅`: structures agreeing on
  the symbols of `φ`.

## Prerequisites (tsort edges into this node)
`free_bound_variables`, `tarski_satisfaction`, `structural_induction_wff`.

## Proof
Structural induction on `t` / `φ`. Terms: base cases `s(x) = s'(x)` (agree on
`var(t)`), `c^𝔄`; recursive case applies `f^𝔄` to equal arguments. Formulas:
atomic from the term case; connectives by IH; **quantifier** `∀x φ`:
`FV(∀x φ) = FV(φ) \ {x}`, so `s` and `s'` may disagree at `x` — but `s(x ↦ a)`
and `s'(x ↦ a)` agree on all of `FV(φ)`, and the IH applies for every `a`.

## Constructive grade
`intuitionistic` — a structural induction with no classical step.

## Lean status
`lean_status: cited`. Not built (FOL satisfaction not in
`validation/proof-checks.lean`); the propositional truth-functionality analogue
(`eval v φ` depends only on the atoms of `φ`) is implicit in the `equiv_*`
lemmas.

## Type / well-formedness check
`well_formed`. This lemma is what **licenses** the notation `𝔄 ⊨ σ` for
sentences (dropping `s`), and is used in the **quantifier cases** of
`substitution_lemma_semantic` and `soundness_fol` (`∀I`: the eigenvariable is
not free in the open assumptions, so changing its value does not affect their
satisfaction).

## Specialization / boundary cases
- **sentence**: `FV(σ) = ∅`, so *any* two assignments agree on it — `s`
  irrelevant.
- **reduct/expansion**: adding interpretations of symbols not in `φ` does not
  change `𝔄 ⊨ φ`.
- `φ` with `FV(φ) = {x}`: `𝔄 ⊨ φ [s]` depends only on `s(x)` — so `φ` "defines"
  the set `{a : 𝔄 ⊨ φ [s(x ↦ a)]}`.

## Hypothesis-dropped counterexamples
- **`s`, `s'` disagree on a free variable of `φ`**: `φ = P(x)`, `s(x)` in `P^𝔄`,
  `s'(x)` not — different truth values. The "agree on `FV(φ)`" hypothesis is
  essential.
- **`𝔄`, `𝔅` disagree on a symbol occurring in `φ`**: different `R^𝔄`, `R^𝔅` ⟹
  `R(t)` can differ.
- **different domains**: the lemma needs `|𝔄| = |𝔅|`.

## Common misuse
Assuming truth is `s`-independent for open formulas; ignoring that a reduct must
still agree on the symbols *of that formula*; forgetting the quantifier case
needs the "agree on `FV(φ)` after updating at `x`" argument; using it across
structures with different domains.

## Related nodes (non-prerequisite)
- `licenses`: the notation `𝔄 ⊨ σ` for sentences.
- `used_by`: `substitution_lemma_semantic`, `soundness_fol`, `truth_lemma_fol`.
- `related`: definability (`φ` with one free variable defines a subset).
- `propositional_analogue`: truth-functionality of `truth_value_recursion`.

## Sources
[enderton_logic_2e] §2.2 (Coincidence / Agreement Lemma); [chiswell_hodges]
ch. 5; [vandalen_5e] §3.1.
