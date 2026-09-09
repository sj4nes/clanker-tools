# Assumption / regime index (Release 0.1)

Each regime node below is a first-class graph node; every node listed
under it names it as a **direct** prerequisite edge, so applying that
node outside the regime is a visible graph violation. Source:
`indexes/reverse-dependencies.txt` (regenerate with `build/build-tree.sh`
then `build/gen-assumption-index.sh`).

## `dilute_ideal_solution` (type: assumption)
Solute–solute interactions negligible; activity ≈ concentration / c°.
Direct dependents:
  - equilibrium_constant
  - ph_definition

**Transitive reach:** through `equilibrium_constant` and
`ph_definition` this assumption also underlies every downstream
equilibrium and acid–base node — `reaction_quotient`, `q_versus_k`,
`kp_kc_relation`, `water_autoionization`, `weak_acid_equilibrium`,
`ka_kb_relation`, `henderson_hasselbalch`, `strong_acid_base_ph`,
`poh_relation`, `ice_table`, `percent_ionization`, `buffer`,
`acid_base_titration_curve`, `reaction_isotherm`. Debye–Hückel and
non-ideal solution theory are out of scope (`scope.md`).

## `ideal_gas` (embedded in `ideal_gas_law`, not yet a node)
Point molecules, no intermolecular forces; the low-`P`, high-`T` limit.
`ideal_gas_law` is `bridge_imported` and carries this assumption in its
entry prose. Direct dependents of `ideal_gas_law`:
  - daltons_law
  - gas_stoichiometry
  - kp_kc_relation
  - molar_volume
  - standard_conditions_stp

Promoting `ideal_gas` to its own node is a Release 0.2 item
(`validation/consistency-audit.md`).

## `heat_work_sign_convention` (type: convention) — `ΔU = q − w`
  - first_law_thermo
  - heat_of_reaction_calorimetry
  - specific_heat_capacity

## `standard_state` (type: convention) — `P° = 1 bar`, solutes `1 mol/L`
  - gibbs_free_energy
  - reaction_isotherm
  - standard_enthalpy_of_formation

## `standard_conditions_stp` (type: convention) — IUPAC STP, `1 bar`
A leaf reference node (no direct dependents); used when reading a molar
volume off `molar_volume` at STP. Note the 1 bar vs 1 atm split.

## `dimensional_analysis` (type: convention) — `[M L T Θ N]` bookkeeping
  - ideal_gas_law
