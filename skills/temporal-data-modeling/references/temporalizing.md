# Temporalizing static notions

The third desideratum of the narratives paper (D3): a theory of temporal data
should give **systematic** ways to build the temporal analogue of a static
notion, rather than hand-rolling one per case. This file is the recipe and its
applications.

## The three moves

Any static property you care about — "is a path", "is a clique", "is connected",
"has tree-width ≤ k", "is a power user" — is expressible categorically as either
(a) membership in a sub-collection of objects, or (b) the existence of morphisms
from test objects (paths, cliques, colourings). Once phrased that way, three
moves lift it to time-varying data:

### Move 1 — change of data type

If `K : C → D` converts one kind of static data to another and preserves the
constructions that define persistent (limits) or cumulative (colimits)
narratives, then post-composing with `K` transports narratives:
`F ↦ K ∘ F`. So a graph→simplicial-complex map, a graph→its-line-graph map, a
record→feature-vector map all "temporalize for free". A contravariant `K` that
swaps limits and colimits swaps persistent ↔ cumulative — useful when the
natural static operation is a dualising one (complementation, transpose).

### Move 2 — change of resolution

A sub-lattice inclusion `S ↪ T` (fewer intervals — a coarser clock) gives a
restriction functor: evaluate the narrative only on `S`. Combined with Move 1,
you get **"the property holds at resolution `S`"** rather than "at every
instant". This is how "weekly-active user" becomes well-defined: it is a
property of the narrative *restricted to week-length intervals*, not of the raw
session stream.

### Move 3 — characterization by morphisms

A static decision problem is often "does a homomorphism from a test object
exist?" (a path of length k, a k-clique, a proper k-colouring). The temporal
analogue is "does a morphism of **narratives** from the temporalized test object
exist?" — and it inherits the static problem's structure (and often its
algorithms). It also inherits static **dualities**: cliques ↔ colourings dualise
statically, and their temporal analogues dualise too — but *which* dual you get
depends on whether you work persistently or cumulatively.

## Applications

### Temporal paths and reachability

A temporal path is a subobject of a graph narrative that is, at the right
resolution, path-shaped. Persistent reading: the path's edges must all be
present *throughout* the traversal window. Cumulative reading: the edges must
appear *at some point, in order* over the window — this is the standard
"time-respecting path" of temporal-graph theory. **State which you mean.** A
reachability query answered persistently and one answered cumulatively give
different, both-valid, answers.

### Temporal cliques

Lift the sub-collection of complete graphs (Move 1), then restrict to intervals
of length ≥ n (Move 2): "a set of vertices mutually adjacent over every window
of length ≥ n". This recovers the temporal-graph literature's k-cliques as a
morphism condition on narratives.

### Structured decomposition and temporal tree-width

*Structured decompositions* (Bumpus–Kocsis–Master–Minichiello, 2025) generalise
tree-decompositions: break an object into small pieces, record how they overlap,
reconstruct by gluing. Bumpus–Nickel (2026) lift this to persistent narratives:
the **pieces are themselves time-varying**, with structure maps recording how
they persist, merge, split, or vanish — you do **not** decompose each snapshot
independently, because that loses how the pieces evolve.

The payoff is a **structural-complexity invariant for time-varying data**:
temporal tree-width. The paper's Theorem 3.9 gives conditions (pullbacks in the
data category and its spine; pushouts along monos that are also pullbacks — the
same adhesive condition as left-rigidity; a sheafification left adjoint) under
which the static width lifts. Examples worked in the paper: **maximum
tree-width** over the window (from ordinary tree-width), maximum complemented
tree-width, maximum tree independence number.

Practical use: when you need one number for "how structurally complicated is
this evolving network", temporal tree-width (max over the window of the
per-snapshot width, computed on a decomposition whose bags are time-varying) is
the principled choice — and bounded temporal tree-width is what makes dynamic
programming over the history tractable, exactly as in the static case.

### Switching-topology networks (multi-agent / comms / org charts)

Model a system whose interaction graph changes over time as a narrative valued
in graphs — or, richer, in **cellular sheaves** (a graph plus a vector space per
vertex and edge and linear maps for the incidences, encoding local state,
sensing, and what is communicated). The paper's Vignette 3:

- Each interval `[a,b]` is assigned a morphism `P^b_a → C^b_a` of cellular
  sheaves: the persistent component is the sub-system that **survives** the
  whole interval, the cumulative component is everything that **appeared** in
  it, `γ` compares them.
- A topology change from `G_{t_i}` to `G_{t_k}` is handled by pulling back the
  two inclusions into the union graph: the apex is exactly "the agents and links
  common to both" — the persistent sub-system across the switch.
- This carries strictly more information than "a sequence of communication
  graphs": it records how state spaces and interaction maps are identified
  across the switch, not just which edges exist when.

Use this when "who talks to whom" changes over time **and** you care about what
is being exchanged and whether the local state carries across a
reconfiguration — robotic swarms, sensor networks, failover topologies,
reorganising teams, evolving supply chains.

## The discipline

For every static notion you need temporalized, write down:

| slot | value |
|---|---|
| static definition | <the property, phrased as membership or a morphism condition> |
| move used | change of data type / change of resolution / morphism characterization |
| resolution | <coarsest interval length at which it is defined> |
| semantics | persistent (holds throughout) / cumulative (holds at some point, in order) |
| temporal definition | <what follows> |
| dual (if any) | <the dual notion, and whether it flips with persistent/cumulative> |
