# Rule register — <domain>

One row per transition rule. The read-set and write-set are enforced by the
engine and are the basis of the causal graph — declare them exactly, not
approximately.

## Schema

- **Entity types:** <role, user, item, node, …>
- **Relations:** <holds(user, role), adjacent(node, node), …>
- **Varying fields** (persistent / cumulative — see `temporal-data-modeling`):

  | Field | Type / domain | Persistent or cumulative | Resolution |
  |---|---|---|---|
  | `stock(item)` | int 0..100 | persistent | per step |
  | `total_consumed(item)` | int ≥ 0 | cumulative | run to date |

- **Exogenous inputs as fields** (time, randomness, external signals — set explicitly per step):

  | Field | Domain | Set by |
  |---|---|---|

## Rules

### `<rule_name>(<params>)`

| | |
|---|---|
| **Parameters** | `item: Item` |
| **Guard** | `stock(item) < threshold(item) ∧ ¬pending_order(item)` |
| **Read-set** | `stock(item), threshold(item), pending_order(item)` |
| **Write-set** | `pending_order(item)` |
| **Effect** | `pending_order(item) := true` |
| **Nondeterministic?** | no — one successor per binding |
| **Justification** | the reorder policy fires exactly once when stock crosses the threshold from above |
| **Source** | inventory-policy.md §3.2 |

### `<rule_name>(<params>)`

| | |
|---|---|
| **Parameters** | |
| **Guard** | |
| **Read-set** | |
| **Write-set** | |
| **Effect** | |
| **Nondeterministic?** | |
| **Justification** | |
| **Source** | |

## Confluence pass

| Rule pair | Can both be enabled together? | Write/read overlap? | Orders reach different states? | Verdict | Resolution |
|---|---|---|---|---|---|
| `grant` / `revoke` (same role) | yes | yes (`holds`) | yes | **conflict** | arbitrate: deny-wins rule added |
| `grant` / `grant` (different users) | yes | no | no | not a conflict | — |
| `consume` / `restock` (same item) | yes | yes (`stock`) | no (commutative on the level) | not a conflict | — |

**Per-slice verdict for the scenario:**

| Slice | Confluence | Deliverable |
|---|---|---|
| inventory | confluent | causal graph |
| roles | non-confluent | branch set — no single "A caused B" |
