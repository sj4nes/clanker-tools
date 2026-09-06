# Conventions and foundational choices — Release 0.1

## Notation conventions (each is a `notation_convention` node where it affects a statement)

| Convention | Choice for this release | Node |
|---|---|---|
| ℕ contains 0 | **Yes.** `peano_axioms` is stated with `0` and successor `S`. `ℕ⁺ = ℕ ∖ {0}`. | `peano_axioms` |
| ℕ vs `math-real-analysis` | That capsule uses `ℕ = {1,2,…}`. The order-isomorphism `n ↦ n+1` translates; downstream statements shift indices. | `nat_embeds_in_integer` |
| Equivalence class | `[x]` or `[x]_∼`; the quotient set is `X/∼`. A construction names its relation explicitly (`∼_ℤ`, `∼_ℚ`). | `quotient_set` |
| ℤ as pairs | `[(a,b)]_ℤ` represents "a − b". `(a,b) ∼_ℤ (c,d)` iff `a + d = b + c` (stated with `+` only — subtraction does not exist yet). | `integer` |
| ℚ as pairs | `[(a,b)]_ℚ` represents "a / b", `b ≠ 0`. `(a,b) ∼_ℚ (c,d)` iff `a·d = b·c`. | `rational_number` |
| Dedekind cut | A cut is the **lower** set: `A ⊂ ℚ`, `A ≠ ∅`, `A ≠ ℚ`, downward closed, no greatest element. `q* = {p ∈ ℚ : p < q}` is the rational cut. Order is `A ≤ B ⟺ A ⊆ B`. | `dedekind_cut` |
| Cut for a real | `x` *is* its cut; "`q ∈ x`" means the rational `q` is below the real `x`. | `real_number` |
| `<` vs `≤` | `≤` is the primary order (reflexive); `<` is `≤ ∧ ≠`. Trichotomy is proved, not assumed. | `nat_order` |
| Numerals | `2 := S(S 0)`, `3 := S 2`, … in ℕ; the same symbols name their images under each embedding. | `nat_embeds_in_integer` |
| `ℤ*`, `ℚ*` | the nonzero elements (used as the second coordinate in the ℚ construction and as the multiplicative group). | `rational_number` |
| "countable" | injection into ℕ (so **finite sets are countable**); "countably infinite" = bijection with ℕ. | `countable_set` |
| Decimal expansions | used only in `cantor_diagonal_argument`, with the `0.999… = 1.000…` ambiguity handled by forbidding the digits `0` and `9` in the constructed diagonal. | `cantor_diagonal_argument` |

## Foundational primitives (documented per the method, step 3)

- **`set`, `function`, `relation`** — primitive at the working level; ZFC used
  informally, never unfolded. `cartesian_product`, `equivalence_relation`, and
  the formation of a **quotient set** `X/∼` are taken as available set-forming
  operations. Alternative foundations (type theory, ETCS, NF) are out of scope.
- **`peano_axioms`** — the five Peano axioms are the **floor** of this capsule:
  `0 ∈ ℕ`; `S : ℕ → ℕ`; `S` is injective; `0` is not a successor; and induction
  (any `X ⊆ ℕ` with `0 ∈ X` and `S`-closed is all of ℕ). Chosen as the floor
  because the capsule's subject is the *constructions above* ℕ; building ℕ
  itself from `∅` and Infinity is set theory, cited to [enderton] ch. 4. `ℕ` is
  determined up to unique isomorphism by these axioms (a corollary of
  `recursion_theorem`), so "the natural numbers" is well-posed.
- **`axiom_of_choice`** — an independent axiom, kept first-class. Its weak form
  `countable_choice` is the only choice used essentially in 0.1
  (`countable_union_countable`); everything in the ℤ/ℚ/ℝ constructions and the
  least-upper-bound property is choice-free. A term is not primitive because it
  is hard to prove — AC is primitive here because it is genuinely independent of
  ZF.

