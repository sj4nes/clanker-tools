# satisfiability

## Type
definition  (epistemic status: `definition`; `constructive_grade: intuitionistic`)

## Statement
A wff `φ` is **satisfiable** iff `v ⊨ φ` for **at least one** truth assignment
`v` — `∃v, ⟦φ⟧_v = T`. A set `Γ` is satisfiable iff some `v` satisfies every
member.

## Symbols
- `φ`: a wff; `Γ`: a set of wffs.
- the witness: a satisfying assignment `v`.

## Prerequisites (tsort edges into this node)
`satisfaction`.

## Content
The existential dual of `tautology`. `φ` satisfiable iff `φ` is **not** a
`contradiction_unsat` iff `¬φ` is not a tautology. It is the propositional
**SAT** problem — decidable (`truth_table`), NP-complete.

Key roles:
- `Γ` satisfiable ⟺ `Γ` **consistent** (`consistency`), by
  `soundness_prop` + `post_completeness_theorem`;
- `Γ ⊨ φ` ⟺ `Γ ∪ {¬φ}` **unsatisfiable** (refutation);
- `compactness_prop`: `Γ` satisfiable ⟺ every finite subset is.

## Constructive grade
`intuitionistic` — as a definition, and for a **finite** atom set the witness is
found by finite search (constructive). For an infinite atom set,
`compactness_prop` (which produces a satisfying assignment from finite
satisfiability) is `needs_full_classical`.

## Lean status
`lean_status: core`. `validation/proof-checks.lean`:
`Wff.Sat a := ∃ v, eval v a = true`;
`sat_iff_not_contra : Sat a ↔ ¬ Contradiction a` (`←` via
`Classical.byContradiction`). A concrete satisfiable `φ` gets its witness by
`exact ⟨fun _ => true, by decide⟩`-style.

## Type / well-formedness check
`well_formed`. `∃v` over assignments; the witness is a **total** assignment
(`truth_assignment`), though only its restriction to `atoms(φ)` matters. For
infinite `Γ`, "satisfiable" is genuinely `Σ¹`-flavoured and its finite
character (`compactness_prop`) is the substantive fact.

## Specialization / boundary cases
- `φ` a tautology ⟹ satisfiable (every `v` works).
- `φ = p`: satisfiable, not a tautology.
- `φ = ⊥`: unsatisfiable.
- `Γ` finite: satisfiable iff `⋀Γ` is; check the `2ⁿ` truth table.
- `Γ` = a set of Horn clauses / 2-CNF: satisfiability is **polynomial**
  (unit propagation / implication graph) — the tractable fragments of SAT.

## Hypothesis-dropped counterexamples
- **check one assignment and conclude unsatisfiable**: `p ∨ q` is `F` at
  `p = q = F` but satisfiable elsewhere — one failing assignment proves nothing.
- **`Γ` finitely satisfiable but not satisfiable**: forbidden by
  `compactness_prop` — this is exactly the content of compactness.
- **confuse with "consistent"**: same extension by soundness+completeness, but
  "satisfiable" is semantic and "consistent" is `Γ ⊬ ⊥`.

## Common misuse
Concluding unsatisfiability from a single failing assignment; conflating
satisfiability (semantic) with consistency (syntactic); assuming SAT is easy
because the truth table is "just" `2ⁿ` rows; forgetting the refutation reduction
for entailment.

## Related nodes (non-prerequisite)
- `complement_of`: `contradiction_unsat`.
- `dual_of`: `tautology`.
- `equivalent_to` (for sets, via completeness): `consistency`.
- `feeds`: `compactness_prop`, the refutation form of `semantic_consequence`.
- `related`: SAT, NP-completeness, Horn/2-CNF tractable fragments.

## Sources
[enderton_logic_2e] §1.2; [vandalen_5e] §1.2; [chiswell_hodges] §2.3.
