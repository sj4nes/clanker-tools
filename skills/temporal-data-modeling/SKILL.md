---
name: temporal-data-modeling
description: >-
  Model time-varying data as a system of relations across time intervals — not a
  sequence of snapshots — so the cross-time facts survive: whether an entity at
  one time is the same one seen earlier, whether a group split or was merely
  re-measured, whether a link disappeared or was never observed. Use when
  designing a schema, event log, metrics pipeline, feature table, audit trail,
  versioned store, or forecast that changes over time; when asked to model
  temporal / longitudinal / panel / streaming data, define time-windowed
  metrics, reconcile histories from several sources, decide point-in-time vs
  as-of-now vs period-to-date semantics, or track how entities persist, merge,
  split, appear, and disappear. Enforces an explicit time base (instants vs
  intervals, fixed vs branching), a per-field classification as PERSISTENT
  (holds throughout an interval) or CUMULATIVE (accumulates over it) with the
  conversion rule and its information loss stated, cross-time identity as
  first-class transitions rather than reconstructed diffs, a declared resolution
  at which each property is visible, and a gluing check that overlapping
  intervals must agree. NOT a time-series forecasting method, not a
  temporal-database product guide, and not a licence to call a snapshot
  sequence a temporal model.
version: 0.2.0
author: Simon Janes
tags: [temporal-data, time-varying, longitudinal, panel-data, event-log, point-in-time, persistent-cumulative, entity-resolution, data-modeling, provenance, narratives, sheaves, llm-memory]
---

# Temporal Data Modeling

You are a temporal-data modelling agent. Your job is not to "add a timestamp
column" — it is to **represent time-varying data as a structured system of
relations across time, so that the facts that live *between* observations are
recorded, not thrown away**. The deliverable is a modelling package: a time
base, a field register that classifies every time-varying field, an
identity-transition log, a resolution declaration, and a gluing check — plus the
schema or pipeline that follows from them.

This skill is a practitioner's translation of the *theory of narratives*
(Leal, Bumpus, Nickel et al., *Time-Varying Data as Sheaves*, 2026): temporal
data is a (co)sheaf over a category of time intervals, not a function from
timestamps to states. You do not need the category theory to apply it. You need
the five disciplines below.

## The failure mode this skill exists to prevent

The default representation of time-varying data is a **snapshot sequence**:

```
state@t0 , state@t1 , state@t2 , ...
```

Read back, a snapshot sequence cannot answer:

| Question | Why the sequence loses it |
|---|---|
| Is `node 7` at `t1` the *same* node as `node 7` at `t0`, or was the id reused? | No identity relation between snapshots — only a coincidence of keys |
| Did team A **split** into A and B, or was B always there and just first measured at `t1`? | Appearance of a row ≠ a split event |
| Did the edge `A–B` **disappear**, or was it simply **not observed** in this window? | Absence in a snapshot conflates "gone" with "unknown" |
| Is this balance the value **at** `t1`, or the total **accumulated up to** `t1`? | The field carries no persistent/cumulative marker |
| Two sources disagree on the `t1` snapshot — is that a conflict or a resolution difference? | No rule for how sub-interval data must agree on overlaps |

Every one of these is a **cross-time relation**. The snapshot sequence records
the states and drops the relations. This skill makes the relations first-class.

## The two semantics: persistent vs cumulative

For every time-varying field you must decide which of two things it is. This is
the load-bearing distinction.

| | **Persistent** | **Cumulative** |
|---|---|---|
| Meaning | The value **holds throughout** the interval | The value **accumulates over** the interval |
| Interval `[a,b]` is rebuilt from parts by | **agreement** — the pullback / intersection of what sub-intervals say | **aggregation** — the pushout / union of what sub-intervals contribute |
| Sub-interval `[a,c] ⊆ [a,b]` gives | a **restriction** (what still holds on the smaller window) | a **partial total** (what accumulated so far) |
| Examples | account balance at a date; currently-active membership; a sensor's current reading; a configuration in force | transactions in a month; distinct users seen in a quarter; total downtime over a window; every file ever touched |
| Query phrasing | "as of", "in force on", "current" | "to date", "over the period", "ever", "total" |

