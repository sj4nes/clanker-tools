# proof_by_cases

## Type
definition  (epistemic status: `definition`; `constructive_grade: intuitionistic`
given the disjunction; obtaining the disjunction is often `needs_LEM`)

## Statement
Given a goal `R` and a disjunction `C₁ ∨ C₂ ∨ … ∨ Cₙ` that is **exhaustive**
(known to hold), prove `R` under each `Cᵢ` separately. Conclude `R`. Formally the
`∨E` rule iterated.

## Symbols
- `R`: the goal.
- `C₁, …, Cₙ`: the cases; their disjunction must be a theorem (or hypothesis).

## Prerequisites (tsort edges into this node)
`nd_rules_propositional` (for `∨E`), `de_morgan_prop` (for obtaining an
exhaustive disjunction classically, e.g. `Cᵢ ∨ ¬Cᵢ`).

## Content
Two obligations: (1) **exhaustiveness** — `⊢ C₁ ∨ … ∨ Cₙ`; (2) **each case** —
`Cᵢ ⊢ R` for every `i`. The cases need not be mutually exclusive. The disjunction
is frequently `P ∨ ¬P` (`LEM`), or "`n` even ∨ `n` odd", or a trichotomy
`a < b ∨ a = b ∨ a > b`.

## Constructive grade
The `∨E` step itself is **`intuitionistic`**. The grade of a given
`proof_by_cases` is inherited from **how the disjunction is obtained**: a decided
disjunction (parity, trichotomy of a linear order, a decidable predicate) keeps
the whole proof constructive; splitting on `P ∨ ¬P` for an undecidable `P` makes
it `needs_LEM`.

## Lean status
`lean_status: core`. `rcases h with h | h` / `cases` / `match` are `∨E`. In
`validation/proof-checks.lean`: `not_and_iff` splits on `Classical.em p`
(`needs_LEM` flavour); `xor_nf` etc. split on `cases a <;> cases b` over `Bool`
(decidable, constructive).

## Type / well-formedness check
`well_formed`. The disjunction must be **proved exhaustive** — the classic gap
is a "case analysis" that silently omits a case (e.g. forgetting `a = b` in a
`<` trichotomy, or `n = 0` in an induction-flavoured split). Each sub-proof may
use only its own `Cᵢ`, not the others.

## Specialization / boundary cases
- `n = 1`: trivial (`C₁` is the whole hypothesis).
- `n = 2`, `C₂ = ¬C₁`: the "either it holds or it doesn't" split.
- `wlog`: a `proof_by_cases` where the cases are related by a symmetry, so one
  case's proof is reused (`wlog` node).
- nested cases: a decision tree of `∨E` applications.

## Where it fails
- **non-exhaustive split**: proving `R` for `x > 0` and `x < 0` but not `x = 0`
  — the conclusion `R` is not established. This is the dominant real-world bug.
- **overlapping cases treated as a partition**: harmless for correctness but
  invites double-counting in enumerative arguments.
- **infinitely many cases**: `∨E` is finitary; "prove it for each `n ∈ ℕ`
  separately" is `weak_induction` / `structural_induction`, not
  `proof_by_cases`.

## Common misuse
Omitting a boundary case; using a hypothesis from case `i` inside case `j`;
splitting on `P ∨ ¬P` when `P` is exactly what a constructive argument was
supposed to decide; calling an induction a "case analysis".

## Related nodes (non-prerequisite)
- `derives_from`: `∨E` of `nd_rules_propositional`.
- `specialised_by`: `wlog`.
- `contrasts_with`: `weak_induction` / `structural_induction` (finitely many
  cases vs an inductive schema).

## Sources
[velleman_3e] §3.5; [hammack_bop] ch. 8; [vandalen_5e] §2.3.
