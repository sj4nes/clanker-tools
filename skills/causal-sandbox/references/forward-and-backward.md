# Forward and backward queries

Forward: run the rules, emit the trace and causal graph. Backward: from an
unwanted outcome, find the minimal earlier change that avoids it.

## Forward

### Construction

```
run(S0, rules, interventions, scheduler_seed, bounds):
    root ← S0
    for each intervention I in interventions:
        branch_root ← apply(I, S0)          # I is itself an event, labelled
        expand(branch_root, depth = bounds.steps)
    return trace

expand(S, depth):
    if depth = 0: return
    enabled ← [ (r, binding) for r in rules
                             for binding in bindings(r, S)
                             if guard(r, binding) holds in S ]
    if enabled is empty: mark S terminal; return          # frozen — not a bug per se
    e ← scheduler.pick(enabled, seed)
    if nondeterministic(e):
        for each choice c in choices(e, S):
            S' ← apply(e, S, c);  child branch labelled c;  expand(S', depth-1)
    else:
        S' ← apply(e, S);  expand(S', depth-1)
```

The engine checks, on every `apply`: the guard read only declared fields, the
effect wrote only declared fields. A violation halts the run with the offending
rule — a wrong causal graph is worse than no run.

### The causal graph for a branch

Walk the branch's event sequence `e_1 … e_n`. For each pair `i < j`, add edge
`e_i → e_j` if `writeset(e_i) ∩ readset(e_j) ≠ ∅` and no `e_k` (`i < k < j`)
overwrote all of that intersection. Take the transitive reduction. Attach, to
each event, the initial facts of `S_0` its guard read (the root causes on that
branch).

### What the agent reads

Not the states. The **event list** (`id, rule, binding, step, branch`), the
**causal edges**, the **per-branch intervention label**, and the **observable**
evaluated at each state (`stock(widget)` per step; `holds(alice, admin)` per
step). See [`driving-the-sandbox.md`](driving-the-sandbox.md) for the format.

## Backward

A backward query names a **target event** or a **target predicate transition**:
"stock(widget) became 0 at step 5", "holds(alice, admin) became false at step 3".
The question is one of two:

### "Why did this happen?" — the causal-dependency walk

Start at the target event. Walk causal edges backward. Stop at events with no
causal predecessor and at the initial facts their guards read. Return the
subgraph. This is deterministic and cheap — it is a reverse reachability over the
causal edges already built.

The value: it defeats the **recency heuristic**. An agent narrating "why did
stock hit zero" will blame the last `consume`. The walk shows the actual chain —
e.g. `restock` never fired because `reorder` never fired because `threshold` was
set too low in `S_0`. The root cause is an initial fact three events back, not
the visible last event.

### "What is the smallest change that prevents this?" — bounded abduction

The search space is **changes to `S_0`** (initial facts and field values) and
**changes to the intervention set**. Not changes to the rules — the rules are the
authored model; if they are wrong, fix them and re-run, do not search over them.

```
minimal_intervention(S0, rules, target, budget):
    for k in 1 .. budget:
        for each candidate set Δ of k changes to S0 / interventions:
            drawn from: initial facts the target's causal ancestors read,
                        field values in those facts' domains,
                        add/remove of an intervention
            S0' ← apply(Δ, S0)
            trace' ← run(S0', rules, ...)
            if target event never fires on any branch of trace'
               and trace' is valid (every applied event's guard held):
                return Δ                      # first minimal fix found
    return NO_FIX_WITHIN_BUDGET
```

Notes:

- **"Minimal" = fewest changes**, searched in increasing `k`. Ties (several
  1-change fixes) are all reported; the agent picks on domain grounds.
- **The candidate set is scoped by the causal graph.** Only initial facts that
  the target's causal ancestors actually read can matter — changing an unrelated
  fact cannot prevent the target. This keeps the search small.
- **Validity is rechecked.** A Δ that prevents the target by making some *other*
  rule's guard fail partway (an incoherent world) is rejected.
- **`NO_FIX_WITHIN_BUDGET` is a real answer.** It means: within `budget` changes
  to the initial conditions, the target is unavoidable under these rules. Report
  it as that — not as "impossible", and not by silently raising the budget.

### Why "delete the bad event" fails

The naive backward answer is "just don't let `consume` fire on day 4". Three
problems:

1. **It is not an initial-condition change.** You cannot "not fire" an enabled
   rule without changing what enabled it — which *is* an `S_0` change, and the
   search will find the real one (`raise threshold`, `add a restock`).
2. **It can invalidate the trace.** A later event's guard may have depended on
   that `consume` having happened. Removing it leaves a branch where an applied
   event's guard did not actually hold.
3. **It is not actionable.** "Don't consume" is not a lever the domain owner has;
   "set the reorder threshold to 30" is.

The search returns levers that exist in `S_0`, which is where real controls live.

## Comparing two policies

Two interventions from a shared root → two branches. The deliverable is the
**diff**:

- events present on branch A but not B (and vice versa);
- the first step at which the observable diverges;
- the causal-graph difference — which new causal edge under A explains the
  divergence.

"Policy A connects the last demand pair; policy B does not, because under B the
`build_segment` rule for edge 7 was never enabled — its budget guard failed after
B spent the budget on edge 3." That sentence is the output, and every clause of
it is a trace fact.
