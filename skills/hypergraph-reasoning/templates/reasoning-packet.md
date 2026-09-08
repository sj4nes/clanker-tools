# Reasoning packet — <question>

The answer, with its evidence and its gaps. Handed to the model / user in place
of raw chunks.

## Question / proposed action

<the task hyperedge goal, restated; the action under consideration>

## Facts (asserted / observed — each with a source span)

| claim | epistemic_status | source_id : span | valid as of |
|---|---|---|---|
| Maya chose managed PostgreSQL for Atlas | asserted | doc:notes_0912 : "Maya chose managed PostgreSQL for Atlas" | 2026-10-01 → open |

## Conclusions (inferred — with the chain)

| conclusion | from edges | note |
|---|---|---|
| The migration is authorized for Atlas only | decision_… + requirement_… | scope role = atlas; other projects not covered |

## Uncertain (proposed / unknown)

| item | status | what would settle it |
|---|---|---|
| "PostgreSQL cuts cost 30%" | proposed | a measured cost comparison post-migration |
| security-signoff for deploy | unknown | check the change ticket |

## Constraints that apply

| constraint | status | supporting edge |
|---|---|---|
| ci-green(sha) | satisfied | observation:ci_run_… |
| deploy-window-open | violated | now = Wed 18:00; window is Tue/Thu 10–16 |

## Contradictions

| edges | verdict | handling |
|---|---|---|
| operational_owner(payments)=A vs budget_owner(payments)=B | no conflict (roles differ) | recorded, no action |
| operational_owner(payments)=A vs operational_owner(payments)=C, same window | genuine conflict | both sources reported; ownership question routed to <owner> |

## Recommendation

<one of: proceed / proceed with conditions / do not proceed / escalate>

- **Conditional on:** <the unmet or unknown conjuncts>
- **Requires execution-time approval:** yes / no (irreversible or outward-facing?)

## Non-claims

- Not claiming <X> — <why: no evidence / out of scope / expired>
- Building this model does not authorize the action; the precondition
  conjunction has <N> unmet/unknown terms.

## Revisit when

<new evidence, a date, a policy change>
