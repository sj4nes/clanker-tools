# Package layout, schemas, and build scripts

## Directory skeleton

```text
<release-name>/
  README.md            what this release is, how to read it
  scope.md             included/excluded areas, level, background,
                       foundational stance, notation conventions,
                       proof policy, epistemic-status policy
  conventions.md       every notation convention, the foundational stance
                       (what is primitive and why), every cycle resolution
  notation.md          master symbol list: symbol -> meaning, type, area
  objects.md           the type vocabulary: which sets / spaces / structures
                       objects inhabit, and the well-formedness rules used

  nodes/
    nodes.tsv          the node registry (schema below)
    <id>.md            one detail page per node

  edges/
    dependencies.plan  commented prerequisite edges (evidence per edge)
    dependencies.edges generated: comments stripped, two fields per line
    relations.tsv      non-prerequisite relations (generalizes, equivalent_to, ...)
    cycles.md          every cycle found and how it was resolved

  results/
    <id>.yaml          one structured entry per theorem/lemma/identity/definition
    <area>.md          optional human-readable area notes (a VIEW, reconciled
                       against the graph, never the source of truth)

  indexes/             all GENERATED, read-only
    tsort-order.txt
    topic-index.md  symbol-index.md  hypothesis-index.md  status-index.md
    counterexample-index.md  reverse-dependencies.txt  prerequisite-paths.md
    generalization-map.md  equivalent-definitions-map.md  common-misuse-index.md

  validation/
    graph-check.sh
    tsort-errors.txt        (generated)
    type-checks.md          well-formedness worksheets + results
    proof-checks.md         lean statements + what the kernel verified vs cited
    instance-checks.md      bc worksheets: specializations, sample points,
                            counterexample computations + results
    specialization-cases.md  consistency-audit.md  coverage-audit.md

  sources/
    bibliography.md
    source-map.tsv         source_key -> title, edition, section, conventions

  build/
    build-tree.sh
    *.txt                  (generated intermediates)
```

A first, small release may collapse to: `scope.md`, `conventions.md`,
`nodes/nodes.tsv`, per-node pages, `edges/dependencies.plan`, `results/*.yaml`,
`build/build-tree.sh`, and the generated `indexes/`.

## Node registry — `nodes/nodes.tsv`

