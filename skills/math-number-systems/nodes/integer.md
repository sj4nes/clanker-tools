# integer

## Type
construction  (epistemic status: `constructive_result`)

## Statement
`ℤ = (ℕ × ℕ) / ∼_ℤ`, where `(a,b) ∼_ℤ (c,d)  :⟺  a + d = b + c`. The class
`[(a,b)]` represents the integer "`a − b`".

## Symbols
- `(a,b)`: an ordered pair of naturals
- `[(a,b)]`: its `∼_ℤ`-class, an element of `ℤ`

## Prerequisites (tsort edges into this node)
`natural_number`, `cartesian_product`, `quotient_set`,
`integer_relation_equivalence`.

## The relation must be an equivalence *first*
`integer_relation_equivalence` is a **separate upstream node**, stated about the
relation on `ℕ × ℕ` (not about integers — see `edges/cycles.md` #6):
- *reflexive*: `a + b = b + a` (`nat_semiring_laws`).
- *symmetric*: immediate.
- *transitive*: from `a + d = b + c` and `c + f = d + e`, add to get
  `a + d + c + f = b + c + d + e`, then cancel `c + d` (`nat_cancellation`) for
  `a + f = b + e`.

**Checked with Lean:** `proof-checks.lean` §1 — `z_rel_trans` proves transitivity
**universally over ℤ** with `omega`.

## Construction
Form `ℕ × ℕ`; `ℤ := (ℕ × ℕ)/∼_ℤ`. Addition `[(a,b)] + [(c,d)] := [(a+c, b+d)]`,
multiplication `[(a,b)]·[(c,d)] := [(ac+bd, ad+bc)]`, negation
`−[(a,b)] := [(b,a)]`, order `[(a,b)] ≤ [(c,d)] :⟺ a + d ≤ b + c` — each on
representatives, each then shown to **respect `∼_ℤ`**
(`integer_operations_well_defined`; Lean §2 does the addition case universally,
§7 the multiplication case as an instance).

## Epistemic status
`constructive_result` — `ℤ` is a specific set (of classes of pairs), and every
operation is exhibited. No choice.

## Type / well-formedness check
`well_formed` (`validation/type-checks.md#integer`). The relation uses `+`
only — subtraction does not exist until it is defined *on* `ℤ`.

## Specialization / boundary cases
- `[(n,0)]` is the image of `n ∈ ℕ` (`nat_embeds_in_integer`); `[(0,n)] = −[(n,0)]`.
- `[(a,b)] = [(a+k, b+k)]` for all `k` — a class is a whole diagonal line.
- `[(5,2)] = [(8,5)]` since `5 + 5 = 2 + 8` (`instance-checks.bc`).

## Hypothesis-dropped counterexamples
- **`∼_ℤ` not transitive:** it would not partition `ℕ × ℕ`, and "the set of
  classes" is ill-defined.
- **no additive cancellation in the base:** transitivity fails — `ℕ` must be a
  cancellative monoid. (This is why the construction generalises exactly to the
  *Grothendieck group* of a commutative cancellative monoid.)

## Common misuse
Treating `[(a,b)]` as the pair rather than its class; writing `a − b` before
subtraction is defined on `ℤ`.

## Related nodes (non-prerequisite)
- `generalizes`: the Grothendieck group construction
- feeds: `rational_number`, `integer_is_ordered_integral_domain`,
  `nat_embeds_in_integer`

## Sources
[landau] §§4–11; [enderton] ch. 4; [tao_analysis_I] §4.1.
