# Trace report — <domain / question>

## Question

- **Direction:** forward | backward
- **Restated:** <the one-sentence question>
- **Observable:** <predicate/field and how read>

## Model

- **Rules used:** <list, each with its source>
- **State schema:** <entities, relations, varying fields with persistent/cumulative marks>
- **Bounds:** steps <n>; entities <…>; value domains <…>; scheduler <…>, seed <…>

## Confluence verdict

| Slice | Verdict | How each conflict was resolved | Deliverable for this slice |
|---|---|---|---|
| | confluent / non-confluent | commute / arbitrate / accepted | causal graph / branch set |

## Result — forward

**Branches:**

| Branch | Intervention | Terminal | Observable trajectory |
|---|---|---|---|
| A | | step <n> (budget / frozen) | `[…]` |
| B | | | `[…]` |

**Causal graph (branch A):**

```
e1 (revoke alice admin)
e2 (consume widget) ──stock(widget)──> e3 (reorder widget) ──pending_order──> e5 (restock widget)
root causes of e3: threshold(widget)=25 [initial], stock(widget)=40 [initial]
```

**The causal path from the intervention to the observable:**
<one paragraph, every clause a trace fact>

## Result — backward

- **Target:** <"stock became 0 at step 5">
- **Why (causal chain):** <the backward walk to root causes>
- **Minimal intervention:** <Δ of k changes> | **NO_FIX_WITHIN_BUDGET (<n> changes)**
- **Rejected candidates and why:** <"skip the day-4 consume" — not an S_0 change; invalidates e7's guard>

## Policy comparison (if applicable)

- **Events unique to A:** …
- **Events unique to B:** …
- **First divergent step:** …
- **Causal-edge difference explaining it:** …

## Non-claims

- This trace is behaviour under the authored rules in this scenario — **not**
  proof about the real system.
- Consequences past step <n> or with more than <k> entities are **not observed
  within the bound**, not shown to be absent.
- <if any slice non-confluent:> No single causal claim is made for the <slice>
  slice; the branch set is the answer there.
- The rules are authored from <sources>; if a rule is wrong the trace is wrong —
  the rules, not the trace, are the thing to review first.
