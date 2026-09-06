# proof_by_contradiction

## Type
definition  (epistemic status: `definition`; `constructive_grade: needs_DNE`)

## Statement
To prove `P`: assume `¬P`, derive a contradiction (`⊥`, or some `Q ∧ ¬Q`),
conclude `P`. Formally the `raa_rule`: a derivation of `⊥` from `Γ ∪ {¬P}`
yields a derivation of `P` from `Γ`.

## Symbols
- `P`: the goal formula.
- `¬P`: the temporary assumption, discharged by `RAA`.
- `⊥`: falsum (`true_false_constants`).

## Prerequisites (tsort edges into this node)
`raa_rule`, `double_negation`.

## Content vs. `¬`-introduction
Two distinct moves share the name "contradiction":
- **`¬I`** — to prove `¬P`, assume `P`, derive `⊥`. **Intuitionistic**, always
  available. This is really `direct_proof` of `P → ⊥`.
- **`RAA` / `proof_by_contradiction` proper** — to prove `P` (a *positive*
  goal), assume `¬P`, derive `⊥`. **Classical** (`needs_DNE`): it is
  interderivable with `¬¬P → P`.

This node is the second. Reaching for it when `¬I` or `direct_proof` would do is
the single most common stylistic error in written proofs.

## Constructive grade
`needs_DNE`. `RAA` and double-negation elimination are interderivable over
intuitionistic natural deduction; adding either to minimal/intuitionistic logic
gives full classical logic. A `proof_by_contradiction` of a `Σ`-type
(existence) claim yields **no witness**.

## Lean status
`lean_status: core`. `dne` in `validation/proof-checks.lean` is
`Classical.byContradiction ∘ …`; the `raa` case of the `soundness` theorem is
where the soundness proof itself goes classical. `#print axioms dne` /
`not_forall_iff` shows `Classical.choice`.

## Type / well-formedness check
`well_formed`. The derived contradiction must be a genuine `⊥` (or `Q ∧ ¬Q` for
some `Q` *actually derived*, not assumed). The assumption discharged must be
exactly `¬P` — discharging `¬P'` proves `P'`.

## Specialization / boundary cases
- `P = ¬R`: "assume `¬¬R`, derive `⊥`" — this collapses to `¬I` on `¬R` and is
  **intuitionistic**; proving a *negative* statement by contradiction is fine.
- `P` decidable: equivalent to a direct/contrapositive proof, no real classical
  content.
- irrationality of `√2`, infinitude of primes (Euclid), uncountability of `ℝ`
  (diagonal) — classic genuine uses, though each also has a direct rephrasing.

## Where it fails / must not be used
- **constructive mathematics / type theory as foundation**: a
  `proof_by_contradiction` of `∃x φ(x)` is rejected — it does not build `x`.
  `existence_proof` (constructive branch) is required.
- **deriving `⊥` from `¬P` alone without using the theory**: if `¬P` is
  self-contradictory then `P` is a theorem of pure logic; if the contradiction
  secretly used an unstated assumption, the proof is incomplete.
- pedagogically: hiding a direct proof inside a contradiction wrapper ("assume
  `¬P` … [never use `¬P`] … derive `⊥`") — the `¬P` is dead weight.

## Common misuse
Using it for `¬P` goals where `¬I` suffices (and stays constructive);
concluding `∃`-statements by contradiction and then speaking of "the" object;
forgetting which assumption produced the contradiction; assuming `¬P` **and**
`¬Q` to prove `P → Q` when contraposition needs only `¬Q`.

## Related nodes (non-prerequisite)
- `equivalent_to`: `proof_by_contrapositive` (classically); `double_negation`
  (as a rule).
- `contains`: `¬I` as its intuitionistic sub-case.
- `used_by`: `well_ordering_principle` proof, `induction_equivalence`
  (strong → well-ordering direction), `cantor`-style diagonal arguments.

## Sources
[velleman_3e] §3.2; [vandalen_5e] §2.3 (the `RAA` vs `¬I` distinction);
[hammack_bop] ch. 6.
