# negation_normal_form

## Type
theorem  (epistemic status: `proved_theorem`; `constructive_grade: needs_LEM` —
inherits the classical steps of `de_morgan_prop` and `implication_as_disjunction`)

## Statement
Every wff is logically equivalent to one in **negation normal form (NNF)**:
built from **literals** (atoms and negated atoms), `∧`, `∨` (and `⊤`, `⊥`) only
— negation appears **only directly on atoms**, and `→`, `↔` do not appear.

## Symbols
- `φ`: any wff; `nnf(φ)`: an equivalent NNF wff.
- literal: `p` or `¬p`.

## Prerequisites (tsort edges into this node)
`de_morgan_prop`, `double_negation`, `implication_as_disjunction`,
`recursion_on_wff`.

## Proof / algorithm (by `recursion_on_wff`)
1. eliminate `↔`: `φ ↔ ψ ↝ (φ → ψ) ∧ (ψ → φ)` (`biconditional_as_conjunction`);
2. eliminate `→`: `φ → ψ ↝ ¬φ ∨ ψ` (`implication_as_disjunction`);
3. drive `¬` inward: `¬¬φ ↝ φ` (`double_negation`),
   `¬(φ ∧ ψ) ↝ ¬φ ∨ ¬ψ`, `¬(φ ∨ ψ) ↝ ¬φ ∧ ¬ψ` (`de_morgan_prop`),
   until every `¬` sits on an atom.
Each rewrite preserves `≡` (`substitution_of_equivalents`); the recursion
terminates (each step reduces a `formula_complexity`-style measure).

## Constructive grade
`needs_LEM` — step 2 (`→ ↝ ¬φ ∨ ψ`) and the `¬(φ ∧ ψ) ↝ ¬φ ∨ ¬ψ` case of step 3
are the classical directions (`implication_as_disjunction`, `de_morgan_prop`).
For **decidable** atoms the whole conversion is intuitionistic. The
intuitionistic analogue keeps `→` (there is no classical NNF).

## Lean status
`lean_status: cited`. Not a named `nnf : Wff → Wff` function in
`validation/proof-checks.lean` — but every rewrite it uses **is** checked:
`not_or_iff`, `not_and_iff`, `impl_iff_or`, `dne`/`dni`, `biconditional_as_conj`.
A Mathlib-style formalisation would add the function + a `≡`-correctness proof by
`structural_induction_wff`.

## Type / well-formedness check
`well_formed`. NNF is a **syntactic normal form**, not unique: `p ∧ (q ∨ ¬q)`
and `p` are both NNF and equivalent. The output uses only `{literal, ∧, ∨, ⊤,
⊥}`; a residual `→` or a `¬` on a compound means the conversion is incomplete.

## Specialization / boundary cases
- already NNF: the identity.
- literal or `⊤`/`⊥`: trivially NNF.
- **stepping stone** to `conjunctive_normal_form` / `disjunctive_normal_form`
  (apply `distributivity_prop` to an NNF).
- **circuit / SAT preprocessing**: NNF (then Tseitin) is the standard first
  pass.
- first-order analogue: **prenex** + matrix-NNF (`prenex_normal_form`).

## Hypothesis-dropped counterexamples
- **skip `¬` on a compound**: `¬(p ∧ q)` left as-is is not NNF.
- **skip `→` elimination**: `p → q` is not NNF.
- **naive `¬` distribution without flipping the connective**: `¬(p ∧ q) ↝ ¬p ∧
  ¬q` — **wrong** (that is the De Morgan trap), gives a non-equivalent formula.
- **intuitionistic setting**: there is no `→`-free NNF; the theorem needs
  classical logic.

## Common misuse
Distributing `¬` without flipping `∧`/`∨`; leaving a `→` or `↔`; assuming NNF is
unique / canonical; using the classical conversion in a constructive proof;
confusing NNF (negations on atoms) with CNF/DNF (a specific `∧`/`∨` shape).

## Related nodes (non-prerequisite)
- `uses`: `de_morgan_prop`, `double_negation`, `implication_as_disjunction`,
  `biconditional_as_conjunction`, `substitution_of_equivalents`.
- `precedes`: `conjunctive_normal_form`, `disjunctive_normal_form`.
- `first_order_analogue`: `prenex_normal_form`.
- `related`: Tseitin transformation (equisatisfiable CNF in linear size).

## Sources
[enderton_logic_2e] §1.5; [chiswell_hodges] ch. 3; [vandalen_5e] §1.3.
