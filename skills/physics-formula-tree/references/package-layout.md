# Package layout, schemas, and build scripts

## Directory skeleton

```text
<release-name>/
  README.md            what this release is, how to read it
  scope.md             included/excluded domains, math level, background,
                       unit system, sign/coordinate conventions, exactness policy
  conventions.md       every notation/sign/coordinate/transform convention,
                       and every foundational primitive/cycle-resolution choice
  symbols.md           master symbol list: symbol -> meaning, type, SI unit
  units.md             base-dimension basis used, quantity -> dimension table

  nodes/
    nodes.tsv          the node registry (schema below)
    <id>.md            one detail page per node

  edges/
    dependencies.plan  commented prerequisite edges (evidence per edge)
    dependencies.edges generated: comments stripped, two fields per line
    relations.tsv      non-prerequisite relations (generalizes, approximates, ...)
    cycles.md          every cycle found and how it was resolved

  formulas/
    <id>.yaml          one structured entry per formula (schema below)
    <domain>.md        optional human-readable domain notes (a VIEW, reconciled
                       against the graph, never the source of truth)

  indexes/             all GENERATED, read-only
    tsort-order.txt
    topic-index.md  symbol-index.md  assumption-index.md  formula-index.md
    reverse-dependencies.txt  prerequisite-paths.md
    generalization-map.md  common-misuse-index.md  unit-dimension-index.md

  validation/
    graph-check.sh
    tsort-errors.txt        (generated)
    dimensional-checks.md   bc worksheets + results
    derivation-checks.md    lean statements + what the kernel verified
    special-cases.md  consistency-audit.md  coverage-audit.md

  sources/
    bibliography.md
    source-map.tsv         source_key -> title, edition, section, conventions

  build/
    build-tree.sh
    *.txt                  (generated intermediates)
```

A first, small release may collapse to: `scope.md`, `conventions.md`,
`nodes/nodes.tsv`, per-node pages, `edges/dependencies.plan`, `formulas/*.yaml`,
`build/build-tree.sh`, and the generated `indexes/`.

## Node registry — `nodes/nodes.tsv`

