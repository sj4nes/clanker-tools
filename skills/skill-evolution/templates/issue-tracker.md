# Issue tracker

One tracker for the whole run. Update it every round, after the acceptance
decision. Do not reset it between rounds — its purpose is to keep round `t`'s
edit consistent with the edits from earlier rounds that worked.

## Status legend

- `open` — identified, not yet resolved
- `resolved` — the failure is absent from the latest accepted candidate
- `reopened` — a resolved issue's failure came back; record the round

Two failed attempts on a `reopened` issue → stop patching it, review the
document's structure for that problem.

---

## ISS-001

- **Pattern:** <the failure, described so a later round can recognize a recurrence>
- **Status:** open
- **Opened:** round 0 (from `S_0` traces) | round N
- **Reopened:** —
- **Attempts:**

| Round | Edit summary | Accepted? | Outcome |
|---|---|---|---|
| 2 | added "list every constraint before optimizing" | yes | partial — 2/5 cases |
| 4 | added an explicit constraint checklist | yes | resolved 5/5 |

---

## ISS-002

- **Pattern:**
- **Status:**
- **Opened:**
- **Reopened:**
- **Attempts:**

| Round | Edit summary | Accepted? | Outcome |
|---|---|---|---|
| | | | |

---

## Round summary

| Round | Issues open | Resolved this round | Reopened this round | New issues |
|---|---|---|---|---|
| 1 | | | | |
| 2 | | | | |
