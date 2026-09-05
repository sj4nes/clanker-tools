# Formula entries — Release 0.1

A view generated from and reconciled against the graph. Each entry: statement,
symbols (with SI unit and `[M L T]` dimension), exactness label, assumptions,
preconditions, direct prerequisites, one limiting/special case, failure modes,
source. Dimensional checks: `validation/dimensional-checks.bc`. Derivation-step
algebra: `validation/derivation-checks.lean`.

Sources: `HRW` = Halliday, Resnick & Walker, *Fundamentals of Physics*, 11th ed.;
`KK` = Kleppner & Kolenkow, *An Introduction to Mechanics*, 2nd ed.;
`SI` = BIPM SI Brochure, 9th ed.

---

## displacement — `Delta x = x - x_0`
- x, x_0: position, m, `L`. Delta x: displacement, m, `L`.
- Label: definition. Assumptions: one chosen axis. Preconditions: none.
- Prereqs: position. Special case: x = x_0 ⇒ Delta x = 0.
- Failure: conflating displacement (vector) with distance travelled (path length).
- Source: HRW ch. 2.

## velocity — `v = dx/dt`
- v: velocity component, m/s, `L T^-1`. x: position, m, `L`. t: time, s, `T`.
- Label: definition. Assumptions: x differentiable in t; inertial frame.
- Prereqs: position, time, derivative. Special case: x constant ⇒ v = 0.
- Failure: using average `Delta x / Delta t` where instantaneous v is meant.
- Source: HRW ch. 2.

## speed — `speed = |v|`
- speed: m/s, `L T^-1`. Label: definition. Prereqs: velocity.
- Special case: speed >= 0 always; speed = 0 ⇔ v = 0.
- Failure: treating speed as frame-independent; it is not.
- Source: HRW ch. 2.

## acceleration — `a = dv/dt`
- a: acceleration component, m/s^2, `L T^-2`. v: m/s, `L T^-1`. t: s, `T`.
- Label: definition. Assumptions: v differentiable in t; inertial frame.
- Prereqs: velocity, time, derivative. Special case: v constant ⇒ a = 0 (first law).
- Failure: assuming a = 0 means v = 0.
- Source: HRW ch. 2.

## constant_acceleration_kinematics
- `v = v_0 + a t` ; `x = x_0 + v_0 t + (1/2) a t^2` ; `v^2 = v_0^2 + 2 a (x - x_0)`
- v_0, v: m/s, `L T^-1`. a: m/s^2, `L T^-2`. t: s, `T`. x_0, x: m, `L`.
- Label: derived_exact. Assumptions: **a constant over the whole interval**;
  Newtonian; one axis; t measured from the stated initial instant.
- Preconditions: none (the third form needs `a != 0` only to solve for a).
- Prereqs: acceleration, velocity, displacement, integral, squaring,
  newton_second_law, newtonian_mechanics, SI_units.
- Special case: a = 0 ⇒ x = x_0 + v_0 t (uniform motion). Limiting check: the
  third form is the first two with t eliminated — `kinematics_timeless`
  (lean instance check 1).
- Failure: applying across an interval where a changes (e.g. before/after a
  collision, or with drag); using scalar form for genuinely 2-D motion.
- Source: HRW ch. 2; KK ch. 1.

## newton_first_law — `F_net = 0  ⇒  a = 0`
- Label: fundamental_law (Newtonian). Asserts inertial frames exist.
- Prereqs: inertial_frame, force, newtonian_mechanics.
- Special case: defines the regime in which the second law's `F_net` is measured.
- Failure: applying in a rotating/accelerating frame without fictitious forces.
- Source: HRW ch. 5; KK ch. 2.

## newton_second_law — `F_net = m a`
- F_net: net force, N, `M L T^-2`. m: mass, kg, `M`. a: m/s^2, `L T^-2`.
- Label: fundamental_law (Newtonian). Assumptions: inertial frame; constant
  mass (else use `F = dp/dt`); m is the total or point mass.
