# Retention and repository sizing

Two questions: **how far back** must you be able to restore (retention), and
**how much disk** does that take (sizing). Retention is a policy decision driven
by cost-of-loss; sizing is arithmetic — do it with the [`bc`](../bc/SKILL.md)
skill, never shell `$(( ))`.

## Setting retention from cost-of-loss

Do not copy `24 / 30 / 12 / 7` off a blog. For each data class ask:

1. **How long until you would notice a problem?** Corruption or an unwanted
   change in rarely-touched archives can go unseen for months — the retention
   tail must be longer than the detection lag.
2. **What is the regulatory / practical floor?** Tax and financial records:
   often 7 years. Legal documents: indefinite. Photos and authored work:
   effectively forever.
3. **How much recent work can you afford to redo?** This is the RPO and it sets
   snapshot *frequency*, not the tail. Active project code: hourly. Documents:
   daily. Media library: daily is plenty.
4. **How fast must it come back?** The RTO. It decides whether the class also
   needs a full-disk image or a fast local layer, not retention depth.

A reasonable set of tiers, adjusted per class:

| Data class | Frequency (RPO) | Retention tiers | Also needs |
|---|---|---|---|
| Active projects / code | hourly | 24 hourly, 14 daily, 6 monthly | fast local snapshot |
| Documents / correspondence | daily | 30 daily, 12 monthly, 7 yearly | off-site |
| Photos / media / authored work | daily | 30 daily, 24 monthly, **forever** yearly | off-site **and** offline |
| Financial / legal / tax | daily | 30 daily, 12 monthly, 10 yearly | off-site **and** offline |
| Regenerable (checkouts, caches) | — | excluded | — |
| System / OS | weekly image | last 3 images | — |

"Forever" in practice means: never let the prune policy delete the oldest yearly
snapshot; migrate it forward when you change tools.

## Retention mechanics per tool

All three keep the **last N** of each bucket, not "one per calendar period
regardless of gaps":

- **Restic**: `restic forget --keep-hourly 24 --keep-daily 30 --keep-monthly 12
  --keep-yearly 7 --prune`
- **Borg**: `borg prune --keep-hourly=24 --keep-daily=30 --keep-monthly=12
  --keep-yearly=7`
- **Kopia**: per-policy `--keep-hourly` / `--keep-daily` / … on the source.

Run `forget`/`prune` from the **prune credential**, never the backup job's
append-only credential. Schedule it as its own `unattended-automation` job with a
dry-run first (`--dry-run` / `borg prune -n`) whose output is logged and
alertable if the delete count is surprising.

## Sizing the repository

Inputs you need (measure, don't guess):

- `S` = total source size after exclusions (GB)
- `c` = daily change rate as a fraction of `S` (new + modified unique bytes).
  Typical: documents 0.5–2 %, code 2–5 %, photos 0.1–1 % (mostly additions),
  a mail store 1–3 %.
- `d` = deduplication + compression factor the tool achieves (unique stored
  bytes ÷ logical bytes). Borg/Restic/Kopia on mixed data: often 0.5–0.8;
  already-compressed media: ~1.0.
- The retention tier counts: `h` hourly, `D` daily, `m` monthly, `y` yearly.

Approximate stored size:

```
first_snapshot         = S * d
incremental_per_period ≈ S * c * d           (unique new/changed bytes)
retained_increments    ≈ h_span + D + m + y   distinct retained points beyond the first
                         where h_span collapses to ~1 day of change
repo_size ≈ S*d  +  S*c*d * (D + m + y)
```

Worked example with `bc` (`scale=2`): `S = 400`, `c = 0.01`, `d = 0.7`,
`D = 30`, `m = 12`, `y = 7`:

```
base = 400 * 0.7                      = 280.00 GB
incr = 400 * 0.01 * 0.7               = 2.80 GB per retained point
tail = 2.80 * (30 + 12 + 7)           = 137.20 GB
repo ≈ 280.00 + 137.20               = 417.20 GB
```

Then apply headroom: provision **at least 2×** the estimate. `prune` needs free
space to repack; churn is bursty (a photo import, a new VM); and you want room
before the capacity alert fires. So budget ~850 GB for this example.

Re-run the estimate from *actual* `repo size` vs `source size` after the first
month and correct `c` and `d`.

## Capacity monitoring

- Alert at **75 %** full (time to act) and **90 %** full (urgent).
- Track repo growth per week; a sudden slope change means a new large source, a
  broken exclusion, or dedup falling over on newly-incompressible data.
- Before raising retention, re-size. Before lowering retention to save space,
  check nothing in the deleted tail is the only copy of something irreplaceable.
