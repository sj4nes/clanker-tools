# Minimal prerequisite paths (Release 0.1)

Derived from the graph structure (transitive closure of `edges/dependencies.edges`),
not from the flat `tsort` order. Each list is the set of nodes that must be
understood first; within a list the `tsort` order applies. `[A]` marks an
assumption/regime node — required but not "learned".

## kinetic_energy
[newtonian_mechanics] [nonrelativistic] [inertial_frame] [point_particle]
SI_units · real_numbers→function→limit→derivative · length · time · mass ·
scalar_multiplication · squaring ·
position → velocity → speed
→ **kinetic_energy**

## work_energy_theorem
everything under kinetic_energy, plus:
force · displacement · integral ·
acceleration · newton_first_law → newton_second_law ·
work
→ **work_energy_theorem**

## conservation_of_mechanical_energy
everything under work_energy_theorem, plus:
[conservative_force] [isolated_system] ·
potential_energy · mechanical_energy
→ **conservation_of_mechanical_energy**
Do-not-use if: friction, drag, inelastic collision, or external drive does work.

## simple_pendulum
[newtonian_mechanics] [small_oscillation] [uniform_gravity] ·
trigonometry · limit · derivative · length · mass · force ·
newton_first_law → newton_second_law ·
displacement → hookes_law ·
small_angle_approximation ·
simple_harmonic_motion → angular_frequency_shm → shm_period ·
weight
→ **simple_pendulum**
Do-not-use if: amplitude not small; extended/physical pendulum; non-uniform g.
More elementary route in: none (this is the base case for pendulums in 0.1).

## conservation_of_momentum
[newtonian_mechanics] [nonrelativistic] [isolated_system] ·
SI_units · mass · scalar_multiplication ·
position → velocity · time · integral · force ·
newton_first_law → newton_second_law · newton_third_law ·
momentum · impulse → impulse_momentum_theorem
→ **conservation_of_momentum**
Do-not-use if: net external force acts over the interval.

## newton_gravitation
[newtonian_mechanics] [point_particle] ·
SI_units · mass · length · squaring
→ **newton_gravitation**
Then: → gravitational_field, → gravitational_pe_general (needs potential_energy,
integral, [conservative_force]).
Do-not-use if: strong field / high precision (→ general relativity).
