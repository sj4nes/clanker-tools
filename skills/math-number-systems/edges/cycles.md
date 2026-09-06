# Cycles found and how they were resolved — Release 0.1

`build/build-tree.sh` runs `tsort` with the BSD-safe check (stderr, not just
exit status). The final graph is **acyclic**: `validation/tsort-errors.txt` is
empty and every one of the 274 edges is respected by `indexes/tsort-order.txt`.
The graph has a **single root**, `set`, and three assumed `axiom`-typed nodes
(`peano_axioms`, `axiom_of_choice`, `countable_choice`).

No cycle survived into the committed graph. The would-be cycles below were
anticipated during edge authoring and designed out via `conventions.md`.

## 1. induction ⟺ strong induction ⟺ well-ordering

**Would-be cycle:** all three are equivalent over the remaining Peano axioms,
and texts prove them from each other in a ring.

**Resolution:** `induction_principle` (Peano axiom 5) is upstream.
`strong_induction` and `well_ordering_principle` each `derive_from` it
one-directionally. The reverse implications are `equivalent_to` rows in
`edges/relations.tsv`. **Do not add an edge whose target is `induction_principle`.**

## 2. recursion theorem ⟺ arithmetic

**Would-be cycle:** `nat_addition` is *defined by* `recursion_theorem`, and it is
tempting to phrase the recursion theorem using `+`.

**Resolution:** `recursion_theorem` is stated for an **arbitrary** target set
`X`, element `a ∈ X`, and function `g : ℕ × X → X` — needing only
`peano_axioms`, `function`, and `induction_principle`. Every `nat_*` operation
`requires` it; nothing flows back. This is why `recursion_theorem` sits at
position ~21 in the order, before all arithmetic.

## 3. order ⟺ addition

**Would-be cycle:** `a ≤ b` is *defined as* `∃c, a + c = b`.

**Resolution:** `nat_order` `requires` `nat_addition` (and `integer_order`
`requires` `integer_addition`). One-directional. The order-compatibility
*propositions* then use both, downstream.

## 4. ℤ ⊂ ℚ ⊂ ℝ "as subsets"

**Would-be cycle:** each system is habitually written as a subset of the next,
while each is *constructed from* the previous — inviting edges both ways.

**Resolution:** the construction edges run strictly upward
`natural_number → integer → rational_number → real_number`. The inclusions are
installed by the embedding propositions (`nat_embeds_in_integer`,
`integer_embeds_in_rational`, `rational_embeds_in_real`), each of which
`requires` the constructed system and asserts "injective **and** preserves
`+`, `·`, `≤`". No node claims literal `⊆`.

## 5. ℝ by cuts ⟺ ℝ by Cauchy sequences

**Would-be cycle:** two constructions of the same object, each used to motivate
the other.

**Resolution:** `real_number` is the Dedekind construction (canonical — the
`lub_property` proof is one line: the sup is the union of the cuts).
`cauchy_completion` is a separate `construction` node that `requires` only
`cauchy_sequence_rational` and the quotient machinery — **not** `real_number`,
and nothing downstream requires `cauchy_completion`. `dedekind_cauchy_equivalent`
is the `theorem` that bridges them, requiring both.

## 6. the relation must be an equivalence before the quotient exists

**Would-be cycle:** `integer` is `(ℕ×ℕ)/∼_ℤ`, but "∼_ℤ is an equivalence" looks
like a statement *about integers*.

**Resolution:** `integer_relation_equivalence` is phrased about the relation on
**`ℕ × ℕ`** — it `requires` `nat_addition`, `nat_semiring_laws`,
`nat_cancellation`, `cartesian_product`, but **not** `integer`. Then `integer`
`requires` `integer_relation_equivalence`. Identically,
`rational_relation_equivalence` is about the relation on `ℤ × ℤ*` (requiring
`integer_is_integral_domain` and `integer_cancellation`, not `rational_number`),
and `rational_number` requires it.

## 7. completeness ⟺ real number — and why it is not a cycle here

**In `math-real-analysis` this pair is broken by making `lub_axiom` a primitive
axiom.** Here it is broken *the other way*: `real_number` is **constructed**
from cuts (requiring only ℚ and set operations), and `lub_property` is a
**theorem** that `requires` `real_number`. Because the object is built first and
the property proved second, the dependency is one-directional and honest. This
is the whole reason the capsule exists.
