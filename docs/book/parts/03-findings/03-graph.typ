#import "../../preamble.typ": keyterm, headline, practice, chref

= A graph that could not be wrong <ch-graph>

#headline[36 edges][
  that the node text required and the dependency graph did not carry—plus 7
  result files, in two capsules, that had never been successfully parsed by
  anything.
]

== What a capsule is

// DRAFT 2026-09-16 (agent-written, at the author's request). Ledger: C-III-01.
Most skills in this corpus are what the earlier chapters describe: a SKILL.md
of instructions that changes what an agent does. Fourteen are something less
familiar, and this chapter is about them. The corpus calls them
#keyterm[knowledge capsules].

A capsule packages a body of domain knowledge—probability, linear algebra,
thermodynamics, electrochemistry—as a graph rather than as prose. Each
definition, axiom, theorem, formula or counterexample is a #keyterm[node], with
an entry of its own: the precise statement, its symbols, its hypotheses, what
it depends on, and how it is checked. Each #keyterm[edge] records that one node
is a prerequisite of another, with a comment giving the evidence. `tsort` turns
the edges into an order in which nothing is used before it is stated.

A single node shows the shape. In `math-probability`, Bayes' theorem lists
three dependencies in its entry—conditional probability, the law of total
probability, the multiplication rule—and the capsule's edge file carries the
same three as edges into `bayes_theorem`. Its entry also points at a Lean
proof of the step that needs one, and the capsule's `bc` script checks a
numeric instance.

The fourteen hold about 1,500 nodes between them. What they are #emph[for] is
traceability: an agent asked what a result rests on reads a chain it can
follow and check, instead of recalling one. The domain content is outside this
book's scope. The structure is not, because every part of it makes a claim—an
edge claims a dependency, a `lean_status` claims a proof—and each of those
claims can be checked or left unchecked.

== Hygiene has no opinion about truth

`tsort` must be able to order every capsule's nodes so that each node's
prerequisites come before it.#footnote[The
previous two chapters mention capsules in passing; this is where their
structure starts to matter.] The build checked the emitted order
against the edge list it had been handed.

Restating the edges and comparing them to themselves certifies nothing—the
same objection the `bc` chapter makes about restating a formula. Established,
again, by planting defects rather than by reading the scripts:

#table(
  columns: (1fr, auto, auto),
  align: (left, center, left),
  table.header([*planted defect*], [*caught?*], [*by what*]),
  [a cycle (reverse an edge)], [yes], [the stderr guard],
  [an edge to an unregistered node], [yes], [the endpoint check],
  [a self-edge], [yes], [a field scan],
  [*a real edge deleted*], [*no*], [nothing],
  [*a spurious edge added*], [*no*], [nothing],
)

The first three are #emph[hygiene]: is the graph well-formed? The last two are
#emph[truth]: are these the right edges? A capsule can be perfectly well-formed
and entirely wrong.

(`tsort` contributes its own version of the recurring problem: BSD `tsort`
#keyterm[exits 0 on a cycle], writing `cycle in data` to stderr. Cycle detection
has to read stderr, not the status.)

== The oracle that was already there

The fix required an oracle independent of the edge list, and one existed without
being used. Every node carries text written separately from the graph: a
`dependencies:` list, a `Prereqs:` line, a proof or derivation naming what it
rests on. That independence is what makes it evidence rather than an echo.

Gating on it over fourteen capsules found #keyterm[18 hard violations]—dependency lists disagreeing with the graph, one formula entry with no
prerequisite line at all, one holding prose where the list belongs—and about
55 soft hits, of which #keyterm[36 were real missing edges].

And then the finding nobody was looking for. The checker had to *load* every
result file to read it, and #keyterm[7 files in two capsules did not parse at
all]. They were in the two capsules that had no consistency checker. Nothing had
ever read them.

== Two of the corrections were to the harness

Which is the expected yield of building one. The soft scan first fired on
contrast text and symbol definitions—about 180 hits, mostly noise—and had to
be narrowed twice. And the deleted-edge mutation matched its target line
#emph[literally], so a trailing `\# evidence` comment made the deletion silently
do nothing: #keyterm[a mutation that reports itself as surviving].

A falsifiability harness that cannot falsify itself is the same defect one level
up, and it appeared while fixing the first instance of it.

The practice for this finding is @pr-oracle, in #chref(<ch-oracle>).
