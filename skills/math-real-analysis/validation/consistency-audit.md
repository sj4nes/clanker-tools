# Consistency audit — Release 0.1

Run everything: `sh build/all.sh`

## Graph (`build/build-tree.sh`)

- **109** registered nodes, **247** prerequisite edges after `sort -u`.
- Every edge line has exactly 2 fields; no self-edges (`graph-check.sh`).
- Every edge endpoint exists in `nodes/nodes.tsv`
  (`build/unknown-edge-nodes.txt` empty).
- `tsort`: **empty stderr**, 109-node order emitted → **acyclic**
  (BSD-safe check: stderr, not just exit status — macOS `tsort` exits 0 on a
  cycle).
- Every one of the 247 edges satisfied by `indexes/tsort-order.txt` (no
  `order violation` from `build-tree.sh`).
- **0 isolated nodes** — every registered node participates in the graph
  (`build/isolated-nodes.txt` empty). In particular every hypothesis/axiom node
  (`bounded_sequence`, `countable_choice`, `lub_axiom`, …) is a real
  prerequisite of something.
- **5 root nodes** (no prerequisites): `set`, `natural_number`,
  `rational_field`, `real_number`, `axiom_of_choice` — exactly the declared
  primitives plus the choice axiom. Documented in `conventions.md`.

## Nodes by type

| type | count |
|---|---|
| definition | 36 |
| theorem | 33 |
| proposition | 24 |
| hypothesis | 5 |
| primitive | 4 |
| axiom | 3 |
| structure | 1 |
| principle_law | 1 |
| notation_convention | 1 |
| mathematical_identity | 1 |
| **total** | **109** |

Areas: continuity 13, integration 16, sequences 15, series 13, topology 12,
differentiation 11, reals 10, function_sequences 9, foundations 7,
cross_domain 3.

## Cycles

None in the committed graph. Five *would-be* cycles were designed out before the
first `tsort` run and are recorded in `edges/cycles.md`: the completeness
pentagon (resolved: `lub_axiom` is the single upstream axiom), limit⟺continuity
(resolved: independent ε–δ definitions), derivative⟺continuity (resolved:
`derivative` requires `function_limit`, not `continuity_at_point`),
compact⟺sequentially-compact⟺closed-bounded (resolved: open-cover definition
canonical, the rest are theorems), and the IVT proof route (resolved: direct
`lub_axiom` argument canonical).

## Type / well-formedness checks (`validation/type-checks.md`)

11 headline nodes checked. All **well_formed**. The pass forced these into
explicit preconditions on the relevant nodes: limit-point requirement for every
functional limit / derivative; bounded + compact domain for every Riemann
integral; strictly-increasing index map for every subsequence; nonempty +
bounded-above for every `sup` written as a real; the exact quantifier that moves
between a pointwise and a uniform notion.

## Lean proof-core checks (`validation/proof-checks.lean`, `.md`)

- Lean **4.33.1, no Mathlib**. `lean validation/proof-checks.lean` → **exit 0**,
  no `sorry`, 12 checked items.
- **Universal (genuine proofs):** triangle inequality, reverse triangle, the
  squeeze / 3-ε pattern (all `omega` over ℤ); the telescoping sum and the
  geometric ratio bound (induction).
- **Instance checks (`decide`, not universal):** geometric partial-sum identity,
  2nd-order Taylor remainder, AM–GM step, MVT auxiliary-function endpoints.
- Per `validation/proof-checks.md`, no node's epistemic label rests on this
  file: `proved_theorem` / `proposition` labels rest on cited standard proofs;
  `lean_status` in each `results/*.yaml` records separately what was actually
  machine-checked (`core-arith` / `instance` / `none`).

## bc instance checks (`validation/instance-checks.bc`)

`bc -q -l` → clean run, output archived to `build/instance-checks.out`. Covers:
geometric series convergence + divergence at `r ∈ {1,2}`; the √2 recursion
matching `sqrt(2)` to 40 places and its failure in ℚ; `x_n = n` spacing;
harmonic (diverges) vs `p=2` (→ π²/6); alternating harmonic → `ln 2`;
`x^n` sup on `[0,1]` (stays 1) vs `[0,0.9]` (→ 0); the MVT point `c=2` for
`x²` on `[1,3]`; IVT bisection → `sqrt(2)`; Taylor `e^x` degree-4 remainder
under the Lagrange bound. **Every one is an instance** — a disproof of a
dropped-hypothesis claim or a specialization sanity check, never a proof.

Two `bc` gotchas hit and fixed during authoring: `n % 2` is scale-dependent
(computed a fractional "remainder") — replaced with a sign-flip variable; and
the modulo issue only, no truncation-rounding issues since every rounding-
sensitive check is stated as an inequality.

## Coverage of the deliverable

- `results/*.yaml`: 15 (the headline nodes). Remaining nodes are covered by
  `nodes/nodes.tsv` + `edges/dependencies.plan` + the indexes; result YAMLs are
  added as nodes are promoted past `reviewed`.
- `nodes/*.md` detail pages: 3 exemplars (`bolzano_weierstrass`,
  `mean_value_theorem`, `uniform_convergence`) matching the method's template.
- Every headline node has: a type check, ≥1 specialization, ≥1
  hypothesis-dropped counterexample, a proof provenance with explicit
  `lean_status`, ≥1 source.

## Standing limitations

A curated dependency graph, **not** a complete account of real analysis. A valid
`tsort` order confirms only the encoded prerequisite constraints — not proof
order, not pedagogical order, not historical order. A passing type check and
passing `bc`/`decide` instances are **not** proofs. Lean here verified only
small algebraic cores, never an analytic theorem and never the informal-to-
formal gap. Every result's validity stays conditional on its stated hypotheses,
the `lub_axiom`-based foundational stance, the conventions in `conventions.md`,
and its cited source.
