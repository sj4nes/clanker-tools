# Representation and schema

## The formal object

A knowledge hypergraph is:

```
H = (V, E, tau_v, tau_e, A, P)
```

| Component | Meaning |
|---|---|
| `V` | Vertices / entities — people, tools, documents, tasks, claims, organizations |
| `E` | Hyperedges — events, decisions, experiments, requirements, incidents, plans |
| `tau_v` | Vertex-type map — `Person`, `System`, `Document`, `Goal`, `Constraint`, … |
| `tau_e` | Hyperedge-type map — `Decision`, `Event`, `Action`, `Requirement`, … |
| `A` | Role assignments — which vertex plays which part in which hyperedge |
| `P` | Properties / provenance — timestamps, confidence, source spans, status, access |

A hyperedge generalizes the binary edge: it connects **two or more** vertices in
one semantic unit. The point is not "many-to-many" — it is that the *joint
co-occurrence, with roles, is the fact*. Decomposing it into binary edges can
assert false combinations.

## Node types (compact starter ontology)

Model events and decisions well before you model everything.

| Type | Covers |
|---|---|
| `Entity` | Person, company, project, asset, location, concept |
| `Artifact` | Document, email, dataset, code revision, policy, message |
| `Task` | Objective, subtask, plan, proposed action |
| `Claim` | An atomic or composite assertion |
| `Constraint` | Requirement, permission, budget, deadline, policy |
| `State` | An observed condition or system snapshot |
| `Metric` | An outcome measure or KPI |

## Hyperedge types

| Type | Represents | Example |
|---|---|---|
| `Event` | A multi-party occurrence | A deployment changed latency for one customer segment in a window |
| `Decision` | A choice under evidence and constraints | The team chose rollback given the error-rate evidence and the policy |
| `Action` | An agent or human operation | The agent sent an approved report built from a named source |
| `ClaimSupport` | Evidence supports or challenges a claim | A study supports a recommendation *for a specified population* |
| `CausalHypothesis` | A conditional mechanism | A config change *may* cause failures *under high concurrency* |
| `Requirement` | A constraint applying to an objective or action | Export requires approval, correct scope, and a retention policy |
| `Experiment` | Intervention, context, measurement, outcome | An A/B test linked to its audience, metric, dates, and result |
| `Dependency` | Several things must jointly hold | A release depends on code, security sign-off, and a deploy window |
| `Contradiction` | Incompatible assertions in a shared context | Two sources disagree on the active owner of one service |
| `Outcome` | The recorded result of an action against a context | The redeploy lowered the error rate; written back after execution |

## The role vocabulary

Roles are drawn from a defined list, not free text, so that role-aware joins and
contradiction detection can compare them. A minimal set:

```
subject          the entity the edge is primarily about
actor            who performed the action / made the decision
decision_maker   who chose (for Decision edges)
approver         who authorized
selected_option  the option chosen (Decision)
rejected_option  an option considered and declined (Decision)
constraint       a Constraint node that applies
evidence         an Artifact / Claim node supporting the edge
input            a resource consumed
output           a resource produced
target           the environment / system acted on
budget           the budget authority in force
scope            the entity the assertion is limited to (project, segment, region)
operational_owner / budget_owner / data_owner   distinct ownership roles
```

If the source does not fill a role, it stays `unknown` — never guess.
`{Maya, Postgres, Atlas}` with no roles cannot say whether Maya selected,
rejected, maintained, or commented on Postgres.

## The universal property block

Every material hyperedge carries:

```yaml
id: decision_2026_0912_014
type: Decision
participants:
  - {node: "project:atlas",        role: subject}
  - {node: "person:maya",          role: decision_maker}
  - {node: "option:postgres",      role: selected_option}
  - {node: "requirement:low_ops",  role: constraint}
  - {node: "org:finance",          role: approver}
  - {node: "budget:q3_40k",        role: budget}
  - {node: "doc:arch_note_42",     role: evidence}
valid_time: {start: "2026-10-01", end: null}   # end null = open interval
recorded_at: "2026-09-12T14:20:00Z"
provenance:
  - source_id: "doc:meeting_notes_0912"
    source_span: "After Finance approved the $40k Q3 budget, Maya chose managed PostgreSQL for Atlas because the team lacked DBA capacity."
    extractor: "agent"
    extraction_time: "2026-09-12T14:20:00Z"
epistemic_status: asserted
confidence: 0.92
access_scope: "team:platform"
version: 1
```

## The epistemic-status ladder

This field prevents an agent from treating its own hypothesis as a source-backed
fact. It is the single most important property on the edge.

| Status | Meaning | May be stated as fact? |
|---|---|---|
| `asserted` | A source directly states it | Yes, with the source span |
| `observed` | Directly measured / seen in tool output | Yes, with the observation |
| `inferred` | Derived by reasoning from other edges | No — report as a conclusion, show the chain |
| `proposed` | A hypothesis (often LLM-generated) not yet tested | No — report under "uncertain" |
| `superseded` | Was `asserted`/`observed`, now overridden by a newer edge | No — retained for history only |

"Maya chose Postgres" can be `asserted`. "Postgres will reduce cost 30%" is a
prediction — `proposed` until measured. They must not sit in the same list in
the answer.

## Storage options

You do not need a native hypergraph database on day one.

| Approach | Best for | Trade-off |
|---|---|---|
| Reified event nodes in a property graph | Existing Cypher / Gremlin tooling | Hyperedges become nodes; queries get verbose |
| Relational tables + JSON roles | Transactional integrity, analytics | Multi-hop traversal needs design |
| RDF n-ary relation patterns | Semantic-web interoperability | Verbose modelling, operational complexity |
| Native hypergraph store | Higher-order traversal, research | Small ecosystem, fewer ops tools |
| Document store + vector index + hyperedge tables | Fast agent prototype | Needs disciplined provenance and consistency |

A pragmatic production layering: source layer → immutable evidence layer →
identity layer (canonical entities + aliases) → hyperedge layer → index layer
(vector, keyword, temporal, adjacency) → agent layer (retrieve → reason → plan →
verify → approve → act → record) → governance layer (access, calibration,
retention, audit).

## When not to use a hypergraph

Use ordinary documents + vector retrieval when the task is summarization or
semantic search, the relationships are mostly pairwise, or extraction quality
would be too low to trust the edges.

Use a conventional knowledge graph when binary edges preserve the meaning, you
need mature graph algorithms, or the queries are principally "who owns what" /
"what depends on what".

Use a hypergraph when the costly errors come from **context collapse**: approval
scope, multi-step incidents, scientific protocols, contracts, complex policies,
coordinated multi-agent work, or decisions gated on several joint conditions.
