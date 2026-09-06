# wff_unique_readability

## Type
theorem  (epistemic status: `proved_theorem`; `constructive_grade: intuitionistic`)

## Statement
Every wff has **exactly one** parse: it is an atom, or `⊥`, or `¬ψ` for a unique
`ψ`, or `(ψ ∘ χ)` for a unique connective `∘ ∈ {∧, ∨, →, ↔}` and unique
immediate subformulas `ψ`, `χ`. Consequently a function or predicate may be
defined "by recursion on `φ`" / proved "by induction on `φ`" with one clause per
form.

## Symbols
- `φ`: a wff; `ψ`, `χ`: its immediate subformulas; `∘`: its principal
  connective.

## Prerequisites (tsort edges into this node)
`wff_syntax`, `formula_complexity`.

## Proof
**String grammar** (fully parenthesised or with a fixed precedence): the
combinatorial lemma — *every proper nonempty prefix of a wff has strictly more
left than right parentheses* — is proved by `structural_induction_wff`; it
implies no wff is a proper prefix of another, so the principal connective and
the split point are forced. Induction on `formula_complexity`.
**AST form** (`Wff` as an inductive type): the constructors are injective and
pairwise disjoint by construction — `no-confusion` — so unique readability is
free.

## Constructive grade
`intuitionistic` — a decidable structural fact; parsing is an algorithm.

## Lean status
`lean_status: core` (AST form). `validation/proof-checks.lean`:
`conj_injective` (`conj p q = conj p' q' → p = p' ∧ q = q'`, via `injection`)
and `conj_ne_disj` (`conj p q ≠ disj p' q'`, via `injection`) are the
no-confusion facts; `example : eval v (conj p q) = (eval v p && eval v q) := rfl`
shows the recursion is well-defined. The **string-grammar** parenthesis-counting
proof is cited, not formalised (the file works with the AST).

## Type / well-formedness check
`well_formed`. This theorem **is** the licence for `recursion_on_wff` and
`structural_induction_wff`; without it those are ill-founded. The convention
layer (`wff_syntax`) is what it depends on for the string form — drop the
precedence rule and the theorem is false.

## Specialization / boundary cases
- **Polish (prefix) notation**: unique readability holds with **no parentheses**
  — the classic demonstration that it is a property of the grammar, not of
  punctuation.
- **AST / de Bruijn**: trivially unique (constructors).
- atoms: the base case, one parse.
- first-order: the analogue for `term_syntax` and `first_order_wff` (terms and
  formulas each uniquely readable) — same proof style.

## Hypothesis-dropped counterexamples
- **drop the precedence/parenthesis convention**: `p ∧ q ∨ r` parses as
  `(p ∧ q) ∨ r` **and** `p ∧ (q ∨ r)` — two different wffs, so `⟦·⟧_v`,
  substitution, and every rule become ambiguous.
- **ambiguous grammar** (e.g. allow both `φ∧ψ` and `∧φψ`): a string can have
  multiple derivations.
- **overloaded symbol** (same token for a connective and an atom): breaks the
  case analysis.

## Common misuse
Defining a semantic function "by recursion on `φ`" without citing this first;
assuming it is obvious (the prefix-counting lemma is the real content);
forgetting it depends on the notation conventions; conflating "unique parse
tree" (this) with "unique normal form" (`conjunctive_normal_form` — **not**
unique).

## Related nodes (non-prerequisite)
- `licenses`: `recursion_on_wff`, `structural_induction_wff`, `subformula`.
- `depends_on_convention`: `wff_syntax` (precedence/parentheses).
- `analogue`: unique readability of `term_syntax`, `first_order_wff`.
- `contrast`: normal forms are **not** unique.

## Sources
[enderton_logic_2e] §1.3 (the parenthesis lemma); [vandalen_5e] §1.1;
[chiswell_hodges] ch. 2.
