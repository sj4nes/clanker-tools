# Cycle log — Release 0.1

`tsort` on `build/dependencies.sorted.edges` completed with **empty stderr and a
complete 58-node order** — the prerequisite graph is acyclic. No cycle-resolution
was forced during the build.

Four classic mechanics cycles were avoided *by construction* when choosing edge
direction (full rationale in `../conventions.md`):

| Potential cycle | Choice made | Edge kept | Edge NOT added |
|---|---|---|---|
| mass ↔ force | `mass` is primitive; operational "measure mass via `F=ma`" is a note on the node | `mass → newton_second_law` | `force → mass` / `newton_second_law → mass` |
| force ↔ acceleration | `acceleration` is purely kinematic (`a = dv/dt`); the second law relates net force to that `a`; predicting motion is a *use* of the law | `acceleration → newton_second_law`, `newton_second_law → constant_acceleration_kinematics` | `force → acceleration` |
| energy ↔ work | `work` (`∫F dx`) is the entry point; energies derive from it one-way | `work → kinetic_energy` (via theorem), `work → potential_energy` | `kinetic_energy → work` |
| momentum ↔ force | `momentum` defined as `m v`; the impulse-momentum theorem then links `∫F dt` to `Δp` | `momentum → impulse_momentum_theorem` | `force → momentum` |

Verification that the order respects every edge: `build/build-tree.sh` step
"every supplied edge is respected by the emitted order" — passed (no
`order violation` lines).
