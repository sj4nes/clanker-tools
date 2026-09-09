# Assumption / regime / convention index (Release 0.1)

Each node below governs how a relation may be used; every node listed
under it names it as a **direct** prerequisite edge. Source:
`indexes/reverse-dependencies.txt` (regenerate with `build/build-tree.sh`
then `build/gen-assumption-index.sh`).

## `dilute_ideal_solution` (type: assumption, imported)
Activity approximated by concentration. Direct dependents:
  - debye_huckel_onsager
  - kohlrausch_law
  - nernst_equation

**Transitive reach:** every `E`, `Q`, `K`, and `Lambda_m` expression
in the capsule rests on this. It fails first for the multiply-charged
ions at flow-battery concentrations (1-2 M) -- real cells use empirical
corrections. Debye-Huckel-Onsager (`debye_huckel_onsager`) is the named
conductivity correction; it is not applied.

## `standard_state` (convention, imported) -- unit activity, 1 bar, 298.15 K
  - standard_cell_potential
  - standard_hydrogen_electrode

## `standard_hydrogen_electrode` (convention) -- E0(SHE) = 0
  - standard_reduction_potential

Every `standard_reduction_potential` value, and therefore every
`E0_cell`, `dG`, `K`, and Nernst `E`, is a difference from this
chosen zero.

## `butler_volmer_equation` (principle_law -- STATED, NOT DERIVED)
The current-overpotential law is a boundary node: its microkinetic
derivation, and the meaning of the transfer coefficient alpha, are out
of scope. Direct dependents:
  - tafel_equation

## Embedded assumptions (not their own nodes -- Release 0.2 candidates)

- **298.15 K** -- every quoted `E0`, `K`, `RT/F = 0.02569 V`, and the
  `0.05916 V` Nernst prefactor. `temperature_coefficient_emf` is the
  node that handles the `T`-dependence explicitly.
- **ideal gas** for electrolysis products (H2, O2, Cl2) -- carried by
  `gas_volume_electrolysis` via the imported `ideal_gas_law`.
- **alpha ~ 0.5** (symmetric transfer coefficient) in `butler_volmer_equation`
  and the `tafel_equation` slope.
- **ideal membrane selectivity** as the reference against which
  `crossover` and `shunt_current` are the deviations.
