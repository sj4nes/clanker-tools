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

## `validation/graph-check.sh`

```sh
#!/bin/sh
set -eu
cd "$(dirname "$0")/.."
mkdir -p build

grep -Ev '^[[:space:]]*(#|$)' edges/dependencies.plan > edges/dependencies.edges

awk 'NF != 2 { print "line " NR ": expected 2 fields, got " NF > "/dev/stderr"; bad=1 }
     $1 == $2 { print "line " NR ": self-edge " $1 > "/dev/stderr"; bad=1 }
     END { exit bad+0 }' edges/dependencies.edges

awk -F '\t' 'NR>1 { print $1 }' nodes/nodes.tsv | LC_ALL=C sort -u > build/node-ids.txt
awk '{ print $1; print $2 }' edges/dependencies.edges | LC_ALL=C sort -u > build/edge-node-ids.txt
comm -23 build/edge-node-ids.txt build/node-ids.txt > build/unknown-edge-nodes.txt
if [ -s build/unknown-edge-nodes.txt ]; then
  echo "edges reference unregistered nodes:" >&2
  cat build/unknown-edge-nodes.txt >&2
  exit 1
fi

LC_ALL=C sort -u edges/dependencies.edges > build/dependencies.sorted.edges
echo "graph-check: ok"
```

## `build/build-tree.sh`

```sh
#!/bin/sh
set -eu
cd "$(dirname "$0")/.."
sh validation/graph-check.sh

# BSD tsort exits 0 on a cycle and prints to stderr -- check both.
tsort build/dependencies.sorted.edges > indexes/tsort-order.txt 2> validation/tsort-errors.txt || true
if [ -s validation/tsort-errors.txt ]; then
  echo "tsort reported a problem (cycle?):" >&2
  cat validation/tsort-errors.txt >&2
  exit 1
fi

# every supplied edge must be respected by the emitted order
awk 'NR==FNR { pos[$1]=NR; next }
     { if (!($1 in pos) || !($2 in pos) || pos[$1] >= pos[$2]) {
         print "order violation: " $1 " must precede " $2 > "/dev/stderr"; bad=1 } }
     END { exit bad+0 }' indexes/tsort-order.txt build/dependencies.sorted.edges

# reverse dependencies
awk '{ u[$1] = u[$1] " " $2 } END { for (n in u) print n ":" u[n] }' \
  build/dependencies.sorted.edges | LC_ALL=C sort > indexes/reverse-dependencies.txt

# node coverage: registered nodes with no edge are roots/isolated, list them
awk '{ print $1; print $2 }' build/dependencies.sorted.edges | LC_ALL=C sort -u > build/edge-node-ids.txt
comm -23 build/node-ids.txt build/edge-node-ids.txt > build/isolated-nodes.txt

echo "build-tree: ok ($(wc -l < indexes/tsort-order.txt) ordered nodes)"
```

Isolated/root nodes are merged into presentation views by a controlled append —
never by adding a fake prerequisite edge to force them into `tsort` output.
