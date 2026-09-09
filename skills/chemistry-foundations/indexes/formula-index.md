# Formula index (Release 0.1) — by relation

Full entries (symbols, units, assumptions, special case, failure modes, source):
`../formulas/chemistry-foundations.md`. Exactness label in the last column.
`†` = a dimensional check in `../validation/dimensional-checks.bc`; `‡` = a
kernel-checked algebra instance in `../validation/derivation-checks.lean`.

| Quantity / relation | Node | Formula | Label |
|---|---|---|---|
| Relative atomic mass | relative_atomic_mass | `A_r(X) = Σ fᵢ Aᵢ` ‡ | definition |
| Entities from amount | number_from_amount | `N = n N_A` † | derived_formula |
| Molar mass | molar_mass | `M = m / n` † | definition |
| Molar mass from formula | molar_mass_from_formula | `M = Σ (countᵢ · A_r,ᵢ)` g/mol | derived_formula |
| Amount from mass | amount_from_mass | `n = m / M` † | derived_formula |
| Percent composition | percent_composition | `%X = (countₓ · A_r,X) / M · 100` | derived_formula |
| Molecular formula | molecular_formula | `(EF)_k`, `k = M / M(EF)` ‡ | derived_formula |
| Mole ratio | mole_ratio | `n_B = n_A · (ν_B / ν_A)` | derived_formula |
| Limiting reagent | limiting_reagent | smallest `nᵢ / νᵢ` ‡ | bookkeeping_procedure |
| Theoretical yield | theoretical_yield | `n_prod = n_limiting · (ν_prod/ν_limiting)`, `m = nM` | derived_formula |
| Percent yield | percent_yield | `%yield = actual / theoretical · 100` | derived_formula |
| Molarity | molarity | `c = n / V` † | definition |
| Dilution | dilution_equation | `c₁V₁ = c₂V₂` † | derived_formula |
| Solution stoichiometry | solution_stoichiometry | `n = cV`, then mole ratio | derived_formula |
| Equivalence point | equivalence_point | `c_A = c_T V_T (ν_A/ν_T) / V_A` † | definition |
| Ideal gas law | ideal_gas_law | `P V = n R T` † | bridge_imported / constitutive_model |
| Molar volume | molar_volume | `V_m = R T / P` † | derived_formula |
| Mole fraction | mole_fraction | `xᵢ = nᵢ / n_total` | definition |
| Dalton's law | daltons_law | `P_total = Σ Pᵢ` † | empirical_law |
| Partial pressure | partial_pressure | `Pᵢ = xᵢ P_total` † | definition |
| Specific heat capacity | specific_heat_capacity | `c = q / (m ΔT)` † | definition |
| Calorimetry | calorimetry | `q = m c ΔT` † | derived_formula |
| First law | first_law_thermo | `ΔU = q − w` † | bridge_imported |
| Enthalpy | enthalpy | `H = U + P V` † | bridge_imported |
| Reaction enthalpy | enthalpy_of_reaction | `ΔH_rxn = H(products) − H(reactants)` | definition |
| Calorimetric ΔH_rxn | heat_of_reaction_calorimetry | `q_rxn = − q_calorimeter` | derived_formula |
| Hess's law | hess_law | `ΔH_rxn = Σ ΔH(steps)` ‡ | derived_exact |
| ΔH from formation | enthalpy_from_formation_enthalpies | `ΔH_rxn° = Σ n ΔH_f°(prod) − Σ n ΔH_f°(react)` †‡ | derived_exact |
| ΔH from bond enthalpies | enthalpy_from_bond_enthalpies | `ΔH_rxn ≈ Σ D(broken) − Σ D(formed)` | approximation |
| Equilibrium constant | equilibrium_constant | `K_c = Π [prod]^ν / Π [react]^ν` | definition |
| Reaction quotient | reaction_quotient | `Q` = same form, any composition | definition |
| Direction from Q vs K | q_versus_k | `Q < K` forward; `Q > K` reverse ‡ | derived_formula |
| Kp–Kc relation | kp_kc_relation | `K_p = K_c (RT / P°)^{Δn}` †‡ | derived_formula |
| Gibbs energy | gibbs_free_energy | `G = H − T S` † | bridge_imported |
| Gibbs–Helmholtz | gibbs_helmholtz_relation | `ΔG = ΔH − T ΔS` † | bridge_imported |
| Spontaneity | spontaneity_criterion | `ΔG < 0` spontaneous ‡ | derived_formula |
| Reaction isotherm | reaction_isotherm | `ΔG° = − R T ln K` †‡ | bridge_imported |
| Water autoionization | water_autoionization | `K_w = [H⁺][OH⁻] = 1.0×10⁻¹⁴` (25 °C) | derived_formula |
| pH | ph_definition | `pH = − log₁₀ ([H⁺]/c°)` | approximation |
| pOH | poh_relation | `pH + pOH = pK_w = 14.00` (25 °C) ‡ | derived_formula |
| Strong-acid pH | strong_acid_base_ph | `[H⁺] = c(acid)`, `pH = − log c` | derived_formula |
| Weak-acid constant | weak_acid_equilibrium | `K_a = [H⁺][A⁻] / [HA]` | definition |
| Ka–Kb relation | ka_kb_relation | `K_a K_b = K_w` ‡ | derived_exact |
| Percent ionization | percent_ionization | `α = ([H⁺]_eq / c(HA)₀) · 100` | derived_formula |
| Henderson–Hasselbalch | henderson_hasselbalch | `pH = pK_a + log₁₀([A⁻] / [HA])` ‡ | derived_formula |
| Formal charge | formal_charge | `FC = V − N_lone − ½ N_bond` ‡ | derived_formula |
| Redox balancing | balancing_redox_half_reactions | electrons lost = electrons gained; mass + charge balanced ‡ | bookkeeping_procedure |

## Qualitative / bookkeeping nodes (no single formula)
periodic_law · periodic_trends · balancing_chemical_equations · titration ·
standard_conditions_stp · gas_stoichiometry · standard_state ·
standard_enthalpy_of_formation · bond_enthalpy · law_of_mass_action ·
heterogeneous_equilibrium · le_chatelier · ice_table · arrhenius_acid_base ·
bronsted_lowry · conjugate_acid_base_pair · buffer · acid_base_titration_curve ·
oxidation_number_rules · oxidation_reduction · oxidizing_reducing_agent ·
half_reaction · ionic_bond · covalent_bond · octet_rule · lewis_structure ·
vsepr · bond_polarity · molecular_polarity · intermolecular_forces
