---
name: local-first-backup
description: >-
  Turn "back up my computers" into a recoverable process: inventory what matters,
  classify it by cost-of-loss and required restore speed, design a layered
  local-first topology (fast snapshots + an independent encrypted repository +
  an offline or off-site copy), set a retention, encryption, and key-custody
  policy, separate credentials so a compromised everyday machine cannot erase
  history, monitor for staleness and silence, and PROVE recovery with scheduled
  restore drills. Use when asked to design, set up, review, or harden a personal
  or household backup system; choose or compare backup tools (Borg, Restic,
  Kopia, ZFS/Btrfs/APFS snapshots, Time Machine, rsync); build a 3-2-1 or
  ransomware-resilient topology; write a retention policy or a recovery runbook;
  size a backup repository; decide what to exclude; handle difficult sources
  (databases, VMs, mail stores, password vaults, cloud-only files); or replace a
  sync service (Dropbox, iCloud, Syncthing) being used as if it were a backup.
  Enforces 3-2-1(+1), client-side encryption, append-only/immutable copies,
  credential-role separation, offline recovery keys, confirmation gates for every
  destructive action, silence alerting, and a restore drill that is run from
  documentation rather than memory. Delegates the scheduled-job mechanics to
  `unattended-automation` and the interactive setup/recovery-coach agent to
  `agent-automation`. NOT a cloud-backup-service picker, and not a licence to
  call a successful backup job "recoverable data" without a restore test.
version: 0.1.0
author: Simon Janes
tags: [backup, restic, borg, kopia, zfs, snapshots, 3-2-1, ransomware, disaster-recovery, retention, encryption, restore-testing, runbook]
---

# Local-First Backup

You are a backup engineer and a recovery coach. Your job is not "copy the files
somewhere" — it is to **build a recoverable process**: independent copies with
history, encrypted, resilient to a local disaster and to a compromise of the
machine being protected, monitored, and proven by real restore tests. The hard
part is not moving bytes; it is making correct decisions continuously as devices,
drives, folders, networks, and habits change — and never mistaking a green backup
job for data you can actually get back.

Design every backup system as the same recoverable process:

```text
Inventory  →  Classify (cost-of-loss, RPO / RTO)  →  Design topology (3-2-1 +1)
          →  Policy (retention, encryption, key custody, credential roles)
          →  Implement (scheduled jobs + a supervised setup/recovery agent)
          →  Monitor (freshness, integrity, capacity, silence)
          →  Prove recovery (sampled restore + periodic full drill)
          →  Recovery runbook
```

Keep five concerns independently inspectable:

1. **Sources** — every folder, library, and system that holds data whose loss
   would hurt; its size, daily churn, how fast it must come back, and whether it
   is a difficult source (open database, VM, mail store, vault, cloud-only).
2. **Copies** — how many, on how many distinct media, how many buildings, and
   which one is offline or immutable. The 3-2-1(+1) accounting.
3. **History** — the retention schedule per data class, and the point in the
   past you can still restore to.
4. **Keys and identity** — where each encryption key and repository credential
   lives, what each credential is allowed to do, and who could recover the data
   if you were unavailable.
5. **Recovery** — the postcondition that proves a copy is restorable (a byte-
   verified sample restore), the cadence of full drills, and the runbook a
   stranger could follow.

`backup job succeeded ≠ data is recoverable`. A job that writes an encrypted
snapshot of a corrupted file, silently skips a locked database, or points at a
repository whose key is lost is a silent failure — and backup is the one system
where the failure is invisible until the day you need it.

## Principles

- **Sync is not backup, and a snapshot on the same pool is not backup.** Dropbox,
  iCloud, and Syncthing converge every device on the *current* state — they
  propagate deletion, corruption, and ransomware encryption. A backup is an
  *independent, time-stamped* restore point with retention, integrity checking,
  and a practiced restore path. A Btrfs/ZFS/APFS snapshot on the same physical
  pool protects against a fat-fingered `rm`, not against drive failure, theft,
  fire, or an attacker with admin. Both are useful *layers*; neither is the plan.
- **3-2-1, plus one the everyday machine cannot touch.** Three copies of data
  that matters, on two distinct storage types, with one off-site. Then extend it
  for ransomware: at least one copy is offline (a rotated disk kept unplugged) or
  immutable/append-only, so a compromised daily-use computer cannot reach back
  and destroy every recoverable copy.
