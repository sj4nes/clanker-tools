# Topic index (Release 0.1)

Browse the 110 nodes by sub-domain. Full statements:
`../formulas/electrochemistry.md`. One valid prerequisite order:
`tsort-order.txt`. Minimal chains for the headline results:
`prerequisite-paths.md`.

**Bold** = a quantitative relation with a dimensional or arithmetic check in
`../validation/`. `[imp]` = a `bridge_imported` node (derivation lives in
`chemistry-foundations` or `physics-thermodynamics`). `[bd]` = a boundary node
(named / stated, not developed). `[A]` = a first-class assumption.

## Electrical primitives (root set — a future physics-circuits capsule)
electric_charge · elementary_charge · electric_current · electric_potential ·
electrical_work · electrical_power · resistance · ohms_law

## Imported bridges
avogadro_constant `[imp]` · amount_of_substance `[imp]` · molar_mass `[imp]` ·
mole_ratio `[imp]` · molarity `[imp]` · standard_state `[imp]` ·
dilute_ideal_solution `[A]` · ideal_gas_law `[imp]` · molar_volume `[imp]` ·
gas_constant · oxidation_reduction `[imp]` · oxidation_number_rules `[imp]` ·
oxidizing_reducing_agent `[imp]` · half_reaction `[imp]` ·
balancing_redox_half_reactions `[imp]` · gibbs_free_energy `[imp]` ·
entropy `[imp]` · reaction_quotient `[imp]` · equilibrium_constant `[imp]` ·
reaction_isotherm `[imp]`

## Faraday — charge ↔ moles of electrons ↔ mass
**faraday_constant** · **charge_from_current** · electrons_per_formula_unit ·
**charge_mole_electron_bridge** · **faradays_law_electrolysis** ·
**moles_of_product_electrolysis** · **gas_volume_electrolysis** ·
current_efficiency · **specific_energy_consumption**

## Electrochemical cells
electrolyte · electrode · electrochemical_cell · anode · cathode · salt_bridge ·
ion_exchange_membrane · cell_notation · galvanic_cell · electrolytic_cell

## Electrode potentials
standard_hydrogen_electrode · standard_reduction_potential ·
electrochemical_series · **cell_potential** · **standard_cell_potential** ·
spontaneity_from_cell_potential

## The thermodynamic bridge
**gibbs_from_cell_potential** · **standard_gibbs_from_cell_potential** ·
**equilibrium_from_cell_potential** · **temperature_coefficient_emf**

## The Nernst equation
**nernst_equation** · **nernst_298k_form** · **concentration_cell** ·
cell_potential_vs_soc

## Kinetics and the real cell voltage
**current_density** · overpotential · activation_overpotential ·
concentration_overpotential · **ohmic_drop** ·
**butler_volmer_equation** `[bd]` · exchange_current_density ·
**tafel_equation** · decomposition_potential ·
**cell_voltage_electrolysis** · **cell_voltage_discharge**

## Product selectivity
competing_electrode_reactions · thermodynamic_vs_kinetic_product ·
oxygen_overpotential · electrode_material_selection · supporting_electrolyte

## Electrolyte transport
ionic_conduction · conductivity · **molar_conductivity** · **kohlrausch_law** ·
ionic_mobility · **transport_number** · migration_vs_diffusion

## Named production processes
water_electrolysis · reversible_fuel_cell · chlor_alkali_process ·
chlorate_perchlorate · hall_heroult_process · copper_electrorefining ·
zinc_electrowinning

## Redox flow batteries
redox_flow_battery · energy_power_decoupling · **flow_battery_energy_capacity** ·
**flow_battery_power** · state_of_charge · coulombic_efficiency ·
voltage_efficiency · **energy_efficiency** · shunt_current · crossover ·
capacity_fade · all_vanadium_flow_battery · iron_chromium_flow_battery ·
zinc_bromine_flow_battery · fixed_cell_battery_contrast

## Boundary nodes (named, not developed)
corrosion_as_galvanic_cell `[bd]` · pourbaix_diagram `[bd]` ·
electrical_double_layer `[bd]` · debye_huckel_onsager `[bd]`