**Both views of the same underlying phenomenon are legitimate**, and they carry
**different information**. "Active members on 2026-06-30" (persistent) and
"members active at some point in June" (cumulative) are different facts. A
metric that silently mixes them is a defect.

### Conversion and its information loss

You can convert between the two, and you must state the rule and whether it is
reversible:

- **persistent → cumulative** (`K`): accumulate the persistent values over the
  interval — union, sum, max-extent. Example: daily "is active" → monthly "was
  active at some point".
- **cumulative → persistent** (`P`): extract what is compatible across all
  sub-intervals — intersection, the common part. Example: "files touched this
  week" → "files touched *every* day this week".

A **round trip is generally lossy.** Classify each convertible field:

| Class | Meaning | Practical consequence |
|---|---|---|
| **rigid** | both round trips recover the original | either view is a faithful store; convert freely |
| **left-rigid** | persistent → cumulative → persistent recovers the persistent value | safe to store cumulatively and derive the persistent view; not the reverse |
| **right-rigid** | cumulative → persistent → cumulative recovers the cumulative value | safe to store persistently and derive the cumulative view; not the reverse |
| **loose** | neither round trip recovers | you must store **both**, or pick one and document the loss |

A useful sufficient condition: if the persistent values across an interval are
related only by **inclusions** (memberships that only grow or only shrink, never
crossing), the field is left-rigid — the accumulate-then-restrict round trip is
exact. Sets that both gain and lose members over the interval are typically
loose.

## Cross-time identity: transitions, not diffs

An entity observed at two times is connected by an explicit **transition**, from
a fixed vocabulary — never inferred from a key match or a row diff:

| Transition | Meaning |
|---|---|
| `persist` | same entity, carried forward (optionally with attribute changes) |
| `appear` | genuinely new — did not exist before, not merely first observed |
| `disappear` | genuinely gone — ended, not merely unobserved this window |
| `merge` | two-or-more prior entities become one |
| `split` | one prior entity becomes two-or-more |
| `unobserved` | the entity's state in this window is unknown (explicitly, not silently) |

`unobserved` is a real value. Conflating it with `disappear` is the most common
temporal-data bug: a gap in coverage gets read as an event.

## Resolution: the granularity a property is visible at

Some properties only exist after aggregating over a wide enough window. "This
user is a weekly-active user" is not visible at the resolution of a single
session. Declare, per property, the **coarsest resolution** at which it is
defined, and evaluate it by **restricting to that resolution first, then
checking** — not by checking at raw granularity and hoping.

## The gluing check

Overlapping intervals must tell a consistent story. If `[a,c]` and `[c,b]` cover
`[a,b]`, then:

- **persistent fields**: the value on `[a,b]` must equal what `[a,c]` and
  `[c,b]` *agree on* at the shared instant `c` (pullback over `[c,c]`).
- **cumulative fields**: the value on `[a,b]` must equal the contribution of
  `[a,c]` and `[c,b]` *combined*, not double-counting the overlap (pushout over
  `[c,c]`).

A model where reconciling two windows depends on which order you glue them, or
where the overlap is silently double-counted or dropped, fails the check.

## Branching time

Time is not always a line. A version-control history, a set of scenario
forecasts, a "what-if" tree, or a plan with alternative futures is **branching**
time. The interval model still applies — intervals live on a tree instead of a
line — but every field's semantics, identity transitions, and gluing check must
be stated per branch, and merges across branches are `merge` transitions with
their own conflict rule.

## When a language model is the downstream reader

If an LLM consumes the temporal data — an agent memory, a RAG pipeline, a
"summarize this account's history" step — the representation you hand it matters
as much as the model. **The model will not do the interval reconciliation for
you.** Give it the raw versioned rows or the full set of relevant sessions and
expect it to derive current-state-per-field, notice that a proposed decision
conflicts with the trajectory, or keep persistent and cumulative straight — and
it largely will not, *even when every row it needs is in context*.

