# Encryption and recovery keys

Encryption protects **confidentiality** — a stolen disk or an untrusted remote
host holds ciphertext. It does nothing for **availability**: a lost passphrase is
lost data, permanently, with every tool here. Treat key custody as the highest-
stakes part of the whole system.

## What to encrypt, where

| Target | Encryption | Mechanism |
|---|---|---|
| Fast local (external SSD, Time Machine disk) | yes | FileVault / BitLocker / LUKS on the disk, or the backup tool's own |
| Independent repository (home NAS) | yes | the backup tool's client-side encryption (Borg repokey/keyfile, restic, Kopia) |
| Offline rotation disk | **yes, always** | LUKS / VeraCrypt / hardware-encrypted enclosure, *and* the tool's encryption |
| Off-site repository (someone else's machine) | **yes, always** | client-side only — the remote end must never hold plaintext or the key |
| The initial seed you carry on a disk | yes | full-disk encryption on the transport disk |

Client-side encryption means the data is encrypted **before it leaves the
machine being backed up**. Borg states this model explicitly: the backup server
does not need to be trusted because it only ever sees encrypted data.

## Passphrase vs keyfile

- **Passphrase (repokey)**: the key material is stored in the repo, unlocked by
  a passphrase. Simplest. The passphrase *is* the recovery secret.
- **Keyfile**: key material is a file on the client, plus an optional
  passphrase. Stronger, but now you must back up *the keyfile* somewhere the
  repo is not — losing it loses the repo even though the data is intact.

For a household, repokey + a strong passphrase (a 5–6 word diceware phrase) is
usually the right trade. If you use keyfiles, the keyfile goes in the sealed
recovery record below, not only on the laptop.

## The sealed recovery record

For **each** repository, store — physically and separately from any everyday
device — a record containing:

1. The repository **passphrase** (and keyfile, if used).
2. The repository **location** (host, path, bucket, URL) and how to reach it
   (SSH key or its location, mesh VPN join info, rest-server URL).
3. The **tool and version**, and the exact **restore commands** (copy them from
   the recovery runbook).
4. The **disk-encryption passphrases** (LUKS/VeraCrypt/FileVault recovery keys)
   for every offline and transport disk.
5. Date and a "test-restored on ____" line.

Where "sealed and separate" can be:

- a password manager entry **plus** a printed copy in a home safe or a
  bank deposit box;
- a printed copy given to the named recovery contact (see below);
- for the truly critical, split with Shamir's Secret Sharing (e.g. `ssss`,
  or a hardware wallet's seed-split feature) across two trusted people.

Never: only in the password manager whose 2FA lives on the phone that is also
being backed up; only in a file inside the repository you are trying to unlock;
only in your memory.

## The recovery contact

Name at least one trusted person who **could** recover the data if you were
unavailable — and make sure they actually can:

- They have (or can retrieve) the sealed recovery record.
- The recovery runbook is written for someone with their skill level, or they
  know who to hand it to.
- For an off-site copy hosted on *their* hardware: they know which disk/dataset
  it is and agree not to repurpose it without telling you.

## Key rotation

Changing a repository passphrase or key is a **gated action** — it must be
deliberate and immediately reflected in every copy of the sealed record.

- Borg: `borg key change-passphrase` (rotates the passphrase, not the underlying
  key). `borg key export` to refresh the sealed copy.
- Restic: `restic key add` then `restic key remove` the old one — restic
  supports multiple keys, so add-then-verify-then-remove is safe.
- Kopia: `kopia repository change-password`.

After any rotation: re-test a restore with **only** the new sealed record, then
destroy the old printed copies.

## Do not confuse encryption with backup

An encrypted single copy is still one copy. Encrypt *and* keep the layer count.
And an encrypted repo you cannot open is worse than no backup — it is a false
sense of security. The restore drill (see
[`restore-drills.md`](restore-drills.md)) exists partly to prove the keys work.
