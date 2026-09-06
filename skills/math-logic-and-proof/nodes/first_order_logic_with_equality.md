# first_order_logic_with_equality

## Type
axiom  (a convention/axiom root; `constructive_grade: intuitionistic`)

## Statement
Equality `=` is a **logical symbol**: it is present in every first-order
language, and in **every** structure it is interpreted as **genuine identity**
on the domain — `𝔄 ⊨ (t₁ = t₂)[s]` iff `s̄(t₁)` and `s̄(t₂)` are the *same*
element of `|𝔄|`. This capsule uses first-order logic **with** equality
throughout.

## Symbols
- `=`: the (binary) equality symbol; never in a `signature`, always available.

## Prerequisites (tsort edges into this node)
none — a **root** (a foundational convention, like the ZF axioms in the set
capsule).

## Content
Consequences bundled here:
- `atomic_formula` includes `t₁ = t₂`;
- `equality_axioms` (reflexivity + the substitution schema) are **logical**
  axioms — valid in every structure by the identity interpretation;
- `equality_congruence`: `=` is a congruence for every function and relation
  symbol;
- the `term_model` quotient (`t ≈ u :⟺ (t = u) ∈ T`) is well-defined **because**
  `=` is forced to be identity.

## Constructive grade
`intuitionistic` — identity is decidable-agnostic here; the equality axioms are
Horn and constructively fine.

## Lean status
`lean_status: core` (as a stance). Lean's `Eq` is definitional identity with
`Eq.refl` and `Eq.subst` (`▸`) — exactly reflexivity + the substitution schema.
`validation/proof-checks.lean` uses `=` and `rfl` freely; the FOL object-level
version is `cited` (Mathlib `FirstOrder.Language` with `= ` primitive).

## Type / well-formedness check
`well_formed`. `=` between **two terms** of the single sort; not in `ℒ`; not
between formulas. "Interpreted as identity" is a **constraint on structures**,
not something proved. Cardinality: adding `=` does not change `|ℒ|`.

## Specialization / boundary cases
- **FOL without equality**: `=` is just another binary relation symbol in `ℒ`,
  with no identity constraint — then structures can have "equal" elements that
  are distinct, and one works up to the `=`-congruence (a quotient). A
  legitimate variant; this capsule does not use it.
- **finite structures**: "there are exactly `n` elements" is expressible only
  with `=` (`∃x₁ … xₙ (⋀ xᵢ ≠ xⱼ ∧ ∀y ⋁ y = xᵢ)`).
- **elimination of `=`** (for equality-free FOL): replace `=` by a fresh
  congruence relation + its axioms — provably equivalent for satisfiability.

## Hypothesis-dropped counterexamples
- **`=` not forced to be identity**: `equality_congruence` fails; the term model
  is not well-defined; "exactly `n` elements" is not expressible.
- **`=` between formulas**: ill-typed.
- **higher-order `=`** (Leibniz equality `∀P (P x ↔ P y)`): second-order — a
  different, categorical-flavoured notion.

## Common misuse
Putting `=` in the signature; using `=` for an intended equivalence relation
(needs a relation symbol + axioms); assuming "FOL" means "FOL without equality"
(conventions differ — this capsule fixes *with* equality); Leibniz equality by
analogy (that is second-order).

## Related nodes (non-prerequisite)
- `entails`: `equality_axioms`, `equality_congruence`.
- `enables`: `term_model` (the quotient), expressing finiteness/cardinalities.
- `required_by`: `atomic_formula`, `structure`.
- `variant`: FOL without equality.

## Sources
[enderton_logic_2e] §2.2 (equality as logical); [chiswell_hodges] ch. 5;
[hodges_shorter] §1.3.
