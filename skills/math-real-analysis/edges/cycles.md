# Cycles found and how they were resolved — Release 0.1

`build/build-tree.sh` runs `tsort` with the BSD-safe check (stderr, not just
exit status). The final graph is **acyclic**: `validation/tsort-errors.txt` is
empty and every one of the 247 edges is respected by `indexes/tsort-order.txt`.

No cycle survived into the committed graph. The cycles below were anticipated
during edge authoring (SKILL.md step 6 / `references/relations.md`) and
**designed out** before the first `tsort` run, by the decisions recorded in
`conventions.md`. They are listed here so a future editor does not reintroduce
them.

## 1. The completeness pentagon

**Would-be cycle:** `lub_axiom → monotone_convergence_theorem → nested_interval_theorem
→ cauchy_convergence_criterion → bolzano_weierstrass → lub_axiom`, because each
of the five is provably equivalent to the others (over an Archimedean ordered
field) and different textbooks derive them in different directions.

**Classification of each would-be reverse edge:** equivalence, not prerequisite.

**Resolution:** `lub_axiom` is *the* completeness axiom for Release 0.1 and is
upstream of all four theorems. The four theorems `derive_from` it
one-directionally. The reverse implications are `equivalent_to` rows in
`edges/relations.tsv`, each naming an equivalence-lemma note (`eqv_lub_mct`,
`eqv_lub_nip`, `eqv_lub_cauchy`, `eqv_lub_bw`) that a later release could
formalize. **Do not add any edge whose target is `lub_axiom`.**

## 2. limit ⟺ continuity

**Would-be cycle:** `function_limit → continuity_at_point` (continuity defined as
"the limit equals the value") together with the pedagogical instinct to put
continuity first.

**Resolution:** `continuity_at_point` has its **own** ε–δ definition and does
**not** require `function_limit`. The bridging fact "for `c` a limit point of
the domain, `f` is continuous at `c` iff `lim_{x→c} f = f(c)`" is deliberately
*not a node* in 0.1 (it would be a `proposition` requiring both); the two ε–δ
statements stand independently. `function_limit` requires `limit_point`;
`continuity_at_point` does not.

## 3. derivative ⟺ continuity

**Would-be cycle:** define `f'(c)` only for `f` continuous at `c`, while
`differentiable_implies_continuous` needs the derivative.

**Resolution:** `derivative` requires `function_limit` (of the difference
quotient), **not** `continuity_at_point`. `differentiable_implies_continuous`
is a separate `proposition` downstream of both.

## 4. compactness ⟺ sequential compactness ⟺ closed-and-bounded

**Would-be cycle:** three equivalent properties, each used to prove the others.

**Resolution:** `compact_set` is defined by the **open-cover / finite-subcover**
property alone (requires `open_cover`). `heine_borel` ("compact ⟺ closed and
bounded", subsets of ℝ) and `sequential_compactness` ("compact ⟺ every sequence
has a subsequence converging in the set") are **theorems** downstream of the
open-cover definition plus `nested_interval_theorem` / `bolzano_weierstrass`.
Downstream users (EVT, Heine–Cantor, `continuous_implies_integrable`) edge
whichever characterization their proof sketch actually invokes — recorded in
each node's detail page.

## 5. `intermediate_value_theorem` proof route

**Would-be cycle:** proving the IVT from `continuous_image_of_connected` and
also motivating connectedness by the IVT.

**Resolution:** the canonical 0.1 proof of the IVT is the direct
`lub_axiom` argument on `{x ∈ [a,b] : f(x) < y}`; the edge is
`lub_axiom intermediate_value_theorem`. The topological route
(`continuous_image_of_connected` → interval → IVT) is a `proved_using` row in
`edges/relations.tsv`, not a graph edge. `continuous_image_of_connected` and
`connected_iff_interval` remain in the graph for their own sake.
