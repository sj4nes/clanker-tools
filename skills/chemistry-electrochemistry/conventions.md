# Conventions and foundational choices — Release 0.1 (draft)

## Notation

- `Q` — electric charge, C (coulomb). `I` — electric current, A. `t` — time, s.
  `Q = I t` at constant current; `Q = ∫ I dt` in general.
- `F` — the Faraday constant, `96485.332 C/mol` (`= N_A e`). `e` — elementary
  charge, `1.602176634×10⁻¹⁹ C` (exact, 2019 SI).
- `z` — number of electrons transferred per formula unit of the cell (or
  half-) reaction *as written*; dimensionless positive integer.
- `n` — amount of substance, mol (imported from `chemistry-foundations`).
  `Q = z F n` links charge to moles of the reacting species.
- `E` — electrode or cell potential, V. `E°` — standard potential (unit
  activity, 1 bar, stated `T`). `E°_cell = E°_cathode − E°_anode`.
- `η` (eta) — overpotential, V: `η = E_applied − E_equilibrium` at one
  electrode. `η_act`, `η_conc`, `η_ohmic` its activation / concentration /
  ohmic parts. Distinct from the efficiencies `η_C`, `η_V`, `η_E`, `η_F` below
  (context disambiguates; the efficiencies are dimensionless ratios in `[0, 1]`).
- `V_cell` — the actual terminal voltage under current (≠ `E_cell` at
  equilibrium).
- `j` — current density, A/m² (`= I / A_electrode`). `j₀` — exchange current
  density.
- `Λ_m` — molar conductivity, S m² mol⁻¹. `λ_i°` — limiting molar ionic
  conductivity of ion `i`. `u_i` — ionic mobility, m² V⁻¹ s⁻¹. `t_i` —
  transport (transference) number, dimensionless, `Σ t_i = 1`.
- `SOC` — state of charge of a battery, dimensionless `[0, 1]`.
- Efficiencies: `η_C = Q_out/Q_in` (coulombic); `η_V = V_discharge/V_charge`
  (voltage, at a stated current); `η_E = η_C η_V` (energy / round-trip);
  `η_F = n_actual/n_theoretical` (Faradaic / current efficiency of a synthesis).

## Dimensional basis

`[M L T Θ N I]` — mass, length, time, temperature, amount of substance, and
**electric current `I`** (the SI base electrical quantity). Derived:

| quantity | dimension |
|---|---|
| charge `Q` | `I T` |
| potential `E`, `V` | `M L² T⁻³ I⁻¹` |
| Faraday constant `F` | `I T N⁻¹` |
| energy `z F E` | `M L² T⁻²` |
| current density `j` | `I L⁻²` |
| molar conductivity `Λ_m` | `I² T³ M⁻¹ L⁻² N⁻¹` |
| ionic mobility `u` | `I T² M⁻¹` |

`z`, `Q/(zF n)`, `t_i`, `SOC`, and every efficiency are dimensionless.

## Sign conventions

- **Reduction potentials.** Every tabulated `E°` is a *reduction* potential
  versus the standard hydrogen electrode, `E°(SHE) ≡ 0` (taken as exact at every
  temperature in this capsule). A more positive `E°` = a stronger oxidising
  agent = a species more easily reduced.
- **Anode / cathode by reaction, not by sign.** Oxidation occurs at the anode;
  reduction at the cathode — always. The terminal polarity is a *consequence*:
  the cathode is the `+` terminal of a galvanic (discharging) cell and the `−`
  terminal of an electrolytic (driven) cell.
- **`E°_cell = E°_cathode − E°_anode`**, both inserted as reduction potentials.
  `E°_cell > 0` ⇒ the reaction is spontaneous as written (galvanic);
  `E°_cell < 0` ⇒ it must be driven (electrolytic), and `|E°_cell|` is the
  reversible (thermodynamic minimum) decomposition voltage.
