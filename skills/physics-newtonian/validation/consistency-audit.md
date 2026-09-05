# Consistency audit — Release 0.1

Run all: `sh build/build-tree.sh && bc -q -l validation/dimensional-checks.bc && lean validation/derivation-checks.lean && sh build/gen-symbol-index.sh && sh build/gen-assumption-index.sh`

## Graph (`build/build-tree.sh`)

- 58 registered nodes, 145 prerequisite edges after `sort -u`.
- Every edge line has exactly 2 fields; no self-edges.
- Every edge endpoint exists in `nodes/nodes.tsv` (`build/unknown-edge-nodes.txt` empty).
- `tsort`: empty stderr, 58-node order → **acyclic** (BSD-safe check: stderr, not
  just exit status).
- Every one of the 145 edges satisfied by `indexes/tsort-order.txt` (no
  `order violation`).
- Node coverage: edge-node set == ordered-node set (`build/coverage.diff` empty).
- 0 isolated / root-only nodes — every registered node participates in the graph.

## Dimensional consistency (`validation/dimensional-checks.bc`, GNU bc 7.0.3)

13 formulas checked on `[M, L, T]` exponents; all give `0 0 0` (LHS − RHS):
`F=ma`, `K=½mv²`, `W=Fx`, `U=mgh`, `U=½kx²`, `p=mv`, `J=Ft`, `P=Fv`,
`ω=√(k/m)`, `T=2π√(L/g)`, `F=Gm₁m₂/r²`, `U=−Gm₁m₂/r`, `g=GM/r²`.
Special cases: `K(v=0)=0`; `K(2v)/K(v)=4`; `sin(0.1)−0.1 = −1.67e-4` (small-angle
leading error); `1−cos(0.1) = 5.0e-3` (first dropped term).
**Recorded caveat:** dimensional consistency is necessary, not sufficient — it
does not fix a wrong constant, sign, direction, regime, or missing term.

## Derivation-step algebra (`validation/derivation-checks.lean`, Lean 4.33.1, no Mathlib)

5 kernel-`decide`d instance checks over `Int` (no Mathlib ⇒ no `ring` over the
reals, so these are instance checks, not universal proofs):
1. `kinematics_timeless` — `(v₀+at)² = v₀² + 2a(v₀t + ½at²)` at (3,2,5).
2. `work_equals_ΔK` — `2·(m a·dx) = m·((v₀²+2a·dx) − v₀²)` at (4,6,10,3).
3. `elastic_pe` — `(2kx²)/2 = kx²` at (5,7).
4. `angular_frequency_shm` — `m·(−Aω²c) = −k·(Ac)` ⇔ `mω²=k` at (3,4,12,9).
5. `simple_pendulum` — `(mgL)/(mL²) = g/L` at (2,10,5).
**Recorded caveat:** Lean verified the *algebra* of each step only — not
Newton's second law, not the constant-acceleration / Hooke / small-angle /
nonrelativistic premises.

## Views

- `indexes/tsort-order.txt`, `indexes/reverse-dependencies.txt` — generated.
- `indexes/symbol-index.md` — 70 formula-statement symbol occurrences, ptx
  discovery pass + whole-token confirmation.
- `indexes/assumption-index.md` — 9 assumption nodes → dependents, from the
  reverse-dependency view.
- `indexes/topic-index.md`, `formula-index.md`, `prerequisite-paths.md` — curated.

## Known gaps (tracked for Release 0.2)

- Per-node detail pages under `nodes/` — currently primitives/assumptions live in
  `conventions.md` and formula nodes in `formulas/newtonian.md`.
- `formulas/*.yaml` structured entries and `sources/source-map.tsv`.
- Static friction, 2-D vector kinematics, projectile example node, escape
  velocity / orbital energy, generalization edges to a future relativity capsule
  in `edges/relations.tsv`.
- Upgrade Lean checks to universal `by ring` proofs when Mathlib is available.
