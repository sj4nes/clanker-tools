# formula_complexity

## Type
definition  (epistemic status: `definition`; `constructive_grade: intuitionistic`)

## Statement
Measures of the size of a wff, defined by recursion:
- **length** `|φ|` — number of symbol occurrences;
- **connective count / degree** `deg(φ)` — number of connective occurrences
  (`deg(atom) = deg(⊥) = 0`, `deg(¬φ) = deg(φ) + 1`, `deg(φ ∘ ψ) = deg(φ) +
  deg(ψ) + 1`);
- **height / depth** `ht(φ)` — height of the parse tree.

Each is a natural number and **strictly decreases** on immediate subformulas —
which is what makes recursion and induction on wffs **well-founded**.

## Symbols
- `φ`: a wff; `|φ|`, `deg(φ)`, `ht(φ)`: naturals (metatheoretic `ℕ`).

## Prerequisites (tsort edges into this node)
`wff_syntax`, `inductive_definition`.

## Content
The bridge from "structural induction on wffs" to "strong induction on `ℕ`": a
property `P(φ)` provable by `structural_induction_wff` is equally provable by
`strong_induction` on `deg(φ)` (or `ht(φ)`), and vice versa — this is the
**course-of-values** view of formula induction, useful when the IH needs *all*
smaller formulas, not just immediate subformulas (e.g. after a substitution that
is not a subformula but is smaller in degree).

Also fixes the **finiteness** facts: `atoms(φ)` is finite (`|atoms(φ)| ≤ deg(φ)
+ 1`), so a `truth_table` has finitely many (`2^|atoms(φ)|`) rows —
`tautology_decidable`.

## Constructive grade
`intuitionistic` — a computable recursion into `ℕ`.

## Lean status
`lean_status: core` (implicit). `Wff` is an inductive type, so Lean's
**structural recursion / well-founded recursion** is automatic (`Wff.eval` and
every function in the file recurse without an explicit measure); `sizeOf` is the
auto-generated degree-like measure. No named theorem, but every `induction d` /
structural `def` in `validation/proof-checks.lean` relies on it.

## Type / well-formedness check
`well_formed`. All three measures are total functions `Wff → ℕ`. The key
property to record is **strict decrease**: `deg(ψ) < deg(φ)` for every immediate
subformula `ψ` of `φ` — this, plus well-foundedness of `<` on `ℕ`
(`well_ordering_principle`), licenses the recursion.

## Specialization / boundary cases
- `φ` atomic: all measures minimal (`deg = ht = 0`, `|φ| = 1`).
- `deg(φ) = 0` iff `φ` is an atom or `⊥`.
- **quantifier rank** (first-order): the analogous measure counting nested
  quantifiers — drives induction in `prenex_normal_form`, `coincidence_lemma`,
  `truth_lemma_fol`.
- **substitution** `φ[t/x]`: **not** a subformula of `φ`, and can have larger
  length, but the same *quantifier rank* — so lemmas about substitution induct
  on quantifier rank, not on subformula structure (a common subtlety in
  `substitution_lemma_semantic`).

## Hypothesis-dropped counterexamples
- **a measure that does not strictly decrease** (e.g. "number of atoms" — `¬φ`
  and `φ` have the same): recursion using it is not well-founded; the definition
  may not terminate / the induction is invalid.
- **infinite formula**: no finite complexity — not a wff.
- **circular "definition"** (`φ` a subformula of itself): impossible for wffs,
  possible for the *co*inductive analogue (streams) — where formula induction
  fails.

## Common misuse
Inducting on "number of atoms" or "number of `∧`s" (not strictly decreasing on
all subformulas); assuming a substitution result is structurally smaller (use
quantifier rank instead); ignoring the finiteness of `atoms(φ)` when it is
exactly what makes a decision procedure terminate.

## Related nodes (non-prerequisite)
- `bridges`: `structural_induction_wff` ↔ `strong_induction` on `ℕ`.
- `enables`: `tautology_decidable` (finite atom set), `truth_table` (`2ⁿ` rows).
- `analogue`: quantifier rank (first-order).
- `needs`: `well_ordering_principle` / `metatheoretic_induction` (`<` on `ℕ`
  well-founded).

## Sources
[enderton_logic_2e] §1.4; [vandalen_5e] §1.1; [chiswell_hodges] ch. 2.
