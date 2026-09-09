# Conventions and foundational choices — Release 0.1

## Notation

- `n` — amount of substance, mol. `N` — number of entities (dimensionless
  count). `N_A` — the Avogadro constant, `mol^-1`.
- `M` — molar mass, g/mol (capsule keeps the chemistry-customary g/mol, not the
  SI-coherent kg/mol; every formula using `M` names the unit).
- `m` — mass, g or kg per the node. `c` — amount concentration (molarity),
  mol/L, written `c(X)` or `[X]`. `[X]` inside an equilibrium expression means
  the numerical value of the molarity divided by the standard `1 mol/L` (so `K`
  is dimensionless) — see `equilibrium_constant`.
- `P` — pressure, Pa (with atm/bar/torr as named non-SI units). `V` — volume,
  m³ or L per the node. `T` — thermodynamic temperature, K, in every gas-law
  and equilibrium expression.
- `x(X)` — mole fraction. `ΔH`, `ΔG`, `ΔS` — molar reaction quantities for the
  reaction as written; `°` superscript = standard state.
- `Q` — reaction quotient (same algebraic form as `K`, arbitrary composition).
  Also `q` — heat, J (lower case; distinct from `Q`).

## Dimensional basis

`[M L T Θ N]` — mass, length, time, temperature, amount of substance. Amount of
substance `N` is a **base dimension** in this capsule (SI treats the mole as a
base unit). Count of entities is dimensionless; `N_A` carries `N^-1`.

## Sign conventions

- **Thermochemistry:** heat added to the system `q > 0`; work done by the system
  `w > 0`; `ΔU = q − w`. `ΔH < 0` exothermic, `ΔH > 0` endothermic. Node:
  `heat_work_sign_convention`. Consistent with
  [`physics-thermodynamics`](../physics-thermodynamics/scope.md).
- **Redox:** oxidation = loss of electrons = increase in oxidation number.
  Oxidation numbers assigned by the rule hierarchy in `oxidation_number_rules`
  (free element 0; monatomic ion = charge; F −1; O −2 except peroxides/OF₂;
  H +1 with nonmetals, −1 with metals; sum = overall charge).

## Standard state

`P° = 1 bar`; solutes at `1 mol/L`; pure condensed phases as themselves. The
standard state does **not** fix temperature; tabulated `ΔH_f°`, `S°`, `ΔG_f°`
are at 298.15 K unless stated. Node: `standard_state`.

## Imported (bridge) nodes — not derived here

| node | imported from | used for |
|---|---|---|
| `gibbs_free_energy` | physics-thermodynamics `gibbs_free_energy` | sign of spontaneity, `ΔG° = −RT ln K` |
| `gibbs_helmholtz_relation` (`ΔG = ΔH − TΔS`) | physics-thermodynamics | connecting thermochemistry to equilibrium |
| `entropy` | physics-thermodynamics `entropy` | qualitative Le Chatelier / spontaneity discussion |
| `ideal_gas_law` | physics-thermodynamics `ideal_gas_law` | gas stoichiometry, `K_p` |

Each is a `bridge_imported` node: its statement is quoted, its provenance is the
thermodynamics capsule, and this capsule does not re-verify its derivation.

## Foundational primitive choices (see `edges/cycles.md` for the cycle each resolves)

- **`atom` is primitive.** The capsule does not construct the atom from
  subatomic theory; it takes atoms, their nuclear charge (atomic number), and
  their mass as empirically given. `proton`/`neutron`/`electron` appear only as
  labels inside `atomic_structure`, itself primitive.
- **`element` and the periodic table** are primitive: an empirical ordering by
  atomic number with recurring properties. The *periodic law* node states the
  regularity; it is `empirical_law`, not derived.
- **`chemical_reaction` is primitive** as "a rearrangement of atoms among
  substances conserving each element and total charge". Balancing is a
  `bookkeeping_procedure` on top of it.
- **`amount_of_substance` (the mole) is primitive**, defined via a fixed
  numerical value of `N_A` (2019 SI redefinition). `molar_mass` is then a
  measured/derived bridge to gram masses.
- Resolves the `equilibrium ↔ rate` cycle by **excluding rate entirely**:
  equilibrium is defined thermodynamically (`Q = K`, `ΔG = 0`), never as
  "forward rate equals reverse rate".

## Topological order ≠ teaching order ≠ discovery order

`indexes/tsort-order.txt` is one valid prerequisite-respecting linearization.
Independent nodes fall in an arbitrary tie order; do not read adjacency as
"comes right before". Conceptual priority, historical order, and lab-course
order are all separate.
