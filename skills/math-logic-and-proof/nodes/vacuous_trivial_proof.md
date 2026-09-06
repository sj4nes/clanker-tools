# vacuous_trivial_proof

## Type
definition  (epistemic status: `definition`; `constructive_grade: intuitionistic`)

## Statement
Two degenerate ways an implication `P → Q` holds outright:
- **vacuous**: `¬P` (the antecedent is false / unsatisfiable) — then `P → Q` for
  any `Q`.
- **trivial**: `Q` (the consequent is provable outright) — then `P → Q` for any
  `P`.

For a universally quantified `∀x (P(x) → Q(x))`: vacuously true if no `x`
satisfies `P`; trivially true if every `x` satisfies `Q`.

## Symbols
- `P`, `Q`: formulas.

## Prerequisites (tsort edges into this node)
`vacuous_quantification`, `implication_as_disjunction`.

## Content
Both are immediate from `implication_as_disjunction`'s **intuitionistic**
direction `(¬P ∨ Q) → (P → Q)`: a proof of `¬P` or a proof of `Q` gives `P → Q`
directly (`vacuous_trivial_proof` in Lean would be `fun _ => hQ` or
`fun hp => absurd hp hnP`). The `↔` needs `LEM`; the *use as a proof method*
does not.

## Constructive grade
`intuitionistic` — `fun hp => absurd hp hnP` and `fun _ => hQ` are minimal-logic
terms.

## Lean status
`lean_status: core`. `fun _ => h` and `fun hp => absurd hp hnp` /
`(hnp hp).elim` are the two patterns; `False.elim` / `absurd` are the vacuous
case. Not a headline node, not separately checked, but the mechanism is
`impl_iff_or`'s `←` direction in `validation/proof-checks.lean`.

## Type / well-formedness check
`well_formed`. The vacuous case requires an **actual proof of `¬P`** (or that
the domain of the quantifier restricted by `P` is empty) — "P looks unlikely" is
not vacuous truth. The trivial case requires `Q` proved **without** using `P`.

## Specialization / boundary cases
- `∀x ∈ ∅, φ(x)` — vacuously true (empty domain); `∀x ∈ ∅, φ(x) ∧ ¬φ(x)` is
  also true, which is a useful sanity check on quantifier conventions
  (`conventions.md`).
- "every element of the empty set is a group" — vacuously true.
- base cases of inductions are often trivial (`P(0)` holds by computation) or
  vacuous (`∀k < 0, P(k)` in `strong_induction`).
- `0 = 1 → (anything)` — vacuous; the standard "ex falso" flavour.

## Where it misleads
- **hidden non-vacuity**: claiming `∀x (P(x) → Q(x))` is vacuous when `P` *is*
  sometimes satisfied — the claim then has real content that was skipped.
- **the trivial proof used `P` after all**: then it is a genuine
  `direct_proof`, not trivial, and the dependence must be acknowledged.
- **vacuous truth mistaken for evidence**: "every `x` with `P(x)` has `Q(x)`,
  and I proved it, therefore `P` is interesting" — no, it may be that nothing
  has `P`.
- in definitions: a vacuously-satisfied condition may indicate the definition is
  degenerate (e.g. "a relation `R` is transitive on `∅`").

## Common misuse
Presenting a vacuous proof as if the antecedent were realisable; using the
consequent's proof while believing the antecedent was needed; forgetting that
under the empty-domain / free-logic conventions (`objects.md`: domains are
nonempty here) some vacuous readings change.

## Related nodes (non-prerequisite)
- `derives_from`: `implication_as_disjunction` (`←`), `vacuous_quantification`.
- `related`: `explosion_ex_falso` (the vacuous case with `P = ⊥`).
- `contrast`: `direct_proof` (which uses `P`).

## Sources
[velleman_3e] §3.2; [hammack_bop] ch. 4 (vacuous and trivial proof).