Evidence: PRAGMA (Yu et al., *Evaluating Personalized Guidance with Memory
Alignment in Lifelong Conversations*, 2026). On guidance grounded in an evolving
user trajectory, handing the model the gold evidence sessions **raw** scored
78 / 17 (alignment / grounding); the **same evidence pre-distilled into a
trajectory summary** scored 99 / 86. Retrieval was not the bottleneck —
representation was. Raw-content memory systems preserved ~99% of the evidence
but under half of it survived into the response; summarized memories preserved
less yet were used more.

What this skill's disciplines give you is exactly the artifact to hand over:

- **Feed the derived facts, not the event stream.** The current persistent value
  per field *as of now*, the identity-transition log, and the cumulative rollups
  the question actually needs — materialized. The field register and
  identity-transition log *are* that distilled representation; put them in the
  prompt, not the raw history.
- **Diagnose a model-facing pipeline in three stages:** preservation (did the
  derived temporal fact survive ingestion?) → retrieval (did it get selected for
  this query?) → utilization (did the model use it?). A pipeline can preserve
  raw history perfectly and still fail utilization because it never built the
  persistent / cumulative view — the failure is upstream of the model.
- **An ungrounded temporal answer becomes next turn's input.** If one turn
  silently drops a persistent constraint ("low-salt meal plan in force"), the
  next turn reasons from the degraded state and the error compounds. Grounding
  each temporal claim to its interval evidence is what stops the drift.

## Principles

- **No time base, no model.** State it first: are observations at instants or
  over intervals; is time a line or a tree; what is the finest granularity;
  what is the time zone and calendar; is the clock event-time or
  processing-time. `templates/temporal-charter.md`.
- **Classify every time-varying field as persistent or cumulative.** Not "it has
  a timestamp" — *which semantics*. Record the conversion rule to the other view
  and the round-trip class (rigid / left-rigid / right-rigid / loose). A field
  you cannot classify is a field you do not yet understand.
  `templates/field-register.md`.
- **A snapshot sequence is not a temporal model.** If the design is
  `list<state>` with no identity transitions and no persistent/cumulative
  marks, say so and add them. The states are the easy part; the relations are
  the point.
- **Identity is asserted, never diffed.** Every entity carried across a time
  boundary gets a `persist` / `appear` / `disappear` / `merge` / `split` /
  `unobserved` transition with its evidence. Do not reconstruct history from key
  equality. `templates/identity-transition-log.md`.
- **`unobserved` ≠ `disappear`.** Absence of data is its own state. A coverage
  gap must never be recorded as an event, and a metric must never treat a
  missing window as a zero unless zero is genuinely observed.
- **Declare the resolution each property needs.** Evaluate coarse-grained
  properties by restricting to their resolution and then checking, not by
  checking at raw granularity.
- **Overlaps must glue.** Run the gluing check: persistent fields agree on the
  shared boundary, cumulative fields combine without double-counting, and the
  result does not depend on gluing order.
- **Store the view you can't derive.** If a field is loose, store both the
  persistent and cumulative forms, or store one and document — in the register —
  exactly what the other view loses.
- **When a language model reads the data, hand it the derived facts, not the raw
  history.** Materialize the as-of persistent values, the transition log, and the
  needed cumulative rollups; do not expect the model to reconstruct them from
  versioned rows in context. Grounding beats retrieval volume.
- **Reconcile multi-source histories per interval, not per snapshot.** When two
  sources both describe a period, align them on intervals and check the gluing
  condition; a disagreement at one instant may be a resolution-mismatch that
  the interval view dissolves.
- **Calibrated language.** "persistent, as of <date>", "cumulative, period to
  date", "loose round trip — both views stored", "coverage gap, state
  unobserved", "split asserted from <evidence>", "sources reconciled on
  <interval>, conflict at <instant> retained". Never "the history shows" for a
  fact that was diffed rather than asserted; never a period total reported as a
  point-in-time value.

## Workflow

1. **Write the temporal charter and gate on it.** Time base (instants vs
   intervals; line vs tree; finest granularity; clock type; time zone),
   the entities that vary, the questions the model must answer, the decisions
   those answers feed, and the reversibility of getting the model wrong. List
   assumptions for gaps; ask only blocking questions.
   [`templates/temporal-charter.md`](templates/temporal-charter.md).
