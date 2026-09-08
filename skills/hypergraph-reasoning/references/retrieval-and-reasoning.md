# Retrieval and reasoning

A hypergraph agent retrieves an **evidence sub-hypergraph**, not top-k text
chunks. The output handed to the model is a *reasoning packet*: facts,
citations, conflicts, unknowns, candidate actions.

## Retrieval pipeline

1. Parse the request into entities, the action, the desired outcome, the
   constraints, and the time scope.
2. Retrieve candidate documents by lexical / vector similarity.
3. Resolve mentions to graph nodes.
4. Seed traversal from the query entities, the constraints, and the relevant
   evidence spans.
5. Expand across high-value hyperedge types: `Decision`, `Requirement`,
   `Action`, `ClaimSupport`, `Dependency`.
6. Rank hyperedges (score below).
7. Return a compact reasoning packet: facts, citations, conflicts, unknowns,
   candidate actions — not everything connected.

## The ranking score

```
score(e, q) = alpha * rr(e,q)    query relevance (lexical + embedding)
            + beta  * aa(e)       source authority
            + gamma * cc(e)       edge confidence
            + delta * tt(e,q)     temporal compatibility with the task window
            + eps   * ss(e,q)     structural fit
```

**Structural fit `ss`** is the term that makes this hypergraph retrieval rather
than graph-walking: it scores whether the edge actually contains the *roles the
decision needs*. A `Decision` edge that names the approver, the scope, and the
budget scores high for an authorization question; a lexically-closer `Event`
edge that mentions the same nouns but has none of those roles scores low. A
role-complete edge should outrank a role-poor one even when the role-poor one
has higher raw text similarity — this is verified in `verification/`.

Keep the component values visible. The blended number is a ranking aid, not a
truth measure.

## The reasoning operators

### 1. Neighbourhood grounding

Find the minimal connected sub-hypergraph sufficient to answer or act. Start
from the task nodes; expand through typed, role-compatible edges; stop when the
chain reaches evidence, an active constraint, or a verified outcome. Do not
pull in everything one hop away.

### 2. Role-aware joins

Graph traversal asks "what is adjacent?". Hypergraph reasoning asks: *which
`Decision` edges have this project as `subject`, this person as `approver`, and
this policy as an active `constraint`?* This is relational query processing over
event records, not generic walking.

### 3. Constraint intersection

For a candidate action `a`, compute `C(a)` = the constraints that apply under
the current context. Mark each:

| Status | Meaning | Response |
|---|---|---|
| `satisfied` | A time-valid edge shows it holds | Proceed on this conjunct |
| `violated` | A time-valid edge shows it fails | Block; report the edge |
| `unknown` | No edge settles it | Targeted retrieval, or one narrow question, before a high-impact step |
| `conflicting` | Two credible edges disagree | Contradiction detection; do not pick silently |

### 4. Contradiction detection

Two hyperedges conflict when they have overlapping **subject and relation
roles**, incompatible values, overlapping time / context, and credible sources.

- `operational_owner(payments) = Team A` and `budget_owner(payments) = Team B`
  — **no contradiction**; the roles differ.
- `operational_owner(payments) = Team A` and `operational_owner(payments) =
  Team C`, same window — **a contradiction**; surface both sources and the
  check that would resolve it.

Role typing is exactly what separates the two cases. A role-blind check
(matching `{payments, owner, *}`) raises a false alarm on the first pair.

### 5. Temporal-scope resolution

For a time-scoped question, evaluate against `valid_time`. An approval with
`end` before the task date does not hold. A `Requirement` with `start` after an
approval and no `end` supersedes it within its window — mark the approval
`superseded`, keep it for history, answer from the policy.

### 6. Precondition conjunction

`Allowed = c1 ∧ c2 ∧ … ∧ cn` over the time-valid context. Every conjunct must
map to a supporting edge. The first `false` or `unknown` conjunct is the answer
— name it. A single satisfied conjunct (a "release is ready" note) is not a
partial yes; it is one term.

### 7. Counterfactual precondition test

Represent a proposed action as an *uncommitted* hyperedge with its preconditions
listed, and check their availability *before* any commitment. This is how you
answer "what would have to be true for us to do X?" without doing X.

### 8. Provenance-aware synthesis

The final answer separates claims by epistemic status: `asserted` / `observed`
claims (each with a source span) go in the facts list; `inferred` claims are
reported as conclusions with their chain; `proposed` claims go under
"uncertain". A `proposed` hypothesis rendered as a fact is a synthesis failure,
caught in `verification/`.

## Example query

**"Can the agent deploy version 4.2 to production today?"**

Retrieve the sub-hypergraph around: Release 4.2, the production environment, the
deploy policy, the change window, the security sign-off, the test results, the
current incident state, the deployer's permission, the rollback plan.

Do **not** answer "yes" because a release note says 4.2 is ready. The answer is:

```
DeployAllowed = TestsPass
              ∧ SecurityApproved
              ∧ WindowOpen
              ∧ PermissionGranted
              ∧ NoBlockingIncident
```

evaluated over edges that are valid *today*. Report the first conjunct that is
`false` or `unknown`, with its edge (or its absence).
