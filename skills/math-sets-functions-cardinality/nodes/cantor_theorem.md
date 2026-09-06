# cantor_theorem

## Type
theorem  (epistemic status: `proved_theorem`, `choice_free`, `constructive`)

## Statement
For every set `X`, `|X| < |𝒫(X)|`: there is no surjection `X → 𝒫(X)`.

## Prerequisites (tsort edges into this node)
`surjection`, `power_set`, `cardinal_lt`, `quantifier_negation`.

## Proof
Given any `f : X → 𝒫(X)`, form the **diagonal set**

    D = { x ∈ X : x ∉ f(x) }        (a subset of X, by Separation)

If `f(a) = D` for some `a ∈ X`, then

    a ∈ D  ⟺  a ∉ f(a)  =  a ∉ D

— a contradiction. So `D ∉ ran(f)`, i.e. `f` is not surjective. The map
`x ↦ {x}` is an injection `X → 𝒫(X)`, so `|X| ≤ |𝒫(X)|`; with no bijection,
`|X| < |𝒫(X)|`.

**Checked with Lean:** `validation/proof-checks.lean` §4 — `cantor`, a 2-line
plain-Lean proof (`iff_not_self (iff_of_eq (congrFun h a))`), **no Mathlib**.
`validation/instance-checks.bc` works `X = {0,1,2,3}` and exhibits `D = {2,3}`.

## No choice, and no hypotheses to drop
The theorem is **unconditional** — there is no finite, small, or special `X`
that escapes it, and the proof uses no form of choice. This is worth stating
because Cantor's theorem is the engine behind:

- `cantor_diagonal` (`X = ω`: `2^ω` uncountable) and hence
  `math-number-systems` `real_uncountable`;
- the unbounded cardinal chain `|X| < |𝒫(X)| < |𝒫(𝒫(X))| < ⋯`;
- the non-existence of a "universal set" (a set of all sets would surject onto
  its own power set via the identity).

## Type / well-formedness check
`well_formed` (`validation/type-checks.md#cantor_theorem`). The proof must
**exhibit** `D` — a Separation instance bounded by `X` (`objects.md` rule 8),
not a bare `{x : φ}`.

## Specialization / boundary cases
- `X = ∅`: `0 < 1` (`|∅| = 0`, `|{∅}| = 1`).
- `X = ω`: `|ω| < |𝒫(ω)|` — the uncountability of the continuum.
- the same diagonal move on `X → {0,1}` (via `powerset_iso_two_power`) is
  `cantor_diagonal`.

## Common misuse
Thinking it needs choice; concluding a *specific* set is "too big to enumerate"
rather than "no enumeration exists"; assuming `|𝒫(X)|` is the *successor*
cardinal of `|X|` (that is GCH — independent of ZFC).

## Related nodes (non-prerequisite)
- generalises to `cantor_diagonal`, `real_uncountable`
- `historically_precedes` `zf` (Cantor 1891 predates the axiomatization)

## Sources
[cantor_1891]; [enderton] ch. 6; [halmos] §25.
