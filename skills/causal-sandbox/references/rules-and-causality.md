# Rules and causality

The rule formalism, how a causal graph falls out of it, and the confluence check
that decides whether a causal claim is meaningful.

## The state schema

State is a **typed relational store**: a set of entities each with a type, a set
of relations over them, and a set of fields whose values change. Concretely, a
state `S` is a set of ground facts:

```
role(admin)                       -- entity
user(alice)                       -- entity
holds(alice, admin)               -- relation
stock(widget) = 40                -- field
threshold(widget) = 25            -- field
```

Two rules on the schema:

- **Everything the rules touch is in the store.** If a rule's behaviour depends
  on wall-clock time, a random draw, or an external service, that input is a
  field in the store (`now = 5`, `coin = heads`), set explicitly at the start of
  the step. No hidden inputs — a hidden input is an undeclared read.
- **Classify every varying field persistent or cumulative** and declare its
  resolution. `stock(widget)` is persistent (its value *is* the level now);
  `total_consumed(widget)` is cumulative (it accumulates over the run). This is
  [`temporal-data-modeling`](../../temporal-data-modeling/SKILL.md)'s discipline
  — a field summed when it should be read as-of, or vice versa, is a bug the
  sandbox will faithfully propagate.

## A rule

A rule is a guarded transition:

```
rule reorder(item):
  guard:     stock(item) < threshold(item)  ∧  ¬pending_order(item)
  reads:     stock(item), threshold(item), pending_order(item)
  writes:    pending_order(item)
  effect:    pending_order(item) := true
```

| Part | Meaning | Constraint |
|---|---|---|
| **name + parameters** | the rule and the entities it binds (`reorder(item)`) | parameters are typed; the engine enumerates bindings over entities of that type |
| **guard** | a predicate over the store; the rule is *enabled* in states where it holds | the guard may reference only fields in the **read-set** |
| **read-set** | every field the guard and the effect inspect | declared, not inferred; the engine rejects a rule whose guard/effect reads an undeclared field |
| **write-set** | every field the effect changes | declared; the engine rejects an effect that assigns outside it |
| **nondeterministic?** | whether one enabled binding can produce more than one successor state | a nondeterministic rule branches the trace; its choices must be finite and enumerable |
| **justification** | why this rule models the domain faithfully | one or two sentences a domain owner can check |
| **source** | where the rule comes from — a policy doc, a spec section, an SLA, an observed procedure | a rule with no source is a rule nobody has agreed to |

**The read-set / write-set declaration is the load-bearing part.** It is not
documentation. The engine enforces it at every step, and the causal graph is
derived from it. A rule that "just reads a little extra" or "also nudges" a field
it did not declare produces a causal graph that is quietly wrong.

## An event and a trace

Applying an enabled rule under a specific parameter binding, in a specific state,
is an **event**: `e = ⟨reorder, {item ↦ widget}, S_before, S_after⟩`.

A **trace** is a tree of states connected by events:

- the root is the initial state;
- each edge is one event;
- the tree **branches** when the agent compares interventions (one branch per
  intervention) or when a nondeterministic rule fires (one branch per choice);
- each branch is labelled with the intervention or choice that created it.

The **scheduler** decides, among the enabled events in a state, which fires next.
It is seeded. Same initial state + same rules + same seed → the same trace. Two
common schedulers: *priority* (a fixed rule order, ties broken by binding order)
and *round-robin*. The scheduler choice is part of the scenario and is reported.

## The causal graph

Given a path `S_0 --e_1--> S_1 --e_2--> ... --e_n--> S_n` through the trace:

> Event `e_j` **causally depends on** event `e_i` (`i < j`) iff
> `writeset(e_i) ∩ readset(e_j) ≠ ∅` and no event between them overwrote every
> field in that intersection.

The causal graph is the transitive reduction of that relation over the path's
events. It answers:

- **forward** — "what did `e_i` enable?": the events reachable from `e_i` along
  causal edges;
- **backward** — "why did `e_j` happen?": the events `e_j` is reachable *from*,
  back to facts in `S_0`.

Because the read-set and write-set are declared and enforced, building this graph
is a set-intersection per event pair — no dataflow analysis, no instrumentation,
no guessing. That is the whole reason the formalism constrains rules this way.

