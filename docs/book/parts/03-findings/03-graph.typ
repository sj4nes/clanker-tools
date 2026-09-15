#import "../../preamble.typ": keyterm, headline

= A graph that could not be wrong

#headline[36 edges][
  that the node text required and the dependency graph did not carry — plus 7
  result files, in two capsules, that had never been successfully parsed by
  anything.
]

== Hygiene has no opinion about truth

The capsules are dependency graphs: each node's prerequisites precede it, and
`tsort` produces a valid linearisation. The build checked the emitted order
against the edge list it had been handed.

Restating the edges and comparing them to themselves certifies nothing — the
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

Gating on it over fourteen capsules found #keyterm[18 hard violations] —
dependency lists disagreeing with the graph, one formula entry with no
prerequisite line at all, one holding prose where the list belongs — and about
55 soft hits, of which #keyterm[36 were real missing edges].

And then the finding nobody was looking for. The checker had to *load* every
result file to read it, and #keyterm[7 files in two capsules did not parse at
all]. They were in the two capsules that had no consistency checker. Nothing had
ever read them.

== Two of the corrections were to the harness

Which is the expected yield of building one. The soft scan first fired on
contrast text and symbol definitions — about 180 hits, mostly noise — and had to
be narrowed twice. And the deleted-edge mutation matched its target line
#emph[literally], so a trailing `\# evidence` comment made the deletion silently
do nothing: #keyterm[a mutation that reports itself as surviving].

A falsifiability harness that cannot falsify itself is the same defect one level
up, and it appeared while fixing the first instance of it.
