# truth_table

## Type
algorithm  (epistemic status: `algorithm`; `constructive_grade: intuitionistic`)

## Statement
For a wff `φ` whose atoms are among `p₁, …, pₙ`, the **truth table** of `φ` is
the tabulation of `⟦φ⟧_v` over all `2ⁿ` assignments `v : {p₁,…,pₙ} → {T,F}`. It
is a finite object that **completely determines** `φ` up to logical equivalence.

## Symbols
- `φ`: a wff with `n` atoms.
- rows: the `2ⁿ` assignments (`truth_assignment` restricted to `atoms(φ)`).
- the last column: `⟦φ⟧_v` for each row (`truth_value_recursion`).

## Prerequisites (tsort edges into this node)
`satisfaction`, `formula_complexity`.

## Content
The truth table is the **decision procedure** for every propositional semantic
question:
- `tautology`: all rows `T`;
- `contradiction_unsat`: all rows `F`;
- `satisfiability`: some row `T`;
- `logical_equivalence` of `φ`, `ψ`: identical final columns (over the union of
  their atoms);
- `semantic_consequence` `{φ₁,…,φₖ} ⊨ ψ`: every row where all `φᵢ` are `T` has
  `ψ` `T`.

Cost: `2ⁿ` rows — exponential in the number of atoms, but **finite and
mechanical**. This is `tautology_decidable` made concrete, and the `bc`
instance-check file runs it for the hypothetical syllogism.

## Constructive grade
`intuitionistic` — a finite computation. Each row is `eval` (decidable); the
verdict is a finite conjunction/disjunction over rows.

## Lean status
`lean_status: instance`. For a **concrete** `φ` with atoms fixed to `Fin k`,
`decide` evaluates the table (`validation/proof-checks.lean` uses
`cases a <;> cases b <;> rfl` / `decide` for the connective and functional-
completeness checks — the same enumeration). `bc validation/instance-checks.bc`
prints an 8-row table.

## Type / well-formedness check
`well_formed`. The table must range over **all** `2ⁿ` assignments to
`atoms(φ)` — omitting a row, or using more atoms than occur, gives a wrong
verdict. Comparing two formulas requires the table over the **union** of their
atom sets (a formula that ignores an atom still needs that atom's column when
compared to one that uses it).

## Specialization / boundary cases
- `n = 0`: a 1-row table; `φ` is `⊤` or `⊥` up to equivalence.
- `n = 1`: 2 rows — one of the 4 unary functions.
- `n = 2`: 4 rows — one of the 16 binary connectives
  (`binary_boolean_functions_16`).
- large `n`: still decidable, but `2ⁿ` is why **SAT** is the canonical
  NP-complete problem — the table is a *certificate-checkable* but not
  *efficient* method.

## Hypothesis-dropped counterexamples
- **skip a row**: `p ∨ ¬p` "verified" as a tautology from 1 of its 2 rows is
  vacuous; the method's validity is exactly its exhaustiveness.
- **compare final columns over mismatched atom sets**: `p` and `p ∧ (q ∨ ¬q)`
  have "the same" 2-row table for `p` but are only equivalent because the second
  is checked over `{p, q}` (4 rows) and the `q` columns cancel.
- **infinitely many atoms in `φ`**: impossible — every wff is finite, so the
  table is always finite (`formula_complexity`).

## Common misuse
Treating a passing table as a *proof in the object logic* (it is a semantic
verification — `post_completeness_theorem` says a derivation also exists, but the
table is not one); comparing formulas over different atom sets; forgetting the
`2ⁿ` blow-up when reasoning about feasibility; using a partial table.

## Related nodes (non-prerequisite)
- `implements`: `tautology_decidable`.
- `computes`: `tautology`, `satisfiability`, `logical_equivalence`,
  `semantic_consequence`.
- `alternative_to`: `negation_normal_form` → `disjunctive_normal_form`
  (`dnf_from_truth_table` reads a DNF straight off the `T` rows).
- `related`: SAT, DPLL/CDCL (efficient-in-practice alternatives — out of scope).

## Sources
[enderton_logic_2e] §1.2; [vandalen_5e] §1.2; [chiswell_hodges] §2.3.
