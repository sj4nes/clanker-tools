# truth_assignment

## Type
definition  (epistemic status: `definition`; `constructive_grade: intuitionistic`)

## Statement
A **truth assignment** (valuation) for a propositional language is a function
`v : Atom → {T, F}` assigning a truth value to every atomic formula.

## Symbols
- `Atom`: the set of atomic formulas — here identified with a set of `symbol`s
  (`v₀, v₁, …`).
- `v`: the assignment; in the Lean model `v : Nat → Bool`.
- `{T, F}` = `Bool` — the two-element set of truth values (`objects.md`,
  `TruthValue`).

## Prerequisites (tsort edges into this node)
`symbol`, `wff_syntax`.

## Content
The primitive semantic input. Everything on the `⊨` side is a function of `v`:
`truth_value_recursion` lifts `v` from atoms to all wffs; `satisfaction`,
`tautology`, `satisfiability`, `semantic_consequence`, `logical_equivalence` all
quantify over assignments. A truth assignment is the propositional shadow of a
first-order `structure` **+** `assignment` (there the domain and interpretations
carry the load; here a single bit per atom suffices).

## Constructive grade
`intuitionistic` — a function into a decidable two-element type. Deciding
`v n` for a given `n` is immediate; the classicality on the `⊨` side enters only
when **quantifying over all `v`** (`tautology`, `logical_equivalence`) for an
infinite atom set.

## Lean status
`lean_status: core`. `validation/proof-checks.lean` models `v : Nat → Bool`
directly; `eval v : Wff → Bool` and `Entails Γ p := ∀ v, …` are built on it.

## Type / well-formedness check
`well_formed`. `v` must be **total** on `Atom` — a partial assignment does not
determine truth values for wffs mentioning the undefined atoms (partial
valuations are used in tableaux / DPLL as *intermediate* objects, but a
`truth_assignment` proper is total). Only the **finitely many** atoms occurring
in a given wff `φ` matter (`formula_complexity`, the coincidence property):
`eval v φ` depends only on `v ↾ atoms(φ)`.

## Specialization / boundary cases
- **finite atom set** `{p₁, …, pₙ}`: exactly `2ⁿ` assignments — the rows of a
  `truth_table`; the whole propositional semantics is then decidable by
  enumeration.
- a wff with **no atoms** (built from `⊤`, `⊥` only): its value is
  assignment-independent.
- **restricting** `v` to `atoms(φ)`: the coincidence property — `eval v φ`
  unchanged.
- identifying `v` with the subset `{p : v p = T} ⊆ Atom`: assignments ↔ subsets
  of `Atom` ↔ points of `2^Atom` (`function_space`).

## Hypothesis-dropped counterexamples
- **partial `v`** (undefined at some atom of `φ`): `eval v φ` is undefined —
  `truth_value_recursion` has no clause for a missing atom value. This is why
  the definition insists on totality.
- **three-valued `v`** (`{T, F, U}`): a different semantics (Kleene / Łukasiewicz)
  — out of scope; classical propositional logic is two-valued by definition.

## Common misuse
Treating a partial assignment as a `truth_assignment`; conflating `v` (a
semantic object) with an assumption set `Γ` (syntactic); forgetting that a
tautology check needs **all** assignments, not a sample; assuming an infinite
atom set makes the semantics undecidable (each *wff* still has finitely many
atoms — `tautology_decidable`).

## Related nodes (non-prerequisite)
- `lifts_to`: `truth_value_recursion` (atoms → all wffs).
- `propositional_shadow_of`: `structure` + `assignment` (first-order).
- `identified_with`: a point of `2^Atom` / a subset of `Atom`.
- `feeds`: `satisfaction`, `semantic_consequence`, and everything downstream.

## Sources
[enderton_logic_2e] §1.2; [vandalen_5e] §1.2; [chiswell_hodges] §2.3.
