# Scope — Release 0.1

Scope signed off 2026-09-09. Three boundary calls confirmed: the H₂/O₂ **fuel
cell** is one node ("the electrolyser run backwards"), no fuel-cell engineering;
**corrosion** is one boundary node (a short-circuited galvanic cell; Pourbaix
named); **non-flow batteries** (lead-acid, Li-ion) are one contrast node, no
cell chemistry.

Knowledge capsule: **electrochemistry for making substances and storing energy**,
built with the [`physics-formula-tree`](../physics-formula-tree/SKILL.md) method
(adapted, as [`chemistry-foundations`](../chemistry-foundations/SKILL.md) was:
half-reactions, cells, and named production processes are first-class nodes; a
table of standard electrode potentials is a cited reference the graph draws on,
not derived).

Two applied targets shape the selection:

1. **Electrosynthesis / production electrolysis** — the charge → moles-of-electrons
   → mass bookkeeping (Faraday's laws), current efficiency, specific energy
   consumption, overpotential, and product selectivity, worked through named
   processes: water electrolysis, chlor-alkali, chlorate/perchlorate,
   Hall–Héroult aluminium, copper electrorefining, electrowinning.
2. **Redox flow batteries** — the cell/stack/tank architecture, the decoupling of
   energy capacity from power, state of charge, the coulombic / voltage / energy
   efficiencies, crossover and capacity fade, and the all-vanadium system.

Intended, like `chemistry-foundations`, as a verified substrate for a later
**synthesis / process capsule** for the homesteading / self-sufficiency project
— electrosynthesis is a large part of "how to make X from air, water, salt, and
electricity".

## Assumed / imported

Builds directly on `chemistry-foundations` (Release 0.1) — imported as
`bridge_imported` nodes, not re-derived:

- `half_reaction`, `balancing_redox_half_reactions`, `oxidation_reduction`,
  `oxidation_number_rules`, `oxidizing_reducing_agent`
- `amount_of_substance`, `molar_mass`, `mole_ratio`, `molarity`
- `equilibrium_constant`, `reaction_quotient`, `reaction_isotherm`
  (`ΔG° = −RT ln K`), `standard_state`, `dilute_ideal_solution`
- `ideal_gas_law`, `molar_volume` (for gaseous products: H₂, O₂, Cl₂)

From [`physics-thermodynamics`](../physics-thermodynamics/SKILL.md):
`gibbs_free_energy`, `entropy` (the temperature coefficient `dE/dT = ΔS / zF`).

Electrical primitives — **charge, current, potential difference, electrical work,
electrical power, Ohm's law** — are taken as given (a small root set; a future
`physics-circuits` capsule would supply them properly). SI adds **electric
current `I`** as a base dimension here (basis `[M L T Θ N I]`).

## Included

- **Charge and the Faraday constant.** `Q = I t` (constant current) / `Q = ∫I dt`;
  the Faraday constant `F = 96485 C/mol` (`= N_A · e`); the electron-mole bridge
  `Q = z F n`, with `z` the electrons transferred per formula unit.
- **Electrochemical cells.** Electrode, electrolyte, the anode/cathode definition
  **by half-reaction** (oxidation at the anode, reduction at the cathode) not by
  terminal sign; cell notation; salt bridge / porous separator / ion-exchange
  membrane; galvanic (spontaneous) vs electrolytic (driven) cells.
- **Electrode potential.** The standard hydrogen electrode reference
  (`E°(SHE) ≡ 0`); the standard reduction potential `E°` as a `reference_data`
  table; the electrochemical (activity) series; why a more positive `E°` means a
  stronger oxidant.
