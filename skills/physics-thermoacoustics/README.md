# physics-thermoacoustics

Linear thermoacoustics as a **knowledge capsule** — built with the
[`physics-formula-tree`](../physics-formula-tree/SKILL.md) method, the second
domain capsule after [`physics-newtonian`](../physics-newtonian/SKILL.md).

- Start: [`SKILL.md`](SKILL.md) · [`scope.md`](scope.md) · [`conventions.md`](conventions.md)
- Graph: [`nodes/nodes.tsv`](nodes/nodes.tsv) · [`edges/dependencies.plan`](edges/dependencies.plan) · [`edges/cycles.md`](edges/cycles.md)
- Formulas: [`formulas/thermoacoustics.md`](formulas/thermoacoustics.md)
- Views: [`indexes/`](indexes/) — formula/topic/symbol/assumption indexes, tsort order, prerequisite paths
- Verification: [`validation/consistency-audit.md`](validation/consistency-audit.md)

## Build

```sh
sh build/build-tree.sh                       # graph-check -> tsort -> views
bc -q -l validation/dimensional-checks.bc    # [M L T Theta] consistency, 19 checks
lean validation/derivation-checks.lean       # 13 kernel-checked algebra instances
sh build/gen-symbol-index.sh
sh build/gen-assumption-index.sh
```

## Scope rationale

Scoped to track the theory behind the most effective real devices. The
**traveling-wave / Stirling** framework (Ceperley 1979 → Rott linear theory →
Backhaus & Swift 2000, `η ≈ 0.30 ≈ 0.40 η_C`) produced far more effective
engines and refrigerators than the standing-wave approach, because the
regenerator's near-reversible heat exchange (`f_κ → 1`, `r_h ≪ δ_κ`) removes the
intrinsic irreversibility of the standing-wave stack. So Release 0.1 carries the
**full Rott wave equation** (complex `f_ν`, `f_κ`; distributed treatment) with
Swift's **short-stack standing-wave** analysis as the analytic on-ramp, and
covers both device classes plus the Carnot limit.

## Method verification (Release 0.1)

Second capsule built end-to-end with `physics-formula-tree`; a larger and
deeper graph than `physics-newtonian` (104 vs 58 nodes, complex-valued fields,
four-dimensional `[M L T Θ]` basis).

| Stage | Tool | Result |
|---|---|---|
| graph + sort | BSD `tsort` | 104 nodes, 253 edges, **acyclic**; every edge respected; one initially-isolated assumption node (`no_mean_flow`) caught by the coverage step and edged. |
| dimensional | GNU `bc` 7.0.3 | 19/19 consistent on the `[M L T Θ]` basis. **Two bc gotchas re-confirmed and folded into the method:** uppercase names rejected (`Pr` → `pr`), and `_` rejected in names (`_d` → `dd`). Four-exponent quadruples via a small `p4` helper. |
| derivations | Lean 4.33.1, **no Mathlib** | 13/13 `Int` instance checks; complex numbers carried as explicit `(re, im)` pairs since core Lean has no complex instances. Same no-`ring` fallback as `physics-newtonian`. |
| assumption index | shell | Rewrote `gen-assumption-index.sh` to derive the assumption list from `nodes.tsv` (`type ∈ {assumption, regime_limit}`) instead of a hard-coded list — a reusable improvement over the `physics-newtonian` version. |
| symbol index | GNU `ptx` 9.11 | discovery pass + whole-token confirmation. Limitation surfaced: `## node *(draft)*` headers with the formula on the next line are not symbol-indexed (10 draft nodes). |

Nothing in the method proved wrong. Ten nodes are at `draft` status: their
structure/prerequisites/dimensions are checked but the exact Rott/Swift
coefficient forms await a line-by-line source pass (see
`sources/bibliography.md`).