Tab-separated, one header row. Node IDs are stable, lowercase, `snake_case`, no
whitespace (they must survive `tsort`'s whitespace tokenizer).

```text
id	type	title	domain	status	knowledge_level	primary_formula
velocity	physical_definition	Velocity	mechanics	active	foundation	v = dx/dt
kinetic_energy	derived_formula	Kinetic energy	mechanics	reviewed	core	K = 1/2 m v^2
nonrelativistic	assumption	Nonrelativistic regime	cross_domain	active	foundation	v << c
```

`type` is one of: `primitive`, `math_definition`, `physical_definition`,
`convention`, `assumption`, `principle_law`, `constitutive_relation`, `identity`,
`derived_formula`, `regime_limit`, `bridge`, `diagnostic`, `example`.
`status`: `draft` → `reviewed` → `verified`, or `deprecated`.

## Node detail page — `nodes/<id>.md`

```markdown
# kinetic_energy

## Type
derived_formula

## Statement
K = (1/2) m v^2

## Symbols
- K: kinetic energy, J
- m: inertial mass, kg
- v: speed relative to the chosen inertial frame, m/s

## Prerequisites (tsort edges into this node)
mass, speed, scalar_multiplication, squaring, SI_units,
newtonian_mechanics, nonrelativistic, inertial_frame

## Assumptions and validity
Newtonian mechanics; constant inertial mass; v << c; point-particle or
centre-of-mass treatment; measured in an inertial frame.

## Derivation status
derived_exact from work_energy_theorem for constant mass.
Checked with lean: <statement id / result>.

## Dimensional check
[K] = M L^2 T^-2 ; [m][v]^2 = M (L T^-1)^2 = M L^2 T^-2  -> consistent
(checked with bc: validation/dimensional-checks.md#kinetic_energy)

## Limiting / special cases
v = 0 => K = 0 ; doubling v quadruples K ; NOT a relativistic KE formula.

## Common misuse
Applying when v is not small vs c; treating speed as frame-independent;
confusing kinetic energy with momentum.

## Related nodes (non-prerequisite)
generalized_by: relativistic_kinetic_energy
related_quantity: momentum
derivation_routes: [work_energy_theorem, integrate_newton_second_law]

## Sources
[source_key], section / equation
```

## Formula entry — `formulas/<id>.yaml`

```yaml
id: mechanics.kinetic_energy.newtonian
node: kinetic_energy
class: derived_formula          # exactness label (see SKILL.md list)
display: 'K = \frac{1}{2} m v^2'
parseable: 'K = (1/2) * m * v^2'
symbols:
  K: { meaning: kinetic energy, dimension: 'M L^2 T^-2', SI_unit: J }
  m: { meaning: inertial mass, dimension: 'M', SI_unit: kg }
  v: { meaning: speed in the chosen inertial frame, dimension: 'L T^-1', SI_unit: m/s }
dimensions_lhs: 'M L^2 T^-2'
dimensions_rhs: 'M L^2 T^-2'
dimension_check_status: consistent      # necessary, NOT sufficient
assumptions: [newtonian_mechanics, nonrelativistic, constant_mass, inertial_frame]
preconditions: []
dependencies: [mass, speed, scalar_multiplication, squaring, SI_units]
derivation_provenance: work_energy_theorem
solving_for:
  m: 'm = 2K / v^2   (v != 0)'
  v: 'v = sqrt(2K / m)   (m > 0)'
special_cases:
  - 'v = 0 => K = 0'
failure_modes:
  - 'v not << c'
  - 'speed taken as frame-independent'
sources: [halliday_resnick_walker_11e]
status: reviewed
checks:
  dimensional: validation/dimensional-checks.md#kinetic_energy
  limits: validation/special-cases.md#kinetic_energy
  derivation: validation/derivation-checks.md#kinetic_energy
```

## `validation/graph-check.sh` and `build/build-tree.sh`

Both scripts are **identical across every capsule**, so they are not duplicated
per capsule and are no longer inlined here — a listing in prose is a copy that
drifts. Each capsule carries a two-line shim that `exec`s the single canonical
implementation:

| file | canonical source |
|---|---|
| `validation/graph-check.sh` | `skills/math-theorem-tree/lib/graph-check.sh` |
| `build/build-tree.sh` | `skills/math-theorem-tree/lib/build-tree.sh` |

Physics and chemistry capsules shim through
`skills/physics-formula-tree/lib/`, which re-exports the same two files.
A stand-alone capsule outside this repo copies the two files verbatim.

`graph-check.sh` — **hygiene only**: node registry (7 tab fields, non-empty ids,
no duplicates); `edges/dependencies.plan` stripped of full-line *and* trailing
`# evidence` comments into `edges/dependencies.edges`; two fields per edge and
no self-edges; every endpoint a registered node; a deterministic `LC_ALL=C
sort -u` edge file at `build/dependencies.sorted.edges` (never sorting *within*
a pair).

`build-tree.sh` — runs `graph-check.sh`, then `tsort` with a **stderr** cycle
guard (BSD `tsort` exits 0 on a cycle and emits a meaningless order), an
order-violation check of every supplied edge against the emitted order, a
node-coverage diff with a duplicate-node check, and the generated views:
`indexes/tsort-order.txt`, `indexes/reverse-dependencies.txt`,
`build/isolated-nodes.txt`, and `build/node-deps.txt` (the per-node
incoming-edge list that `gen-results.py`, `check-consistency.py` and
`check-edge-evidence.py` read).

Every check in both files is hygiene or internal consistency: the emitted order
is checked against the edge list it was built from. **A spurious edge and a
missing edge both pass**, which `validation/mutation-check.sh` demonstrates
rather than asserts. Edge *truth* is `build/check-edge-evidence.py`'s job. See
[`docs/verifying-skills.md` §5](../../../docs/verifying-skills.md) for the
graph-artifact rubric.


Isolated/root nodes are merged into presentation views by a controlled append —
never by adding a fake prerequisite edge to force them into `tsort` output. An
assumption/regime node showing up isolated usually means a real missing edge —
that formula *does* depend on the assumption; add it rather than shrugging.

## View generators

Keep the index generators as small committed scripts under `build/` (e.g.
`gen-symbol-index.sh`, `gen-assumption-index.sh`). Derive their inputs from the
registry, not hard-coded lists — e.g. the assumption index iterates the node ids
whose `type` is `assumption` or `regime_limit`:

```sh
awk -F '\t' 'NR>1 && ($2=="assumption" || $2=="regime_limit") { print $1 }' nodes/nodes.tsv
```

so the view stays correct as nodes are added. The symbol index is a `ptx`
discovery pass followed by a whole-token confirmation against each
`## node — statement` line; keep every formula's one-line statement *on that
header line* so it is indexed (a formula parked on the next line is missed).