- **Cell potential and thermodynamics.** `E°_cell = E°_cathode − E°_anode`
  (both reduction potentials); spontaneity (`E°_cell > 0` galvanic, `< 0`
  requires an external source); `ΔG = −z F E` and `ΔG° = −z F E° = −R T ln K`
  (the bridge to `chemistry-foundations`' reaction isotherm); the temperature
  coefficient `(∂E/∂T)_P = ΔS / zF`.
- **The Nernst equation.** `E = E° − (R T / z F) ln Q`; the `0.05916 V / z` per
  decade form at 298.15 K; concentration cells; how `E` drifts as a battery
  discharges (`Q → K`, `E → 0`).
- **Faraday's laws of electrolysis.** `m = (Q / F)(M / z) = (I t M) / (z F)`;
  moles of product per mole of electrons; gas volume via the ideal-gas law.
  **Current (Faradaic) efficiency** `η_F = m_actual / m_theoretical`. **Specific
  energy consumption** `E_spec = z F V_cell / (M η_F)` (J/kg, quoted as kWh/kg or
  kWh/t).
- **Why real electrolysis costs more than `E°_cell`.** The decomposition
  potential; **overpotential** `η` split into activation, concentration, and
  ohmic (`IR`) contributions; `V_cell = E°_cell + Σ|η| + I R`; the exchange
  current density `j₀` and Tafel slope named as the parameters `η_act` depends
  on (Butler–Volmer **stated, not derived** — a boundary node).
- **Product selectivity.** Competing electrode reactions; the thermodynamic vs
  kinetic product (the chlor-alkali anode gives Cl₂ not O₂ because of oxygen
  overpotential); electrode material and electrolyte choice; the role of a
  supporting electrolyte.
- **Electrolyte transport.** Molar conductivity `Λ_m`; ionic mobility `u`;
  transport (transference) number `t_i`; migration vs diffusion; Kohlrausch's law
  of independent ionic migration (empirical); `Λ_m° = ν_+ λ_+° + ν_− λ_−°`.
- **Named production processes** (as `example` nodes, each carrying its
  half-reactions, `z`, `E°_cell`, a typical `V_cell` and `η_F`, and the specific
  energy): water electrolysis (alkaline / PEM), chlor-alkali (membrane cell),
  sodium chlorate and perchlorate, Hall–Héroult aluminium (molten cryolite),
  copper electrorefining, zinc electrowinning.
- **Redox flow batteries.** The architecture (two electrolyte reservoirs, pumps,
  a stack of cells with an ion-exchange membrane, inert carbon/felt electrodes);
  **energy–power decoupling** — energy capacity `= c V_tank z F ΔE_avg` set by
  tank size and concentration, power `= A_stack j V_cell` set by stack area;
  **state of charge**; **coulombic efficiency** `η_C`, **voltage efficiency**
  `η_V`, **energy (round-trip) efficiency** `η_E = η_C η_V`; shunt (bypass)
  currents; capacity fade from ion crossover and oxidation-state imbalance;
  the all-vanadium system (`VO₂⁺/VO²⁺` positive, `V³⁺/V²⁺` negative — one element
  on both sides to survive crossover); iron–chromium and zinc–bromine as
  contrasts.

## Excluded

- **Electrode microkinetics.** The Butler–Volmer equation, Tafel analysis,
  Marcus theory, the transfer coefficient's meaning — **stated as boundary nodes
  only**. `j₀` and the Tafel slope are named; their derivation is a future
  `electrode-kinetics` capsule.
- **The electrical double layer** — Helmholtz / Gouy–Chapman / Stern models,
  zeta potential, electrocapillarity, differential capacitance.
- **Semiconductor and photoelectrochemistry** — band bending, the
  semiconductor–electrolyte junction, dye-sensitised and photocatalytic water
  splitting, photovoltage.
- **Corrosion engineering** — Pourbaix (E–pH) diagrams beyond naming them,
  galvanic-series design for alloys, passivation kinetics, cathodic-protection
  sizing.
- **Analytical electrochemistry as methods** — cyclic voltammetry, chronoamperometry,
  rotating-disk electrodes, electrochemical impedance spectroscopy (named, not
  developed).
- **Non-flow batteries in depth** — lead-acid, Li-ion, NiMH, solid-state; used
  only as a contrast to the flow architecture.
- **Fuel-cell engineering** — hydrogen electrolysis and the reversible cell are
  in; catalyst-loading optimisation, membrane humidification, gas-diffusion-layer
  and bipolar-plate design, and stack thermal management are out.
- **Molten-salt and non-aqueous electrochemistry** beyond stating that the
  Faraday bookkeeping is identical (Hall–Héroult is kept as an `example` node
  with its molten-cryolite half-reactions, not a solvent-theory treatment).
- **Bioelectrochemistry**, microbial fuel cells, supercapacitors and
  pseudocapacitance, electrokinetic phenomena (electrophoresis, electro-osmosis).
- **The derivation of `ΔG = ΔH − TΔS` and `ΔG° = −RT ln K`** — imported from
  `physics-thermodynamics` / `chemistry-foundations`.
- **Activity coefficients / non-ideal electrolytes** — every `E`, `Q`, `K`, and
  `Λ_m` expression carries `dilute_ideal_solution`; Debye–Hückel–Onsager
  conductivity is named, not used.

## Conventions

- **Math level:** algebra, natural and base-10 logarithms, `I = dQ/dt` and
  `Q = ∫I dt` as a rate/accumulation pair, ratios and proportion. No differential
  equations, no vector calculus. The Nernst `0.05916 V` form is the base-10
  shortcut at 298.15 K.
- **Dimensional basis:** `[M L T Θ N I]` — mass, length, time, temperature,
  amount of substance, **electric current** (SI base). Charge is `I T`; potential
  is `M L² T⁻³ I⁻¹`; `F` is `I T N⁻¹`.
- **Electrode sign convention:** all tabulated potentials are **standard
  reduction potentials** versus the SHE (`E°(SHE) ≡ 0` at all `T`). **Anode =
  oxidation, cathode = reduction**, independent of which terminal is `+` (the
  cathode is `+` in a galvanic cell, `−` in an electrolytic cell).
  `E°_cell = E°_cathode − E°_anode`.
- **`z`** is the number of electrons transferred per formula unit of the cell
  reaction *as written* (dimensionless); scaling the equation scales `z` and
  `ΔG` together but leaves `E` unchanged (`E` is intensive).
- **Free-energy sign:** `ΔG = −z F E`; `E > 0 ⇔ ΔG < 0 ⇔ spontaneous as written`.
- **Overpotential:** `η = E_applied − E_equilibrium` at an electrode; `|η|`
  always *adds* to the voltage an electrolyser must supply and *subtracts* from
  the voltage a battery delivers. `V_cell(electrolysis) = E°_cell + |η_a| +
  |η_c| + I R`.
- **Standard state:** unit activity (≈ `1 mol/L`, `1 bar`), `T = 298.15 K` unless
  stated; `dilute_ideal_solution` (activity ≈ concentration) on every `E` / `Q` /
  `K` / `Λ_m` expression.
- **Efficiencies:** coulombic `η_C = Q_out / Q_in`; voltage
  `η_V = V_discharge / V_charge` (at a stated current); energy
  `η_E = η_C η_V`. Faradaic (current) efficiency of a synthesis
  `η_F = n_product,actual / n_product,theoretical`.

## Release boundary in one line

Charge ↔ moles of electrons (Faraday) → half-reactions and standard potentials →
`E°_cell` and `ΔG = −zFE` → the Nernst equation → Faraday's laws with current
efficiency and specific energy → overpotential and product selectivity → named
production processes → redox flow batteries with decoupled energy/power and the
three efficiencies. Electrode microkinetics, the double layer, photo- and
semiconductor electrochemistry, corrosion engineering, and non-flow batteries
are out.
