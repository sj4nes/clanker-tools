# contradiction_unsat

## Type
definition  (epistemic status: `definition`; `constructive_grade: intuitionistic`)

## Statement
A wff `φ` is a **contradiction** (unsatisfiable) iff `v ⊭ φ` for **every**
truth assignment `v` — `⟦φ⟧_v = F` for all `v`. A set `Γ` is **unsatisfiable**
iff no `v` satisfies all of `Γ`.

## Symbols
- `φ`: a wff; `Γ`: a set of wffs.

## Prerequisites (tsort edges into this node)
`satisfaction`.

## Content
The dual of `tautology`: `φ` is a contradiction iff `¬φ` is a tautology iff `φ`
is not `satisfiability`. Central to proof by refutation:
- `Γ ⊨ ψ` iff `Γ ∪ {¬ψ}` is unsatisfiable — the reduction every SAT-based
  theorem prover uses;
- `Γ` **consistent** (`consistency`) iff `Γ` is satisfiable
  (`soundness_prop` + `post_completeness_theorem`);
- `compactness_prop`: `Γ` unsatisfiable iff some **finite** subset is.

## Constructive grade
`intuitionistic` as a definition. `φ` classically unsatisfiable ⟺ `⊢ ¬φ`
(completeness); and `⊢ ¬φ` is *often* intuitionistic even when `⊢ φ ∨ ¬φ` is not
— proving something is contradictory is constructively easier than proving a
disjunction.

## Lean status
`lean_status: core`. `validation/proof-checks.lean`:
`Wff.Contradiction a := ∀ v, eval v a = false`, with
`taut_iff_neg_contra : Taut a ↔ Contradiction (neg a)` and
`sat_iff_not_contra : Sat a ↔ ¬ Contradiction a` (the latter's `←` uses
`Classical.byContradiction`).

## Type / well-formedness check
`well_formed`. "For every `v`" ranges over all `2ⁿ` assignments to `atoms(φ)`.
`Γ` unsatisfiable is `¬ ∃ v, v ⊨ Γ` — a `Π`-flavoured statement; for infinite
`Γ` its finite character (`compactness_prop`) is what makes it tractable.

## Specialization / boundary cases
- `φ = ⊥`: the paradigm contradiction.
- `φ = p ∧ ¬p`: contradiction; `Γ = {p, ¬p}`: unsatisfiable set.
- `φ = p ↔ ¬p`: contradiction (no `v` makes a formula equivalent to its
  negation).
- `Γ` finite and unsatisfiable ⟹ `⋀Γ` is a contradiction; `Γ` infinite ⟹
  compactness gives a finite unsatisfiable `Γ₀ ⊆ Γ`.

## Hypothesis-dropped counterexamples
- **check some assignments**: `p ∧ ¬q` is `F` at `p = F` — but it is
  **satisfiable** (`p = T, q = F`); a partial check misleads.
- **confuse with "not a tautology"**: `p` is neither a tautology nor a
  contradiction (contingent).
- **`Γ` finitely satisfiable but claimed unsatisfiable**: impossible by
  `compactness_prop` — an infinite unsatisfiable set always has a finite
  unsatisfiable subset.

## Common misuse
Calling a contingent formula a contradiction; conflating "`Γ` is inconsistent"
(syntactic) with "`Γ` is unsatisfiable" (semantic) — equivalent by
soundness+completeness, but distinct notions; forgetting the refutation
reduction `Γ ⊨ ψ ⟺ Γ ∪ {¬ψ}` unsatisfiable; assuming an infinite unsatisfiable
set has no finite unsatisfiable core.

## Related nodes (non-prerequisite)
- `dual_of`: `tautology` (`φ` contradiction ⟺ `¬φ` tautology).
- `complement_of`: `satisfiability`.
- `feeds`: the refutation form of `semantic_consequence`; `compactness_prop`;
  `consistency` (via completeness).

## Sources
[enderton_logic_2e] §1.2; [vandalen_5e] §1.2; [chiswell_hodges] §2.3.
