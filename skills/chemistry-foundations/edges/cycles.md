# Cycles found and how they were resolved — Release 0.1

`tsort` on `build/dependencies.sorted.edges` reports **no cycle** (stderr empty,
BSD-safe check in `build/build-tree.sh`). The graph is acyclic as authored.

Cycles that were anticipated and pre-empted in modeling (never encoded as edges):

| latent cycle | resolution |
|---|---|
| `equilibrium ↔ reaction rate` | Rate is **excluded from scope**. `dynamic_equilibrium` is defined thermodynamically (`Q = K`, `ΔG = 0`), never as "forward rate = reverse rate". No rate node exists to close the loop. |
| `element ↔ atomic_number` (identity is Z; Z is a property of the element's atoms) | `atom` and `atomic_structure` are primitive; `atomic_number` derives from `atomic_structure` (proton count); `element` derives from `atom` + `atomic_number`. One-directional. |
| `enthalpy ↔ first law` (H defined via U; ΔH interpreted via the first law at constant P) | `internal_energy` and `first_law_thermo` precede `enthalpy`; the constant-pressure interpretation is metadata on `enthalpy_of_reaction`, not a back-edge. |
| `equilibrium_constant ↔ reaction_quotient` (same algebraic form) | `equilibrium_constant` is the primary; `reaction_quotient` is "the same expression evaluated away from equilibrium" and depends on it. `q_versus_k` depends on both. |
| `weak_acid_equilibrium ↔ ice_table` (Ka problems are solved with an ICE table; the ICE table needs a K) | `ice_table` depends only on the generic `equilibrium_constant` / `reaction_quotient`; `weak_acid_equilibrium` then depends on `ice_table`. No back-edge from `ice_table` to the acid-specific node. |
| `Gibbs / thermodynamics` imports | `gibbs_free_energy`, `gibbs_helmholtz_relation`, `reaction_isotherm`, `first_law_thermo`, `internal_energy`, `enthalpy`, `ideal_gas_law` are `bridge_imported` from `physics-thermodynamics`. Their upstream derivations live in that capsule and are not re-encoded here, so no cross-capsule cycle is possible. |
