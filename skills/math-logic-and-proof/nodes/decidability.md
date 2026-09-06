# decidability

## Type
definition  (an informal primitive for the boundary block;
`constructive_grade: intuitionistic`)

## Statement
A set `S` (of naturals, strings, wffs, …) is **decidable** (recursive,
computable) if there is an **always-halting** procedure that, given an input,
correctly answers "yes, `x ∈ S`" or "no, `x ∉ S`". **Semidecidable**
(recursively enumerable, r.e.): a procedure that halts with "yes" exactly when
`x ∈ S` (and may run forever otherwise).

## Symbols
- `S`: a set; the "procedure" — made precise by `church_turing_thesis`.

## Prerequisites (tsort edges into this node)
none — an **informal primitive** for the boundary block (`conventions.md`).
Computability theory (Turing machines, recursive functions) is out of scope; the
capsule uses only the named boundary facts.

## Content
The predicate distinguishing the **decidable** results of the capsule
(`tautology_decidable` — propositional validity; monadic FOL; Presburger
arithmetic; real closed fields) from the **undecidable** ones
(`undecidability_fol_validity`, `halting_problem`, `godel_incompleteness_first`'s
"recursively axiomatised" hypothesis, first-order theory-membership in general).

Key facts (stated, used, not proved): `S` decidable iff both `S` and its
complement are r.e.; the decidable sets are closed under `∩`, `∪`, complement;
the r.e. sets are closed under `∩`, `∪` but **not** complement.

## Constructive grade
`intuitionistic` — "decidable" is itself a constructive notion (an algorithm is
a construction). A *classically* decidable set with no known algorithm is
"decidable" only in a non-effective sense — the capsule means the effective one.

## Lean status
`lean_status: none` (informal). Lean has a `Decidable` type class (a proof-
relevant decision procedure) and `decide` — used in `validation/proof-checks.lean`
for finite checks — but that is decidability of *specific propositions*, not the
computability-theoretic notion of a decidable *set*.

## Type / well-formedness check
`well_formed` as a predicate on sets, **relative to** an identification of
"procedure" with a formal model (`church_turing_thesis`). The always-halting
requirement is what separates it from semidecidability.

## Specialization / boundary cases
- **finite `S`**: decidable (table lookup).
- **`S` and complement both r.e.**: decidable (dovetail).
- propositional tautologies: decidable (`tautology_decidable`, `2ⁿ` table) but
  **NP-complete** — decidable ≠ efficient.
- first-order validity: r.e. (enumerate proofs — `godel_completeness_theorem`)
  but **not** decidable (`undecidability_fol_validity`).
- the set of theorems of a **recursively axiomatised** theory: r.e.; decidable
  iff the theory is **complete** (decide `σ` by searching for a proof of `σ` or
  of `¬σ`).

## Hypothesis-dropped counterexamples
- **drop "always halting"**: you get semidecidability — strictly weaker; the
  halting set is r.e. but not decidable.
- **non-effective "decidability"** (classical existence of an algorithm): e.g.
  "is `n` in the finite set of counterexamples to a settled conjecture" — the
  set is decidable, but you may not know the procedure.

## Common misuse
Conflating decidable with efficiently decidable (SAT); conflating decidable with
r.e.; assuming FOL validity is decidable by analogy with propositional; treating
Lean's `Decidable` class as the computability notion.

## Related nodes (non-prerequisite)
- `made_precise_by`: `church_turing_thesis`.
- `used_by`: `tautology_decidable`, `undecidability_fol_validity`,
  `halting_problem`, `godel_incompleteness_first` (the "recursively axiomatised"
  hypothesis).
- `related`: r.e. sets, NP-completeness, the arithmetical hierarchy (all out of
  scope to develop).

## Sources
[bbj_5e] ch. 3–4; [enderton_logic_2e] §3.0; Sipser, *Introduction to the Theory
of Computation*.