## Cycle resolutions (full record; see `edges/cycles.md`)

1. **induction ⟺ strong induction ⟺ well-ordering.** All three are equivalent
   over the other Peano axioms and each is routinely used to prove the others.
   **Resolution:** `induction_principle` (Peano axiom 5) is upstream;
   `strong_induction` and `well_ordering_principle` `derive_from` it
   one-directionally, with the reverse implications as `equivalent_to` rows in
   `edges/relations.tsv`.

2. **recursion theorem ⟺ addition.** Addition is *defined by* recursion, and one
   is tempted to use addition when stating recursion. **Resolution:**
   `recursion_theorem` is stated abstractly — for any set `X`, any `a ∈ X`, any
   `g : ℕ × X → X` there is a unique `f : ℕ → X` with `f(0) = a`,
   `f(S n) = g(n, f n)` — needing only `peano_axioms` and `function`. Every ℕ
   operation then `derives_from` it. No edge from any `nat_*` operation back
   into `recursion_theorem`.

3. **order ⟺ addition** (in each of ℕ, ℤ). `a ≤ b` is *defined as* `∃c, a + c =
   b` (ℕ) / via the positive cone (ℤ). **Resolution:** `nat_order` `requires`
   `nat_addition`; `integer_order` `requires` `integer_addition`. One-directional.

4. **ℤ ⟺ ℚ ⟺ ℝ via "is a subset of".** ℤ ⊂ ℚ ⊂ ℝ *as commonly written*, but each
   is really a distinct set with an **embedding**. **Resolution:** the edges run
   `natural_number → integer → rational_number → real_number` (each construction
   consumes the previous), and `nat_embeds_in_integer`,
   `integer_embeds_in_rational`, `rational_embeds_in_real` are the
   `proposition` nodes that install the inclusions. No node claims literal
   subset-hood.

5. **ℝ by cuts ⟺ ℝ by Cauchy sequences.** Two constructions of the same object.
   **Resolution:** `real_number` = the Dedekind construction (canonical).
   `cauchy_completion` is a separate `construction` node; `dedekind_cauchy_equivalent`
   is the `theorem` bridging them. `cauchy_completion` is **not** a prerequisite
   of anything downstream — cuts carry the release.

6. **lub_property depends on real_number — and that is not a cycle.** The
   least-upper-bound property is a *theorem about the constructed ℝ*; it `requires` `real_number`
   and `dedekind_cut`. Because ℝ is **built first and the property proved
   second**, there is no circularity — this is the entire methodological point
   of the capsule, and the contrast with `math-real-analysis`, where the same
   statement is an axiom (`lub_axiom`).

## Distinguishing three orderings

`indexes/tsort-order.txt` is a **prerequisite** order. It is not the historical
order (Dedekind and Cantor's constructions, 1872, postdate two centuries of
calculus), nor a pedagogical order, nor the logical order within a single proof.
Independent nodes (e.g. `sqrt2_irrational` and `cantor_theorem`) may linearize
in either order; tie-order is not necessity.

## The bridge to `math-real-analysis`

`math-real-analysis` Release 0.1 has five primitive roots: `set`,
`natural_number`, `rational_field`, `real_number`, `axiom_of_choice`. This
capsule's outputs discharge them:

| analysis root | discharged by | how |
|---|---|---|
| `rational_field` | `rational_is_ordered_field` | ℚ constructed and proved to be an ordered field |
| `real_number` | `real_number` (this capsule) + `real_is_ordered_field` | ℝ constructed from cuts |
| `lub_axiom` (its axiom) | `lub_property` (this capsule's **theorem**) | proved: sup = union of cuts |
| `natural_number` | `peano_axioms` + `recursion_theorem` + the ℕ-arithmetic props | refined from "bare Peano" to a fully developed semiring; the set model is still cited |
| `axiom_of_choice` | — | stays an axiom; correctly independent |

A future `math-real-analysis` Release 0.2 would replace those roots with
`requires` edges into this capsule.
