# Minimal prerequisite paths (Release 0.1)

Derived from the graph structure (transitive closure of
`edges/dependencies.edges`), not from the flat `tsort` order. Each list is the
full set of nodes that must be understood first; within a list the
`tsort-order.txt` order applies. `[A]` marks an assumption / regime /
convention node — required, but not "learned". `[imp]` marks a
`bridge_imported` node (derivation lives in `physics-thermodynamics`).

These seven targets are the recommended tutorial cuts (see the repo's
`docs/tutorial-map.md`); the first is the recommended first tutorial.

## enthalpy_from_formation_enthalpies — `ΔH_rxn° = Σ n ΔH_f°(prod) − Σ n ΔH_f°(react)`
si_units · summation_notation · ratio_proportion ·
atom → atomic_structure → atomic_number → element ·
avogadro_constant → amount_of_substance ·
ion · chemical_substance → chemical_formula ·
chemical_reaction → chemical_equation ·
conservation_of_mass · conservation_of_charge · stoichiometric_coefficient →
balancing_chemical_equations → mole_ratio ·
[A] system_surroundings · [A] heat_work_sign_convention · state_function ·
[imp] internal_energy → [imp] first_law_thermo → [imp] enthalpy ·
enthalpy_of_reaction · [A] standard_state ·
hess_law · standard_enthalpy_of_formation
→ **enthalpy_from_formation_enthalpies**
Do-not-use if: physical states of products/reactants not matched to the table;
coefficient weights dropped; temperature far from 298.15 K. `bc` + Lean checks.

## percent_yield — `%yield = actual / theoretical · 100`
si_units · summation_notation · ratio_proportion ·
atom → atomic_structure → atomic_number → element ·
atomic_mass_unit · isotope · isotopic_abundance → relative_atomic_mass ·
avogadro_constant → amount_of_substance ·
molar_mass → amount_from_mass ·
ion · chemical_substance → chemical_formula → molar_mass_from_formula ·
chemical_reaction → chemical_equation ·
conservation_of_mass · conservation_of_charge · stoichiometric_coefficient →
balancing_chemical_equations → mole_ratio →
limiting_reagent → theoretical_yield
→ **percent_yield**
Do-not-use if: theoretical value taken off the excess reagent; actual (mass)
compared to a theoretical mole figure; `> 100 %` read as a real excess.

## ice_table — tabulate Initial/Change/Equilibrium, substitute into `K`, solve for `x`
si_units · quadratic_formula ·
atom → atomic_structure → atomic_number → element ·
avogadro_constant → amount_of_substance ·
chemical_substance → chemical_formula ·
chemical_reaction → chemical_equation · stoichiometric_coefficient ·
solution → molarity · reversible_reaction → dynamic_equilibrium ·
[A] dilute_ideal_solution ·
law_of_mass_action → equilibrium_constant → reaction_quotient
→ **ice_table**
Do-not-use if: small-`x` approximation applied when `x / c₀ ≥ 0.05`; negative
root kept; reaction direction not fixed from `Q` vs `K` first.

## henderson_hasselbalch — `pH = pK_a + log₁₀([A⁻] / [HA])`
everything under **ice_table**, plus:
logarithm · arrhenius_acid_base → bronsted_lowry ·
water_autoionization · ph_definition ·
weak_acid_equilibrium
→ **henderson_hasselbalch**
Do-not-use if: `[HA]` or `[A⁻]` comparable to `[H⁺]`, or buffer very dilute
(the `[HA]_eq ≈ [HA]_0` approximation fails); outside `pK_a ± 1`. Lean check.

## reaction_isotherm — `ΔG° = − R T ln K` `[imp]`
si_units · logarithm ·
atom → atomic_structure → atomic_number → element ·
avogadro_constant → amount_of_substance ·
[A] system_surroundings · [A] heat_work_sign_convention · state_function ·
[imp] internal_energy → [imp] first_law_thermo → [imp] enthalpy ·
[A] standard_state · [imp] gibbs_free_energy ·
chemical_substance → chemical_formula · chemical_reaction → chemical_equation ·
solution → molarity · reversible_reaction → dynamic_equilibrium ·
[A] dilute_ideal_solution · stoichiometric_coefficient ·
law_of_mass_action → equilibrium_constant
→ **reaction_isotherm**
Do-not-use if: `log₁₀` used for `ln`; `T` in °C; `K` still carries units.
Imported — the ΔG machinery is not re-derived here. Lean check.

## gas_stoichiometry — combine `PV = nRT` with the balanced-equation mole ratio
si_units · ratio_proportion · dimensional_analysis · gas_constant ·
atom → atomic_structure → atomic_number → element ·
avogadro_constant → amount_of_substance ·
[A] ideal_gas (embedded in ideal_gas_law) · [imp] ideal_gas_law ·
ion · chemical_substance → chemical_formula ·
chemical_reaction → chemical_equation ·
conservation_of_mass · conservation_of_charge · stoichiometric_coefficient →
balancing_chemical_equations → mole_ratio
→ **gas_stoichiometry**
Do-not-use if: the volume-ratio shortcut is applied when `T` or `P` differ
between measurements, or to non-gaseous species; °C used in `RT`.

## balancing_redox_half_reactions — balance each half, scale to equal electrons, add
atom → atomic_structure → atomic_number → element → periodic_table →
periodic_law → periodic_trends → electronegativity ·
ion · chemical_substance → chemical_formula ·
chemical_reaction → chemical_equation ·
conservation_of_mass · conservation_of_charge · stoichiometric_coefficient →
balancing_chemical_equations ·
oxidation_number_rules → oxidation_reduction → half_reaction
→ **balancing_redox_half_reactions**
Do-not-use if: electrons remain in the final equation; H⁺ not cleared for a
basic-solution answer; net charge unequal after adding the halves. Lean check.
