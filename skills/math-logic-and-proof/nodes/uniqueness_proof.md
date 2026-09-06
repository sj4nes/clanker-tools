# uniqueness_proof

## Type
definition  (epistemic status: `definition`; `constructive_grade: intuitionistic`)

## Statement
To prove uniqueness (the `∀y (φ(y) → y = a)` part of `∃!x φ(x)`): assume two
objects `y₁`, `y₂` both satisfy `φ`, and derive `y₁ = y₂`. Combined with an
`existence_proof` this establishes `∃!x φ(x)`, which unfolds as
`∃x (φ(x) ∧ ∀y (φ(y) → y = x))`.

## Symbols
- `φ`: a formula with one free variable.
- `y₁`, `y₂`: two arbitrary objects assumed to satisfy `φ`; goal `y₁ = y₂`.
- `=`: logical equality (`first_order_logic_with_equality`).

## Prerequisites (tsort edges into this node)
`existence_proof`, `first_order_logic_with_equality`.

## Content
Uniqueness is a `direct_proof` of `φ(y₁) ∧ φ(y₂) → y₁ = y₂` with `y₁`, `y₂`
arbitrary. It uses `equality_congruence` / `equality_axioms` to substitute one
for the other. Note uniqueness **alone** does not assert anything exists:
`∀y₁ y₂ (φ(y₁) ∧ φ(y₂) → y₁ = y₂)` is vacuously true if nothing satisfies `φ`
("at most one").

## Constructive grade
`intuitionistic` — a `direct_proof` ending in an equality, using only the
equality rules. `∃!` is constructive iff its existence half is.

## Lean status
`lean_status: core`. `⟨a, ha, fun y hy => …⟩` for an `∃!` goal, or the
`ExistsUnique` unfolding; the uniqueness obligation is `fun y hy => (eq proof)`.
Not separately exercised in `validation/proof-checks.lean` (no `∃!` headline
node) but it is `direct_proof` + `equality`, both covered.

## Type / well-formedness check
`well_formed`. `y₁`, `y₂` must be **genuinely arbitrary** (eigenvariable
condition) — not the witness from the existence half, and not constrained by
`Γ`. The conclusion must be `y₁ = y₂` (identity), not merely "`y₁` and `y₂` have
the same properties" unless that has been shown to entail equality in the
structure.

## Specialization / boundary cases
- "**at most one**" = uniqueness without existence — a standalone, vacuously-true
  when `φ` is unsatisfiable.
- uniqueness up to isomorphism / up to a congruence: replace `=` by the relevant
  equivalence, and note it is *not* logical equality (e.g. "the" completion,
  "the" algebraic closure).
- functional dependence: "`for each x there is exactly one y with ψ(x,y)`"
  licenses defining a function `f(x) = y` — the standard use.

## Where it fails / traps
- **proving existence twice instead of uniqueness**: exhibiting one witness does
  not show there is no other.
- **assuming the two objects are equal to prove they are equal** (circularity),
  often disguised as "both equal `a`, so equal" when `a` was defined *as* the
  witness.
- **uniqueness up to iso mistaken for literal uniqueness**: there are many
  distinct-but-isomorphic complete ordered fields *as sets*; the capsule stack's
  `uniqueness_of_R` is up to unique isomorphism.

## Common misuse
Writing `∃!` proofs that establish only `∃`; using the existence witness as one
of the two "arbitrary" objects; conflating `=` with an equivalence relation;
forgetting the domain/nonemptiness conditions inherited from `existence_proof`.

## Related nodes (non-prerequisite)
- `pairs_with`: `existence_proof` (→ `∃!x φ`).
- `uses`: `direct_proof`, `equality_congruence`.
- `related`: `biconditional_proof` (both are "two obligations" schemes).

## Sources
[velleman_3e] §3.6; [enderton_logic_2e] §2.1 (`∃!` as an abbreviation);
[hammack_bop] ch. 7.
