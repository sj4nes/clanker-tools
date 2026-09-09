# Minimal prerequisite paths (Release 0.1)

Derived from the graph structure (transitive closure of
`edges/dependencies.edges`), not from the flat `tsort` order. Each list is the
full set of nodes that must be understood first; within a list the
`tsort-order.txt` order applies. `[imp]` = a `bridge_imported` node; `[A]` =
an assumption; `[bd]` = a boundary node. `[root]` = an electrical primitive
(a future `physics-circuits` capsule).

These seven targets are the recommended tutorial cuts, shaped by the capsule's
two applied aims — **making substances** and **flow batteries**. The
electrical primitives (`electric_charge` → `electric_current` /
`electric_potential` / `electrical_work` / `electrical_power` /
`resistance` → `ohms_law`) and the `chemistry-foundations` / `physics-
thermodynamics` imports are prerequisites of *every* path below; a tutorial
names them once as "assumed" and starts from `faraday_constant`.

## faradays_law_electrolysis — `m = I t M / (z F)` (how much product per amp-hour)
[root] electrical primitives ·
[imp] avogadro_constant · [imp] amount_of_substance · [imp] molar_mass ·
[imp] mole_ratio · [imp] oxidation_reduction · [imp] oxidation_number_rules ·
[imp] half_reaction ·
elementary_charge → faraday_constant · charge_from_current ·
electrons_per_formula_unit · charge_mole_electron_bridge
→ **faradays_law_electrolysis**
Then → `moles_of_product_electrolysis` → `gas_volume_electrolysis`;
→ `current_efficiency`.
Do-not-use if: `z` taken from an unbalanced half-reaction; `M` of the atom where
a molecule (H₂, Cl₂) is the product.

## specific_energy_consumption — `E_spec = z F V_cell / (M η_F)` (what the electricity costs)
everything under **faradays_law_electrolysis**, plus:
[imp] gibbs_free_energy · [imp] reaction_isotherm · [A] dilute_ideal_solution ·
electrolyte · electrode → electrochemical_cell → anode / cathode ·
standard_hydrogen_electrode → standard_reduction_potential → cell_potential →
standard_cell_potential → spontaneity_from_cell_potential → electrolytic_cell ·
gibbs_from_cell_potential → nernst_equation → overpotential →
activation_overpotential / concentration_overpotential ·
ohms_law → ohmic_drop ·
ionic_conduction → ionic_mobility → transport_number → migration_vs_diffusion ·
cell_voltage_electrolysis · current_efficiency
→ **specific_energy_consumption**
Do-not-use if: `E°_cell` is used for `V_cell` (halves the answer); `η_F` omitted.
Worked example in the entry: aluminium, ≈ 13–15 kWh/kg.

## water_electrolysis — `2H₂O → 2H₂ + O₂` (making hydrogen and oxygen)
everything under **specific_energy_consumption**, plus:
[imp] ideal_gas_law → [imp] molar_volume · gas_volume_electrolysis ·
oxygen_overpotential
→ **water_electrolysis**
Then → `reversible_fuel_cell` (the same cell discharging).
Do-not-use if: `1.23 V` is taken as achievable — the O₂ overpotential pushes a
real cell to ≈ 1.9 V.

## chlor_alkali_process — `2NaCl + 2H₂O → Cl₂ + H₂ + 2NaOH` (Cl₂ vs O₂ selectivity)
everything under **specific_energy_consumption**, plus:
salt_bridge → ion_exchange_membrane ·
competing_electrode_reactions → thermodynamic_vs_kinetic_product ·
oxygen_overpotential
→ **chlor_alkali_process**
Then → `chlorate_perchlorate`.
Do-not-use if: the product is predicted from the `E°` table alone — `E°(O₂) <
E°(Cl₂)` but the DSA anode's oxygen overpotential makes Cl₂ the product.

## nernst_equation — `E = E° − (RT/zF) ln Q` (the potential of a real mixture)
[root] electrical primitives ·
[imp] oxidation_reduction · [imp] half_reaction · [imp] gibbs_free_energy ·
[imp] reaction_quotient · [imp] reaction_isotherm · [imp] standard_state ·
[imp] molarity · [A] dilute_ideal_solution ·
elementary_charge → faraday_constant · gas_constant ·
electrons_per_formula_unit ·
electrolyte · electrode → electrochemical_cell → anode / cathode ·
standard_hydrogen_electrode → standard_reduction_potential → cell_potential →
standard_cell_potential · gibbs_from_cell_potential
→ **nernst_equation**
Then → `nernst_298k_form`, `concentration_cell`, `cell_potential_vs_soc`,
`overpotential`.
Do-not-use if: `Q` has the wrong stoichiometric exponents; a half-reaction `z`
is used where the cell `z` is meant; away from the dilute limit.

## all_vanadium_flow_battery — `VO₂⁺/VO²⁺ ‖ V³⁺/V²⁺`, `E°_cell ≈ 1.26 V`
everything under **nernst_equation** and **specific_energy_consumption**, plus:
galvanic_cell · ion_exchange_membrane ·
redox_flow_battery · energy_power_decoupling (implied) ·
current_density · cell_voltage_discharge · cell_voltage_electrolysis ·
crossover · shunt_current · coulombic_efficiency · voltage_efficiency →
energy_efficiency
→ **all_vanadium_flow_battery**
Then → `iron_chromium_flow_battery`, `zinc_bromine_flow_battery`.
Do-not-use if: run outside ≈ 10–40 °C, or the positive side above ≈ 1.6 V.

## energy_efficiency — `η_E = η_C η_V` (round-trip efficiency of a flow battery)
everything under **nernst_equation**, plus:
current_density · ohms_law → ohmic_drop · overpotential →
activation_overpotential / concentration_overpotential ·
cell_voltage_electrolysis (charge) · cell_voltage_discharge (discharge) ·
galvanic_cell · ion_exchange_membrane → redox_flow_battery ·
transport_number → crossover · shunt_current ·
coulombic_efficiency · voltage_efficiency
→ **energy_efficiency**
Then → `flow_battery_energy_capacity` (sizing the tanks),
`flow_battery_power` (sizing the stack).
Do-not-use if: the stack figure is reported as the system round-trip (omitting
pump, shunt, and standby self-discharge losses).
