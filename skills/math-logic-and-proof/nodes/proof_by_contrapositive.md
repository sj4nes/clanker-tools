# proof_by_contrapositive

## Type
definition  (epistemic status: `definition`; `constructive_grade: needs_DNE`)

## Statement
To prove `P → Q`, instead give a direct proof of `¬Q → ¬P`. Since
`(P → Q) ⊨⊨ (¬Q → ¬P)` (`contraposition`), the two goals are equivalent, so a
proof of the second is a proof of the first.

## Symbols
- `P`, `Q`: formulas.
- the transformed goal: `¬Q → ¬P`, proved by `direct_proof`.

## Prerequisites (tsort edges into this node)
`contraposition`, `nd_rules_propositional`.

## Content
A packaging of `contraposition` + `direct_proof`: replace the goal by its
contrapositive, then assume `¬Q` and derive `¬P`. Useful when `¬Q` is a
concrete, usable hypothesis and `P` is hard to assume directly (e.g. "if `n²` is
even then `n` is even" — assume `n` is odd, i.e. `n = 2k+1`, compute
`n² = 2(2k²+2k)+1` odd).

## Constructive grade
`needs_DNE`. The step from a proof of `¬Q → ¬P` back to `P → Q` requires
`¬¬P → P` (double-negation elimination): a direct proof gives `P → ¬¬Q`, and
without `DNE` you cannot strip the double negation. The **forward** half
`(P → Q) → (¬Q → ¬P)` is intuitionistic (`contrapose_weak` in
`validation/proof-checks.lean`); it is the *use as a proof strategy for `P → Q`*
that is classical.

## Lean status
`lean_status: core`. `contrapose_iff` in `validation/proof-checks.lean` proves
`(p → q) ↔ (¬q → ¬p)` with the `←` direction going through `dne`; `#print
axioms` shows the classical dependency.

## Type / well-formedness check
`well_formed`. Both `Q` and `P` must be negatable as stated; for a quantified
goal `∀x (P(x) → Q(x))` the contrapositive is `∀x (¬Q(x) → ¬P(x))` — the
quantifier stays out front and is **not** touched (a common slip is to also
negate/swap the quantifier, conflating this with `disproof_by_counterexample`).

## Specialization / boundary cases
- `Q = ⊥`: contrapositive of `P → ⊥` is `⊤ → ¬P` = `¬P` — collapses to a direct
  proof of `¬P`.
- `P`, `Q` decidable: intuitionistically equivalent to the direct proof (no
  `DNE` needed), so the classical caveat is vacuous for e.g. statements about
  natural numbers with decidable predicates.
- number theory: "`ab` odd ⟹ `a` odd and `b` odd" is cleanest by
  contrapositive.

## Where it fails / is not equivalent
- **intuitionistic / constructive setting**: `¬Q → ¬P` is strictly weaker than
  `P → Q`. Example: `¬¬(P ∨ ¬P) → ¬¬⊤` is trivially provable, but it does not
  give `⊤ → (P ∨ ¬P)`. Proving the contrapositive of a constructive claim does
  not discharge it.
- when `¬Q` is not meaningfully stronger/more usable than `P` the transformation
  buys nothing.

## Common misuse
Confusing it with the **converse** (`Q → P`) or the **inverse** (`¬P → ¬Q`) —
only the contrapositive is equivalent. Negating the quantifier along with the
matrix. Believing a contrapositive proof is constructive.

## Related nodes (non-prerequisite)
- `equivalent_to`: `proof_by_contradiction` (both classical; contrapositive is
  the more disciplined form — it never introduces `⊥` from thin air).
- `derives_from`: `contraposition` + `direct_proof`.
- `commonly_confused_with`: converse, inverse.

## Sources
[velleman_3e] §3.2; [hammack_bop] ch. 5; [vandalen_5e] §2.3.
