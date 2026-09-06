# direct_proof

## Type
definition  (epistemic status: `definition`; `constructive_grade: intuitionistic`)

## Statement
To prove `P → Q`: assume `P` as a temporary hypothesis, derive `Q` using it and
the ambient theory, then **discharge** the assumption. The result is a proof of
`P → Q` with no undischarged occurrence of `P`.

For a universally quantified goal `∀x (P(x) → Q(x))`: fix an arbitrary `x`
(eigenvariable, no special properties), then run the direct proof of
`P(x) → Q(x)`.

## Symbols
- `P`, `Q`: formulas (`Wff` / `first_order_wff`).
- the discharged hypothesis: an assumption node in the `nd_derivation` tree,
  closed by the `→I` step.

## Prerequisites (tsort edges into this node)
`nd_rules_propositional`, `assumption_discharge`.

## Content
`direct_proof` is the **`→I` rule of natural deduction** as a named strategy: a
derivation of `Q` from `Γ ∪ {P}` becomes a derivation of `P → Q` from `Γ`. It is
the default; `proof_by_contrapositive` and `proof_by_contradiction` are the
fallbacks when the direct route is unavailable or awkward.

## Constructive grade
`intuitionistic` — `→I` is a rule of minimal logic; no `RAA`, no `LEM`. A direct
proof is the constructively strongest kind: it exhibits a function taking
evidence for `P` to evidence for `Q`.

## Lean status
`lean_status: core` (it is the language). Every `fun h : P => …` /
`intro h` in `validation/proof-checks.lean` is a direct proof; e.g. `dni`
(`p → ¬¬p`), `exportation`, `contrapose_weak`, `forall_exists_of_exists_forall`.

## Type / well-formedness check
`well_formed`. The discharged `P` must be **exactly** the antecedent; a proof
that quietly uses a strengthened `P'` proves `P' → Q`, not `P → Q`. For the
quantified form the fixed `x` must be genuinely arbitrary — it may not already
appear in `Γ` with constraints (this is the `eigenvariable_condition` for `∀I`).

## Specialization / boundary cases
- `P = ⊤`: a direct proof of `⊤ → Q` is just a proof of `Q`.
- goal `¬Q` = `Q → ⊥`: assume `Q`, derive `⊥` — this is `proof_by_contradiction`
  restricted to negative goals, and it *is* intuitionistically fine (`¬I`).
- chained: `P → Q → R` — assume `P`, assume `Q`, derive `R` (`exportation`).

## Where it does not apply / fails
- **goal not an implication or negation and no constructive route**: e.g.
  `∀n, P(n) ∨ ¬P(n)` for undecidable `P` — there is no direct proof; you need
  `LEM`. Direct proof cannot manufacture a disjunction you cannot decide.
- **using the conclusion to justify an assumption step** (circularity) — not a
  failure of the method but the commonest way to misapply it.

## Common misuse
Assuming more than `P` (a stronger or differently-quantified hypothesis);
forgetting to discharge, leaving a proof of `Q` from `P` mislabeled as a proof
of `P → Q`; in the `∀` case, choosing an `x` that is not arbitrary.

## Related nodes (non-prerequisite)
- `equivalent_to`: the `→I` rule of `nd_derivation`.
- `contrasts_with`: `proof_by_contrapositive`, `proof_by_contradiction`
  (the classical fallbacks).
- `used_by`: `biconditional_proof`, and essentially every theorem in the stack.

## Sources
[velleman_3e] ch. 3; [hammack_bop] ch. 4; [vandalen_5e] ch. 2.
