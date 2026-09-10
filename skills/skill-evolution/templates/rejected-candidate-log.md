# Rejected-candidate log

One row per proposed patch — accepted or not. The rejected rows are the point:
before proposing a patch, check this log so the loop does not re-propose a
dead-end edit or re-discover a failure it already explained.

| Round | Target issue | Diff summary | Budget / used | Gate result | Reason |
|---|---|---|---|---|---|
| 1 | ISS-001 | added constraint-checklist section (6 lines) | 8 / 6 | accepted | primary +2.4, protected within boundary |
| 2 | ISS-002 | rewrote the cost-optimization guidance (5 lines) | 5 / 5 | rejected | mean +1.1 but cost-per-task regressed 0.8 (boundary 0) |
| 3 | ISS-002 | narrower: one line capping itinerary length | 5 / 1 | accepted | aux metric +2.6 carried a flat primary; protected ok |

## Dead-end edits — do not re-propose

- <short description of an edit that was tried and clearly failed, with the round and outcome>
