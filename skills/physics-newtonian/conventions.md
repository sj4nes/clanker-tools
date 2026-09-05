# Conventions and foundational choices

## Notation

- Scalars in plain type (`v`, `F`); this release works one axis at a time, so
  `v`, `a`, `F` are signed components along a chosen axis, not magnitudes, unless
  named `speed` or written `|.|`.
- `d/dt` for time derivatives; `dx` etc. for exact differentials.
- `Delta` denotes a finite change (`Delta x = x - x_0`), never an uncertainty.
- `x_0`, `v_0` are values at the initial instant `t = 0` of the chosen interval.
- `g` is the positive magnitude of free-fall acceleration near Earth's surface
  (`g ~ 9.81 m/s^2`); direction is supplied by the sign convention of the problem.
- SI base dimensions used: `M` (mass), `L` (length), `T` (time). No `I`, `Theta`,
  `N`, `J` in this release.

## Sign conventions

- One spatial axis per problem. State whether `+` is up, down, right, etc.
- Weight as a component: `+`up ⇒ `W = -mg`; `+`down ⇒ `W = +mg`. Node `weight`
  stores the magnitude `mg` and defers the sign to the problem axis.
- Work `W = integral F dx` is positive when force and displacement components
  share a sign.
- Potential energy differences only are physical; the reference point (`U = 0`)
  is a free choice recorded per problem. `gravitational_pe_uniform` uses the
  ground; `gravitational_pe_general` uses `r -> infinity`.

## Foundational primitive choices

Accepted as **primitive for Release 0.1** (documented, not defined here):

| Node | Why primitive here | Omitted alternative |
|---|---|---|
| `time` | metric time coordinate of an inertial frame | relativistic proper time |
| `length` | Euclidean spatial distance | curved-space metric |
| `mass` | single inertial/gravitational metric quantity (equivalence assumed) | operational mass via `F=ma`; inertial vs gravitational distinction |
| `inertial_frame` | frame where free particles move at constant velocity | relativistic inertial frames; rotating-frame treatment |
| `real_numbers`, `function`, `limit`, `derivative`, `integral` | single-variable calculus assumed known | construction from first principles |

## Cycle-resolution decisions

Recorded in full in `edges/cycles.md`. Summary:

- **mass ↔ force.** `mass` is primitive; the operational procedure "measure mass
  by applying a known force and observing acceleration" is an operational note on
  the `mass` node, **not** a prerequisite edge. So only `mass -> newton_second_law`
  exists, not the reverse.
- **force ↔ acceleration.** `acceleration` is defined kinematically
  (`a = dv/dt`, no reference to force). `newton_second_law` then relates a *net
  force* to that kinematic `a`. Edge direction: `acceleration -> newton_second_law`.
  There is no `force -> acceleration` edge; predicting motion from force is a
  *use* of the law, captured by `newton_second_law -> constant_acceleration_kinematics`.
- **energy ↔ work.** `work` is the entry point (`integral F dx`);
  `kinetic_energy` and the potential energies `derive_from` work and the
  work-energy theorem one-directionally.
- **momentum ↔ force.** `momentum` is defined as `m v` (kinematic + mass);
  `impulse_momentum_theorem` then connects `integral F dt` to `Delta p`. No
  `force -> momentum` prerequisite edge.

## Model vs law labels

- `newton_second_law`, `newton_first_law`, `newton_third_law`,
  `conservation_of_momentum`, `conservation_of_mechanical_energy`,
  `newton_gravitation` → `fundamental_law` **within Newtonian mechanics** (each
  node states the regime).
- `weight`, `friction_kinetic`, `hookes_law` → `constitutive_model` (material/
  configuration dependent; each states its validity window).
- `small_angle_approximation` → `approximation` (`theta` in radians, `theta << 1`).
- `constant_acceleration_kinematics`, `kinetic_energy`, elastic/gravitational PE,
  SHM relations, pendulum period → `derived_exact` **within their stated
  assumptions**.
