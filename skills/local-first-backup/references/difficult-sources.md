# Difficult sources

A file-level backup tool copies files as it finds them. That is wrong for
anything that is *in flight* while the backup runs — an open database, a running
VM, a mail store being written to. Each difficult source needs a capture method
that produces a **consistent** artifact, and each needs its own restore test.

## Databases

Copying live database files gives you a torn, likely-unrecoverable copy.

| DB | Consistent capture | Restore test |
|---|---|---|
| PostgreSQL | `pg_dump` (logical) to a file the backup then picks up; or `pg_basebackup` + WAL archiving for PITR; or a filesystem snapshot with the DB in backup mode | `pg_restore` into a scratch instance; run a sample query |
| MySQL/MariaDB | `mysqldump --single-transaction`, or `mariabackup`, or a filesystem snapshot | import into a scratch instance; check row counts |
| SQLite | `sqlite3 db '.backup out.db'` (safe while in use), or copy when the app is stopped | open `out.db`, `PRAGMA integrity_check` |
| MongoDB | `mongodump`, or a filesystem snapshot with journaling on | `mongorestore` to scratch; count documents |

Pattern: a **pre-backup hook** writes the dump to a staging directory; the
backup job includes that directory; a **post-backup hook** clears old dumps.
Both hooks are part of the `unattended-automation` job and must fail the run if
the dump fails — a backup that silently skipped the database is the classic
silent failure.

## Virtual machines

- **Powered-off**: back up the disk image file directly — it is consistent.
- **Running**: use the hypervisor's snapshot (`virsh snapshot-create`, VMware
  quiesced snapshot, Proxmox backup with `qemu-guest-agent` for fs-freeze),
  then back up the snapshot, then delete the hypervisor snapshot. A guest agent
  that freezes the guest filesystem gives a crash-consistent-plus image.
- Or run the versioned backup **inside** the guest for file-level recovery, and
  take periodic whole-image backups for fast rebuild.

## Mail stores

- **Maildir**: safe to back up file-level (one file per message), though a
  message being delivered mid-run is just missed until next run.
- **mbox / single-file stores (some clients)**: back up when the client is
  closed, or use the client's export.
- **Server (Dovecot/Cyrus)**: `doveadm backup` / filesystem snapshot; or pull a
  full copy with `offlineimap` / `mbsync` to a Maildir that you then back up.
- **Cloud mail (Gmail/IMAP-only)**: this is a *cloud-only source* — pull it
  local with `mbsync`/`imapsync` on a schedule, then back up the local copy.

## Password-manager vaults

- **KeePass (.kdbx)**: a single encrypted file — safe to back up file-level, but
  back up *after* the app has saved and closed to avoid a half-written file;
  keep several versions (a corrupted save is silent).
- **1Password / Bitwarden self-hosted (Vaultwarden)**: export the encrypted
  vault on a schedule (`bw export`, Vaultwarden's `data/` + SQLite via
  `.backup`), back up the export.
- **Hosted 1Password/Bitwarden**: treat as cloud-only; use their export; the
  encryption key is your account password + secret key — record those in the
  sealed recovery record too.
- The vault's own master password: **not** in the vault. Sealed recovery record.

## Encrypted volumes and full-disk encryption

- Back up the **decrypted contents** (mount it, let the backup tool read files)
  so you get file-level restore — the repo is encrypted anyway.
- Also record the volume's own recovery key in the sealed record, in case you
  need to restore the whole container.
- Do **not** back up the raw encrypted block device as a file-level source —
  every byte changes, dedup fails, and you can only restore all-or-nothing.

## Cloud-only files

Files that exist only in a provider (Google Drive "online only", iCloud
optimized storage, Dropbox smart sync, Notion, Google Photos):

- Force a **local materialization**: disable "optimize storage" / use
  `rclone sync remote: /local/mirror` / use the provider's Takeout/export on a
  schedule.
- Back up the local mirror like any other source.
- Until a file is local, it is **not** backed up — flag any source where a
  meaningful fraction of bytes is cloud-stubbed.

## The rule

Every difficult source is listed in the protection charter with: its capture
method, the hook that performs it, what makes the run **fail** if capture
fails, and the date it was last restore-tested. No difficult source is
considered protected until it has been restored once.
