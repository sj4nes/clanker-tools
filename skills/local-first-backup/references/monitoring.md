# Monitoring

Backup is the system where failure is invisible until you need it. Monitor for
**failure** (a job errored) and for **silence** (a job stopped running, or a
copy stopped updating, with nothing logged). Silence is the one plain error-
alerting misses.

## Signals to track

| Signal | Source | Healthy | Alert when |
|---|---|---|---|
| Last successful backup, per device | backup job's audit event | < 1.5× the schedule interval | older than 2× interval (warn), 4× (page) |
| Last successful off-site replication | replication job | < 2 days | > 3 days (warn), > 7 (page) |
| Last successful offline-disk backup | rotation job / manual log | < rotation interval | overdue by one interval |
| Repository integrity check | `restic check` / `borg check` / `kopia snapshot verify` | last run passed, < 7–30 days ago | failed, or overdue |
| Sampled restore test | monthly drill job | last run passed | failed, or > 5 weeks ago |
| Free space on each target | `df` / pool status | < 75 % used | ≥ 75 % (warn), ≥ 90 % (page) |
| Repo growth rate | weekly repo size delta | steady | slope doubles week-on-week |
| Disk health (SMART) | `smartctl -H`, `zpool status` | PASSED / ONLINE | any reallocated/pending sectors, DEGRADED pool, checksum errors |
| Prune dry-run delete count | prune job's dry-run | within expected band | deletes far more snapshots than the tier math predicts |

## Silence detection

A job that should run and doesn't is broken even with zero error output.
Implement one of:

- **Dead-man's switch**: each successful run pings a monitor
  (self-hosted: Healthchecks.io, Uptime Kuma; or a cron that checks a timestamp
  file). The *monitor* alerts when the ping doesn't arrive in the window.
- **Timestamp check**: a separate small job reads
  `seconds_since_last_success` from each device's audit record and alerts past
  threshold. This job itself needs a dead-man's switch (quis custodiet).

Every backed-up device reports independently. "The NAS backup ran" does not
mean laptop C — which has been shut in a drawer for three weeks — is protected.

## Repository verification

Reading back data proves the repo is not silently rotting:

- **Metadata check** (fast, frequent — weekly): `restic check`,
  `borg check --repository-only`, `kopia snapshot verify --verify-files-percent=0`.
- **Full data check** (slow, IO-heavy — monthly or quarterly):
  `restic check --read-data` (or `--read-data-subset=10%` rotating),
  `borg check` (full), `kopia snapshot verify --verify-files-percent=100`.
- On the ZFS/Btrfs layer: a monthly `scrub`.

A failed check is a real incident: the repo may have bad blocks. Do not prune,
do not let it be the only copy — restore what you can from another layer, then
rebuild the repo.

## Reporting

The human-facing report (weekly, or on request) is plain and calibrated:

```
Backup status — 2026-09-09

  Device            Last backup     Repo        Off-site     Notes
  laptop-a          02:14 today     ok          4 days old   off-site slow — relative's ISP down
  laptop-b          01:50 today     ok          6h ago       ok
  desktop           03:02 today     ok          6h ago       ok
  laptop-c          19 days ago     STALE       19 days      >>> shut in drawer; not protected

  Repo integrity:   passed 2026-09-07 (metadata), 2026-08-30 (full read)
  Free space:       NAS 61% used, offsite 44% used, rotation disk 70% used
  Restore test:     2026-09-01 — 40/40 sampled files byte-verified, 12 min to restore 5 GB
  Offline disk:     rotated 2026-09-05 (on schedule)

  Action needed: power on laptop-c and let it back up; chase off-site link for laptop-a.
```

Never report "backups are working". Report each device, each copy, each check,
with a date and a number.

## Wire it as jobs

Each monitor is an `unattended-automation` job: bounded, idempotent, its own
audit event, alert on failure and on its own silence. The weekly report is a
job that reads the others' audit records — it does not re-derive state by
querying repos directly (that is slow and can itself fail).
