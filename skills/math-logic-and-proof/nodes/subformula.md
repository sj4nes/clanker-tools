# subformula

## Type
definition  (epistemic status: `definition`; `constructive_grade: intuitionistic`)

## Statement
The **subformulas** of a wff `φ` are the wffs at the nodes of its (unique) parse
tree:
- `Sub(p) = {p}`, `Sub(⊥) = {⊥}`;
- `Sub(¬φ) = {¬φ} ∪ Sub(φ)`;
- `Sub(φ ∘ ψ) = {φ ∘ ψ} ∪ Sub(φ) ∪ Sub(ψ)`.

`φ` is a subformula of itself; a **proper** subformula is one `≠ φ`.

## Symbols
- `φ`, `ψ`: wffs; `Sub(φ)`: the (finite) set of subformulas.

## Prerequisites (tsort edges into this node)
`wff_syntax`, `wff_unique_readability`.

## Content
Well-defined **only given `wff_unique_readability`** — otherwise "the parse
tree" is ambiguous. `Sub(φ)` is finite, with `|Sub(φ)| ≤ deg(φ) + 1`
(`formula_complexity`). Uses:
- **`substitution_of_equivalents`** replaces *subformula* occurrences (not
  arbitrary fragments);
- **normal-form** algorithms rewrite subformulas;
- the **subformula property** of a cut-free sequent proof: every formula in the
  proof is a subformula of the endsequent (out of scope, but the reason cut
  elimination matters);
- **tableau / DPLL** branch on subformulas of the input.

## Constructive grade
`intuitionistic` — a computable set-valued recursion.

## Lean status
`lean_status: cited`. Not a named definition in `validation/proof-checks.lean`
(the file's proofs recurse on `Wff` structure directly). `conj_injective` /
`conj_ne_disj` give the well-definedness (unique immediate subformulas).

## Type / well-formedness check
`well_formed`. A subformula is a **wff occurring at a parse-tree node** — the
substring `p ∧` of `p ∧ q` is **not** a subformula; `q → r` is **not** a
subformula of `(p → q) → r` (the parse is `(p→q) → r`; its subformulas are
`(p→q)→r`, `p→q`, `r`, `p`, `q`). Distinguish **occurrence** (a position) from
the subformula (the wff) — a wff can occur several times.

## Specialization / boundary cases
- atoms and `⊥`: their only subformula is themselves.
- `Sub(¬¬φ) = {¬¬φ, ¬φ} ∪ Sub(φ)`.
- **positive / negative** occurrences: a subformula occurrence is *positive* if
  under an even number of `¬`s / left-of-`→`s, else *negative* — the polarity
  that governs monotonicity and one-directional quantifier laws.
- first-order: `Sub` extends through `∀x`, `∃x` (the subformula `φ` of `∀x φ`
  has `x` **free**, though bound in `∀x φ`) — a common confusion.

## Hypothesis-dropped counterexamples
- **without unique readability**: `p ∧ q ∨ r` has *two* subformula sets; the
  notion is not well-defined.
- **treat a non-subformula fragment as one**: `substitution_of_equivalents`
  applied to `p →` inside `p → q` is meaningless.
- **first-order, forget the binder**: taking `φ(x)` as a "subformula" of
  `∀x φ(x)` and then reasoning as if `x` were free everywhere.

## Common misuse
Confusing a subformula with a substring; misparsing (`q → r` "in" `p → q → r`
which is `p → (q → r)`, so `q → r` **is** a subformula there, but **not** in
`(p → q) → r`); ignoring occurrence vs subformula; forgetting binder scope in
the first-order case.

## Related nodes (non-prerequisite)
- `needs`: `wff_unique_readability`.
- `used_by`: `substitution_of_equivalents`, `negation_normal_form`, CNF/DNF
  algorithms, tableaux.
- `related`: the subformula property (cut-free proofs), positive/negative
  polarity.

## Sources
[enderton_logic_2e] §1.3; [vandalen_5e] §1.1; [chiswell_hodges] ch. 2.
