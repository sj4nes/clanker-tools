# Recovery runbook: <site>

> Written so someone who is NOT the author can recover the data.
> Tested by having someone else follow it (see drill reports).
> Keep a printed copy with the sealed recovery record.

## At a glance

- **Owner**: · **Recovery contact**:
- **Backup tool + version**: · **Install**: `<how to get the same version>`
- **Repositories**:

| Repo | Location / URL | Access (SSH key, mesh, htpasswd) | Holds |
|---|---|---|---|
| NAS (primary repo) |  |  | all devices, full history |
| Off-site |  |  | all devices |
| Offline USB HDD |  | physically at `<location>`; LUKS key in sealed record | all devices, as of last rotation |

- **Sealed recovery record location(s)**:
- **Encryption**: passphrase / keyfile — retrieved from the sealed record.

## Step 0 — before touching anything

1. **Stop the bleeding.** If this is ransomware or a compromised machine:
   disconnect that machine from the network. Do **not** connect the offline
   disk to it. Do **not** run backups from it.
2. Get the sealed recovery record.
3. Decide the point in time to restore to (for corruption/ransomware: the last
   snapshot *before* the event — list snapshots with dates, see Step 2).
4. Pick a **clean** machine to restore onto (not the compromised one).

## Step 1 — install the tool and set credentials

```
<exact install command for the pinned version>
export RESTIC_REPOSITORY="<repo URL/path>"      # or BORG_REPO / kopia connect
export RESTIC_PASSWORD_FILE="<path to the passphrase you just wrote from the sealed record>"
# access: <ssh-add the key / bring up the mesh / …>
```

## Step 2 — list what is available

```
restic snapshots            # note snapshot IDs and dates per host/path
restic ls <snapshot-id>     # browse a snapshot
```

Choose the snapshot ID for each thing you need to restore.

## Step 3 — restore, by scenario

### A single file / folder

```
restic restore <snapshot-id> --target /restore --include "/path/inside/snapshot"
```

### A whole home directory

```
restic restore <snapshot-id> --target /restore --include "/home/<user>"
# then move into place / rsync onto the fresh machine
```

### A dead machine (bare metal)

1. Restore the OS image if one exists: `<imaging tool restore command>`.
2. Boot it. Then file-level restore user data on top (scenario above).
3. Reinstall apps from `<list / Brewfile / package manifest location>`.

### Ransomware — roll back past the event

1. Confirm the pre-event snapshot ID (Step 2), dated before `<event date>`.
2. Restore it to a **clean** target as above.
3. Do **not** prune anything. Do **not** let the compromised machine near the
   repo. Rebuild the machine from scratch, then restore data onto it.

### A database / VM / vault (difficult sources)

| Source | Restore command | Verify |
|---|---|---|
| Postgres |  `pg_restore -d scratch <dump>` | run `<a known query>` |
| KeePass | restore `<vault>.kdbx`; open with master pw from sealed record | check entry count |
| VM |  restore image file; boot in isolation | log in |

## Step 4 — verify the restore

- `sha256sum` a sample of restored files against anything you still trust.
- For a home dir: log in as that user; open mail, browser, keychain/vault.
- For a DB: integrity check + row counts.
- Record it as a drill report.

## Step 5 — return to service

1. Put restored data in place on the (rebuilt) machine.
2. Re-point backups: reinstall the **writer** credential (append-only) — never
   the admin or prune credential — and run one backup, verify it lands.
3. Re-enable monitoring; confirm last-success updates.
4. If any key was exposed, rotate it (see retention-policy.md) and update every
   sealed copy.
5. Write the incident up; file the drill/restore report.

## Contacts

| Who | For | How to reach |
|---|---|---|
| Recovery contact |  |  |
| Off-site host (relative) | access to their NAS |  |
| ISP / network |  |  |
