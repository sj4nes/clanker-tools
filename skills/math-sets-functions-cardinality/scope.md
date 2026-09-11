# Scope — Release 0.1

**Sets, functions, orders, and cardinality — the layer below the number
systems.**

The capsule that discharges what
[`math-number-systems`](../math-number-systems/SKILL.md) takes as primitive:
`set`, `function`, `relation`, `equivalence_relation`, `quotient_set`,
`cartesian_product`, `axiom_of_choice`, `countable_choice`, and — via the Axiom
of Infinity — `peano_axioms` itself. It develops the ZF(C) axioms, the algebra
of sets and functions (including the **preimage algebra** that continuity and
compactness proofs run on), equivalence relations and quotients, order theory
with Zorn's lemma, a minimal ordinal spine, and the theory of cardinality
through Cantor's theorem, Cantor–Schröder–Bernstein, and the arithmetic of
`ℵ₀` and `2^ℵ₀`.

## Included

- **Logic floor** (discharged by [`math-logic-and-proof`](../math-logic-and-proof/SKILL.md) — see `edges/cross-capsule.md`): propositional and
  predicate logic; **quantifier negation** (`¬∀ ↔ ∃¬`, `¬∃ ↔ ∀¬`) — the engine
  of every counterexample; quantifier order (`∀∃` vs `∃∀`); proof by
  contradiction, contrapositive, and cases.
- **ZF(C) axioms** as first-class `axiom` nodes: extensionality, empty set,
  pairing, union, power set, separation (schema), replacement (schema),
  infinity, foundation; and **choice**, with its weak forms `countable_choice`
  and `dependent_choice`.
- **Set algebra**: subset, power set, binary and **arbitrary / indexed** union
  and intersection, difference and relative complement, De Morgan and
  distributive laws, ordered pairs (Kuratowski), Cartesian products, disjoint
  unions, function spaces `Y^X`.
- **Relations**: domain/range, composition, inverse, the property vocabulary
  (reflexive, symmetric, antisymmetric, transitive, connex), restriction.
- **Equivalence relations and quotients**: classes, partitions, the
  equivalence–partition correspondence, the quotient set `X/∼`, the canonical
  projection, **well-definedness on a quotient**, and the universal property.
- **Functions**: injection / surjection / bijection; image and preimage; the
  **preimage algebra** (`f⁻¹` commutes with `⋃`, `⋂`, complement) and the
  weaker image laws (`f[⋃]=⋃f[·]`, `f[⋂]⊆⋂f[·]`); composition; identity and
  two-sided inverse (`inverse ⟺ bijective`); one-sided inverses (left inverse
  ⟺ injective; **right inverse ⟺ surjective, using choice**); the pigeonhole
  principle; the bijection `𝒫(X) ≅ 2^X` via characteristic functions.
- **Order theory**: partial, total, and strict orders; bounds, suprema/infima,
  maxima/minima; chains and antichains; well-orders; **Zorn's lemma**, the
  **well-ordering theorem**, and the equivalence AC ⟺ Zorn ⟺ well-ordering
  ⟺ cardinal comparability.
- **Ordinal spine** (minimal): the von Neumann ordinal, transfinite induction,
  transfinite recursion, and "every well-order has an order type".
- **ℕ from sets**: `ω` as the smallest inductive set (Infinity + Separation),
  and the theorem that `(ω, ∅, S)` **satisfies the Peano axioms** — discharging
  `math-number-systems`'s floor.
- **Cardinality**: equinumerosity and `≤` on cardinals;
  **Cantor–Schröder–Bernstein** (choice-free); **Cantor's theorem**
  (`|X| < |𝒫(X)|`); finite vs Dedekind-infinite; countable sets and their
  closure properties (`ℕ×ℕ` countable; countable unions of countable sets, using
  countable choice); the diagonal argument; `|𝒫(ℕ)| = 2^ℵ₀ = |ℝ|`; the
  arithmetic of infinite cardinals (`ℵ₀+ℵ₀ = ℵ₀·ℵ₀ = ℵ₀`; `κ·κ = κ` for
  infinite `κ`, using AC); the aleph hierarchy and Hartogs' number; the
  continuum `𝔠` and a statement (not a proof) of the independence of CH.

## Excluded (out of scope for 0.1)

- **Formal logic and metamathematics**: proof systems, completeness /
  incompleteness, model theory, the arithmetization of syntax. The logic floor
  is used, not developed — that is `math-logic-and-proof`, which now
  discharges it (Release 0.2; see `edges/cross-capsule.md`).
- **The independence proofs**: Gödel's constructible universe `L`, forcing, the
  consistency of `¬CH` / `¬AC`. CH's independence is **stated and cited**, never
  proved.
- **Deep ordinal / cardinal theory**: ordinal arithmetic beyond the definition,
  the cumulative hierarchy `V_α`, cofinality, regular / singular / inaccessible
  cardinals, the continuum function in general, large cardinals, infinitary
  combinatorics.
- **Category theory**: the universal property of the quotient is stated in
  elementary terms, not as a colimit.
- **Everything downstream**: the number systems (`math-number-systems`),
  analysis, algebra, topology.

## Level and audience

A first rigorous "sets and logic" / "foundations" course: Enderton *Elements of
Set Theory*; Halmos *Naive Set Theory*; Jech *Set Theory* ch. 1–3 (for the
harder cardinal results); Kaplansky *Set Theory and Metric Spaces* ch. 1. The
reader can follow a proof by induction and read quantifier notation.

## Foundational stance

- Working foundation: **ZFC**. The nine ZF axioms plus Choice are `axiom` nodes;
  `set` is "an element of a model of ZFC" — no longer a bare primitive, but the
  axioms themselves are the floor (their consistency is not addressed).
- **Classical logic** throughout (excluded middle, so `¬∀ ↔ ∃¬` and proof by
  contradiction are available). Recorded on `quantifier_negation`.
- **Choice is first-class and every use is edged.** The capsule marks each
  result `choice_free`, `needs_countable_choice`, or `needs_full_AC`.
  Cantor–Schröder–Bernstein, Cantor's theorem, Hartogs' number, and the finite
  pigeonhole are **choice-free** and flagged as such.
- **ℕ is constructed here** (`ω` = smallest inductive set), and
  `peano_holds_in_omega` is the theorem that hands `math-number-systems` its
  floor. `math-number-systems` Release 0.1 cites this; a Release 0.2 would edge
  it.
- **Ordinals** are von Neumann ordinals (transitive sets well-ordered by `∈`).
  Only the spine needed for transfinite recursion and order types is built.

## Proof policy

Proofs are sketched per node. The genuinely finitary / first-order cores are
checked with the `lean` skill: the preimage and image algebra, De Morgan,
quantifier negation, composition of injections/surjections, the
equivalence-class facts, and **Cantor's diagonal theorem** all go through in
**plain Lean 4 (no Mathlib)**. Finite pigeonhole and small cardinal facts are
`decide` instances. `bc` enumerates the countability bijections, runs the
diagonal argument, and computes `|𝒫(X)| = 2^{|X|}`.

## Epistemic-status policy

Labels: `axiom`, `definition`, `mathematical_identity`, `proved_theorem`,
`proved_lemma`, `proposition`, `corollary`, `constructive_result`,
`independent_of_ZFC` (for `continuum_hypothesis` only). `lean_status` per node
records what this capsule's Lean file verified (`core` = genuine plain-Lean
proof, `instance` = `decide` sample, `cited`, `none`).