2. **Enumerate the time-varying fields.** Every attribute, relationship, and
   metric whose value depends on when you ask.
3. **Classify each field.** Persistent or cumulative; the query phrasing that
   fits; the conversion rule to the other view; the round-trip class. Flag loose
   fields for dual storage.
   [`templates/field-register.md`](templates/field-register.md).
   [`references/narratives-and-semantics.md`](references/narratives-and-semantics.md).
4. **Define the identity model.** For each entity type, the key, and the
   transition vocabulary that applies. State how each transition is detected and
   what evidence records it. Decide the policy for `unobserved`.
   [`templates/identity-transition-log.md`](templates/identity-transition-log.md).
5. **Derive temporal analogues of the static notions you need.** For each
   static property or metric (a path, a clique, a "power user", a tree-width, a
   connected component), state: the static definition, the resolution it needs,
   whether it is evaluated persistently or cumulatively, and the temporal
   definition that follows.
   [`references/temporalizing.md`](references/temporalizing.md).
6. **Run the gluing check.** Pick a covered interval and its sub-intervals;
   verify persistent fields agree on the boundary and cumulative fields combine
   without double-count; verify order-independence. Do this on real or realistic
   data, not just on paper.
   [`references/checks-and-evaluation.md`](references/checks-and-evaluation.md).
7. **Reconcile sources.** If more than one source feeds the model, align them on
   intervals, apply the gluing check across sources, and record any retained
   conflict with both sources and the interval it occurs on.
8. **Emit the schema or pipeline.** The tables / events / transforms that follow
   from steps 1–5, with the persistent/cumulative mark and the identity
   transition carried through into column names, view definitions, and metric
   docs — not left implicit.
9. **Report with limits.** The time base; the field register with round-trip
   classes; the identity model and `unobserved` policy; the temporal analogues
   derived; the gluing-check result; the source reconciliation and retained
   conflicts; the fields stored in both views and why; and explicit non-claims —
   in particular, never that a snapshot sequence with keys is a temporal model.

## Method selection

| Situation | Primary move | What it must produce |
|---|---|---|
| "Add history to this table" | Charter + field register | Each column marked persistent (valid-time row versioning) or cumulative (running aggregate); the two not mixed in one column |
| A metric that "looks wrong over long windows" | Classify the metric | Whether it is persistent or cumulative; if the pipeline sums a persistent field or intersects a cumulative one, the bug is named |
| Rows appearing/disappearing between loads | Identity model | A transition per change: `appear` vs first-`observed`, `disappear` vs `unobserved`, `merge`/`split` with evidence |
| "Distinct users this quarter" from daily tables | persistent → cumulative (`K`); check left-rigidity | The accumulation rule (union of daily actives); confirmation the daily→quarterly→daily round trip is exact, or a note that it is not |
| "Users active every day this week" from a weekly set | cumulative → persistent (`P`) | The intersection rule; a note that this is generally *not* reversible back to the weekly set |
| Temporal graph question (path/clique/reachability) | Derive the temporal analogue | Static definition + resolution + persistent-or-cumulative + the temporal definition; not an ad-hoc reimplementation |
| Two systems' histories disagree at an instant | Interval reconciliation | Alignment on intervals; the gluing check across sources; the conflict retained with both sources if it survives |
| A property invisible at raw granularity ("weekly active") | Resolution declaration | The coarsest resolution it is defined at; evaluation by restrict-then-check |
| Version history / scenario tree | Branching-time model | Per-branch field semantics and identity; cross-branch merges as `merge` transitions with a conflict rule |
| An LLM / agent memory / RAG step consumes the history | Distil to a model-facing representation | The as-of persistent values, transition log, and needed cumulative rollups — materialized into the prompt, not raw versioned rows; a preservation → retrieval → utilization check on the pipeline |
| An invariant that must hold across all intervals ("balance never negative in any window") | Hand the core to `lean` or `tla-checker` | A machine-checked statement of the interval invariant with its out-of-model assumptions listed |

## Guardrails — refuse or escalate when

- There is no time base — no statement of instants vs intervals, granularity,
  clock type, or (line vs tree).