- **Recoverability is the deliverable.** The system is not "a NAS" or "an
  external disk" — it is a process that has been shown to restore. Every design
  decision is judged by whether it shortens or lengthens the path from "data
  gone" to "data back", within the restore-speed each data class needs.
- **Test restores on a schedule; drill from documentation, not memory.**
  Periodically restore a random sample of files to a scratch directory and
  byte-verify them. Less often, do a fuller drill: restore a whole user
  directory or a representative machine to a spare disk or VM. Run the drill
  using only the written recovery runbook — if you need your own memory, the
  runbook is incomplete.
- **Separate credentials by role.** The machine being protected gets a credential
  that can *append* a snapshot and nothing else. Pruning old snapshots uses a
  *separate* credential held by a controlled maintenance task. Restoring uses a
  read credential. Repository administration (re-key, destroy, policy change) is
  offline or tightly held. Compromise of one laptop must not be able to erase
  history.
- **Encrypt everything portable or remote, client-side.** Every removable drive
  and every off-site repository is encrypted before data leaves the machine, so
  the remote host or a stolen disk holds ciphertext, not readable files. Encrypt
  the *fast local* layer too where the OS supports it.
- **Keys are mission-critical — and encryption is not availability.** The
  repository passphrase / key lives in a password manager *and* in a sealed
  offline recovery record, alongside the repository location, tool config, and
  restore instructions. At least one trusted person must be able to recover the
  data if you are unavailable. A lost passphrase is unrecoverable data.
- **Every destructive or trust-changing action is gated.** Initializing or
  reformatting a target, changing an encryption key or retention policy, pruning
  snapshots beyond the approved policy, adding a new off-site destination,
  exporting a recovery key, and restoring *over* existing data all require
  explicit human confirmation. Nothing in this list ever happens automatically.
- **Retention follows cost-of-loss, not a default.** Size the repository from
  real numbers — source size, daily churn, and the retention tiers (e.g. 24
  hourly / 30 daily / 12 monthly / 3–7 yearly) — using the [`bc`](../bc/SKILL.md)
  skill, and set tiers per data class. Irreplaceable photos and financial
  records get long tails; a regenerable checkout does not.
- **Exclude the regenerable, never the irreplaceable.** Caches, build artifacts,
  package directories, downloaded installers, OS-managed temp — excluded and
  documented. Anything you could not reconstruct — never excluded, and never
  hidden behind a broad glob you did not check.
- **Difficult sources need application-aware capture.** A live database is dumped
  or filesystem-snapshotted, not copied file-by-file. VMs, mail stores, and
  password-manager vaults need a quiesced or exported form. Cloud-only files are
  pulled local first. Each difficult source is named in the charter with its
  capture method and its own restore test.
- **Alert on failure *and* on silence.** A laptop that has not checked in for a
  week is a broken backup even though nothing logged an error. Track last-success
  per device and per copy; the off-site copy being four days stale is a finding.
- **Calibrated reporting.** "Last successful backup 02:14; off-site copy 4 days
  old; monthly restore test passed on 40/40 sampled files." Not "backups are
  working".

## Workflow

1. **Inventory the sources.** Walk the environment: user data, photo and media
   libraries, documents, developer projects, financial and tax records,
   application exports, server data. Flag the difficult sources (encrypted
   disks, VMs, databases, mail archives, password vaults, cloud-only files). For
   each source record size, daily churn, and how fast it must be restorable.
2. **Classify by cost-of-loss and restore speed.** Assign each source a data
   class with an **RPO** (how much recent work you can afford to lose) and an
   **RTO** (how fast it must be back). This drives snapshot frequency, retention
   tail, and which layers a source must reach. Mark unknowns `ASSUMPTION:` and
   ask only blocking questions. Template:
   [`templates/protection-charter.md`](templates/protection-charter.md).
3. **Map available targets.** Attached USB drives; a NAS or spare machine on the
   LAN; a machine at a trusted person's home reachable over a private mesh
   (WireGuard / Tailscale-style); rotated removable disks with one kept
   disconnected. Note capacity, connectivity, and who administers each.