### Root causes

Trace a backward walk to its leaves and you reach either events with no causal
predecessor or **initial facts** in `S_0` that some event's guard read. Those
initial facts are the root causes — and they are exactly the search space for a
backward "what prevents this" query (see
[`forward-and-backward.md`](forward-and-backward.md)).

## Confluence

A causal graph is only meaningful where **the order in which the scheduler fired
independent events did not change the outcome**. Where order matters, "A caused
B" is an artifact of the seed.

### What is and is not a conflict

Two enabled events **interleave harmlessly** if firing them in either order
reaches the same state. Example: `grant(bob, editor)` and `grant(carol, viewer)`
touch disjoint facts — either order, same result. Not a conflict.

Two enabled events **conflict** if:

1. both are enabled in some reachable state, and
2. `writeset(e_1) ∩ (writeset(e_2) ∪ readset(e_2)) ≠ ∅` (or symmetrically), and
3. firing them in the two orders reaches **different** states.

Example: `grant(alice, admin)` and `revoke(alice, admin)` — order decides whether
alice ends holding the role. A conflict.

Interleaving that **diverges and then reconverges** is fine — that is just the
diamond property, and the causal graph is well-defined on it. Only a *persistent*
divergence is a conflict.

### The convergence of three names

| Field | Name | Statement |
|---|---|---|
| Term rewriting | **confluence** / Church–Rosser | if `a → b` and `a → c` then some `d` with `b →* d` and `c →* d` |
| Wolfram Physics Project | **causal invariance** | the causal graph is independent of the updating order |
| [`temporal-data-modeling`](../../temporal-data-modeling/SKILL.md) | **the gluing check** | overlapping intervals must agree on their shared boundary; the reconciled result does not depend on gluing order |

They are the same requirement viewed from rewriting, from physics, and from data
modelling. This skill checks it because **the agent's causal claim is only valid
on a confluent slice**.

### The confluence pass

Per scenario slice (a bounded region of the trace):

1. **Enumerate reachable states** within the slice's bound (small — this is a
   scenario, not an exhaustive check; for exhaustive reachability use
   [`tla-checker`](../../tla-checker/SKILL.md)).
2. **For each state with ≥ 2 enabled events**, test each pair against the
   three-part conflict definition.
3. **For each conflicting pair, resolve it:**

   | Resolution | How | When |
   |---|---|---|
   | **Commute** | rewrite the rules so order does not matter — e.g. make `revoke` a no-op if a later `grant` is pending, or split the field so the two rules touch disjoint parts | the conflict is incidental; the domain does not actually care about order |
   | **Arbitrate** | add an explicit rule that fixes order — a priority, a tie-break predicate, a request queue with FIFO discipline | the domain *does* care about order and there is a real rule for it (e.g. "deny wins over allow") |
   | **Accept non-confluence** | mark the slice; the deliverable for that slice becomes a **branch set**, not a causal graph | order genuinely is unresolved in the domain (a race) — and the honest answer is "it depends on timing" |

4. **Record the verdict per slice** in the trace report. A confluent slice gets a
   causal graph. A non-confluent slice gets "under order ⟨e_1, e_2⟩: outcome X
   with causal graph G_X; under ⟨e_2, e_1⟩: outcome Y with causal graph G_Y" —
   and the agent is told, explicitly, that there is no single "A caused B" here.

### The guardrail with teeth

If the confluence pass flags a slice and someone still wants a single causal
answer for it, that is the refuse-or-escalate condition. The verification case
demonstrates the failure directly: a causal claim read off the non-confluent
`grant`/`revoke` slice flips when the scheduler seed flips — so any single claim
was a coin toss.

## Bounds

Every sandbox is finite and every bound is a modelling claim:

- **entities** — how many users, items, nodes; named explicitly;
- **steps** — the maximum trace depth per branch;
- **value domains** — `stock ∈ 0..100`, not `stock ∈ ℕ`;
- **branching** — the maximum number of intervention branches and the maximum
  nondeterministic fan-out.

A consequence that appears only at step `budget + 1`, or only with a 4th entity,
is **not observed within the bound** — never "will not happen". This mirrors
[`tla-checker`](../../tla-checker/SKILL.md)'s stance on its state bound exactly.