- A field is used in a metric or join without a persistent/cumulative
  classification, or one column carries both semantics depending on the row.
- A persistent field is being summed across time, or a cumulative field is being
  intersected / treated as point-in-time.
- Identity across time is being reconstructed from key equality or row diffs
  instead of asserted transitions.
- A coverage gap is being recorded as `disappear`, or a missing window is being
  treated as a zero without zero being observed.
- A loose field is stored in one view only, with no note of what the other view
  loses.
- Overlapping intervals are reconciled in a way that depends on gluing order, or
  double-counts / drops the overlap.
- A coarse-grained property is evaluated at raw granularity.
- A snapshot sequence with primary keys is being presented as a temporal model.
- Raw versioned rows or a full session history are being fed to a language model
  with the expectation that it will derive current state, detect trajectory
  conflicts, or keep persistent/cumulative straight — instead of handing it the
  materialized derived facts.
- The work is being used to manufacture confidence ("we modelled the history,
  so the number is right") without the field classification and the gluing
  check.

## References

- [`references/narratives-and-semantics.md`](references/narratives-and-semantics.md)
  — the narrative picture in full: time categories and the interval lattice, the
  persistent (sheaf) and cumulative (cosheaf) conditions stated without jargon,
  the `K ⊣ P` conversion adjunction, the unit/counit as the round-trip
  comparison, the rigidity classification (rigid / left-rigid / right-rigid /
  loose) with the monomorphism sufficient condition, and worked
  persistent-vs-cumulative examples.
- [`references/temporalizing.md`](references/temporalizing.md) — deriving
  temporal analogues of static notions by three moves (change of data type,
  change of resolution, characterization by morphisms); temporal paths, cliques,
  and reachability; structured decomposition and temporal tree-width as a
  structural-complexity invariant for time-varying data; switching-topology
  multi-agent / network models as interval-indexed graphs with persist/merge/
  split on vertices and edges.
- [`references/checks-and-evaluation.md`](references/checks-and-evaluation.md) —
  the gluing check as a concrete procedure, multi-source interval reconciliation,
  the `unobserved` policy, evaluation metrics (classification coverage,
  round-trip-loss disclosure, identity-transition precision, gluing-check pass
  rate, resolution correctness, reconciliation conflict retention), the failure
  modes, and the "when a snapshot sequence is actually fine" decision.

## Templates

- [`templates/temporal-charter.md`](templates/temporal-charter.md) — the time
  base, the varying entities, the questions and decisions, the reversibility of
  a wrong model.
- [`templates/field-register.md`](templates/field-register.md) — one row per
  time-varying field: persistent/cumulative, query phrasing, conversion rule,
  round-trip class, storage decision.
- [`templates/identity-transition-log.md`](templates/identity-transition-log.md)
  — one row per entity crossing a time boundary: transition, evidence,
  attribute changes, `unobserved` handling.

[`verification/`](verification/) (`sh verification/run.sh`) re-solves a
known-answer case — a daily active-membership log with one merge, one coverage
gap, and one field of each semantics — and asserts each prescribed check fires:
the persistent view summed across days over-counts while the correct
as-of query does not (`bc`); the daily→monthly→daily round trip is exact for the
inclusion-only field (left-rigid) and lossy for the churning field (loose)
(`bc`); the gluing check passes for a consistent cover and fails when the
overlap instant is double-counted (`py`); a coverage gap scored as `disappear`
produces a spurious churn event that the `unobserved` policy suppresses (`py`);
and a "weekly active" property evaluated at daily granularity disagrees with the
restrict-then-check result (`py`).

## Completion report

Report: the time base as charted; the field register with every time-varying
field classified persistent or cumulative and assigned a round-trip class; the
identity model with its transition vocabulary and `unobserved` policy; the
temporal analogues derived and the resolution each needs; the gluing-check
result on real or realistic data; the multi-source reconciliation and any
retained conflicts with their intervals; the fields stored in both views and
what each single view would lose; if a language model reads the data, the
model-facing distilled representation and the preservation → retrieval →
utilization check; and explicit non-claims — above all, never
that a keyed snapshot sequence is a temporal model, and never a cumulative
quantity reported as point-in-time or vice versa.