- Preconditions: F_net is the vector sum of *all* forces.
- Prereqs: newton_first_law, mass, force, acceleration, inertial_frame,
  newtonian_mechanics, constant_mass, SI_units.
- Special case: F_net = 0 recovers the first law.
- Failure: omitting a force from the sum; variable-mass systems (rockets);
  relativistic speeds; non-inertial frame.
- Source: HRW ch. 5; KK ch. 2.

## newton_third_law — `F_(A on B) = - F_(B on A)`
- Label: fundamental_law (Newtonian). Prereqs: force, newtonian_mechanics.
- Special case: underlies momentum conservation for an isolated pair.
- Failure: pairing forces on the *same* body; time-delayed field interactions.
- Source: HRW ch. 5.

## normal_force — `N` (contact reaction, perpendicular to surface)
- N: N, `M L T^-2`. Label: physical_definition. Prereqs: force, newton_third_law.
- Special case: on a horizontal surface with vertical equilibrium, N = mg.
- Failure: assuming N = mg on an incline or under vertical acceleration.
- Source: HRW ch. 6.

## weight — `W = m g`
- W: weight (magnitude), N, `M L T^-2`. m: kg, `M`. g: free-fall acceleration
  magnitude, m/s^2, `L T^-2` (≈ 9.81 near Earth's surface).
- Label: constitutive_model (uniform-field limit of gravitation).
- Assumptions: uniform gravitational field; near a specific surface.
- Prereqs: mass, uniform_gravity, gravitational_field, SI_units.
- Special case: the `r → R_surface` limit of `F = G m M / r^2`, with
  `g = G M / R^2`.
- Failure: using a fixed g far from the surface or on another body; confusing
  weight with mass.
- Source: HRW ch. 5; SI (kilogram).

## friction_kinetic — `f_k = mu_k N`
- f_k: kinetic friction force, N, `M L T^-2`. mu_k: dimensionless. N: normal
  force, N, `M L T^-2`.
- Label: constitutive_model. Assumptions: surfaces in relative sliding;
  mu_k roughly constant, speed- and area-independent (Coulomb model).
- Preconditions: N >= 0; opposes relative velocity.
- Prereqs: force, normal_force.
- Special case: static case uses `f_s <= mu_s N` (not in 0.1 as a separate node).
- Failure: lubricated / high-speed / deformable contacts; treating it as exact.
- Source: HRW ch. 6.

## hookes_law — `F = - k x`
- F: restoring force component, N, `M L T^-2`. k: stiffness, N/m, `M T^-2`.
  x: displacement from equilibrium, m, `L`.
- Label: constitutive_model. Assumptions: elastic regime, |x| small enough
  that the linear term dominates.
- Preconditions: x measured from the natural/equilibrium length.
- Prereqs: force, displacement, SI_units.
- Special case: x = 0 ⇒ F = 0 (equilibrium).
- Failure: beyond the elastic limit; large deformation; plastic/viscoelastic
  materials.
- Source: HRW ch. 8; KK ch. 4.

## work — `W = integral F dx`  (component along displacement)
- W: work, J, `M L^2 T^-2`. F: force component along the path, N, `M L T^-2`.
  x: position along the path, m, `L`.
- Label: definition. Assumptions: F is the component along the displacement.
- Preconditions: path specified; F integrable along it.
- Prereqs: force, displacement, integral, SI_units.
- Special case: constant F over straight displacement d ⇒ W = F d.
- Failure: using |F||d| when F ⟂ displacement (W = 0); ignoring sign.
- Source: HRW ch. 7.

## kinetic_energy — `K = (1/2) m v^2`
- K: kinetic energy, J, `M L^2 T^-2`. m: kg, `M`. v: speed, m/s, `L T^-1`.
- Label: derived_exact (Newtonian). Assumptions: Newtonian; constant mass;
  `v << c`; point particle / centre of mass; inertial frame.
- Preconditions: none.
- Prereqs: mass, speed, scalar_multiplication, squaring, SI_units,
  newtonian_mechanics, nonrelativistic, inertial_frame, point_particle.
- Special case: v = 0 ⇒ K = 0; v → 2v ⇒ K → 4K (bc check).
- Failure: `v` not small vs c (use `K = (gamma - 1) m c^2`); speed taken as
  frame-independent; confusing K with momentum.
- Source: HRW ch. 7; KK ch. 5.

## work_energy_theorem — `W_net = Delta K`
- W_net: net work by all forces, J, `M L^2 T^-2`. Delta K: change in kinetic
  energy, J, `M L^2 T^-2`.
- Label: derived_exact (Newtonian) — integrate `F_net = m a` along the path.
- Assumptions: constant mass; W_net sums work by every force; inertial frame.
- Prereqs: newton_second_law, work, kinetic_energy, integral.
- Special case: constant a ⇒ `(m a) dx = ½ m (v² − v0²)` identically
  (`work_equals_delta_K`, lean instance check 2).
- Failure: omitting a force from W_net; variable mass; non-inertial frame.
- Source: HRW ch. 7; KK ch. 5.

## potential_energy — `Delta U = - W_cons`
- U: potential energy, J, `M L^2 T^-2`. W_cons: work by the conservative force.
- Label: definition. Assumptions: **force is conservative** (path-independent
  work); reference point chosen.
- Preconditions: only differences are physical; fix U = 0 somewhere.
- Prereqs: work, conservative_force, work_energy_theorem.
- Special case: closed path ⇒ Delta U = 0.
- Failure: defining U for friction/drag (non-conservative); mixing reference
  points within one problem.
- Source: HRW ch. 8; KK ch. 5.

## force_from_potential — `F = - dU/dx`
- F: conservative force component, N, `M L T^-2`. U: J, `M L^2 T^-2`. x: m, `L`.
- Label: derived_exact (inverse of the PE definition).
- Assumptions: conservative force; U differentiable.
- Prereqs: derivative, potential_energy, conservative_force.
- Special case: minima of U are stable equilibria (F = 0, dF/dx < 0).
- Failure: applying to non-conservative forces; sign errors.
- Source: HRW ch. 8; KK ch. 5.

## gravitational_pe_uniform — `U = m g h`
- U: J, `M L^2 T^-2`. m: kg, `M`. g: m/s^2, `L T^-2`. h: height above the
  reference level, m, `L`.
- Label: derived_exact (within the uniform-field model).
- Assumptions: uniform g; h small vs Earth's radius; reference level fixed.
- Prereqs: mass, uniform_gravity, weight, potential_energy, length.
- Special case: h = 0 ⇒ U = 0; the small-h limit of `U = -G m M / r`.
- Failure: large altitude changes (use the inverse-square form); varying g.
- Source: HRW ch. 8.

## elastic_pe — `U = (1/2) k x^2`
- U: J, `M L^2 T^-2`. k: N/m, `M T^-2`. x: displacement from equilibrium, m, `L`.
- Label: derived_exact (within the Hooke model) — `U = -∫₀ˣ(-k s)ds`.
- Assumptions: Hookean spring; x from equilibrium.
- Prereqs: hookes_law, potential_energy, integral, squaring.
- Special case: x = 0 ⇒ U = 0; `(2 k x²)/2 = k x²` (lean instance check 3).
- Failure: beyond the elastic limit; anharmonic springs.
- Source: HRW ch. 8.

## mechanical_energy — `E = K + U`
- E, K, U: J, `M L^2 T^-2`. Label: definition. Prereqs: kinetic_energy,
  potential_energy.
- Special case: with only one conservative force, E is the constant of motion.
- Failure: forgetting a potential-energy term; including non-conservative work in U.
- Source: HRW ch. 8.

## conservation_of_mechanical_energy — `E = K + U = const`
- Label: fundamental_law (Newtonian, conditional).
- Assumptions: **every force doing work is conservative** (or does zero work);
  isolated from external energy input.
- Prereqs: mechanical_energy, conservative_force, work_energy_theorem,
  isolated_system.
- Special case: pendulum/spring at amplitude: all U; at equilibrium: all K.
- Failure: friction, drag, inelastic collision, external drive — use the
  work-energy theorem with all forces instead.
- Source: HRW ch. 8; KK ch. 5.

## power — `P = dE/dt`  (and `P = F v` for a force on a particle)
- P: power, W, `M L^2 T^-3`. E: J, `M L^2 T^-2`. t: s, `T`. F: N, `M L T^-2`.
  v: m/s, `L T^-1`.
- Label: definition. Assumptions: `P = F v` needs F component along v.
- Prereqs: mechanical_energy, work, derivative, time.
- Special case: constant P over t ⇒ Delta E = P t.
- Failure: using `F v` with F ⟂ v (P = 0); average vs instantaneous.
- Source: HRW ch. 7.

## momentum — `p = m v`
- p: momentum, kg·m/s, `M L T^-1`. m: kg, `M`. v: m/s, `L T^-1`.
- Label: definition (Newtonian). Assumptions: `v << c`; constant mass.
- Prereqs: mass, velocity, scalar_multiplication, nonrelativistic,
  newtonian_mechanics, SI_units.
- Special case: v = 0 ⇒ p = 0; direction of p is the direction of v.
- Failure: relativistic speeds (`p = gamma m v`); confusing p with K.
- Source: HRW ch. 9; KK ch. 3.

## impulse — `J = integral F dt`
- J: impulse, N·s = kg·m/s, `M L T^-1`. F: N, `M L T^-2`. t: s, `T`.
- Label: definition. Preconditions: F(t) integrable over the interval.
- Prereqs: force, time, integral.
- Special case: constant F over Delta t ⇒ J = F Delta t.
- Failure: ignoring that J is a vector; using peak force for average effect.
- Source: HRW ch. 9.

## impulse_momentum_theorem — `J = Delta p`
- J, Delta p: kg·m/s, `M L T^-1`.
- Label: derived_exact — integral form of `F_net = dp/dt`.
- Assumptions: J is the net impulse of all forces.
- Prereqs: newton_second_law, impulse, momentum.
- Special case: F_net = 0 over the interval ⇒ Delta p = 0.
- Failure: omitting a force; non-inertial frame.
- Source: HRW ch. 9; KK ch. 3.

## conservation_of_momentum — `sum p = const`
- Label: fundamental_law (Newtonian).
- Assumptions: **no net external force** on the chosen system (internal forces
  cancel by the third law).
- Prereqs: newton_third_law, impulse_momentum_theorem, isolated_system, momentum.
- Special case: two-body collision — total p before = total p after (elastic or
  not).
- Failure: external force present (gravity, friction) over the interval;
  choosing a system that cuts through an interaction.
- Source: HRW ch. 9; KK ch. 3.

## small_angle_approximation — `sin th ~ th`,  `cos th ~ 1 - th^2/2`
- th: angle in **radians**, dimensionless.
- Label: approximation. Assumptions: `|th| << 1` (radians); truncated Taylor
  series.
- Special case: leading error of `sin th ~ th` is `-th^3/6`
  (bc: `sin(0.1) - 0.1 = -1.67e-4`).
- Failure: th in degrees; angles not small (pendulum at large amplitude, where
  the period grows).
- Source: HRW appendix; KK ch. 6.

## simple_harmonic_motion — `x(t) = A cos(w t + phi)`
- x: displacement, m, `L`. A: amplitude, m, `L`. w: angular frequency, rad/s,
  `T^-1`. phi: phase, rad, dimensionless. t: s, `T`.
- Label: derived_exact — the general solution of `m x'' = - k x`.
- Assumptions: linear restoring force (Hooke); small oscillation; no damping.
- Prereqs: trigonometry, hookes_law, newton_second_law, derivative,
  small_oscillation.
- Special case: phi = 0 ⇒ starts at x = A, v = 0.
- Failure: anharmonic restoring force; damping/drive present; large amplitude.
- Source: HRW ch. 15; KK ch. 6.

## angular_frequency_shm — `w = sqrt(k/m)`
- w: rad/s, `T^-1`. k: N/m, `M T^-2`. m: kg, `M`.
- Label: derived_exact — substitute SHM into `m x'' = - k x`.
- Assumptions: as SHM. Preconditions: k > 0, m > 0.
- Prereqs: hookes_law, mass, simple_harmonic_motion, newton_second_law.
- Special case: `m w^2 = k` (lean instance check 4); stiffer spring / lighter
  mass ⇒ higher w.
- Failure: using for a pendulum (different effective k/m); damped systems
  (`w_d = sqrt(w^2 - gamma^2)`).
- Source: HRW ch. 15.

## shm_period — `T = 2 pi / w`
- T: period, s, `T`. w: rad/s, `T^-1`.
- Label: derived_exact. Preconditions: w > 0.
- Prereqs: simple_harmonic_motion, angular_frequency_shm, trigonometry.
- Special case: mass-spring ⇒ `T = 2 pi sqrt(m/k)`; amplitude-independent
  (isochronism).
- Failure: amplitude dependence appears once the restoring force is nonlinear.
- Source: HRW ch. 15.

## simple_pendulum — `T = 2 pi sqrt(L/g)`
- T: period, s, `T`. L: length, m, `L`. g: m/s^2, `L T^-2`.
- Label: derived_exact **within the small-angle approximation**.
- Assumptions: massless rigid rod, point bob, small amplitude, uniform g,
  no damping.
- Preconditions: L > 0, g > 0.
- Prereqs: simple_harmonic_motion, small_angle_approximation, shm_period,
  weight, uniform_gravity, length, small_oscillation.
- Special case: effective `w^2 = g/L`  (`(m g L)/(m L^2) = g/L`,
  lean instance check 5); independent of the bob mass.
- Failure: large amplitude (true period is longer, elliptic integral); a
  physical (extended) pendulum; non-uniform g.
- Source: HRW ch. 15; KK ch. 6.

## newton_gravitation — `F = G m_1 m_2 / r^2`
- F: attractive force magnitude, N, `M L T^-2`. G: 6.674e-11, `M^-1 L^3 T^-2`.
  m_1, m_2: kg, `M`. r: centre-to-centre separation, m, `L`.
- Label: fundamental_law (Newtonian gravity).
- Assumptions: point masses (or spherically symmetric bodies, by the shell
  theorem); non-relativistic; weak field.
- Preconditions: r > 0.
- Prereqs: mass, length, squaring, newtonian_mechanics, point_particle, SI_units.
- Special case: near a large sphere of mass M and radius R, `F/m = G M / R^2 = g`.
- Failure: strong fields / high precision (use general relativity — Mercury's
  perihelion); overlapping or highly non-spherical bodies.
- Source: HRW ch. 13; KK ch. 3.

## gravitational_field — `g = G M / r^2`
- g: field strength = force per unit mass, m/s^2 (= N/kg), `L T^-2`. M: source
  mass, kg, `M`. r: m, `L`.
- Label: derived_exact (from gravitation, divide by test mass).
- Assumptions: as gravitation; test mass negligible.
- Prereqs: newton_gravitation, mass, length, squaring.
- Special case: r = R_Earth ⇒ g ≈ 9.81; inverse-square falloff with altitude.
- Failure: inside the mass distribution; non-spherical sources.
- Source: HRW ch. 13.

## gravitational_pe_general — `U = - G m_1 m_2 / r`
- U: J, `M L^2 T^-2`. Sign: negative, U → 0 as r → ∞.
- Label: derived_exact — `U = -∫_∞^r F·dr` for the inverse-square force.
- Assumptions: as gravitation; reference U = 0 at infinity.
- Preconditions: r > 0.
- Prereqs: newton_gravitation, potential_energy, integral, conservative_force,
  length, mass.
- Special case: near a surface, `Delta U ≈ m g h` for `h << R` (Taylor
  expansion of `-GmM/r` about r = R).
- Failure: using the `m g h` form for orbital / escape problems; sign errors;
  finite reference point mixed with the infinity reference.
- Source: HRW ch. 13; KK ch. 5.
