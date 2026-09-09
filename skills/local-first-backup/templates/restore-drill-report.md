# Restore drill report

> One per drill. Keep them; the series is your evidence that data is recoverable.

## Header

- **Date**:
- **Drill type**: monthly sampled | semi-annual full | ransomware/rollback
- **Scope** (what was restored): 
- **Snapshot / point-in-time restored**:
- **Source layer used**: fast local | NAS repo | offline disk | **off-site only**
- **Driver** (who ran it): 
- **Used the written runbook only?** yes / no (if no — that is a finding)

## Method

- Commands run:
- Restore target (scratch dir / spare disk / VM):
- Verification method: `sha256` compare / tree diff / logged-in-and-used / `PRAGMA integrity_check` / …

## Results

| Metric | Value |
|---|---|
| Files / items in scope |  |
| Items byte-verified |  |
| Unexplained mismatches |  |
| Decryption / key issues |  |
| Bytes restored |  |
| Time to first file |  |
| Time to usable (full drill) |  |
| Throughput (MB/s) |  |
| RTO for this class | (from charter) |
| Met RTO? |  |

## Ransomware/rollback drill only

- Bad snapshot created without overwriting good ones? yes / no
- Last-good snapshot correctly identifiable by timestamp? yes / no
- Writer credential **refused** prune/delete? yes / no  ← must be yes
- Prune credential honored tier policy and stopped? yes / no

## Runbook gaps found

| Step | Gap | Fix applied |
|---|---|---|
|  |  |  |

## Verdict

- **PASS** — this data class is recoverable from this layer at this point in
  time, within (or not) its RTO.
- **FAIL** — reason:  ; re-drill scheduled for:  ; class is **not** claimed
  recoverable until re-drill passes.

## Follow-ups

- [ ] 