Tab-separated, one header row. Node IDs are stable, lowercase, `snake_case`, no
whitespace (they must survive `tsort`'s whitespace tokenizer).

```text
id	type	title	area	status	role	primary_statement
compactness	hypothesis	Compactness	topology	active	foundation	every open cover has a finite subcover
bolzano_weierstrass	theorem	Bolzano-Weierstrass	real_analysis	reviewed	headline	every bounded sequence in R^n has a convergent subsequence
axiom_of_choice	axiom	Axiom of choice	foundations	active	foundation	every family of nonempty sets has a choice function
```

`type` is one of: `primitive`, `notation_convention`, `definition`, `axiom`,
`structure`, `hypothesis`, `theorem`, `lemma`, `proposition`, `corollary`,
`identity`, `construction`, `algorithm`, `counterexample`, `example`, `regime`,
`bridge`, `diagnostic`.
`status`: `draft` → `reviewed` → `verified`, or `deprecated`.
`role` is a free label for view generation (`foundation`, `core`, `headline`,
`support`).

## Node detail page — `nodes/<id>.md`

```markdown
# bolzano_weierstrass

## Type
theorem

## Statement
Every bounded sequence (x_n) in R^k has a subsequence converging to a point of R^k.

## Symbols
- (x_n): a sequence, x_n in R^k for all n
- k: a fixed positive integer (the dimension)
- the limit: a point of R^k

## Epistemic status
proved_theorem (constructive_result in R^1 via bisection; the R^k case iterates
the R^1 case coordinatewise; no choice needed for R^k with the bisection proof).

## Prerequisites (tsort edges into this node)
real_number, completeness_of_R, sequence, subsequence, bounded_set,
convergence_of_sequence, monotone_convergence_theorem, nested_interval_property

## Hypotheses
Boundedness of the sequence. Ambient space R^k with the standard metric and its
completeness. Finite dimension k.

## Proof provenance
technique: bisection / nested intervals (R^1), then induction on coordinates.
derives_from: nested_interval_property (itself from completeness_of_R).
lean_status: stated; R^1 case proved via `Nat`-indexed bisection lemma;
  coordinate induction sketched, not fully formalized. See
  validation/proof-checks.md#bolzano_weierstrass.

## Type / well-formedness check
"(x_n) bounded" : predicate on sequences R -> R^k, well-formed.
"subsequence (x_{n_j})" : needs a strictly increasing n : N -> N, recorded.
"converges to L in R^k" : standard epsilon-N, L quantified existentially, ok.
(checked: validation/type-checks.md#bolzano_weierstrass)

## Specialization / boundary cases
k = 1: reduces to the classic real Bolzano-Weierstrass.
constant sequence x_n = c: the whole sequence converges, trivially a subsequence.
finite sequence range: some value repeats infinitely -> constant subsequence.

## Hypothesis-dropped counterexamples
drop boundedness: x_n = n in R has no convergent subsequence.
drop completeness (work in Q): x_n = truncation of sqrt(2) to n digits is bounded
  in Q, every subsequence is Cauchy but none converges in Q.
drop finite dimension (in l^2): the standard basis (e_n) is bounded (norm 1) but
  ||e_n - e_m|| = sqrt(2) for n != m, so no convergent subsequence.

## Common misuse
Concluding the whole sequence converges; forgetting the ambient space must be
complete; applying it in infinite-dimensional normed spaces.

## Related nodes (non-prerequisite)
equivalent_to: sequential_compactness_of_closed_bounded_sets_in_Rk (Heine-Borel circle)
generalizes_to: sequential compactness in metric spaces
proof_routes: [bisection, via Heine-Borel + sequential compactness, via limsup]

## Sources
[rudin_principles_3e] Theorem 3.6; [tao_analysis_I] Theorem 6.7.x
```

## Result entry — `results/<id>.yaml`

```yaml
id: real_analysis.bolzano_weierstrass
node: bolzano_weierstrass
status_label: proved_theorem      # epistemic status (see SKILL.md list)
display: 'Every bounded sequence in $\mathbb{R}^k$ has a convergent subsequence.'
parseable: 'bounded(x) -> exists (n_j) strictly_increasing, converges(x . n_j)'
symbols:
  x: { meaning: a sequence, type: 'N -> R^k' }
  k: { meaning: dimension, type: 'positive integer' }
  L: { meaning: subsequential limit, type: 'point of R^k' }
type_check_status: well_formed          # necessary, NOT sufficient
hypotheses: [bounded_sequence, ambient_space_complete, finite_dimension]
preconditions: [nonempty_sequence]
dependencies: [real_number, completeness_of_R, sequence, subsequence,
               bounded_set, convergence_of_sequence, nested_interval_property]
proof:
  technique: bisection / nested intervals, then coordinate induction
  derives_from: nested_interval_property
  lean_status: partial       # stated | cited | partial | proved
  lean_ref: validation/proof-checks.md#bolzano_weierstrass
uses_choice: false
constructive: true
solving_for: null
specialization_cases:
  - 'k = 1 => classical real Bolzano-Weierstrass'
  - 'constant sequence => whole sequence converges'
counterexamples_when_dropped:
  bounded_sequence: 'x_n = n in R'
  ambient_space_complete: 'digit truncations of sqrt(2) in Q'
  finite_dimension: 'standard basis (e_n) in l^2'
common_misuse:
  - 'claiming the whole sequence converges'
  - 'applying in infinite dimensions'
applications:            # OPTIONAL. Where the result is deployed in practice.
  - 'named system or paper: the mechanism, i.e. HOW this exact result is used'
  - 'e.g. "UCB1 bandit (Auer et al. 2002): the exploration radius sqrt(2 ln t / n_i)
     is a Hoeffding confidence interval -- ad selection, Yahoo news (LinUCB)"'
sources: [rudin_principles_3e, tao_analysis_I]
status: reviewed
checks:
  type: validation/type-checks.md#bolzano_weierstrass
  specialization: validation/specialization-cases.md#bolzano_weierstrass
  instances: validation/instance-checks.md#bolzano_weierstrass
  proof: validation/proof-checks.md#bolzano_weierstrass
```

For a **definition** or **axiom** node, `status_label` is `definition` /
`axiom`, `proof` is omitted, and the entry instead carries `well_definedness`
(what must be checked for the definition to make sense — independence of
representative, existence and uniqueness of the object defined) and
`equivalent_forms` (other definitions of the same concept, each with a pointer
to the equivalence lemma node).

**`applications`** (optional, most valuable on `headline`-role nodes): a short
list of places the result is *actually deployed* — a named system, algorithm, or
published result, plus the **mechanism** (how this exact statement is used).
Same evidentiary standard as `sources`: name a paper or a real system, never
"used in industry". This is operational knowledge about the result, in the same
category as `common_misuse`; it also lets `theorem-tree-tutorial` render an
"In the wild" beat after each milestone. Where an application is literally the
node's own formula at real-world parameters (the PAC sample-complexity bound,
the polling margin of error), that is a *specialization* and a tutorial may make
it a runnable block.

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

The two scripts above are identical across capsules, so the shipped capsules in
this repo carry a **two-line shim** at `validation/graph-check.sh` and
`build/build-tree.sh` that `exec`s a shared copy in
`skills/math-theorem-tree/lib/`. The listings here are the canonical source for
that copy — a new stand-alone capsule can inline them instead. The shared
`build-tree.sh` also writes `build/node-deps.txt` (per-node incoming-edge list)
for `gen-results.py` / `check-consistency.py`.

Isolated/root nodes are merged into presentation views by a controlled append —
never by adding a fake prerequisite edge to force them into `tsort` output. A
hypothesis or axiom node showing up isolated usually means a real missing edge —
some theorem *does* depend on it; add it rather than shrugging.

## View generators

Keep the index generators as small committed scripts under `build/` (e.g.
`gen-symbol-index.sh`, `gen-hypothesis-index.sh`). Derive their inputs from the
registry, not hard-coded lists — e.g. the hypothesis index iterates the node ids
whose `type` is `hypothesis` or `axiom`:

```sh
awk -F '\t' 'NR>1 && ($2=="hypothesis" || $2=="axiom") { print $1 }' nodes/nodes.tsv
```

so the view stays correct as nodes are added. The status index groups results by
their `status_label`; the counterexample index lists every
`counterexamples_when_dropped` entry keyed by the hypothesis it kills. The
symbol index is a `ptx` discovery pass followed by a whole-token confirmation
against each result's one-line statement — keep every result's statement *on the
`## Statement` header's next single line* (or the YAML `parseable:` line) so it
is indexed.
