# Admission hypothesis — <candidate id>

Written **before** the paired run. If it is written after, the run is an
illustration, not a gate.

## Candidate

- **Rung:** text | structured | procedure | executable
- **If above `text`:** what recurrence justifies the rung (which tasks, how
  many times), and which promotion gate it passed (followable-as-written /
  compiles-and-runs).

## The claim

> Adding this entry improves **<metric>** on **<task family>** by at least
> **<effect>**, because **<mechanism>**.

- **Protected metrics** that must not regress: <list, with orientation —
  lower-is-better or higher-is-better>
- **Where I expect it NOT to help:** <named, in advance>

## The run

| | |
|---|---|
| Task set | <ids; how sampled> |
| Pairing | same tasks, same order, same budget, both arms |
| Control | library @ <version>, candidate absent |
| Treatment | identical, candidate added |
| n tasks | <n> |
| Stop rule | fixed n, decided now |

## Result

| | Value |
|---|---|
| Mean paired difference | |
| Standard error | |
| Decision threshold | |
| Protected metrics | |
| **Admit?** | |

## Independent confirmation

Tasks **not** used to propose the candidate:

| | Value |
|---|---|
| Task set | |
| Result | |

## Displacement

The library is capped at **<cap>**. This entry displaces:

| Displaced id | Contribution at retirement | Archived where |
|---|---|---|

If nothing was displaced, say why the cap did not bind — and check that it
still binds at all.
