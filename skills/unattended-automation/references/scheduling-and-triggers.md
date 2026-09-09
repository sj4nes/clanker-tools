# Scheduling and triggers

The trigger decides three things you must handle explicitly: what happens when a
run overlaps the previous one, what happens when a run is missed, and where the
single-instance lock lives.

## Cron

- **No overlap protection.** If the 02:00 run is still going at 03:00, cron
  starts another. The job itself must take a lock and apply an overrun policy.
- **No catch-up.** A run missed because the host was down is simply lost. If
  missed runs matter, either make the job process "everything since the last
  successful run" (watermark-based, not "the last hour"), or use a scheduler
  that records intervals.
- **Timezone / DST.** `cron` uses the system timezone by default; a job at
  `30 2 * * *` runs twice or zero times on DST-change nights. Prefer UTC for the
  crontab, or a scheduler with DST-aware semantics.
- **Environment.** cron runs with a minimal environment and `PATH`. Set what you
  need explicitly; do not rely on a login shell's profile.
- Redirect output; a job that prints to stdout emails root and hides the real
  signal.

## systemd timers

- `Persistent=true` runs a missed job once after boot — bounded catch-up.
- `RandomizedDelaySpec` spreads load across a fleet.
- One `.service` instance at a time by default (no manual lock needed for
  overlap), plus `RuntimeMaxSec` for a hard timeout, `OnFailure=` for alerting,
  and journald for structured logs.
- Still watch timezone (`OnCalendar` honors `Timezone=`).

## Queue consumers

- Overrun is naturally bounded by a concurrency cap; messages wait.
- **At-least-once delivery** — handlers must be idempotent; the same message can
  arrive twice.
- Set the visibility / ack timeout longer than the slowest expected handler, or
  the message redelivers while you are still processing it.
- Use a dead-letter queue with an alarm; a poison message must not block the
  queue forever.
- "Missed runs" become queue depth — alert on depth and on oldest-message age.

## Webhooks

- **Authenticate**: verify the signature / HMAC / mTLS before doing anything.
- **Deduplicate**: senders retry; dedupe by the event ID, and guard against
  replay (timestamp window + seen-ID set).
- **Respond fast, work async**: ack the webhook immediately, enqueue the work;
  doing the work inline risks the sender timing out and retrying.

## CI / pipeline triggers

- Pin tool and action versions; an unattended pipeline that floats on `latest`
  changes behavior without a commit.
- Isolate credentials per job; least privilege per stage.
- Treat the pipeline definition as code under review.

## Missed-run / catch-up policy (decide and write down)

| Policy | Use when |
|---|---|
| Skip (no catch-up) | The next run subsumes the missed one (e.g. "sync current state") |
| Run once on recovery | One missed run should still happen (`Persistent=true`) |
| Backfill all missed intervals | Each interval produces distinct output (e.g. daily reports) — needs data-interval-aware scheduling |
| Watermark | The job processes "everything since last success" regardless of how many intervals passed |

## Overrun policy (decide and write down)

| Policy | Use when |
|---|---|
| Skip this run (lock held → exit 0) | Runs are equivalent; a slow run should just be left alone — the common default |
| Queue / serialize | Every run must eventually happen, in order |
| Kill the previous run | The new run's data supersedes the old; the old is safe to interrupt (it is — you made it safe to stop) |

## Where the lock lives

- Single host: `flock(1)` on a lockfile, or `mkdir` of a lock dir (atomic,
  portable), removed by an `EXIT`/signal trap.
- Multiple hosts / containers: a lock row (`SELECT ... FOR UPDATE` / an
  `INSERT` that fails on conflict), a lock object in object storage with a
  conditional put, or a distributed lock with a TTL — always with a TTL so a
  dead holder's lock expires.
