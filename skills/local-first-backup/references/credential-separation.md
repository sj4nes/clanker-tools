# Credential-role separation

The machine being protected must not hold a credential that can erase its own
backup history. If it did, ransomware or a mistaken script on that machine would
take out the primary data *and* every online copy in one move. Split the
capability four ways.

## The four roles

| Role | Capability | Lives on | Never |
|---|---|---|---|
| **Writer** | Create a new snapshot; read *its own* uploads for verification | The protected machine / its backup job | Delete, prune, `forget`, re-key, change policy, list other machines' data |
| **Prune** | Apply the approved retention policy (`forget`/`prune`) | A separate, controlled maintenance host or a scheduled job on the NAS itself | Run on any protected endpoint; delete outside the written policy |
| **Restore** | Read and extract any snapshot | Nowhere by default — issued to the operator at recovery time | Write, delete |
| **Admin** | Re-key, destroy the repo, change retention policy, manage credentials | Offline / sealed record / the recovery contact | Be present on an everyday machine or in a cron job |

The writer credential doing an append-only backup is the single most important
control in the system. Everything else is defense in depth.

## How to implement append-only per tool

### Borg

Server-side, in the SSH `authorized_keys` `command=` restriction:

```
command="borg serve --append-only --restrict-to-path /srv/borg/laptop-a",restrict ssh-ed25519 AAAA...
```

The client can `borg create` but `borg delete` / `borg prune` are refused. Run
prune from a **different** key without `--append-only`, invoked only by the
maintenance job. Note Borg's append-only is a soft control (a later
non-append-only session can still compact) — pair it with filesystem snapshots
of the repo on the server, or object-lock if the repo lives on object storage.

### Restic

Use `rest-server --append-only`, giving each machine its own path and htpasswd
user:

```
rest-server --path /srv/restic --append-only --private-repos
```

`--private-repos` isolates each user to `/srv/restic/<user>/`. The prune job
talks to a second `rest-server` instance (or the same one started without
`--append-only`) on a maintenance-only port/host. For S3-compatible back-ends,
give the writer an IAM/bucket policy with `s3:PutObject` and `s3:GetObject` but
**not** `s3:DeleteObject`, and enable **object lock** (compliance or governance
mode) so even a policy slip cannot delete within the retention window.

### Kopia

Server mode with per-user access (`kopia server` + `kopia server user add`), or
an object-lock bucket with a retention period. Kopia's maintenance (which does
the actual deletion) runs from the owner/admin context, separate from the
snapshotting clients.

### Filesystem-snapshot layer

On the receiving ZFS/Btrfs box, the account that `zfs receive`s must **not** have
`zfs destroy` / `zfs rollback` delegated. Snapshot pruning on the target runs
from root via a local timer, not from the sending machine.

## The offline copy needs no credential discipline — it needs a human

A rotated disk that is unplugged is immune to any credential compromise. Its
control is procedural: it is connected only for its backup window, then
disconnected and moved. See [`monitoring.md`](monitoring.md) for tracking that
the rotation actually happens.

## What this buys you

If a protected laptop is fully compromised, the attacker can:

- encrypt or delete its primary data — recoverable from any backup layer;
- write garbage snapshots to the repository — annoying, but the good snapshots
  remain, protected by append-only / object-lock;
- **not** delete history, **not** re-key the repo, **not** reach the offline
  disk.

Recovery is then: restore from the last known-good snapshot (identified by date,
before the compromise), having lost only the work since that snapshot.

## Test it

The verification runner and the restore drill both check the negative case: the
writer credential attempts a `prune`/`delete` and **must be refused**. If it
succeeds, the separation is not real.
