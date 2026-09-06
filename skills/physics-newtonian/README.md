# physics-newtonian

Newtonian point-particle mechanics as a **knowledge capsule** — the first
artifact built with the [`physics-formula-tree`](../physics-formula-tree/SKILL.md)
method, and its proof-of-method.

- Start: [`SKILL.md`](SKILL.md) · [`scope.md`](scope.md) · [`conventions.md`](conventions.md)
- Graph: [`nodes/nodes.tsv`](nodes/nodes.tsv) · [`edges/dependencies.plan`](edges/dependencies.plan) · [`edges/cycles.md`](edges/cycles.md)
- Formulas: [`formulas/newtonian.md`](formulas/newtonian.md)
- Views: [`indexes/`](indexes/) — formula/topic/symbol/assumption indexes, tsort order, prerequisite paths
- Verification: [`validation/consistency-audit.md`](validation/consistency-audit.md)

## Tutorials

- [`tutorial/pendulum.md`](tutorial/pendulum.md) — "Why a Pendulum Keeps Time":
  an interactive walk from Newton's second law to `T = 2π√(L/g)`, built with the
  [`formula-tree-tutorial`](../formula-tree-tutorial/SKILL.md) skill. Run it with
  `upmd tutorial/pendulum.md` (or `upmd --ci --all tutorial/pendulum.md`).

## Build

```sh
sh build/build-tree.sh                       # graph-check -> tsort -> views
bc -q -l validation/dimensional-checks.bc    # [M L T] consistency, 13 formulas
lean validation/derivation-checks.lean       # 5 kernel-checked algebra steps
sh build/gen-symbol-index.sh                 # ptx discovery + confirmed symbol index
sh build/gen-assumption-index.sh
```

## Method verification (Release 0.1)

Building this capsule exercised the `physics-formula-tree` method end-to-end on a
real 58-node graph. Outcome and fixes folded back into the method skill:

| Stage | Tool | Result |
|---|---|---|
| graph + sort | BSD `tsort` | 58 nodes, 145 edges, **acyclic**; every edge respected; scripts from the method's `references/package-layout.md` ran as written (BSD-safe cycle check confirmed necessary — `tsort --version` is rejected on macOS). |
| dimensional | GNU `bc` 7.0.3 | 13/13 consistent. **Fix:** `bc` rejects uppercase identifiers — the method's dimensional-check guidance now says use lowercase `<q>m <q>l <q>t` triples. One sign-typo in a check caught by the `0 0 0` gate (the gate works). |
| derivations | Lean 4.33.1, **no Mathlib** | 5/5 instance checks pass. **Fix:** no Mathlib ⇒ no `ring`/`nlinarith` over the reals; the method's `skill-composition.md` now states the fallback is kernel-`decide`d `Int` instance checks, labelled as such, and to record what Lean did *not* verify. Int `/` truncation bites the ½ factors — write `(2·expr)/2` forms. |
| symbol index | GNU `ptx` 9.11 | ptx raw output is prose-dominated for this corpus; used as a discovery pass only, with a whole-token confirmation step — matches the `ptx` skill's "confirm every lead" rule. |

Nothing in the method proved wrong; the fixes are sharper tool-specific
guidance. See the method skill's own `references/` for where each was folded in.
