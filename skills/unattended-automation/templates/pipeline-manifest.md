# Pipeline run manifest: <pipeline name>

One manifest per run. It is both the checkpoint (where to resume) and the audit
record (what happened). Persist it somewhere the pipeline cannot rewrite after
the fact except to update stage status.

## Header

| Field | Value |
|---|---|
| `run_id` |  |
| `pipeline_version` | (commit / tag of the pipeline definition) |
| `trigger` | schedule / manual / upstream-event + source |
| `started_at` | ISO-8601 UTC |
| `ended_at` |  |
| `outcome` | success / failed / compensated / partial |
| `failure_default` | resume_from_checkpoint / compensate_and_stop |

## Stage order

Resolved once, at run start, by `tsort` over the dependency edges. Resumed runs
reuse this exact order.

```
<stage order, one per line, or the tsort input edges>
```

## Stage records

| Stage | Effect class | Depends on | Status | Input fingerprint | Output ref | Attempts | Started | Ended |
|---|---|---|---|---|---|---|---|---|
| extract | pure |  — | succeeded | sha256:… | s3://…/extract.parquet | 1 |  |  |
| transform | pure | extract | succeeded | sha256:… | s3://…/transform.parquet | 1 |  |  |
| load | internal-state | transform | running | sha256:… |  | 2 |  |  |
| notify | external-commit | load | pending |  |  | 0 |  |  |

`status`: `pending | running | succeeded | failed | compensated | skipped`
`effect class`: `pure` (recomputable) | `internal-state` (idempotent upsert) |
`external-commit` (left an effect outside — needs a compensation)

## Compensations

| Stage | Compensating action | Verified by | Tested? |
|---|---|---|---|
| notify | send correction notice | provider sent-log shows correction | [ ] |
| provision | deprovision resource | resource no longer exists | [ ] |

## Resume / compensate decision log

On failure, record here what was decided and done:

- Failed at stage: · error class:
- Committed `external-commit` stages before failure:
- Action taken: resumed from `<stage>` / compensated `<stages>` in reverse
- Manual reconciliation ticket:
