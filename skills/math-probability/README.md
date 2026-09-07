# math-probability — Release 0.1

A curated, dependency-ordered **knowledge capsule** for probability theory, from
the Kolmogorov axioms to the classical limit theorems and conditional
expectation. Built with the [`math-theorem-tree`](../math-theorem-tree/SKILL.md)
method. The missing foundational floor under
[`design-of-experiments`](../design-of-experiments/SKILL.md),
[`simulation`](../simulation/SKILL.md), and
[`unknown-discovery`](../unknown-discovery/SKILL.md).

## How to read it

1. **[`scope.md`](scope.md)** — what is in, what is out, the level, and the
   **foundational stance** (the abstract Lebesgue integral is *cited, not
   built*; Kolmogorov's third axiom is *countable* additivity).
2. **[`conventions.md`](conventions.md)** — every notation choice, the
   **convergence-mode tag** (the per-result analogue of the sibling capsules'
   choice grade), and the cycle resolutions.
3. **[`nodes/nodes.tsv`](nodes/nodes.tsv)** — the 131-node registry: id, type,
   area, one-line statement.
4. **[`edges/dependencies.plan`](edges/dependencies.plan)** — every prerequisite
   edge with a `#` comment stating its evidence. Stripped to
   `dependencies.edges` and linearized by `tsort`.
5. **[`edges/cycles.md`](edges/cycles.md)** — the four would-be cycles
   (independence ↔ conditional probability; expectation ↔ integral; two
   modelling slips) and how each was resolved.
6. **[`indexes/`](indexes/)** — generated views: `tsort-order.txt`,
   `hypothesis-index.md` (every result reachable from a given
   axiom/hypothesis/primitive), `status-index.md`, `counterexample-index.md`,
   `prerequisite-paths.md` (minimal prerequisite set of each headline result),
   `reverse-dependencies.txt`.
7. **[`validation/`](validation/)** — `proof-checks.lean` (Mathlib-free, Lean
   4.33 `grind`/`omega`; **15 genuine universal cores** — union bound,
   inclusion–exclusion, Bayes denominator, indicator algebra, linearity of
   expectation in the scalars, the centered-moment identity behind
   `Var = E[X²]−E[X]²`, `Var(aX+b)=a²Var(X)`, Markov by induction, the Chebyshev
   reduction, Jensen for `φ = square` via the `t(n−t)(x−y)²` factorization,
   covariance bilinearity, variance of a sum — plus `decide` instances for the
   quadratic facts and the distribution moments); `proof-checks.md` (the
   genuine-vs-cited split, keyed to nodes); `instance-checks.bc` (distribution
   moments + a numerical CLT demo); and the generated worksheets
   `type-checks.md`, `specialization-cases.md`, `instance-checks.md` (one
   `## <node>` section each, so every YAML `checks:` anchor resolves).

## Build

```sh
sh build/build-tree.sh     # graph-check + tsort (BSD-safe cycle detection) + reverse deps
sh build/all.sh            # the above + all index views + lean + bc
```

`build-tree.sh` fails loudly on a cycle (checks `tsort` **stderr**, not just the
exit status) and on any supplied edge the emitted order violates.

## Interactive tutorials

Both built with the [`theorem-tree-tutorial`](../theorem-tree-tutorial/SKILL.md)
skill; a runnable check for each node, a runnable **counterexample** for each
theorem, and an **"In the wild"** beat after each milestone (prose from the
node's `applications` field + a runnable `app_` block computing the real formula
— the Bonferroni threshold, the PAC sample size, a Chernoff tail). `upmd --ci
--all` green; the `lean_` beats need `lean` on `PATH` or they `SKIP`.

- [`tutorial/three-axioms.md`](tutorial/three-axioms.md) — "Three axioms, and
  everything before random variables". The minimal path to `boole_inequality`
  (the union bound) on a fair die.
- [`tutorial/concentration-ladder.md`](tutorial/concentration-ladder.md) — "The
  concentration ladder": `markov_inequality` → `chebyshev` → `jensen` →
  `chernoff` → `hoeffding_lemma` → `hoeffding_inequality`, each rung Markov
  applied to a cleverer function. Three genuine Lean cores
  (`markov_finite`, `chebyshev_reduction_fwd`, `jensen_sq`); the exponential
  rungs are `cited`. Capstone: the Hoeffding sample-size formula vs Chebyshev's
  (~10× fewer samples).

## Headline results

`kolmogorov_axioms` · `boole_inequality` · `borel_cantelli_first` ·
`bayes_theorem` · `probability_integral_transform` · `expectation_linearity` ·
`markov_inequality` · `jensen_inequality` · `chebyshev_inequality` ·
`hoeffding_inequality` · `convergence_implications` · `weak_law_large_numbers` ·
`strong_law_large_numbers` · `central_limit_theorem` · `tower_property` ·
`law_of_total_variance`.

## Standing limitations

A curated graph, not a complete account of probability. A valid `tsort` order
confirms only the **encoded** constraints. A type check and passing `bc`
instances are **not** a proof. `lean` verified only the small finitary cores
listed above — the CLT, SLLN, Lévy continuity, Radon–Nikodym, MCT/DCT, and the
existence of `E[X|𝓖]` carry `lean_status: cited` and rest on Billingsley /
Durrett / Williams. Every result stays conditional on its hypotheses, the
foundational stance, the conventions, and its cited source.

## Status

Release 0.1 — **complete and building green.** 131 nodes, 399 edges, acyclic,
`tsort` clean, 0 isolated. Every node has a `results/<id>.yaml` (typed symbols,
hypotheses, specialization, hypothesis-dropped counterexamples, proof
provenance, sources) and a `nodes/<id>.md` detail page. `edges/relations.tsv`
carries the 45 non-prerequisite relations. `build/check-consistency.py` verifies
that every YAML's `dependencies` match the graph exactly, every source key is in
the bibliography, and every relation endpoint is registered. Lean cores and the
`bc` worksheet pass (exit 0).

Most `results/*.yaml` and node pages are generated from a single spec table
(`build/gen-results.py`) so they cannot drift from the graph; the 6 headline
entries are hand-written. **36 nodes carry `lean_status: core`** (a kernel-checked
core or `decide` instance); 41 deep analytic results are `cited`.
`build/gen-validation-md.py` renders the three `validation/*.md` worksheets from
the YAMLs. `build/all.sh` runs the whole pipeline; `build/check-consistency.py`
gates it.
