# Cycle log — Release 0.1

`tsort` on `build/dependencies.sorted.edges` completed with **empty stderr and a
complete 104-node order** — the prerequisite graph is acyclic. No
cycle-resolution was forced during the build.

Five coupling relationships in thermoacoustics that would create cycles if
modelled as prerequisites were given a direction *by construction* (full
rationale in `../conventions.md`):

| Potential cycle | Choice made | Edge kept | Edge NOT added |
|---|---|---|---|
| sound speed ↔ adiabatic process | `adiabatic_process` is a thermodynamic primitive; the sound speed derives from it | `adiabatic_process → adiabatic_sound_speed` | reverse |
| mean temperature gradient ↔ acoustic field | `∇T_m` is an **imposed** boundary condition of the linear problem; the Rott equations solve the field given it | `mean_temperature_gradient → linearized_energy_equation → rott_continuity_equation` | `rott_* → mean_temperature_gradient` |
| engine ↔ oscillation | the linear theory takes the wave as given and tests whether it grows | `acoustic_power_gradient → oscillation_onset → *_engine` | `*_engine → rott_wave_equation` |
| acoustic power ↔ heat flux | both are consequences of one Rott solution | `rott_wave_equation → {acoustic_power_gradient, thermoacoustic_heat_flux}`; their coupling is the `total_energy_flux` **bridge** | `acoustic_power_gradient ↔ thermoacoustic_heat_flux` |
| f-functions ↔ Rott 1-D equations | `f_ν`, `f_κ` come from the cross-channel boundary-value problem; the 1-D equations use them as coefficients | `linearized_navier_stokes → thermoacoustic_function_fnu → rott_momentum_equation` (and `f_κ` analogue) | reverse |

The `x`-axis convention (cold → hot, `∇T_m > 0` means hot in `+x`) and the
phasor convention (`e^{+iωt}`) are fixed in `../conventions.md` so that every
formula entry and the two `f`-function sign conventions stay consistent.

Verification that the order respects every edge: `build/build-tree.sh` step
"every supplied edge is respected by the emitted order" — passed (no
`order violation` lines).
