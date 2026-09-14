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
