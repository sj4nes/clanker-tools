# truth_value_recursion

## Type
definition  (epistemic status: `definition`; `constructive_grade: intuitionistic`)

## Statement
Given a `truth_assignment` `v : Atom → {T, F}`, extend it to a function
`⟦·⟧_v : Wff → {T, F}` by recursion on wff structure:

    ⟦p⟧_v      = v(p)                      (p atomic)
    ⟦⊥⟧_v      = F
    ⟦¬φ⟧_v     = T  iff  ⟦φ⟧_v = F
    ⟦φ ∧ ψ⟧_v  = T  iff  ⟦φ⟧_v = T and ⟦ψ⟧_v = T
    ⟦φ ∨ ψ⟧_v  = T  iff  ⟦φ⟧_v = T or  ⟦ψ⟧_v = T
    ⟦φ → ψ⟧_v  = F  iff  ⟦φ⟧_v = T and ⟦ψ⟧_v = F
    ⟦φ ↔ ψ⟧_v  = T  iff  ⟦φ⟧_v = ⟦ψ⟧_v

## Symbols
- `v`: a truth assignment (`truth_assignment`).
- `⟦φ⟧_v` (or `v̄(φ)`): the value of `φ` under `v`, in `{T, F}` = `Bool`.

## Prerequisites (tsort edges into this node)
`truth_assignment`, `recursion_on_wff`, `true_false_constants`.

## Content — why it is well defined
This is the exemplar use of `recursion_on_wff`: one clause per constructor of
`Wff`, and `wff_unique_readability` guarantees the clauses do not conflict, so
`⟦·⟧_v` is a **total function**, uniquely determined. Without unique readability
`⟦p ∧ q ∨ r⟧_v` would be ambiguous.

Truth-functionality: `⟦φ⟧_v` depends **only on the values of the atoms
occurring in `φ`** (proved by the same induction) — the propositional
`coincidence_lemma`.

## Constructive grade
`intuitionistic` — a structural recursion into a decidable type; it is exactly
`Wff.eval : (Nat → Bool) → Wff → Bool` in Lean, a computable function.

## Lean status
`lean_status: core`. `validation/proof-checks.lean` §1:
```
def eval (v : Nat → Bool) : Wff → Bool
  | atom n => v n | fls => false | neg p => ! eval v p
  | conj p q => eval v p && eval v q | disj p q => eval v p || eval v q
  | impl p q => (! eval v p) || eval v q
```
and `example : eval v (conj p q) = (eval v p && eval v q) := rfl`.

## Type / well-formedness check
`well_formed`. The recursion is well-founded on `formula_complexity` (each
recursive call is on a strict subformula). Codomain `{T, F}` throughout;
`→` and `↔` clauses defined via the others (or directly). The `⊥` base clause is
essential — a grammar with `⊤` primitive needs its clause too (here
`⊤ := p → p`, so `⟦⊤⟧_v = T` is derived).

## Specialization / boundary cases
- atomic `φ`: `⟦φ⟧_v = v(φ)` — the base case.
- closed `φ` (no atoms): `⟦φ⟧_v` is constant in `v`.
- restricting to `v ↾ atoms(φ)`: unchanged (truth-functionality).
- the **first-order generalisation** is `truth_value_recursion` for
  `first_order_wff` with the added `∀`/`∃` clauses ranging over the domain —
  that is `tarski_satisfaction`.

## Hypothesis-dropped counterexamples
- **drop unique readability**: `⟦·⟧_v` is not well-defined — `p ∧ q ∨ r` gets two
  values. (`wff_unique_readability` is the guard.)
- **drop the `⊥`/atom base clauses**: the recursion does not bottom out.
- **non-truth-functional connective** (e.g. a modal `□`): `⟦□φ⟧_v` cannot be
  computed from `⟦φ⟧_v` alone — needs a Kripke frame, not a single `v`. This is
  precisely what distinguishes classical propositional logic.

## Common misuse
Defining a semantic function "by recursion on `φ`" without `wff_unique_readability`
in hand; forgetting the `↔` or `⊥` clause; assuming the `→` clause is
`⟦φ⟧_v = F or ⟦ψ⟧_v = T` is *wrong* — it is correct (material implication), but
students often expect relevance; treating a modal/temporal operator as
truth-functional.

## Related nodes (non-prerequisite)
- `instance_of`: `recursion_on_wff`.
- `generalised_by`: `tarski_satisfaction` (adds the quantifier clauses).
- `feeds`: `satisfaction` (which is just `⟦φ⟧_v = T`).
- `related`: `coincidence_lemma` (its truth-functionality half).

## Sources
[enderton_logic_2e] §1.2 (the "truth assignment extends uniquely" lemma);
[vandalen_5e] §1.2; [chiswell_hodges] §2.3.
