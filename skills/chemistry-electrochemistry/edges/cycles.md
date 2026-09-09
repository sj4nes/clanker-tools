# Cycles found and how they were resolved — Release 0.1

`tsort` on `build/dependencies.sorted.edges` reports **no cycle** (stderr empty,
BSD-safe check in `build/build-tree.sh`; 110 nodes, 255 edges). The graph is
acyclic as authored.

Cycles that were anticipated and pre-empted in modeling (never encoded as edges):

| latent cycle | resolution |
|---|---|
| `cell_potential ↔ galvanic_cell` (a galvanic cell is one with `E_cell > 0`; the potential is defined for the cell) | `electrochemical_cell` → `anode` / `cathode` → `cell_potential` → `standard_cell_potential` → `spontaneity_from_cell_potential` → `galvanic_cell` / `electrolytic_cell`. The generic cell and its electrodes come first; the galvanic-vs-electrolytic split is a *downstream* reading of the sign of `E°_cell`. One direction. |
| `overpotential ↔ nernst_equation` (overpotential is the excess over "the potential", which is the Nernst value; Nernst gives the reversible potential) | `overpotential` is defined as `E_applied − E_equilibrium`, and `E_equilibrium` **is** the Nernst potential, so `nernst_equation` strictly precedes `overpotential`. No back-edge: Nernst is pure thermodynamics and never refers to a kinetic quantity. |
| `exchange_current_density ↔ butler_volmer_equation` (`j₀` appears in the Butler–Volmer law; `j₀` is "the Butler–Volmer current at `η = 0`") | `activation_overpotential` → `exchange_current_density` → `butler_volmer_equation` → `tafel_equation`. `j₀` is introduced as a measurable parameter (the current density when the forward and back rates are equal); Butler–Volmer then *uses* it. Butler–Volmer is not a prerequisite for defining `j₀`. |
| `crossover ↔ coulombic_efficiency` (crossover lowers `η_C`; you measure `η_C` to detect crossover) | `crossover` depends only on `ion_exchange_membrane`, `transport_number`, and the flow battery existing — all upstream. `coulombic_efficiency` then depends on `crossover` (and `shunt_current`). The measurement direction (`η_C` → infer crossover) is an operational relation, not a `tsort` edge. |
| `capacity_fade ↔ state_of_charge` (fade shows up as an SOC imbalance; SOC is what fades) | `state_of_charge` is defined first (fraction of active species in the charged form, from `molarity` and the Nernst potential). `capacity_fade` then depends on `state_of_charge` and `crossover`. No back-edge. |
| cross-capsule imports (`gibbs_free_energy`, `reaction_isotherm`, `half_reaction`, `ideal_gas_law`, …) | all `bridge_imported`; their upstream derivations live in `chemistry-foundations` / `physics-thermodynamics` and are **not re-encoded here**, so no cross-capsule cycle is possible. The electrical primitives (`electric_charge`, `electric_current`, `electric_potential`, `ohms_law`) are treated as a **root set** pending a future `physics-circuits` capsule. |
