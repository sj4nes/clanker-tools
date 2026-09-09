# Retention, encryption, and key-custody policy: <site>

## Retention tiers

| Data class | Snapshot frequency | keep hourly | keep daily | keep monthly | keep yearly | Notes |
|---|---|---|---|---|---|---|
| projects / code | hourly | 24 | 14 | 6 | 0 |  |
| documents | daily | 0 | 30 | 12 | 7 |  |
| photos / authored | daily | 0 | 30 | 24 | **forever** | never prune oldest yearly |
| financial / legal | daily | 0 | 30 | 12 | 10 |  |
| system images | weekly | — | — | — | — | keep last 3 |

**Prune command** (run from the *prune* credential only, dry-run first):

```
# restic
restic forget --keep-hourly H --keep-daily D --keep-monthly M --keep-yearly Y --prune --dry-run
```

Prune job alerts if the delete count exceeds `<expected band>`.

## Repository sizing

| Repo | Source S (GB) | churn c | dedup/compress d | tier points | Estimate (GB) | Provisioned (GB) | Last actual (GB) |
|---|---|---|---|---|---|---|---|
|  |  |  |  | D+m+y = |  | ≥ 2× estimate |  |

`repo ≈ S*d + S*c*d*(D + m + y)` — compute with the `bc` skill; re-fit `c`/`d`
after month 1.

## Encryption

| Target | Encrypted | Mechanism | Key/passphrase location |
|---|---|---|---|
| external SSD (fast local) |  | FileVault / BitLocker / LUKS |  |
| NAS repository |  | tool client-side (repokey / keyfile) |  |
| offline USB HDD |  | LUKS/VeraCrypt **+** tool |  |
| off-site repository |  | tool client-side only |  |
| transport / seed disk |  | full-disk |  |

## Sealed recovery record

- **Contents**: repo passphrase(s) + keyfile(s); repo locations + access
  (SSH key, mesh join, URL); tool + version; exact restore commands; every
  disk-encryption recovery key; "test-restored on ___".
- **Copy 1 location**:  (e.g. home safe, printed)
- **Copy 2 location**:  (e.g. bank deposit box / with recovery contact)
- **Split scheme** (if any): Shamir k-of-n across <people>
- **Password-manager entry**:  (in addition to, never instead of, physical)

## Key rotation

- **Trigger**: suspected exposure / departing household member / every <N years>
- **Procedure**: <per-tool add-new → verify restore → remove-old>
- **After rotation**: update every sealed copy; test-restore with new record
  only; destroy old printed copies; log the date here.

| Date | Repo | Reason | Sealed copies updated | Test-restore passed |
|---|---|---|---|---|
|  |  |  |  |  |

## Recovery contact

- **Name / relationship**:
- **Has**: sealed record copy? runbook? knows which disk/dataset?
- **Confirmed willing/able on**:
