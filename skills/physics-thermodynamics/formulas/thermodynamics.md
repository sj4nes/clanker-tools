# Formula entries — Release 0.1

A view generated from and reconciled against the graph. Each entry: statement,
symbols (SI unit and `[M L T Θ N]` dimension), exactness label, assumptions,
preconditions, direct prerequisites, one limiting/special case, failure modes,
source. Dimensional checks: `validation/dimensional-checks.bc`. Derivation-step
algebra: `validation/derivation-checks.lean`. **Sign convention: `dU = δQ − δW`,
`δW = P dV`** (heat in, work by system positive) — see `conventions.md`.

Sources: `Cal` = Callen, *Thermodynamics and an Introduction to Thermostatistics*,
2nd ed.; `Fermi` = Fermi, *Thermodynamics*; `Zemansky` = Zemansky & Dittman,
*Heat and Thermodynamics*, 7th ed.; `SI` = BIPM SI Brochure, 9th ed.

---

## zeroth_law — `A ~ C and B ~ C  ⇒  A ~ B`
- `~` = "in thermal equilibrium with". Label: fundamental_law.
- Prereqs: thermal_equilibrium. Asserts the relation is transitive, so a common
  value — temperature — can be assigned.
- Special case: two systems at the same temperature exchange zero net heat.
- Failure: applying to non-equilibrium systems or across a non-diathermal wall.
- Source: Zemansky ch. 1; Fermi ch. 1.

## temperature — `T`
- T: thermodynamic temperature, K, `Θ`. Label: physical_definition (empirical
  here; the absolute scale is fixed later by `thermodynamic_temperature_scale`).
- Prereqs: zeroth_law, thermal_equilibrium, state_variable, SI_units.
- Special case: `T > 0` on the thermodynamic scale (third law).
- Failure: treating a particular thermometric property (gas pressure, resistance)
  as *the* temperature rather than a scale realising it.
- Source: SI §2.3.1; Zemansky ch. 1.

## ideal_gas_law — `P V = n R T`
- P: pressure, Pa, `M L^-1 T^-2`. V: volume, m³, `L^3`. n: amount, mol, `N`.
  R: gas constant, `8.314 J mol⁻¹ K⁻¹`, `M L^2 T^-2 Θ^-1 N^-1`. T: K, `Θ`.
- Label: constitutive_model. Assumptions: `ideal_gas` — no intermolecular
  forces, negligible molecular volume; dilute / high-`T`, low-`P` limit.
- Preconditions: `T > 0`; single-phase gas.
- Prereqs: pressure, volume, temperature, amount_of_substance, gas_constant,
  ideal_gas. Dimensional check: `#P V = n R T` (consistent).
- Special case: at fixed `T`, `P ∝ 1/V` (Boyle); at fixed `P`, `V ∝ T` (Charles).
- Failure: near condensation, at high pressure, for the critical region — use a
  real-gas equation (van der Waals, virial); the model omits the `a/V²`
  attraction and the `b` excluded volume.
- Source: Fermi ch. 2; Zemansky ch. 5.

## internal_energy — `U` (state function)
- U: internal energy, J, `M L^2 T^-2`. Label: physical_definition / state
  function — `∮ dU = 0`.
- Prereqs: energy, state_function, thermodynamic_system, extensive_intensive.
- Special case: for a closed system with no process, `U` is fixed.
- Failure: assigning an absolute `U` (only differences are defined here);
  forgetting `U` is extensive.
- Source: Callen ch. 1.

## work_thermodynamic — `δW = P dV` ; `W = ∫ P dV`
- W: work done *by* the system, J, `M L^2 T^-2`. P: Pa. V: m³.
- Label: definition (quasi-static). Assumptions: `quasistatic` (system pressure
  well-defined throughout); sign per `work_sign_convention`.
- Preconditions: a defined `P(V)` path.
- Prereqs: pressure, volume, integral, quasistatic, work_sign_convention, energy.
- Special case: isochoric `dV = 0 ⇒ W = 0`; isobaric `W = P ΔV`.
- Failure: using `P dV` for a rapid / irreversible expansion where system
  pressure is undefined (use the external pressure and an inequality); sign slips
  from the other convention.
- Source: Fermi ch. 1; Zemansky ch. 3.

## first_law_thermodynamics — `dU = δQ − δW`
- dU: exact; δQ, δW: path-dependent. All J, `M L^2 T^-2`.
- Label: fundamental_law. Assumptions: `closed_system`; energy conservation;
  `U` is a state function (the law's content).
- Prereqs: internal_energy, work_thermodynamic, work_sign_convention,
  energy_conservation, closed_system, state_function.
- Special case: isolated system ⇒ `δQ = δW = 0 ⇒ dU = 0`. Cyclic process ⇒
  `∮ δQ = ∮ δW` (net heat in = net work out).
- Failure: open systems (mass carries energy — add `h dn` terms); the `+δW` sign
  convention without flipping `W`.
- Source: Callen ch. 1; Fermi ch. 3.

## heat — `δQ = dU + δW`
- Q: heat, J, `M L^2 T^-2`. Label: physical_definition (via the first law).
- Prereqs: first_law_thermodynamics, temperature, energy.
- Special case: adiabatic ⇒ `δQ = 0`; then `dU = −δW`.
- Failure: calling `Q` a state function ("heat content" — that is enthalpy, and
  only under constant `P`); confusing heat with temperature.
- Source: Fermi ch. 1.

## heat_capacity — `C = δQ / dT` (path-specified)
- C: J K⁻¹, `M L^2 T^-2 Θ^-1`. Label: definition.
- Prereqs: heat, temperature, derivative.
- Special case: path must be named — `C_V` and `C_P` differ.
- Failure: quoting `C` without the path; using a constant `C` across a phase
  change (where `C → ∞`).
- Source: Zemansky ch. 4.

## heat_capacity_cv — `c_v = (∂u/∂T)_v`
- c_v: molar, J mol⁻¹ K⁻¹, `M L^2 T^-2 Θ^-1 N^-1`. u: molar internal energy.
- Label: definition. Assumptions: isochoric path; `u` differentiable in `T`.
- Prereqs: internal_energy, partial_derivative, isochoric_process,
  heat_capacity, first_law_thermodynamics, extensive_intensive.
- Special case: at constant `V`, `δW = 0`, so `δQ = dU` and `C_V = (∂U/∂T)_V`
  directly.
- Failure: using the molar value where the extensive `C_V = n c_v` is meant.
- Source: Callen ch. 3.

## enthalpy — `H = U + P V`
- H: J, `M L^2 T^-2`. Label: derived_exact (state function, since `U, P, V` are).
- Prereqs: internal_energy, pressure, volume, state_function.
- Special case: at constant `P`, `ΔH = Q_P` (heat equals enthalpy change);
  `dH = δQ + V dP`.
- Failure: reading `H` as "total energy"; using `ΔH = Q` when `P` is not constant.
- Source: Callen ch. 5; Zemansky ch. 4.

## heat_capacity_cp — `c_p = (∂h/∂T)_p`
- c_p: molar, `M L^2 T^-2 Θ^-1 N^-1`. Label: definition. Assumptions: isobaric
  path.
- Prereqs: enthalpy, partial_derivative, isobaric_process, heat_capacity.
- Special case: `c_p > c_v` for any stable substance (expansion does work).
- Failure: same molar/extensive slip as `c_v`.
- Source: Callen ch. 3.

## mayer_relation — `c_p − c_v = R`
- Molar, all `M L^2 T^-2 Θ^-1 N^-1`. Label: derived_exact. Assumptions:
  **ideal gas** (general form is `c_p − c_v = −T (∂P/∂T)_V² / (∂P/∂V)_T`).
- Prereqs: heat_capacity_cv, heat_capacity_cp, ideal_gas_law, enthalpy,
  gas_constant. Lean instance check 1.
- Special case: monatomic ideal gas `c_v = 3R/2 ⇒ c_p = 5R/2`.
- Failure: applying the `R` form to a real gas or a liquid/solid (there
  `c_p − c_v` is small and material-specific).
- Source: Fermi ch. 4.

## heat_capacity_ratio — `γ = c_p / c_v`
- γ: dimensionless. Label: derived_exact. `γ > 1` always.
- Prereqs: heat_capacity_cv, heat_capacity_cp. Lean instance check 2.
- Special case: monatomic `γ = 5/3 ≈ 1.667`; diatomic (room T) `γ = 7/5 = 1.4`.
- Failure: treating `γ` as constant across a wide temperature range (vibrational
  modes activate); using the ideal value for dense fluids.
- Source: Zemansky ch. 5.

## ideal_gas_internal_energy — `u = u(T)` , `du = c_v dT`
- Label: derived_exact. Assumptions: **ideal gas**. Content: `(∂u/∂V)_T = 0`.
- Prereqs: ideal_gas, internal_energy, heat_capacity_cv, joule_free_expansion.
- Special case: any process of an ideal gas has `ΔU = n c_v ΔT` — even
  non-isochoric ones.
- Failure: using `ΔU = n c_v ΔT` for a real gas (there `U` depends on `V` too).
- Source: Fermi ch. 4; Callen ch. 13.

## joule_free_expansion — `ΔU = 0`, `W = 0`, `Q = 0`
- Label: example. Setup: gas expands into an evacuated, rigid, insulated chamber.
- Prereqs: first_law_thermodynamics, internal_energy, work_thermodynamic,
  isolated_system, adiabatic_process. Lean instance check 6.
- Special case: **ideal** gas ⇒ `ΔT = 0`; real gas ⇒ `ΔT ≠ 0` (usually cools).
- Failure: assuming `W = ∫P dV ≠ 0` — there is no opposing pressure, and the
  process is irreversible so system `P` is undefined anyway.
- Source: Fermi ch. 4.

## joule_thomson_coefficient — `μ_JT = (∂T/∂P)_H`
- μ_JT: K Pa⁻¹, `M^-1 L T^2 Θ`. Label: derived_exact. Assumptions: isenthalpic
  (throttling through a porous plug / valve).
- Prereqs: enthalpy, partial_derivative, isenthalpic_process, temperature,
  pressure.
- Special case: **ideal gas ⇒ μ_JT = 0**. Real gas: `μ_JT > 0` below the
  inversion temperature (cooling on expansion — basis of gas liquefaction).
- Failure: predicting cooling for an ideal gas; ignoring the sign change at the
  inversion curve.
- Source: Zemansky ch. 11; Callen ch. 6.

## adiabatic_reversible_ideal_gas — `P V^γ = const` ; `T V^{γ−1} = const`
- Label: derived_exact. Assumptions: `adiabatic_process` (δQ = 0),
  `reversible`, **ideal gas**, `γ` constant over the range.
- Prereqs: adiabatic_process, reversible, ideal_gas_law, heat_capacity_ratio,
  first_law_thermodynamics, ideal_gas_internal_energy, integral, logarithm.
- Special case: `γ = 1` (isothermal limit) recovers `PV = const`. `T V^{γ−1}`
  and `T^γ P^{1−γ}` are equivalent via `PV = nRT`.
- Special case (numeric): `γ = 1.4`, `V₂/V₁ = 2 ⇒ T₂/T₁ = 2^{−0.4} ≈ 0.758`
  (`bc` check).
- Failure: using it for an *irreversible* adiabat (e.g. free expansion — there
  `PV^γ` is not conserved); for a real gas; across a `γ`-changing range.
- Source: Fermi ch. 4; Zemansky ch. 5.

## thermodynamic_cycle — `∮ dU = 0` (and `∮ dS = 0`)
- Label: physical_definition. Any state function nets to zero over a cycle.
- Prereqs: process, state_function, internal_energy.
- Special case: `∮ δQ = ∮ δW` — the first law for a cycle.
- Failure: assuming `∮ δQ = 0` (heat is not a state function).
- Source: Fermi ch. 3.

## heat_engine — `η = |W| / |Q_h|`
- η: dimensionless efficiency. Label: physical_definition.
- Prereqs: thermodynamic_cycle, heat, work_thermodynamic, temperature.
- Special case: `η = 1 − |Q_c|/|Q_h|` by the first law over the cycle.
- Failure: `η > 1` (violates the first law); `η` from a non-cyclic process.
- Source: Zemansky ch. 6.

## refrigerator — `COP = |Q| / |W|`
- COP: coefficient of performance, dimensionless. `COP_ref = |Q_c|/|W|`,
  `COP_hp = |Q_h|/|W|`, and `COP_hp = COP_ref + 1`.
- Label: physical_definition. Prereqs: thermodynamic_cycle, heat,
  work_thermodynamic, temperature.
- Special case: COP can exceed 1 (it is not an efficiency).
- Failure: calling it "efficiency"; expecting `COP ≤ 1`.
- Source: Zemansky ch. 6.

## kelvin_planck_statement — no cyclic engine converts heat from a single reservoir entirely into work
- Label: fundamental_law (second law). Prereqs: heat_engine, thermodynamic_cycle,
  temperature.
- Special case: forbids `η = 1`; a temperature *difference* is required.
- Failure: confusing "single reservoir" with "single cycle step"; ignoring the
  "cyclic" qualifier (a single expansion *can* be 100% conversion once).
- Source: Fermi ch. 3; Zemansky ch. 6.

## clausius_statement — no cyclic process moves heat cold→hot with no other effect
- Label: fundamental_law (second law). Prereqs: refrigerator, heat, temperature.
- Special case: a refrigerator works only because work is supplied.
- Failure: forgetting "with no other effect".
- Source: Fermi ch. 3.

## second_law_equivalence — Kelvin–Planck ⇔ Clausius
- Label: bridge. Each statement's violation constructs a violation of the other.
- Prereqs: kelvin_planck_statement, clausius_statement.
- Source: Fermi ch. 3; Zemansky ch. 6.

## carnot_cycle — two reversible isothermals + two reversible adiabats
- Label: example. Prereqs: isothermal_process, adiabatic_process, reversible,
  thermodynamic_cycle, heat_engine.
- Special case: the working substance is irrelevant to its efficiency.
- Failure: assuming any two-reservoir cycle is a Carnot cycle; drawing it
  irreversibly.
- Source: Fermi ch. 3.

## carnot_theorem — `η_rev ≥ η_any` between the same two reservoirs; all reversible engines have equal `η`
- Label: fundamental_law (from Kelvin–Planck). Prereqs: kelvin_planck_statement,
  carnot_cycle, reversible, second_law_equivalence.
- Special case: it makes `η` a function of the two reservoir temperatures alone.
- Failure: comparing engines across *different* reservoir pairs.
- Source: Fermi ch. 3; Zemansky ch. 7.

## thermodynamic_temperature_scale — `|Q_h| / |Q_c| = T_h / T_c` (reversible engine)
- Label: physical_definition. Defines absolute temperature (ratios) independent
  of any substance; one fixed point (`T_tpw = 273.16 K` historically) set the
  scale.
- Prereqs: carnot_theorem, temperature, heat.
- Special case: `T = 0` would give `Q_c = 0` — a reversible engine rejecting no
  heat, i.e. `η = 1`, forbidden ⇒ `T > 0` unattainable (third law).
- Failure: using an empirical (e.g. ideal-gas) scale where the absolute one is
  required — they coincide for an ideal gas but that is a theorem, not a
  definition.
- Source: Fermi ch. 3; Callen ch. 4.

## carnot_efficiency — `η = 1 − T_c / T_h`
- η: dimensionless. `T_c, T_h`: reservoir temperatures, K, `Θ`.
- Label: derived_exact. Assumptions: reversible engine; two fixed-temperature
  reservoirs. Prereqs: carnot_theorem, thermodynamic_temperature_scale,
  heat_engine. Lean instance check 3.
- Special case: `T_c = 300 K`, `T_h = 600 K ⇒ η = 0.5` (`bc` check).
  `T_c → 0` or `T_h → ∞ ⇒ η → 1`; `T_c = T_h ⇒ η = 0`.
- Failure: applying to a real (irreversible) engine — its `η` is strictly less;
  using Celsius.
- Source: Fermi ch. 3; Zemansky ch. 7.

## carnot_cop — `COP_ref = T_c / (T_h − T_c)` ; `COP_hp = T_h / (T_h − T_c)`
- Label: derived_exact. Reversible refrigerator / heat pump between two
  reservoirs. Prereqs: carnot_theorem, thermodynamic_temperature_scale,
  refrigerator. Lean instance check 4.
- Special case: `T_h − T_c → 0 ⇒ COP → ∞`; `COP_hp = COP_ref + 1`.
- Failure: applying to a real unit (its COP is lower); a large lift `T_h − T_c`
  makes even the ideal COP small.
- Source: Zemansky ch. 7.

## clausius_inequality — `∮ δQ / T ≤ 0`
- Label: fundamental_law (from Carnot's theorem). `T` is the temperature at
  which `δQ` crosses the boundary. Equality iff the cycle is reversible.
- Prereqs: carnot_theorem, thermodynamic_cycle, thermodynamic_temperature_scale,
  temperature, heat, integral.
- Special case: reversible cycle ⇒ `∮ δQ_rev/T = 0` ⇒ `δQ_rev/T` is exact ⇒
  entropy exists.
- Failure: using the system temperature when it differs from the boundary
  temperature in an irreversible exchange.
- Source: Fermi ch. 4; Callen ch. 4.

## entropy — `dS = δQ_rev / T` ; `ΔS = ∫ δQ_rev / T`
- S: J K⁻¹, `M L^2 T^-2 Θ^-1` (extensive). Label: physical_definition (state
  function). Assumptions: integrate along **any reversible** path between the
  two states (`S` is a state function so the path choice is free).
- Prereqs: clausius_inequality, reversible, temperature, heat, state_function,
  integral.
- Special case: reversible adiabatic ⇒ `ΔS = 0` (isentropic).
- Failure: using the *actual* (irreversible) `δQ/T` of the real process — that
  underestimates `ΔS`; you must find a reversible path with the same endpoints.
- Source: Callen ch. 4; Fermi ch. 4.

## entropy_increase_principle — `ΔS_universe ≥ 0`
- Label: fundamental_law. `ΔS_universe = ΔS_system + ΔS_surroundings`. Strict `>`
  for any irreversible process; `= 0` only for a reversible one.
- Prereqs: entropy, clausius_inequality, isolated_system, irreversible.
- Special case: isolated system ⇒ `ΔS_system ≥ 0` and `S` is maximised at
  equilibrium.
- Failure: expecting `ΔS_system ≥ 0` for a *non*-isolated system (a fridge
  interior loses entropy — the surroundings gain more).
- Source: Callen ch. 4; Fermi ch. 4.

## entropy_ideal_gas — `ΔS = n c_v ln(T₂/T₁) + n R ln(V₂/V₁)`
- Also `ΔS = n c_p ln(T₂/T₁) − n R ln(P₂/P₁)`. All terms `M L^2 T^-2 Θ^-1`.
- Label: derived_exact. Assumptions: **ideal gas**; `c_v` constant over the
  range.
- Prereqs: entropy, ideal_gas_law, ideal_gas_internal_energy, heat_capacity_cv,
  logarithm, gas_constant. Lean instance check 7.
- Special case: isothermal `T₂ = T₁ ⇒ ΔS = n R ln(V₂/V₁)`; reversible adiabatic
  ⇒ both terms cancel (`T V^{γ−1} = const`).
- Failure: real gas; `c_v` varying with `T`; forgetting the `V` (or `P`) term for
  a non-isothermal change.
- Source: Fermi ch. 4.

## tds_relations — `T dS = dU + P dV` ; `T dS = dH − V dP`
- Label: mathematical_identity (given the first law and `H = U + PV`).
- Prereqs: first_law_thermodynamics, entropy, enthalpy, work_thermodynamic.
  Lean instance check 5.
- Special case: they hold for *any* process (reversible or not) because every
  term is a state function — only the *derivation* uses a reversible path.
- Failure: reading `T dS` as "the heat" for an irreversible process (then
  `δQ < T dS`).
- Source: Zemansky ch. 9; Callen ch. 3.

## entropy_free_expansion — `ΔS = n R ln(V₂/V₁) > 0` with `Q = 0`
- Label: example. Ideal gas, free expansion `V₁ → V₂ > V₁`.
- Prereqs: entropy, joule_free_expansion, entropy_ideal_gas, irreversible,
  logarithm.
- Special case: `V₂/V₁ = 2`, `n = 1 ⇒ ΔS = R ln 2 ≈ 5.76 J K⁻¹` (`bc` check).
- Failure: concluding `ΔS = 0` because `Q = 0` — that is only true for a
  *reversible* adiabat; here the process is irreversible and `δQ_rev` along a
  reversible path with the same endpoints is nonzero.
- Source: Fermi ch. 4.

## fundamental_relation_u — `dU = T dS − P dV`
- Label: mathematical_identity. `U(S, V)` with natural variables `S, V`; then
  `T = (∂U/∂S)_V`, `P = −(∂U/∂V)_S`.
- Prereqs: tds_relations, entropy, internal_energy, work_thermodynamic,
  exact_differential.
- Special case: contains all of equilibrium thermodynamics for a simple
  compressible system — every other potential is a Legendre transform of it.
- Failure: adding a `μ dn` term without extending the scope to open systems
  (Release 0.2).
- Source: Callen ch. 2.

## helmholtz_free_energy — `F = U − T S` ; `dF = −S dT − P dV`
- F: J, `M L^2 T^-2`. Label: derived_exact (Legendre transform of `U` in `T`).
- Prereqs: internal_energy, temperature, entropy, fundamental_relation_u,
  state_function.
- Special case: at constant `T`, `ΔF = W_by,rev` bound: the maximum work
  extractable is `−ΔF`. `S = −(∂F/∂T)_V`, `P = −(∂F/∂V)_T`.
- Failure: using `−ΔF` as extractable work when `T` is not constant.
- Source: Callen ch. 5; Fermi ch. 5.

## gibbs_free_energy — `G = H − T S` ; `dG = −S dT + V dP`
- G: J, `M L^2 T^-2`. Label: derived_exact (Legendre transform in `T` and `P`).
- Prereqs: enthalpy, temperature, entropy, fundamental_relation_u,
  state_function.
- Special case: at constant `T` and `P`, `ΔG ≤ 0` for a spontaneous change,
  `= 0` at equilibrium. `V = (∂G/∂P)_T`, `S = −(∂G/∂T)_P`.
- Failure: using `G` for phase / chemical equilibrium without the `μ dn` term
  (out of scope here); applying the `ΔG ≤ 0` criterion when `T, P` vary.
- Source: Callen ch. 5; Zemansky ch. 10.

## free_energy_extremum — `dF ≤ 0` at const `T, V` ; `dG ≤ 0` at const `T, P`
- Label: fundamental_law (equivalent to `dS_univ ≥ 0` for the relevant
  constraints). Equilibrium = the constrained minimum.
- Prereqs: helmholtz_free_energy, gibbs_free_energy, entropy_increase_principle,
  isothermal_process, isochoric_process, isobaric_process.
- Special case: isolated system ⇒ the criterion reduces to `dS ≥ 0`, `S` maximal.
- Failure: minimising the wrong potential for the constraints (e.g. `G` at
  constant `V`).
- Source: Callen ch. 5.

## maxwell_relations — e.g. `(∂T/∂V)_S = −(∂P/∂S)_V` , `(∂S/∂V)_T = (∂P/∂T)_V`
- Label: mathematical_identity — equality of mixed second partials of
  `U, H, F, G`.
- Prereqs: exact_differential, partial_derivative, fundamental_relation_u,
  helmholtz_free_energy, gibbs_free_energy, enthalpy.
- Special case: `(∂S/∂V)_T = (∂P/∂T)_V` turns an unmeasurable entropy derivative
  into a measurable `P-V-T` one — the practical payoff.
- Failure: sign errors from the wrong potential; applying to a non-simple system
  without adding the extra natural variables.
- Source: Callen ch. 7; Zemansky ch. 9.

## third_law_thermodynamics — `S → S₀` as `T → 0` (with `S₀ = 0` for a perfect crystal)
- Label: fundamental_law. Consequence: `c_v, c_p → 0` as `T → 0`; the absolute
  zero of temperature is unattainable in a finite number of steps.
- Prereqs: entropy, temperature.
- Special case: entropy differences between states become path-independent and
  computable from `∫ c_p/T dT` down to `T = 0`.
- Failure: assuming a glass or a system with residual configurational disorder
  reaches `S = 0`; treating "unattainable" as "approachable to any finite `T`"
  being easy.
- Source: Callen ch. 9; Zemansky ch. 10.
