# Topology, 3-2-1(+1), and why sync doesn't count

A backup topology is the set of **copies** of your data, where each lives, on
what medium, and which credential can change it. Design it before you pick a
tool.

## The layer model

| Layer | Job it does | Restore speed | Reaches | Cannot save you from |
|---|---|---|---|---|
| Primary | The working copy you edit | instant | you | any loss at all |
| Fast local recovery | "I broke this file yesterday" | seconds–minutes | same machine / same room | pool failure, fire, theft, ransomware with admin |
| Independent repository | Machine died; restore months of history | minutes–hours | separate hardware on the LAN | building loss, LAN-wide compromise |
| Offline / air-gapped | Break-glass after ransomware or repo corruption | hours | a disconnected disk | its own staleness between rotations |
| Off-site | The house is gone | hours–days | another building | needs connectivity + an access agreement |

Every data class must land on **fast local recovery + independent repository +
(offline OR off-site)** at minimum. The most valuable, least replaceable classes
(family photos, financial and legal records, anything you authored) land on
*both* offline and off-site.

## 3-2-1, and the +1

The baseline (CISA, and every backup vendor): **3** copies of data that matters,
on **2** different storage types, with **1** off-site. Backups should run
automatically and on a schedule.

The +1 is the ransomware and "malicious admin" extension: **at least one copy
that a compromised everyday computer cannot alter or delete.** That means one of:

- an **offline** copy — a rotated USB disk that is physically disconnected
  except during its own backup window;
- an **append-only** repository — the writer credential can add snapshots but
  the API/permission set forbids deletion and pruning (Borg `append-only`,
  restic with a restricted `rest-server`/S3 policy, Kopia with a compliant
  object-lock bucket on your own hardware);
- an **immutable** copy — object-lock / WORM retention, or a filesystem where
  the backup account cannot destroy snapshots.

Count copies honestly:

- The source is **not** a copy.
- A second partition on the same disk is **not** a second copy.
- A ZFS/Btrfs/APFS snapshot **on the same pool** is **not** a backup — it shares
  the failure domain of the disk and is deletable by anyone with admin.
- A sync folder replicated to three devices is **one** logical copy — they all
  converge on the same state.

## Why sync is not backup

| Event | Sync-only outcome | Backup outcome |
|---|---|---|
| Accidental delete | Deletion propagates to every device | Restore from a prior snapshot |
| Ransomware encrypts files | Encrypted versions sync out; good versions overwritten | Restore the snapshot from before infection |
| Silent corruption | Corrupt bytes propagate | Restore an older intact version |
| Laptop stolen | Data survives elsewhere, but no *history* | Restore a specific point in time |
| House fire | Every synced device may be in the fire | Restore the off-site copy |
| Account lockout / service shutdown | Access blocked | The repository is yours |

Sync services (Dropbox, iCloud, OneDrive, Google Drive) and Syncthing are built
to make devices agree on the *current* state. Their version history is a
convenience layer, bounded and sometimes off by default — Syncthing's versioning
is disabled out of the box and does not archive versions of changes made
*locally* on the same device. Treat sync history as "undo", never as retention.

## Worked topologies

### Single user, one laptop

- **Fast local**: Time Machine / File History to a dedicated external SSD, or
  APFS local snapshots.
- **Repository**: `restic` (or Kopia) to an SFTP account on a cheap mini-PC or
  NAS at home, or to a `rest-server` in append-only mode.
- **Offline**: a second encrypted USB HDD, backed up weekly then unplugged and
  kept at work or a relative's.
- Tally: primary + local SSD + home repo + offline disk = 4 copies, 3 media
  (internal SSD, external SSD/HDD, NAS), 1 off-site (the offline disk), +1
  offline. ✔

### Household, two laptops + a desktop

- Each machine: hourly/daily OS snapshots → nightly `restic`/Borg backup to a
  home NAS with mirrored disks, using a per-machine append-only credential.
- NAS: retention `24 hourly / 30 daily / 12 monthly / 3–7 yearly`; nightly
  `zfs send` or `restic copy` to:
  - a rotated USB disk (plugged in for the window, then unplugged), **and**
  - an encrypted repository on a trusted relative's always-on machine over a
    private mesh (WireGuard / Tailscale-style).
- Agent/cron checks results daily, verifies the repository weekly, runs a
  sampled restore monthly.
- Tally per machine: primary + local snapshot + NAS repo + offline disk +
  off-site repo = 5 copies, 3+ media, 1 off-site, +1 offline and +1 append-only.
  ✔

## Don't expose file sharing to the internet

Off-site replication rides SSH, a mesh VPN, or a narrowly-scoped repository
endpoint (rest-server, MinIO with a tight policy). Never port-forward SMB/NFS/AFP
to the public internet to reach a remote NAS.
