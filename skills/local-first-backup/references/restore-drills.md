# Restore drills

The backup is not done when the job goes green. It is done when you have
**restored from it** and verified the result. Everything before a successful
restore is untested. Drills come in three sizes.

## 1. Monthly sampled restore (automated)

**Goal**: prove the repository is readable, the key works, and bytes come back
intact.

- Pick N files at random from the latest snapshot (N = 30–50, spanning several
  sources and a range of sizes).
- Restore them to a scratch directory.
- Compare each against the live source **by content hash** (`sha256`), not by
  size or mtime. Files legitimately changed since the snapshot are expected
  mismatches — restore *the same file from the current source's last snapshot*
  or exclude recently-modified files from the sample.
- Also restore one whole small directory and diff the tree.
- Record: files sampled, files byte-verified, mismatches (with cause), bytes
  restored, wall-clock time, MB/s.

Build it as an `unattended-automation` job. It must alert on: any unexplained
mismatch, a restore error, a decryption failure, or the job not having run in
> 5 weeks.

```
restic restore latest --target /scratch/drill --include <sampled paths>
# then: for f in sampled; sha256 compare /scratch/drill/$f  vs  source/$f
```

## 2. Semi-annual full drill (human, from the runbook)

**Goal**: prove you can bring back a *whole* thing, and that the recovery
runbook is sufficient.

Rotate the scenario each time:

- **Whole home directory**: restore one user's entire home to a spare disk or a
  VM. Log in as that user against the restored data. Do the apps work? Mail?
  Keychain/vault? Browser profile?
- **Replacement machine**: take a spare/old laptop or a fresh VM, and rebuild it
  to working state from backups only — OS image if you keep one, then file-level
  restore on top. Time it end to end.
- **Off-site-only restore**: disconnect from the LAN entirely; recover a data
  class using **only** the off-site repository and the sealed recovery record.
  This is the "house burned down" rehearsal.

Rules:

- Follow the **written runbook**, step by step. If you reach for memory or
  improvise, stop and fix the runbook — that gap is the finding.
- Have someone **other than the runbook's author** drive at least one drill a
  year. If only one person can recover the data, that is a single point of
  failure.
- Record time-to-first-file and time-to-usable-system against the class's RTO.

## 3. Ransomware / bad-change rollback drill

**Goal**: prove you can go *back in time* past a bad event, and that the +1 copy
is genuinely out of reach of a compromised endpoint.

- In a scratch area, simulate the event: encrypt or corrupt a set of files in a
  source, then let the **normal backup job run** (this creates a "bad"
  snapshot).
- Confirm: the bad snapshot did **not** overwrite or delete the good ones.
- Identify the last-good snapshot by timestamp (before the simulated event) and
  restore from it. Verify the plaintext is back.
- Attempt a `prune`/`delete` with the **writer** credential — it must be
  **refused**. Then prune with the maintenance credential and confirm it honors
  the tier policy and stops there.

## Scoring a drill

Each drill is pass/fail with a report ([`templates/restore-drill-report.md`](../templates/restore-drill-report.md)):

| Field | Example |
|---|---|
| Date / scope / driver | 2026-09-01 / sampled 42 files / automated |
| Method | `restic restore latest`, sha256 compare |
| Result | 42/42 byte-verified; 0 unexplained mismatch |
| Time-to-restore | 12 min for 5.1 GB (7 MB/s over gigabit — slower than expected, investigate NAS disk) |
| Runbook gaps found | step 4 omitted the `--repo` env var; fixed |
| Verdict | PASS |

A drill with an unexplained mismatch, a decryption failure, or a runbook gap
that blocked progress is a **FAIL** — the class it covers is not recoverable
until a re-drill passes.

## The claim you may make

Only after a passing drill for a data class may you say that class is
recoverable — and the claim is scoped to what the drill actually restored (that
snapshot, that layer, that RTO). "The job succeeded every night" is never that
claim.
