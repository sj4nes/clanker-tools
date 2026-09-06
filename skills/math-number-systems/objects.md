# Type vocabulary and well-formedness rules — Release 0.1

The analog of a dimensional basis. Every result's `type_check_status` is decided
against these. In a *construction* capsule the dominant well-formedness question
is: **does this operation respect the quotient it is defined on?**

## Object kinds

| Kind | What it is | Formed from | Typical predicates |
|---|---|---|---|
| `set` | a set (ZFC, informal) | primitive | `nonempty, finite, countable` |
| `relation` | `R ⊆ X × X` | `cartesian_product` | `reflexive, symmetric, transitive, total, well-founded` |
| `equiv` | an equivalence relation | `relation` | — |
| `class` | an equivalence class `[x]_∼` | `equiv` + a representative | — |
| `quotient` | `X/∼`, the set of classes | `equiv` | — |
| `function` | `f : X → Y` | `set × set` | `injective, surjective, bijective, order-preserving, a homomorphism` |
| `nat` | an element of ℕ | `peano_axioms` | `zero, successor, even/odd, prime` |
| `int` | an element of ℤ = class of a ℕ-pair | `quotient` of `ℕ × ℕ` | `positive, negative, unit, divides` |
| `rat` | an element of ℚ = class of a ℤ×ℤ\* pair | `quotient` of `ℤ × ℤ*` | `positive, integral, in lowest terms` |
| `cut` | a Dedekind cut: a lower subset of ℚ | `subset` of ℚ | `rational (= some q*), positive` |
| `real` | an element of ℝ = a `cut` | the set of cuts | all `cut` predicates + `algebraic, upper bound of S` |
| `sequence` | `x : ℕ → ℚ` or `ℕ → ℝ` | `nat → rat/real` | `Cauchy, null, bounded` |
| `structure` | a signature + axioms (monoid, ring, field, …) | — | `a model of it`, `a sub-structure`, `ordered` |

## Well-formedness rules (checked in `validation/type-checks.md`)

1. **Definition on a quotient.** An operation `X/∼ → X/∼` given by
   `[x] ↦ [h(x)]` is well-formed **only if** `x ∼ x' ⟹ h(x) ∼ h(x')`. Every
   node that defines a `+`, `·`, `−`, `⁻¹`, `≤`, or an embedding on ℤ, ℚ, or ℝ
   carries this obligation explicitly; `well_defined_on_quotient` is the shared
   lemma node. A statement that names such an operation without the check having
   been discharged is **not** well-formed.
2. **The relation is genuinely an equivalence.** Before `X/∼` is formed, `∼`
   must be shown reflexive, symmetric, **and transitive**. For `∼_ℤ`
   (`a+d = b+c`) and `∼_ℚ` (`ad = bc`) transitivity is the non-trivial clause
   (and for `∼_ℚ` it needs a cancellation from `ℤ` being a domain — recorded).
3. **A Dedekind cut is a set, and the cut axioms are the type.** Writing "the
   cut `A`" asserts: `A ⊆ ℚ`, `A ≠ ∅`, `A ≠ ℚ`, `p ∈ A ∧ q < p ⟹ q ∈ A`, and
   `A` has no greatest element. `real_addition`, `real_multiplication`,
   `lub_property` each must show their output set is again a cut (rule 1's
   analog at the ℝ level).
4. **`sup S` as a real.** `sup S` names a `real` only after asserting `S ⊆ ℝ`
   nonempty and bounded above; `lub_property` is what discharges it, and (unlike
   `math-real-analysis`, where this is an axiom citation) here the discharge is
   a **construction**: `sup S = ⋃ S`, shown to be a cut.
5. **Embeddings preserve structure.** `nat_embeds_in_integer` etc. are not just
   injections — each statement includes "and preserves `+`, `·`, `≤`". A use of
   "regard `n ∈ ℕ` as an element of ℚ" carries the implicit claim that the
   relevant identity holds under the embedding.
6. **Numerals are typed.** `2` is `S(S 0) : nat` unless an embedding is in
   scope; `2 ∈ ℝ` means `((S(S 0))_ℤ)_ℚ)*`. Statements mixing levels (`n < x`
   for `n : nat`, `x : real`) carry the coercion.
7. **Cardinality predicates need a witness.** "`X` is countable" is
   `∃ injection X → ℕ`; "`X` is countably infinite" additionally needs `X`
   infinite. "`ℝ` is uncountable" is `¬∃ surjection ℕ → ℝ` and its proof
   (`cantor_diagonal_argument`) must produce, from any candidate list, an
   explicit missing real.
8. **`0 ∈ ℤ*` is a type error.** The second coordinate of a ℚ-pair, and the
   argument of `⁻¹`, range over the **nonzero** elements; every ℚ statement
   involving a denominator or an inverse carries `≠ 0`.

## The "which system does this live in" signature check

For a quick pass, tag every symbol with one of `nat / int / rat / cut / real /
set / function / structure` and verify: every operation's operands share a
system (or a coercion is named); every `[·]` has a representative of the right
pair-type and a discharged well-definedness; every `q*` has `q : rat`; every
`sup` has produced a `real` under rule 4; every "homomorphism / embedding"
claim names the operations it preserves. This is the row-by-row analog of
summing dimension exponents.
