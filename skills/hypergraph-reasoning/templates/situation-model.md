# Situation model — <situation name>

## 1. Task hyperedge

```yaml
type: Task
goal: <the objective, one sentence>
actor: <who / which agent will act>
tools_available: [<tool>, ...]
permissions: [<permission>, ...]
constraints: [<constraint node>, ...]
deadline: <date/time or none>
success_criterion: <observable condition that means done>
decision_fed: <the decision this work informs>
reversibility: reversible | partially-reversible | irreversible
what_would_change_the_decision: <fact that would flip it>
```

Blocking questions (ask only these; assume the rest and list the assumptions):

- <question>

Assumptions made for missing inputs:

- <assumption> — revisit if <trigger>

## 2. Evidence

| source_id | kind | authority | recency | why included |
|---|---|---|---|---|
| doc:… | meeting notes | primary | 2026-09-12 | states the decision |

Source spans are fixed and quoted on each hyperedge record — see
`hyperedge-record.md`.

## 3. Retrieved sub-hypergraph

The minimal connected set that bears on the task. One row per edge.

| id | type | key roles (node:role, …) | valid_time | epistemic_status | confidence | provenance |
|---|---|---|---|---|---|---|
| decision_… | Decision | atlas:subject, maya:decision_maker, postgres:selected_option, finance:approver | 2026-10-01 → open | asserted | 0.92 | doc:meeting_notes_0912 |

Edges deliberately excluded (connected but not relevant), with why:

- <edge> — <reason>

## 4. Constraint intersection (for a proposed action)

| constraint | applies because | status | supporting edge |
|---|---|---|---|
| ci-green(sha) | prod deploy policy v3 | satisfied | observation:ci_run_… |
| security-signoff | prod deploy policy v3 | unknown | — (no edge) |

## 5. Contradictions

| edge A | edge B | same roles? | verdict | handling |
|---|---|---|---|---|
| operational_owner(payments)=A | budget_owner(payments)=B | no | not a contradiction | note the role split |