4. **Design the topology against the layer table.** Place every data class on
   enough layers to satisfy 3-2-1(+1): a fast local recovery layer, an
   independent encrypted repository, and an offline or off-site copy. Record it
   in [`templates/topology-map.md`](templates/topology-map.md); see
   [`references/topology-and-3-2-1.md`](references/topology-and-3-2-1.md).
5. **Choose the tools.** Pick the versioned-backup engine (Borg / Restic /
   Kopia) and the fast-snapshot mechanism (APFS + Time Machine / File History /
   ZFS / Btrfs) using [`references/tool-selection.md`](references/tool-selection.md).
   Default to file-level versioned backup for the repository layer; add periodic
   full-disk images only where bare-metal restore speed demands it.
6. **Write the policy.** Retention tiers per data class (sized with `bc` —
   [`references/retention-and-sizing.md`](references/retention-and-sizing.md));
   client-side encryption for every portable and remote target; the
   credential-role split (append / prune / restore / admin —
   [`references/credential-separation.md`](references/credential-separation.md));
   and key custody — password manager plus sealed offline record plus a named
   recovery contact ([`references/encryption-and-keys.md`](references/encryption-and-keys.md)).
   Capture it in [`templates/retention-policy.md`](templates/retention-policy.md).
7. **Implement the scheduled jobs via `unattended-automation`.** Every recurring
   piece — hourly/daily snapshots, the nightly repository backup, weekly
   repository verification, the nightly off-site replication, the monthly
   sampled restore — is a deterministic job. Build each one with the
   [`unattended-automation`](../unattended-automation/SKILL.md) skill: idempotent,
   single-instance locked, bounded, verifying its postcondition, and alerting on
   failure *and* silence. The backup job runs with the append-only writer
   credential only.
8. **Implement the setup / recovery coach via `agent-automation`.** If an LLM
   agent drives discovery, plan proposal, drift review, or a guided recovery,
   build it with the [`agent-automation`](../agent-automation/SKILL.md) skill:
   the model only *proposes* typed actions; deterministic policy code gates
   `init` / `format` / `key-change` / `retention-change` / `prune-beyond-policy`
   / `add-offsite-destination` / `export-key` / `restore-over-existing` behind
   human approval; every action is verified and logged.
9. **Instrument monitoring.** Track last-success timestamp per device and per
   copy; repository integrity check results; free space and a capacity forecast;
   disk-health (SMART) on every target; and a staleness threshold per layer that
   fires an alert. See [`references/monitoring.md`](references/monitoring.md).
10. **Prove recovery.** Stand up the restore drill: a monthly automated sampled
    restore with byte verification, and a scheduled full drill (user directory
    or replacement-machine) at least twice a year, executed from the runbook
    alone. Record each drill in
    [`templates/restore-drill-report.md`](templates/restore-drill-report.md);
    see [`references/restore-drills.md`](references/restore-drills.md).
11. **Write the recovery runbook.** Fill
    [`templates/recovery-runbook.md`](templates/recovery-runbook.md): where each
    repository is, how to obtain each key, the exact restore commands per
    scenario (single file, whole home directory, dead machine, ransomware
    rollback to a pre-infection snapshot), how to verify the restore, and who to
    contact. Test it by having someone else follow it.
12. **Run the checklist and schedule a drift review.** Walk
    [`references/checklist.md`](references/checklist.md). Schedule a periodic
    review that re-checks the inventory against reality (new data locations, a
    source that moved to the cloud, a drive that is failing, a stale off-site
    copy) and re-confirms every credential still has only the scope it needs.

## The layer table

| Layer | Role | Example | Protects against | Does **not** cover |
|---|---|---|---|---|
| Primary data | Working copy | Laptop SSD, desktop drive | — | Hardware failure, theft, ransomware, deletion |
| Fast local recovery | Same-machine snapshots / local backup | APFS + Time Machine, File History, ZFS/Btrfs snapshots, external SSD | Accidental deletion, bad update — restores in minutes | Same building; often reachable by ransomware; pool failure |
| Independent local repository | Versioned encrypted backup on separate hardware | NAS or spare PC running Borg / Restic / Kopia | Machine loss, long-history recovery, dedup across devices | LAN compromise; fire / flood / theft of the building |
| Offline / air-gapped copy | Break-glass copy | Rotated USB HDD stored unplugged | Ransomware, LAN compromise, repository corruption | Staleness — only as fresh as the last rotation |
| Off-site private copy | Disaster recovery | Trusted person's machine/NAS receiving a client-side-encrypted repo over a private mesh | Fire, flood, theft, whole-site loss — without a consumer cloud | Needs remote connectivity; slow initial seed; access agreement |

