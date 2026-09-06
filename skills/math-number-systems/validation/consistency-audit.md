# Consistency audit — Release 0.1

Run everything: `sh build/all.sh`

## Graph (`build/build-tree.sh`)

- **100** registered nodes, **274** prerequisite edges after `sort -u`.
- Every edge line has exactly 2 fields; no self-edges (`graph-check.sh`).
- Every edge endpoint exists in `nodes/nodes.tsv`
  (`build/unknown-edge-nodes.txt` empty).
- `tsort`: **empty stderr**, 100-node order emitted → **acyclic** (BSD-safe
  check: stderr, not just exit status).
- Every one of the 274 edges satisfied by `indexes/tsort-order.txt` (no
  `order violation`).
- **0 isolated nodes.**
- **1 root node**: `set`. Everything else is derived, except the three assumed
  `axiom`-typed nodes `peano_axioms`, `axiom_of_choice`, `countable_choice`
  (each of which *has* prerequisites — `set`, `function` — so is not a root, but
  is taken on faith). This is the payoff of the capsule: the number systems
  bottom out at `set` + Peano + (optionally) choice.

## Nodes by type

| type | count |
|---|---|
| definition | 32 |
| theorem | 26 |
| proposition | 22 |
| structure | 9 |
| construction | 5 |
| axiom | 3 |
| principle_law | 2 |
| primitive | 1 |
| **total** | **100** |

Areas: rationals 19, naturals 16, integers 15, reals 16, structures 8,
cardinality 10, foundations 16.

## Cycles

None in the committed graph. Seven would-be cycles designed out in advance
(`edges/cycles.md`): induction ⟺ strong induction ⟺ well-ordering; recursion
theorem ⟺ arithmetic; order ⟺ addition; ℤ ⊂ ℚ ⊂ ℝ "as subsets"; ℝ by cuts ⟺
ℝ by Cauchy sequences; "the relation is an equivalence" before the quotient;
and completeness ⟺ real number — the last resolved *opposite* to
`math-real-analysis`: here `real_number` is **built** (from cuts, requiring only
ℚ + set ops) and `lub_property` is a **theorem** requiring it.

## Type / well-formedness checks (`validation/type-checks.md`)

14 headline nodes, all **well_formed**. Recurring obligations forced into the
entries: (1) the defining relation is a genuine equivalence *before* the
quotient exists; (2) every quotient operation carries a "respects `∼`" clause;
(3) every ℝ operation must output a *cut*; (4) sign cases are mandatory in
`real_multiplication`; (5) `cantor_diagonal_argument` must dodge `0.999…`;
(6) `countable_union_countable`'s choice use is edged, not hidden.

## Lean proof-core checks (`validation/proof-checks.lean`, `.md`)

- Lean **4.33.1, no Mathlib**. `lean validation/proof-checks.lean` → **exit 0**,
  no `sorry`, 10 checked items.
- **Genuine universal proofs:** ℤ-relation transitivity, ℤ-addition and
  ℤ-order respecting `∼` (all `omega` over ℤ); commutativity of ℕ-addition
  proved from its recursive definition by induction (`zero_add'`, `succ_add'`,
  `add_comm'`); division-with-remainder existence via core `Nat` lemmas;
  **Cantor's diagonal theorem** (plain Lean, no Mathlib).
- **Instance checks (`decide`):** ℤ-multiplication respecting `∼`, ℚ-relation
  transitivity, √2-irrationality on `q < 50`, Cantor-pairing injectivity on an
  `8×8` grid.
- No epistemic label rests on this file; `lean_status` per YAML records what was
  actually checked (`core-arith` / `instance` / `cited` / `none`).

## bc instance checks (`validation/instance-checks.bc`)

`bc -q -l` → clean run (`build/instance-checks.out`). Covers: the ℤ and ℚ
quotient arithmetic computed concretely (`[(5,2)]=[(8,5)]`, lowest terms via
gcd); division with remainder for `±17`; √2-irrationality (no `p/q`, `q≤2000`);
Archimedean and density witnesses; the incompleteness of ℚ as a decimal search
(square `< 2` forever, next tick `> 2`); the Cantor pairing tabulated as a
bijection onto `{0,1,2,…}`; a worked diagonal real; nth roots by bisection
(`2^{1/3}`, `7^{1/2}`).

Two `bc` gotchas hit and fixed during authoring: a `while` loop whose counter
was incremented *outside* the braces (infinite loop) — rewritten as `for`; and
`a % b` under `bc -l` (which sets `scale = 20`) computing a *fractional*
remainder, so the gcd routine returned garbage — fixed by `scale = 0` for the
integer sections and computing the remainder as `a - b*(a/b)`.

## Coverage of the deliverable

- `results/*.yaml`: 15 (the headline nodes). Remaining nodes covered by
  `nodes/nodes.tsv` + `edges/dependencies.plan` + the indexes.
- `nodes/*.md` detail pages: 3 exemplars (`lub_property`, `integer`,
  `cantor_diagonal_argument`).
- Every headline node has a type check, ≥1 specialization, ≥1
  hypothesis-dropped counterexample, a proof provenance with explicit
  `lean_status`, and ≥1 source.

## The bridge to `math-real-analysis`

`conventions.md` records the mapping. This capsule's outputs discharge
`math-real-analysis`'s five primitive roots: `rational_field` →
`rational_is_ordered_field`; `real_number` → `real_number` +
`real_is_ordered_field`; `lub_axiom` (there an axiom) → `lub_property` (here a
**theorem**); `natural_number` → refined to `peano_axioms` + `recursion_theorem`
+ the ℕ-arithmetic propositions (the set model still cited);
`axiom_of_choice` → stays an axiom (correctly independent).

## Standing limitations

A curated dependency graph, **not** a full development. A valid `tsort` order
confirms only the encoded prerequisite constraints. `peano_axioms` is the floor:
the set-theoretic construction of ℕ is cited, not built. The set-level
constructions (cuts, the ℝ field laws, `lub_property`, `real_uniqueness`) are
not formalised in this Mathlib-free environment — they rest on [landau],
[rudin_principles], [enderton]. A passing type check and passing `bc`/`decide`
instances are not proofs. `countable_union_countable` depends essentially on
countable choice. Every result stays conditional on its stated hypotheses, the
Peano/ZFC/cuts foundational stance in `conventions.md`, and its cited source.
