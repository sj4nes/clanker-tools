# Topology map: <household / person / site>

> Every source, every copy, the medium, the location, the writing credential.
> This is the document you check 3-2-1(+1) against.

## Diagram

```text
                          ┌─────────────────────────┐
  laptop-a ── snapshot ──▶│ local: APFS + ext SSD   │   (fast local recovery)
     │                    └─────────────────────────┘
     │  restic (append-only writer cred)
     ▼
┌──────────────────────────────┐   restic copy / zfs send (prune cred)
│ NAS repo  /srv/restic/laptop-a│──┬──▶ offline USB HDD  (unplugged between windows)   [+1 offline]
│ retention 24h/30d/12m/7y      │  │
│ object-lock: <yes/no>         │  └──▶ off-site repo @ <relative>  over <mesh>        [+1 off-site]
└──────────────────────────────┘        (client-side encrypted; remote holds ciphertext)
```

(Repeat per device, or draw one combined diagram.)

## Copy inventory

| # | What it holds | Medium | Location (building) | Online / offline | Writing credential | Can it delete history? | Encrypted |
|---|---|---|---|---|---|---|---|
| 1 | primary — laptop-a | internal SSD | home | online | — | n/a | FileVault |
| 2 | fast local — laptop-a | external SSD | home | online (attached) | Time Machine | n/a | yes |
| 3 | repository — laptop-a | NAS HDD (mirror) | home | online | writer (append-only) | **no** | tool |
| 4 | offline — all devices | USB HDD | work / relative | **offline** | prune host | no (disconnected) | LUKS + tool |
| 5 | off-site — all devices | relative's NAS | other building | online | replication cred | **no** (object-lock) | tool (client-side) |

## 3-2-1(+1) tally, per data class

| Data class | # copies | # media types | # buildings | ≥1 offline/immutable? | OK? |
|---|---|---|---|---|---|
| photos / authored |  |  |  |  |  |
| financial / legal |  |  |  |  |  |
| documents |  |  |  |  |  |
| projects / code |  |  |  |  |  |

## Credential map

| Credential | Role | Lives on | Scope |
|---|---|---|---|
|  | writer / prune / restore / admin |  |  |

## Data flows / schedules

| Job | From → To | Tool / command | Schedule | Credential | Built as |
|---|---|---|---|---|---|
| local snapshot | laptop-a → ext SSD |  | hourly |  | OS |
| repo backup | laptop-a → NAS |  | 02:00 daily | writer | `unattended-automation` |
| prune | NAS |  | weekly | prune | `unattended-automation` |
| repo verify | NAS |  | weekly meta / monthly full | restore | `unattended-automation` |
| off-site replicate | NAS → relative |  | nightly | replication | `unattended-automation` |
| offline backup | NAS → USB HDD |  | on connect | prune host | `unattended-automation` + human |
| sampled restore | NAS → scratch |  | monthly | restore | `unattended-automation` |
