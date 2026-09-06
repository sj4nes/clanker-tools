# structural_induction

## Type
definition  (epistemic status: `definition`; `constructive_grade: intuitionistic`)

## Statement
For a set `S` given by an `inductive_definition` with base clauses and closure
operations: to prove `∀s ∈ S, P(s)`, prove `P` of each base element and prove
that each closure operation **preserves** `P` (assuming `P` of the immediate
constituents — the structural IH).

## Symbols
- `S`: an inductively defined set (wffs, terms, derivations, lists, trees,
  syntax).
- `P`: a predicate on `S`.
- for each constructor `c` of arity `k`: the obligation
  `P(x₁) ∧ … ∧ P(x_k) → P(c(x₁, …, x_k))`.

## Prerequisites (tsort edges into this node)
`inductive_definition`, `structural_induction_wff`.

## Content
The induction principle **is** part of the data of an `inductive_definition`:
`S` is the *least* set closed under the clauses, so any `P`-closed set contains
`S`. `weak_induction` is the instance for `ℕ` (constructors `0`, `succ`);
`structural_induction_wff` is the instance for `Wff`; the same schema drives
`recursion_on_wff`, `term_evaluation`, `tarski_satisfaction`,
`truth_lemma_prop`/`_fol`, and soundness proofs (induction on the derivation).

## Constructive grade
`intuitionistic` — it is the eliminator (recursor) of an inductive type, pure
minimal logic. Computes.

## Lean status
`lean_status: core`. `induction d with | …` over any `inductive` type. In
`validation/proof-checks.lean`: `soundness` (induction on `Deriv`), `deduction`
(induction on `H`), `Wff.conj_injective` (no-confusion), and the `aux` lemma of
`strong_of_weak` (induction on `Nat`).

## Type / well-formedness check
`well_formed` **iff** every constructor gets a case and the IH offered is
exactly "`P` of the immediate sub-objects" — no more (assuming `P` of
non-constituents is unsound) and no less (skipping a constructor leaves a gap).
For mutually inductive definitions (terms ⇄ formulas), the induction is
**mutual** and every type in the family needs its clauses.

## Specialization / boundary cases
- `S = ℕ`: `weak_induction`.
- `S = List α`: base `[]`, step `P(xs) → P(x :: xs)`.
- `S = Wff`: `structural_induction_wff` — base atoms/`⊥`, steps for
  `¬, ∧, ∨, →, ↔`.
- `S =` derivations of a calculus: "rule induction" — one case per inference
  rule; this is how `soundness_*` and cut-admissibility are proved.
- induction on a **derived** measure (`formula_complexity`, quantifier rank)
  reduces to `strong_induction` on `ℕ`.

## Where it fails / is misapplied
- **the set is not the least fixed point**: if `S` is defined by "the largest
  set such that …" (a *co*inductive definition — streams, bisimilarity),
  structural induction is **invalid**; coinduction is the tool.
- **missing constructor case** — silent unsoundness.
- **IH used on a non-subterm** (e.g. assuming `P` of a substitution result while
  proving `P` of a quantifier) — the substitution instance is not structurally
  smaller; use induction on `formula_complexity` or a size measure instead.
- non-well-founded "inductive" definitions (no base clause).

## Common misuse
Treating a coinductive object inductively; assuming the IH for the whole object;
omitting the base clause(s); on `Wff`, forgetting the `↔` or `⊥` case; using
structural induction where the recursion is on substitution depth.

## Related nodes (non-prerequisite)
- `instance_of` (reverse): `weak_induction`, `structural_induction_wff` are
  instances.
- `dual_of`: coinduction (out of scope).
- `enables`: `recursion_on_wff` and every semantic function defined by it.
- `generalised_by`: well-founded induction, `transfinite_induction`.

## Sources
[vandalen_5e] §1.1 (induction on formulas); [enderton_logic_2e] §1.4
(the induction principle); [chiswell_hodges] ch. 2–3.
