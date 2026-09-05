# Scope — Release 0.1

Knowledge capsule: **Newtonian point-particle mechanics**, built with the
[`physics-formula-tree`](../physics-formula-tree/SKILL.md) method.

## Included

- SI units and `[M, L, T]` dimensional analysis.
- Single-variable calculus prerequisites (derivative, integral) accepted as primitives.
- One-dimensional / vector-consistent scalar kinematics.
- Newton's three laws; weight, kinetic friction, normal force, Hooke's law as models.
- Work, kinetic energy, the work-energy theorem, potential energy (uniform gravity
  and elastic), mechanical energy and its conservation, power.
- Momentum, impulse, the impulse-momentum theorem, conservation of momentum.
- Simple harmonic motion (mass-spring, simple pendulum via small-angle).
- Newtonian gravitation: inverse-square force, field, general gravitational PE.

## Excluded

- Rotation, rigid bodies, torque, angular momentum.
- Special/general relativity and any `v/c` corrections.
- Fields beyond Newtonian gravity; electromagnetism.
- Thermodynamics, statistical mechanics, fluids.
- Lagrangian/Hamiltonian formulations.
- Non-inertial frames, fictitious forces.
- Numerical methods, error analysis.
- Damped/driven/coupled oscillators; anharmonicity beyond leading order.

## Conventions

- **Math level:** single-variable differential and integral calculus.
- **Assumed background:** algebra, functions, vectors as directed quantities,
  trigonometry.
- **Unit system:** SI throughout.
- **Sign/coordinate:** one spatial axis per problem, `+x` (or `+`upward) chosen
  explicitly; `g > 0` is the magnitude of free-fall acceleration, so downward
  weight is `-mg` when `+` is up.
- **Derivations:** summarised in node pages; the load-bearing calculus/algebra
  identities are machine-checked with Lean (`validation/derivation-checks.md`).
- **Exactness policy:** every formula carries one label — only `definition`,
  `mathematical_identity`, `fundamental_law`, `derived_exact`,
  `constitutive_model`, `approximation` appear in this release.
- **Audience:** a downstream agent needing trustworthy mechanics relations with
  explicit prerequisites, assumptions, and failure modes.

## Release status

`draft` — pipeline run recorded in `validation/`. See
`../physics-newtonian/README.md` for the verification summary.
