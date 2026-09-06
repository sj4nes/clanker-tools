# conjunctive_normal_form

## Type
theorem  (epistemic status: `proved_theorem`; `constructive_grade: needs_LEM` —
via `negation_normal_form`)

## Statement
Every wff is logically equivalent to one in **conjunctive normal form (CNF)**: a
**conjunction of clauses**, each clause a **disjunction of literals**:

    ⋀ᵢ ( ⋁ⱼ ℓᵢⱼ )        ℓᵢⱼ a literal (atom or negated atom).

## Symbols
- `φ`: any wff; `cnf(φ)`: an equivalent CNF wff.
- clause: `ℓ₁ ∨ … ∨ ℓₖ`. Empty clause `= ⊥`; empty conjunction `= ⊤`.

## Prerequisites (tsort edges into this node)
`negation_normal_form`, `distributivity_prop`.

## Proof / algorithm
Convert to `negation_normal_form`, then repeatedly apply
`distributivity_prop` **∨ over ∧**: `φ ∨ (ψ ∧ χ) ↝ (φ ∨ ψ) ∧ (φ ∨ χ)`, pushing
`∨` inside `∧` until the formula is a conjunction of clauses. Each step preserves
`≡` (`substitution_of_equivalents`).

**Blow-up**: naive distribution can be **exponential** in size (`(p₁ ∧ q₁) ∨ … ∨
(pₙ ∧ qₙ)` → `2ⁿ` clauses). The **Tseitin transformation** gives an
*equisatisfiable* CNF of *linear* size by introducing fresh atoms — not
logically equivalent, but same satisfiability, which is what SAT solvers need.

## Constructive grade
`needs_LEM` — inherits from `negation_normal_form`. The distribution step itself
is `intuitionistic`.

## Lean status
`lean_status: cited`. The engine `distrib_and_or` **is** checked in
`validation/proof-checks.lean`; the full `cnf` function + correctness is not
built (Mathlib-style).

## Type / well-formedness check
`well_formed`. **Not unique** — `p` and `p ∧ (q ∨ ¬q)` are both CNF and
equivalent; `(p ∨ q) ∧ (p ∨ ¬q)` and `p` likewise. A **canonical** CNF exists
(full clauses over all atoms, à la maxterms) but is exponential and rarely used.
Clause = disjunction; the top level = conjunction — swapping is `DNF`.

## Specialization / boundary cases
- a single clause: `φ` is already a disjunction of literals.
- `⊤` = empty conjunction; `⊥` = a formula with the empty clause.
- **Horn CNF** (≤ 1 positive literal per clause): satisfiability is
  **linear-time** (unit propagation) — the tractable fragment behind Datalog /
  Prolog.
- **2-CNF** (≤ 2 literals per clause): satisfiability in linear time (implication
  graph / SCCs).
- **resolution** operates on CNF: `(C ∨ p) , (D ∨ ¬p) ⊢ (C ∨ D)`; CNF + the
  empty clause = refutation.

## Hypothesis-dropped counterexamples
- **stop before fully distributing**: `p ∨ (q ∧ r)` is not CNF.
- **use `∧` over `∨` distribution** (the DNF direction): produces DNF, not CNF.
- **treat Tseitin CNF as logically equivalent**: it is only *equisatisfiable* —
  the fresh atoms change the models.
- **assume uniqueness**: two very different CNFs can be equivalent.

## Common misuse
Distributing the wrong way (getting DNF); stopping early; conflating logical
equivalence with equisatisfiability (Tseitin); assuming a canonical/unique CNF;
ignoring the exponential blow-up when reasoning about proof size.

## Related nodes (non-prerequisite)
- `uses`: `negation_normal_form`, `distributivity_prop`.
- `dual_of`: `disjunctive_normal_form`.
- `related`: resolution, DPLL/CDCL, Tseitin transformation, Horn/2-CNF
  tractable fragments, `tautology_decidable` (SAT).

## Sources
[enderton_logic_2e] §1.5; [chiswell_hodges] ch. 3; Tseitin (1968).
