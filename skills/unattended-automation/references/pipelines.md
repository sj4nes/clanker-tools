# Multi-step pipelines

A pipeline is the single-job controlled workflow applied per stage, plus three
things a single job does not need: **dependency ordering**, **cross-stage
checkpointing**, and **compensation** for stages whose effects already left the
system.

## Order the stages

List stages and their dependencies as `before after` edges and topologically
sort them with the [`tsort`](../tsort/SKILL.md) skill. This gives a valid linear
order (or a set of them, exposing what can run in parallel) and fails loudly on a
dependency cycle — which in a pipeline is a design bug, not a runtime condition.

Record the resolved order in the run manifest so a resumed run uses the same
order the failed run did.

## Per-stage contract

Each stage is its own controlled workflow and additionally declares:

- **Inputs**: which prior stages' outputs it consumes (by artifact path / table
  / key), and their validation.
- **Idempotency**: re-running the stage on the same inputs produces the same
  result and no duplicate external effect.
- **Outputs**: the artifacts / state it produces, named deterministically
  (content-addressed where possible) so a re-run can detect "already done".
- **Effect class**: `pure` (recomputable, e.g. a transform), `internal-state`
  (own DB/store, idempotent upsert), or `external-commit` (sent an email,
  charged a card, deployed) — this decides resume vs compensate.
- **Compensation**: for an `external-commit` stage, the action that undoes or
  corrects it.

## The run manifest and checkpoints

Persist one manifest per pipeline run (schema shares
[`../templates/audit-event.schema.json`](../templates/audit-event.schema.json)'s
stage records; layout in
[`../templates/pipeline-manifest.md`](../templates/pipeline-manifest.md)):

```text
run_id, pipeline_version, trigger, started_at, stage_order[]
per stage: name, status (pending|running|succeeded|failed|compensated|skipped),
           input_fingerprint, output_ref, attempts, started_at, ended_at
```

Update it after every stage transition. It is both the checkpoint (where to
resume) and the audit record (what happened).

## On failure: resume, restart, or compensate

| Situation | Action |
|---|---|
| Stage k failed, stages 1…k-1 are `pure` or `internal-state` | Resume: re-run from stage k. Earlier stages are idempotent, so optionally re-run them, but a checkpoint lets you skip. |
| Stage k failed, some earlier stage was `external-commit` and the run is being abandoned | Compensate: run compensations for the committed stages in reverse order, each verified; mark them `compensated`. |
| Stage k failed transiently | Retry stage k per [`error-and-retry.md`](error-and-retry.md); if it exhausts its budget, escalate to one of the above. |
| Input to stage k is now stale (a long gap since stage k-1) | Re-run from the stage that produced that input, not from k. |

Decide the default per pipeline — "resume from last checkpoint" for
report/ETL-style pipelines, "compensate and stop" for anything that moves money
or provisions resources — and put it in the charter.

## Fan-out

When a stage processes many items in parallel: cap concurrency, make each item's
work idempotent, checkpoint completed items (not just completed stages), and on
resume process only the incomplete items. A partial fan-out that restarts from
zero either wastes hours or double-processes.

## When to stop wrapping and adopt an engine

A shell/Python wrapper is fine for a short linear pipeline with a handful of
stages. Move to a real workflow engine (Airflow, Dagster, Temporal, Step
Functions, Argo, a CI system's native pipeline) when you need: a genuine DAG
with wide fan-out, per-task retry and backfill, scheduling with data-interval
awareness, a UI for run history and re-runs, distributed execution, or
long-running durable timers. Re-implementing those badly is a bigger risk than
the dependency.
