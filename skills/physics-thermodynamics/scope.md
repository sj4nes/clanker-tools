# Scope — Release 0.1

Knowledge capsule: **classical equilibrium (macroscopic) thermodynamics**, built
with the [`physics-formula-tree`](../physics-formula-tree/SKILL.md) method.

## Included

- SI units and `[M L T Θ N]` dimensional analysis.
- Single-variable and **partial** derivatives, definite integrals, and the
  exact-differential test — accepted as math primitives.
- Systems, surroundings, boundaries; state variables; equilibrium; state
  functions vs path functions; processes (quasi-static, reversible, irreversible)
  and their named specialisations (isothermal, isobaric, isochoric, adiabatic,
  isenthalpic).
- The **zeroth law** and thermodynamic temperature.
- Pressure, volume, amount of substance; the **ideal-gas law** as a constitutive
  model; the universal gas constant.
- **Internal energy, heat, work** (`δW = P dV`, work-done-by-system positive);
  the **first law** `dU = δQ − δW`.
- Heat capacities `c_v = (∂u/∂T)_v`, `c_p = (∂h/∂T)_p`; **enthalpy** `H = U + PV`;
  **Mayer's relation** and `γ = c_p/c_v`; ideal-gas `u = u(T)`; **Joule free
  expansion**; the **Joule–Thomson coefficient**.
- Reversible **adiabatic ideal gas**: `P V^γ = const`, `T V^{γ−1} = const`.
- The **second law** (Kelvin–Planck and Clausius statements and their
  equivalence); **Carnot's theorem**; the thermodynamic temperature scale;
  **Carnot efficiency** `η = 1 − T_c/T_h` and the refrigerator / heat-pump COPs;
  the **Clausius inequality**.
- **Entropy** `dS = δQ_rev/T`; the entropy-increase principle; ideal-gas entropy
  change; the `T dS` relations.
- **Thermodynamic potentials** `U, H, F = U − TS, G = H − TS`; the fundamental
  relation `dU = T dS − P dV`; the **Maxwell relations**; the extremum principles
  for `F` and `G`.
- The **third law** (statement and unattainability).

## Excluded

- **All microscopic / statistical mechanics** — partition functions, Boltzmann
  entropy `S = k_B ln Ω`, kinetic theory, equipartition *as a derivation* (the
  ideal-gas `c_v` values are quoted, not derived).
- Open systems, chemical potential `μ`, mixtures, and chemical / phase
  equilibrium — so **no** `dG = −S dT + V dP + μ dN`, no Gibbs phase rule, no
  Clausius–Clapeyron (Release 0.2).
- Real-gas equations of state (van der Waals, virial) beyond naming them as the
  correction the ideal-gas model omits.
- Non-equilibrium thermodynamics, Onsager relations, entropy *production rate*.
- Radiation thermodynamics (Stefan–Boltzmann, photon gas).
- Thermoacoustics — see the separate
  [`physics-thermoacoustics`](../physics-thermoacoustics/SKILL.md) capsule, which
  assumes this material.
- Numerical methods, measurement uncertainty.

## Conventions

- **Math level:** partial derivatives, exact differentials, line integrals along
  a process path.
- **Assumed background:** algebra, logarithms, single-variable calculus,
  elementary mechanics (force, area, pressure = normal force / area, work =
  `∫F dx`) — imported, not re-derived.
- **Unit system:** SI throughout; temperature is always **thermodynamic
  (absolute) temperature in kelvin** unless a node says "empirical".
- **Sign convention:** the **first law is `dU = δQ − δW` with `δW = P dV`** —
  heat *into* the system and work *done by* the system are positive. The
  alternative `dU = δQ + δW` (work done *on* the system) is noted on
  [`conventions.md`](conventions.md) and **not** used here.
- **Differentials:** `d` for exact differentials of state functions; `δ` for
  path-dependent infinitesimals of heat and work.
- **Specific quantities:** lowercase `u, h, s, c_v, c_p` are **per mole**;
  uppercase `U, H, S` are extensive. `c_p − c_v = R` (molar).
- **Derivations:** summarised in the formula view; the load-bearing algebra
  steps are machine-checked with Lean (`validation/derivation-checks.lean`).
- **Exactness policy:** every formula carries one label — only `definition`,
  `mathematical_identity`, `fundamental_law`, `derived_exact`,
  `constitutive_model`, `empirical_relation`, `approximation` appear in this
  release.
- **Audience:** a downstream agent needing trustworthy thermodynamic relations
  with explicit prerequisites, assumptions, sign convention, and failure modes.

## Release status

`draft` — pipeline run recorded in `validation/`. See
[`README.md`](README.md) for the method-verification summary. Structural nodes
(primitives, conventions, assumptions, laws) are `reviewed`; derived formulas are
`draft` pending per-node `bc` / `lean` cross-checks in Release 0.2.
