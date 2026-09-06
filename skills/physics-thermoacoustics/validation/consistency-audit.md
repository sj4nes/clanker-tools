# Consistency audit — Release 0.1

Run all:
`sh build/build-tree.sh && bc -q -l validation/dimensional-checks.bc && lean validation/derivation-checks.lean && sh build/gen-symbol-index.sh && sh build/gen-assumption-index.sh`

## Graph (`build/build-tree.sh`)

- 104 registered nodes, 253 prerequisite edges after `sort -u`.
- Every edge line has exactly 2 fields; no self-edges.
- Every edge endpoint exists in `nodes/nodes.tsv` (`build/unknown-edge-nodes.txt` empty).
- `tsort`: empty stderr, 104-node order → **acyclic** (BSD-safe check: stderr,
  not just exit status).
- Every one of the 253 edges satisfied by `indexes/tsort-order.txt` (no
  `order violation`).
- Node coverage: edge-node set == ordered-node set (`build/coverage.diff` empty).
- 0 isolated / root-only nodes.
- Five thermoacoustic coupling cycles avoided by documented edge-direction
  choices (`edges/cycles.md`).

## Dimensional consistency (`validation/dimensional-checks.bc`, GNU bc 7.0.3)

Basis `[M, L, T, Θ]`. 16 dimensional + 3 dimensionless checks; all give
`0 0 0 0` (LHS − RHS):
`p=ρRT`, `c_p−c_v=R`, `β=1/T_m`, `ν=μ/ρ`, `α=k/(ρc_p)`, `Pr=ν/α`, `a=sqrt(γRT)`,
`ω=ak`, `λ=2π/k`, `z₀=ρa`, `δ=sqrt(2·(ν or α)/ω)`, `U₁=u₁A`, `Ẇ=½Re[p₁U₁*]`,
`dp₁/dx = ωρ_m U₁/A`, `∇T_crit = ω|p₁|/(ρ_m c_p |u₁|)`, `Q̇₂ = ρ_m c_p ⟨u₁T₁*⟩ A`;
`Ma`, `η_C`, `δ_ν/δ_κ` dimensionless.
Special cases: short-stack `dẆ/dx ∝ (Γ−1) = 0` at `Γ=1`; standing wave
`Re[p₁U₁*] = 0` (no net power); travelling wave `Re[p₁U₁*] = |p₁||U₁| > 0`;
air `δ_ν/δ_κ = sqrt(0.71) = 0.843`; Carnot `T_C=300,T_H=600` ⇒
`η_C=0.5`, `COP_C=1`, `(1−η_C)/η_C=1`.
**Recorded caveat:** dimensional consistency is necessary, not sufficient.

## Derivation-step algebra (`validation/derivation-checks.lean`, Lean 4.33.1, no Mathlib)

13 kernel-`decide`d instance checks over `Int` (complex numbers carried as
`(re, im)` integer pairs; no Mathlib ⇒ no `ring`/complex instances):
1. Mayer + `γ = c_p/c_v` (`γ = 7/5`: `c_p − c_v = R`, `5c_p = 7c_v`).
2. `δ_ν²/δ_κ² = ν/α = Pr` (cross-multiplied instance).
3. Carnot: `η_C = 200/500`, `COP_C = 300/200`, `COP_C = (1−η_C)/η_C`.
4. Acoustic power phasing: standing `Re[p₁U₁*] = 0`, travelling `= |p₁||U₁|`.
5. `Γ − 1` sign: `> 0` engine, `= 0` critical, `< 0` refrigerator.
6. Rott → free wave equation: `ρ_m a² = γ p_m` (consistency of `k² = ω²/a²`).
**Recorded caveat:** Lean verified the *algebra* only — not the linearized
balances, the ideal-gas EOS, the boundary-layer / short-stack ordering, or the
single-frequency assumption.

## Views

- `indexes/tsort-order.txt`, `indexes/reverse-dependencies.txt` — generated.
- `indexes/symbol-index.md` — 25 formula-statement symbol groups, ptx discovery
  + whole-token confirmation. (The four `## node *(draft)*` headers whose formula
  sits on the next line are not symbol-indexed — a known gen-script limitation.)
- `indexes/assumption-index.md` — 15 assumption/regime nodes → dependents,
  derived from `nodes.tsv` (not a hard-coded list).
- `indexes/topic-index.md`, `formula-index.md`, `prerequisite-paths.md` — curated.

## Draft nodes (not yet `reviewed`)

`thermoacoustic_function_fnu`, `thermoacoustic_function_fkappa`,
`boundary_layer_limit_f`, `rott_continuity_equation`, `rott_wave_equation`,
`total_energy_flux`, `thermoacoustic_heat_flux`, `acoustic_power_gradient`,
`short_stack_acoustic_power`, `short_stack_heat_flux`.
Their **structure, prerequisites, and dimensions** are checked; the exact
closed-form coefficients need a line-by-line reconciliation with Swift 1988 /
Swift 2002 ch. 4 (tracked in `sources/bibliography.md`).

## Known gaps (tracked for Release 0.2)

- Per-node detail pages under `nodes/` — currently primitives/assumptions live in
  `conventions.md`, formula nodes in `formulas/thermoacoustics.md`.
- `formulas/*.yaml` structured entries; `sources/source-map.tsv`.
- Finite solid heat capacity/conductivity (`ε_s`); heat-exchanger effectiveness;
  acoustic streaming; the pulse-tube phasor network.
- Upgrade the Lean checks to universal `by ring` proofs and genuine complex
  arithmetic once Mathlib is available (see the `lean` skill).
