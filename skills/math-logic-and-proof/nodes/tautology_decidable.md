# tautology_decidable

## Type
theorem  (epistemic status: `proved_theorem` / `decidability` result;
`constructive_grade: intuitionistic`)

## Statement
The set of propositional tautologies is **decidable**: there is an
always-terminating procedure that, given a wff `φ`, answers whether `⊨ φ`. Same
for satisfiability, unsatisfiability, `φ ⊨⊨ ψ`, and `{φ₁,…,φₖ} ⊨ ψ`.

## Symbols
- `φ`: a wff with `n = |atoms(φ)|` atoms.
- the procedure: build the `2ⁿ`-row `truth_table`, check the final column.

## Prerequisites (tsort edges into this node)
`tautology`, `truth_table`, `decidability`.

## Proof
`⊨ φ` iff `⟦φ⟧_v = T` for all `v`; by truth-functionality `⟦φ⟧_v` depends only
on `v ↾ atoms(φ)`, and there are exactly `2ⁿ` such restrictions. Evaluate `φ`
(`truth_value_recursion`, a terminating recursion on `formula_complexity`) at
each — a finite computation — and conjoin. Terminates always; correct by the
definition of `tautology`.

## Constructive grade
`intuitionistic` — a bounded, effective computation. This is the sharp contrast
with `undecidability_fol_validity`: **propositional** validity is decidable,
first-order validity is not, and the boundary is exactly the quantifiers over an
unbounded domain.

## Lean status
`lean_status: instance`. For a **concrete** `φ` with atoms mapped to `Fin k`,
`decide` runs the table (`validation/proof-checks.lean` uses
`cases … <;> rfl` / `decide` for the connective and functional-completeness
checks — the same enumeration). A general
`instance : Decidable (Wff.Taut φ)` would enumerate `atoms(φ) → Bool`; feasible
in plain Lean with an explicit atom list, not built here.
`bc validation/instance-checks.bc` runs an 8-row instance.

## Type / well-formedness check
`well_formed`. "Decidable" is via `decidability` / the `church_turing_thesis`
(the procedure is patently effective). The `2ⁿ` bound is essential to
termination — it comes from `φ` being **finite** (finitely many atoms).

## Specialization / boundary cases
- `n = 0`: 1-step check.
- **SAT** (the satisfiability version) is decidable but **NP-complete** —
  decidable ≠ efficient. Modern SAT solvers (DPLL/CDCL) decide instances with
  millions of variables in practice but have exponential worst case.
- **QBF** (quantified Boolean formulas): still decidable, PSPACE-complete.
- **fragments**: 2-SAT, Horn-SAT, XOR-SAT are polynomial-time decidable.
- adding a single first-order quantifier over an infinite domain breaks
  decidability (`undecidability_fol_validity`).

## Hypothesis-dropped counterexamples
- **infinitely many atoms in `φ`**: impossible — every wff is finite. This is
  precisely why the propositional case is decidable and the predicate case is
  not.
- **allow a "for all `x`" over a domain**: monadic FOL is still decidable, but
  full FOL is not — the quantifier plus a binary relation suffices to encode
  Turing machines.
- **treat the table as a proof**: the procedure decides `⊨ φ`; a *derivation*
  `⊢ φ` also exists (`post_completeness_theorem`) but the table is not one.

## Common misuse
Conflating "decidable" with "efficiently decidable" (SAT is the counterexample);
assuming FOL validity is decidable by analogy; treating the truth-table verdict
as a formal proof; forgetting that the `2ⁿ` cost makes large-`n` reasoning
infeasible even though it is decidable.

## Related nodes (non-prerequisite)
- `implemented_by`: `truth_table`.
- `contrast_with`: `undecidability_fol_validity` (the FOL boundary).
- `related`: SAT / NP-completeness, DPLL/CDCL, QBF/PSPACE, Horn/2-SAT.

## Sources
[enderton_logic_2e] §1.2; [bbj_5e] ch. 10–11; [chiswell_hodges] §2.3;
Cook (1971) (SAT NP-completeness).