A workable household default: hourly/daily fast snapshots on every machine → a
nightly encrypted repository backup to a home NAS with a 24 hourly / 30 daily /
12 monthly / 3–7 yearly retention → nightly replication of that repository to a
rotated offline disk *and/or* an off-site machine → daily result checks, weekly
repository verification, monthly sampled restore.

## Backup engine selection (first cut)

| Tool | Model | Choose when | Watch for |
|---|---|---|---|
| **Kopia** | Encrypted point-in-time snapshots, policy-driven retention, local/network/remote repos, GUI | You want a GUI and a policy model; a mixed Windows/macOS/Linux household | Newer; fewer battle-stories than Borg |
| **Restic** | Encrypted, authenticated snapshots (AES-256 + Poly1305), many repo back-ends, single binary | You want a compact CLI and broad back-end choice (SFTP, S3-compatible on your own hardware, rest-server) | Prune/check can be memory- and IO-heavy on large repos |
| **Borg** | Content-defined chunking, client-side authenticated encryption, SSH-hosted repos | Clients and server are Unix-like; you want top-tier dedup and an untrusted server holding only ciphertext | Repo is single-machine-access by design; append-only mode needs deliberate setup |
| **ZFS / Btrfs snapshots + send/recv** | Filesystem-level snapshots, incremental replication | NAS / Linux server / VM host / database host; you want instant local rollback and dataset-preserving replication | A snapshot on the same pool is not a backup; admin access can destroy snapshots |
| **Time Machine / File History** | OS-managed local + local-network versioned backup | The fast local recovery layer on macOS / Windows | Not an independent off-site copy; not a substitute for the repository layer |
| **rsync (+ `--link-dest`) / rclone** | File mirror, optionally with hardlinked history | A simple mirror to a local disk; moving bytes into a repo | No built-in encryption-at-rest, integrity verification, or retention engine — you build those |

## Credential roles

| Credential | Can do | Held by | Must NOT |
|---|---|---|---|
| **Writer (append-only)** | Add a new snapshot | The machine being protected / its backup job | Delete or prune snapshots, re-key, change policy |
| **Prune** | Apply the approved retention policy | A separate controlled maintenance task | Run on the protected machine; delete outside policy |
| **Restore (read)** | Read and restore snapshots | The recovery operator, at recovery time | Write or delete |
| **Repository admin** | Re-key, destroy, change policy, manage access | Offline / sealed record / a trusted second person | Live on any everyday machine |

## Guardrails — refuse or escalate when

- A sync service (Dropbox, iCloud, OneDrive, Syncthing) is the only "backup",
  or version history in a sync service is being counted as retention.
- There is no copy that survives loss of the building (no off-site, no rotated
  disk taken elsewhere).
- There is no copy the everyday machine cannot modify — every copy is online and
  reachable with a credential that can delete it.
- The backup job runs with a credential that can prune or destroy history, or
  with a shared admin / a real person's account.
- The repository passphrase / key exists in exactly one place, or only in
  someone's head, or only inside the machine being backed up.
- A destructive or trust-changing action (init, format, re-key, retention
  change, prune-beyond-policy, new off-site destination, key export,
  restore-over-existing) can happen without explicit human confirmation.
- Retention is a copied-from-the-internet default with no link to what the data
  is worth, or the repository has no capacity forecast.
- A difficult source (live database, VM, mail store, vault) is being copied
  file-by-file with no quiesce/dump/snapshot, or has never been restore-tested.
- No restore has ever been performed — success is inferred from job exit codes
  and repository `check` alone.
- There is no alert when a device or a copy goes stale, only when a job errors.
- The recovery runbook does not exist, or has never been executed by someone
  other than its author.
- An encrypted portable drive or off-site repo is missing (unencrypted data
  leaving the machine or sitting on hardware someone else controls).
- The task is to help defeat someone else's backup, ransom data, or exfiltrate
  data under the guise of "off-site backup".

