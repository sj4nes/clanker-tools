# disproof_by_counterexample

## Type
definition  (epistemic status: `definition`; `constructive_grade: needs_LEM`
for the "therefore the universal is false" reading; the witness itself is
constructive)

## Statement
To disprove `∀x φ(x)` — i.e. to prove `¬∀x φ(x)` — exhibit a specific `a` with
`¬φ(a)`. By `quantifier_negation` (`∃x ¬φ ⊨ ¬∀x φ`, the intuitionistic
direction), one counterexample refutes the universal claim.

## Symbols
- `φ`: a formula with `x` free (the claimed-universal property).
- `a`: the counterexample — a specific object of the domain with `¬φ(a)`.

## Prerequisites (tsort edges into this node)
`quantifier_negation`, `nd_rules_quantifier`.

## Content
This is `existence_proof` (constructive branch) applied to `∃x ¬φ`, followed by
`not_forall_of_exists_not`. The **`∃x ¬φ → ¬∀x φ`** step is *intuitionistic*
(`cap_not_forall_of_exists_not` in `validation/proof-checks.lean`) — so
producing the counterexample genuinely refutes the universal, constructively.
The `needs_LEM` label attaches only to the *converse* habit ("the universal
failed, so there **must be** a counterexample" — that is `not_forall_iff`, the
classical direction).

## Constructive grade
- exhibiting `a` and proving `¬φ(a)`: **`intuitionistic`**.
- concluding `¬∀x φ` from it: **`intuitionistic`**.
- concluding "a counterexample exists" *from* `¬∀x φ` without one in hand:
  **`needs_LEM`**.

## Lean status
`lean_status: core`. `exists_forall_not_converse` in
`validation/proof-checks.lean` disproves `∃y ∀x, x ≠ y` on `Bool` by `decide`
(a finite counterexample hunt); `free_for_matters` disproves `∃y, y = y + 1`.
The pattern `fun h => absurd (h a) hna` is `not_forall_of_exists_not`.

## Type / well-formedness check
`well_formed`. `a` must be **in the intended domain** (disproving a claim about
*continuous* functions with a discontinuous `a` is not a counterexample —
`a` must satisfy the claim's antecedents). `¬φ(a)` must be *proved*, not merely
plausible. For `∀x (P(x) → Q(x))` the counterexample needs `P(a) ∧ ¬Q(a)`.

## Specialization / boundary cases
- disproving `∀x (P(x) → Q(x))`: find `a` with `P(a)` true and `Q(a)` false.
- disproving an implication `A → B` (no quantifier): show `A` and `¬B` (a single
  "case").
- a **single** counterexample suffices — you need not characterise all failures.
- this is exactly how every `counterexamples_when_dropped` field in this
  capsule's result YAMLs works.

## Where it fails / is misapplied
- **the "counterexample" does not meet the hypotheses**: e.g. "`f(x)=1/x` is a
  counterexample to 'every continuous function on `(0,1)` is bounded'" — correct;
  but "`f(x)=1/x` is a counterexample to 'every continuous function on `[0,1]`
  is bounded'" — wrong, `1/x` is not continuous (not even defined) on `[0,1]`.
- **disproving `∃x φ`**: needs `∀x ¬φ` (a universal proof), *not* a single
  example — a common direction error.
- **one example does not prove a universal** (the dual mistake): `disproof` by
  example is valid; *proof* by example is not.

## Common misuse
Offering a near-counterexample that violates a stated hypothesis; trying to
disprove an existential by exhibiting one non-example; believing an unproven
`¬∀` guarantees a findable witness; conflating with `proof_by_cases`.

## Related nodes (non-prerequisite)
- `derives_from`: `quantifier_negation` (`∃¬ → ¬∀` direction) + `existence_proof`.
- `dual_of`: universal proof.
- `used_by`: every `counterexample`-type node in the capsule stack; the
  hypothesis-dropped-counterexample obligation of the `math-theorem-tree` method.

## Sources
[velleman_3e] §3.3; [hammack_bop] ch. 9; [vandalen_5e] §3.1.
