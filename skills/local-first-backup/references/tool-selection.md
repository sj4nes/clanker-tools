# Choosing the tools

Two independent choices: the **fast local recovery** mechanism (usually
OS-native) and the **versioned repository** engine (the one that matters most).
A third, optional: **full-disk imaging** for bare-metal speed.

## The default: file-level versioned backup

For almost everyone the repository layer should be a deduplicating,
encrypting, snapshotting backup tool. All three candidates share the model —
encrypted, authenticated, point-in-time snapshots with a retention engine, not a
live mirror.

| | Borg | Restic | Kopia |
|---|---|---|---|
| Interface | CLI | CLI (single static binary) | CLI + GUI |
| Encryption | client-side, authenticated (repokey / keyfile) | client-side, AES-256 + Poly1305-AES | client-side, per-repo |
| Dedup | content-defined chunking, excellent | content-defined chunking | content-defined chunking |
| Repo back-ends | local path, SSH to a Borg binary on the far end | local, SFTP, S3-compatible, REST (rest-server), Backblaze B2, rclone-anything | local, SFTP, S3-compatible, B2, WebDAV, rclone |
| Multi-client to one repo | one machine at a time (lock); use one repo per machine | multiple clients, one repo | multiple clients, one repo |
| Append-only / immutable | native `--append-only` server mode | via restricted rest-server or object-lock bucket policy | via object-lock bucket; retention policies |
| Compression | yes (lz4/zstd/…) | zstd | zstd/pgzip |
| Maturity | very mature, large deployed base | mature, very widely used | newer, active |

**Pick Borg** when every client and the server are Unix-like, you want top-tier
dedup, and an SSH-hosted repo that holds only ciphertext on an untrusted box.
Accept one-repo-per-machine.

**Pick Restic** when you want a single portable binary, a mix of OSes, and broad
back-end choice — especially self-hosted S3-compatible object storage (MinIO,
Garage) or a `rest-server` you can lock to append-only. Budget memory/IO for
`prune` and `check` on large repos.

**Pick Kopia** when a GUI and a visible policy model matter (a household where
more than one person may need to check status), or you want native per-source
retention policies and object-lock immutability.

Whatever you pick: **one tool across the fleet**. Two backup tools means two
restore procedures to keep tested.

## Fast local recovery

| Platform | Mechanism | Notes |
|---|---|---|
| macOS | APFS local snapshots + Time Machine to a dedicated disk | Time Machine also does network targets; keep it *separate* from the repository layer |
| Windows | File History + a system image, or a third-party imager | File History is per-user-folder; it is not a full backup |
| Linux/NAS | ZFS or Btrfs snapshots on a schedule (`sanoid`, `btrbk`, `zfs-auto-snapshot`) | Snapshots on the pool are rollback, not backup — always pair with an off-pool repository |
| Any | An external SSD with a nightly `restic`/Borg run kept plugged in | Doubles as a cheap second copy |

Fast local recovery is for "restore in minutes after a mistake or a bad update".
It is never the only backup and never off-site by itself.

## Full-disk imaging (optional, periodic)

A disk image captures OS + apps + config + data and enables bare-metal restore
to a replacement drive.

- **Pros**: fastest path from dead machine to working machine; captures OS state.
- **Cons**: large; poor for long history; driver/hardware differences complicate
  restore; a full image every day is wasteful without incremental support.
- **Use it as**: a monthly or quarterly *baseline* image per machine, on top of
  daily file-level backups. Disaster recovery, not the primary mechanism.

Tools: Time Machine (does bare-metal on macOS), Clonezilla, `dd` to a
compressed image for a powered-off disk, Windows system image, `virt-*` /
`zfs send` for VMs.

## Filesystem snapshots + replication (servers, NAS, VM/DB hosts)

ZFS/Btrfs snapshots are near-instant and space-efficient; `zfs send | zfs recv`
replicates datasets and their snapshots incrementally, and encrypted send
streams can stay encrypted in transit.

- **Strong for**: a NAS, a Linux server, a VM host, a database host — a fast
  rollback layer *beneath* a separate backup.
- **Not a backup when**: the target pool is the same as the source pool, or the
  backup account has the privileges to `zfs destroy` the snapshots. Send them to
  a *different* machine and restrict the receiving account.

## rsync / rclone

`rsync --link-dest` (hardlinked history) or `rclone` are fine for *moving bytes*
into a repo or making a plain mirror to a local disk. They give you no
encryption-at-rest, no integrity verification, and no retention engine — you
would be rebuilding what Borg/Restic/Kopia already do. Use them as plumbing, not
as the backup system.

## Decision, in order

1. Repository engine: Borg / Restic / Kopia per the table above — one for the
   whole fleet.
2. Fast local recovery: the OS-native mechanism for each machine.
3. Add periodic full-disk images only for machines whose RTO is "back to work in
   an hour" and whose config is expensive to rebuild.
4. On a NAS or server, add filesystem snapshots + off-box replication as the
   fast layer under the repository.