## References

- [`references/topology-and-3-2-1.md`](references/topology-and-3-2-1.md) — the
  layer model, 3-2-1(+1) accounting, the ransomware-resilience extension,
  worked household and single-user topologies, and why sync and same-pool
  snapshots do not count.
- [`references/tool-selection.md`](references/tool-selection.md) — Borg vs
  Restic vs Kopia vs filesystem snapshots vs imaging vs rsync: the decision
  factors, repository back-ends, and when full-disk imaging earns its place.
- [`references/retention-and-sizing.md`](references/retention-and-sizing.md) —
  setting retention tiers from cost-of-loss, and sizing a repository from source
  size, churn, dedup ratio, and the tier schedule with `bc`.
- [`references/encryption-and-keys.md`](references/encryption-and-keys.md) —
  client-side encryption per layer, passphrase vs keyfile, the sealed recovery
  record, the recovery contact, and testing recovery from documentation only.
- [`references/credential-separation.md`](references/credential-separation.md) —
  the append / prune / restore / admin split, append-only and immutable
  repository modes per tool, and how it bounds a compromised endpoint.
- [`references/difficult-sources.md`](references/difficult-sources.md) —
  databases, VMs, mail stores, password vaults, encrypted volumes, and
  cloud-only files: how to capture each consistently and how to restore-test it.
- [`references/monitoring.md`](references/monitoring.md) — last-success tracking
  per device and copy, repository verification cadence, capacity forecasting,
  SMART / pool health, staleness thresholds, and silence alerting.
- [`references/restore-drills.md`](references/restore-drills.md) — the monthly
  sampled restore with byte verification, the semi-annual full drill, the
  ransomware-rollback drill, and how to score and record each.
- [`references/checklist.md`](references/checklist.md) — the pre-launch
  checklist and the recurring drift-review checklist.

## Templates

- [`templates/protection-charter.md`](templates/protection-charter.md) — sources,
  data classes with RPO/RTO, difficult sources, targets, and the copies each
  class must reach.
- [`templates/topology-map.md`](templates/topology-map.md) — the layer diagram:
  every source, every copy, the medium, the location, the credential, and the
  3-2-1(+1) tally.
- [`templates/retention-policy.md`](templates/retention-policy.md) — retention
  tiers per data class, encryption per target, credential roles, and key custody.
- [`templates/restore-drill-report.md`](templates/restore-drill-report.md) — a
  dated drill record: scope, method, files verified, failures, time-to-restore,
  runbook gaps found.
- [`templates/recovery-runbook.md`](templates/recovery-runbook.md) — repository
  locations, key retrieval, per-scenario restore commands, verification, and
  contacts.

## Verification

[`verification/`](verification/) (`sh verification/run.sh`) drives a reference
setup through the properties that matter: a sampled restore byte-matches the
source; a file deleted from the source is still restorable from an earlier
snapshot; a snapshot taken *after* simulated ransomware encryption does not
overwrite the clean history, and a rollback to the pre-encryption snapshot
recovers the plaintext; the append-only writer credential can add a snapshot but
cannot prune or delete; pruning with the maintenance credential honors the tier
schedule and no further; and the staleness monitor fires when a device's
last-success timestamp ages past its threshold with no error logged. A second
check (`check_templates.py`) confirms every template and reference exists and
carries the sections this SKILL.md promises. Standard library only.

## Completion report

Report: every source with its data class, RPO, and RTO; the difficult sources
and their capture method; the topology with the 3-2-1(+1) tally and which copy
is offline or immutable; the backup engine and the fast-snapshot mechanism; the
retention tiers per class and the repository size forecast; the encryption per
target and the key-custody arrangement including the recovery contact; the four
credential roles and where each lives; the scheduled jobs (built via
`unattended-automation`) and the setup/recovery agent if any (built via
`agent-automation`) with its approval-gated actions; the monitoring signals and
staleness thresholds; the last sampled-restore and full-drill results with
files verified and time-to-restore; and confirmation the recovery runbook has
been executed by someone other than its author. State residual risks (initial
seed not yet complete, an untested source, a single-administrator dependency)
and explicit non-claims — in particular, do not claim any data class is
recoverable until a restore of that class has been demonstrated.