- **`ΔG = −z F E`.** `E > 0 ⇔ ΔG < 0 ⇔ spontaneous`. Consistent with
  `chemistry-foundations` `spontaneity_criterion` and `physics-thermodynamics`.
- **Overpotential adds work.** `|η|` at each electrode *raises* the voltage an
  electrolyser must supply and *lowers* the voltage a battery delivers:
  `V_cell(electrolysis) = E°_cell + |η_anode| + |η_cathode| + I R_cell`;
  `V_cell(discharge)   = E°_cell − |η_anode| − |η_cathode| − I R_cell`.
- **Current direction.** Conventional current; `I > 0` in the external circuit
  flows cathode → anode inside the source's convention. Electrons flow anode →
  cathode through the external wire.

## Standard state and regime

- Standard state: unit activity (≈ `1 mol/L` for solutes, `1 bar` for gases,
  pure solids/liquids as themselves), `T = 298.15 K` unless a node states
  otherwise. `E°` values are at 298.15 K.
- **`dilute_ideal_solution`** (imported): activity ≈ concentration. Carried by
  every `E`, `Q`, `K`, and `Λ_m` expression. Debye–Hückel–Onsager corrections
  are named, not applied.
- Gases produced at an electrode are treated as ideal (`ideal_gas_law`,
  imported) for volume bookkeeping.

## Imported (bridge) nodes — not derived here

| node(s) | imported from | used for |
|---|---|---|
| `half_reaction`, `balancing_redox_half_reactions`, `oxidation_reduction`, `oxidation_number_rules` | `chemistry-foundations` | the electrode reactions |
| `amount_of_substance`, `molar_mass`, `mole_ratio`, `molarity` | `chemistry-foundations` | Faraday mass/volume bookkeeping |
| `equilibrium_constant`, `reaction_quotient`, `reaction_isotherm` (`ΔG° = −RT ln K`), `standard_state`, `dilute_ideal_solution` | `chemistry-foundations` | Nernst, `E°`–`K` link |
| `ideal_gas_law`, `molar_volume` | `chemistry-foundations` | gas-product volumes |
| `gibbs_free_energy`, `entropy` | `physics-thermodynamics` | `ΔG = −zFE`, `∂E/∂T = ΔS/zF` |
| `electric_charge`, `electric_current`, `electric_potential`, `electrical_work`, `electrical_power`, `ohms_law` | electrical primitives (future `physics-circuits`) | the electrical side |

## Foundational primitive choices

- **Electrical primitives are a root set.** `electric_charge`, `electric_current`
  (`I = dQ/dt`), `electric_potential` (work per unit charge), `electrical_work`
  (`W = Q ΔV`), `electrical_power` (`P = I V`), and `ohms_law` (`V = I R`) are
  taken as given, with an operational sentence each. A future `physics-circuits`
  capsule would derive them; here they anchor the electrical side the way
  `chemistry-foundations` anchors atoms and the mole.
- **The Faraday constant is a defined bridge.** `F = N_A e` follows from the 2019
  SI fixed values; it is the single constant that turns "coulombs through the
  cell" into "moles of electrons".
- **The SHE is the potential zero.** `E°(SHE) ≡ 0` is a convention, not a
  measurement; every `E°` is a difference from it.
- **Butler–Volmer is a boundary node.** Overpotential's *existence* and its
  additive effect on `V_cell` are in scope; the current–overpotential law
  `j = j₀[exp(αzFη/RT) − exp(−(1−α)zFη/RT)]` is stated with a "not derived here"
  status. Its parameters `j₀` and `α` (or the Tafel slope) are named as
  `reference_data` per electrode couple.

## Topological order ≠ teaching order ≠ discovery order

`indexes/tsort-order.txt` (once generated) is one valid prerequisite-respecting
linearization. Independent nodes fall in an arbitrary tie order; conceptual
priority, historical order, and lab-course order are all separate.
