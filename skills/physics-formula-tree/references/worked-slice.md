# Worked slice: `kinetic_energy` through every stage

A minimal end-to-end pass for one Release 0.1 (Newtonian point-particle
mechanics) node and its prerequisites. Illustrates the method; not a full
release.

## 1. Scope (excerpt of `scope.md`)

> Release 0.1 — Newtonian point-particle mechanics. Included: SI units,
> dimensions `[M,L,T]`, scalar kinematics, work/energy/momentum. Excluded:
> rotation, relativity, fields, thermodynamics. Math level: single-variable
> calculus. Unit system: SI. Sign convention: 1-D, +x chosen per problem.
> Derivations: summarised, key algebra checked with Lean. Exactness: formulas
> labelled `fundamental_law` / `derived_exact` / `definition` only.

## 2. Nodes (`nodes/nodes.tsv` excerpt)

```text
id	type	title	domain	status	knowledge_level	primary_formula
SI_units	convention	SI unit system	cross_domain	active	foundation	-
inertial_frame	primitive	Inertial frame	mechanics	active	foundation	-
newtonian_mechanics	assumption	Newtonian regime	mechanics	active	foundation	-
nonrelativistic	assumption	Nonrelativistic regime	cross_domain	active	foundation	v << c
mass	primitive	Inertial mass	mechanics	active	foundation	-
length	primitive	Length	cross_domain	active	foundation	-
time	primitive	Time	cross_domain	active	foundation	-
derivative	math_definition	Derivative	math	active	foundation	-
position	physical_definition	Position	mechanics	active	foundation	x(t)
velocity	physical_definition	Velocity	mechanics	active	foundation	v = dx/dt
speed	physical_definition	Speed	mechanics	active	foundation	|v|
scalar_multiplication	math_definition	Scalar multiplication	math	active	foundation	-
squaring	math_definition	Squaring	math	active	foundation	-
force	physical_definition	Force	mechanics	active	foundation	-
newton_second_law	principle_law	Newton's second law	mechanics	reviewed	core	F = m a
work	derived_formula	Work	mechanics	reviewed	core	W = integral F dx
work_energy_theorem	bridge	Work-energy theorem	mechanics	reviewed	core	W_net = dK
kinetic_energy	derived_formula	Kinetic energy	mechanics	reviewed	core	K = 1/2 m v^2
```

## 3. Primitives documented (`conventions.md` excerpt)

> `mass`, `length`, `time`, `inertial_frame` are primitive for Release 0.1.
> `mass` is taken as a given metric quantity; its operational measurement via
> `F=ma` is recorded as a note, not a prerequisite edge, to avoid the mass↔force
> cycle. `inertial_frame` is the Newtonian notion (free particles move at
> constant velocity); relativistic frames are out of scope.

## 5. Edges (`edges/dependencies.plan` excerpt)

```text
# Velocity is the time-derivative of position; needs the derivative and time.
position velocity
time velocity
derivative velocity

# Speed is the magnitude of velocity.
velocity speed

# Newton's second law relates force to mass and acceleration in an inertial frame.
mass newton_second_law
force newton_second_law
inertial_frame newton_second_law
newtonian_mechanics newton_second_law
SI_units newton_second_law

# Work is the line integral of force over displacement.
force work
position work

# The work-energy theorem equates net work to the change in kinetic energy;
# it is derived by integrating Newton's second law.
newton_second_law work_energy_theorem
work work_energy_theorem

# Newtonian kinetic energy: a formula in mass and speed, in an inertial frame,
# valid only nonrelativistically. Derived exactly from the work-energy theorem.
mass kinetic_energy
speed kinetic_energy
scalar_multiplication kinetic_energy
squaring kinetic_energy
SI_units kinetic_energy
inertial_frame kinetic_energy
newtonian_mechanics kinetic_energy
nonrelativistic kinetic_energy
work_energy_theorem kinetic_energy
```

Non-prerequisite relations (`edges/relations.tsv`):

```text
generalized_by	kinetic_energy	relativistic_kinetic_energy	out of scope for 0.1
related_quantity	kinetic_energy	momentum	both are p,K in m,v
approximates	kinetic_energy	relativistic_kinetic_energy	v/c << 1
```

## 6. Validate + sort

```sh
sh validation/graph-check.sh      # graph-check: ok
sh build/build-tree.sh            # build-tree: ok (18 ordered nodes)
```

`indexes/tsort-order.txt` (one valid order — independent roots may reorder):

```text
SI_units
inertial_frame
newtonian_mechanics
nonrelativistic
mass
length
time
derivative
scalar_multiplication
squaring
position
force
velocity
speed
newton_second_law
work
work_energy_theorem
kinetic_energy
```

No stderr from `tsort` → acyclic. Every edge verified `pos[A] < pos[B]`.

## 7. Dimensional check — via `bc` skill

Dimension exponent vectors `(M,L,T)`. `K = 1/2 m v^2`:
`[m] = (1,0,0)`, `[v] = (0,1,-1)`, `[v^2] = (0,2,-2)`, sum `(1,2,-2)`.
`[K]` target `M L^2 T^-2 = (1,2,-2)`. Equal → `dimension_check_status: consistent`.

Limiting case `v=0`: `bc` → `K = 0`. Doubling `v` (`v→2v`): factor
`(2)^2 = 4`. Recorded in `validation/dimensional-checks.md#kinetic_energy`.
Note in the file: *dimensional consistency is necessary, not sufficient.*

## 7. Derivation check — via `lean` skill

Claim: for constant `m`, `integral_{0}^{t} F v dt' = integral d(1/2 m v^2)`, i.e.
`m a v = d/dt (1/2 m v^2)`. State in Lean as: for `v : R -> R` differentiable,
`deriv (fun t => (1/2) * m * (v t)^2) t = m * (v t) * deriv v t`. Kernel checks
the calculus identity.

Record: *Lean verified the chain-rule identity `d/dt(½mv²) = mv·(dv/dt)`. It did
**not** verify that `F = m dv/dt` (that is `newton_second_law`, an assumed law) or
the nonrelativistic regime.* → `validation/derivation-checks.md#kinetic_energy`.

## 8. Views

- `indexes/symbol-index.md` via `ptx -W '[A-Za-z0-9_]+' -A` over `formulas/*.yaml`
  → `K`, `m`, `v` each list `kinetic_energy`; `F`, `m`, `a` list
  `newton_second_law`; confirm with `rg`.
- `indexes/prerequisite-paths.md` — minimal path to `kinetic_energy` from graph
  structure: `SI_units, inertial_frame, newtonian_mechanics, nonrelativistic,
  mass, {position,time,derivative}→velocity→speed, scalar_multiplication,
  squaring, force→work, newton_second_law, work_energy_theorem`.
- `indexes/assumption-index.md` — `nonrelativistic`: `kinetic_energy`, …;
  `inertial_frame`: `newton_second_law`, `kinetic_energy`, …

## Completion report (excerpt)

> Scope: Release 0.1 Newtonian point-particle mechanics; excludes rotation,
> relativity, fields, thermo. Graph: 18 nodes, 24 prerequisite edges, 6
> root/convention/assumption nodes. `tsort` succeeded, stderr empty → acyclic
> (BSD-safe check). 1 formula (`kinetic_energy`) dimensionally checked via `bc`;
> its exactness claim checked via `lean` (calculus identity only). No cycles
> encountered. `mass` fixed as primitive to avoid mass↔force. Limitations: a
> curated dependency graph, not a complete account of mechanics; a valid `tsort`
> order confirms only the encoded constraints; dimensional consistency is not
> physical correctness.
