# Driving the sandbox

How an agent poses a scenario, reads the result, and navigates it — and how the
sandbox sits as a pure what-if tool inside an
[`agent-automation`](../../agent-automation/SKILL.md) loop.

## The materialized result

The agent never receives raw state dumps. It receives a **result object**:

```json
{
  "scenario": {
    "initial_facts": ["stock(widget)=40", "threshold(widget)=25", "holds(alice,admin)"],
    "interventions": [
      {"branch": "A", "label": "revoke(alice,admin) at step 0"},
      {"branch": "B", "label": "no change"}
    ],
    "bounds": {"steps": 12, "entities": {"item": 1, "user": 3}, "scheduler": "priority", "seed": 1},
    "confluence": {"slice:roles": "NON_CONFLUENT (grant/revoke on admin)", "slice:inventory": "confluent"}
  },
  "events": [
    {"id": "e1", "branch": "A", "step": 0, "rule": "revoke", "binding": {"u":"alice","r":"admin"},
     "reads": ["holds(alice,admin)"], "writes": ["holds(alice,admin)"]},
    {"id": "e2", "branch": "A", "step": 1, "rule": "consume", "binding": {"item":"widget"},
     "reads": ["stock(widget)"], "writes": ["stock(widget)","total_consumed(widget)"]},
    {"id": "e3", "branch": "A", "step": 2, "rule": "reorder", "binding": {"item":"widget"},
     "reads": ["stock(widget)","threshold(widget)","pending_order(widget)"], "writes": ["pending_order(widget)"]}
  ],
  "causal_edges": [
    {"from": "e2", "to": "e3", "via": ["stock(widget)"]}
  ],
  "root_causes": {
    "e3": ["threshold(widget)=25 (initial)", "stock(widget)=40 (initial)"]
  },
  "observable": {
    "expr": "stock(widget)",
    "by_step": {"A": [40, 40, 15, 15], "B": [40, 40, 15, 15]}
  },
  "terminals": {"A": "step 11 (budget)", "B": "step 11 (budget)"}
}
```

Everything the agent needs to reason about cause and effect is here: the events,
the causal edges with the *field* that carries each dependency, the root causes,
and the observable's trajectory per branch. State reconstruction is never
required.

This is [`temporal-data-modeling`](../../temporal-data-modeling/SKILL.md)'s
"when a language model is the downstream reader" note applied literally: hand the
model the derived facts (events, edges, root causes, observable trajectory), not
the raw versioned store.

## Navigation queries

Four queries, all answered from the result object without re-running:

| Query | Input | Returns |
|---|---|---|
| `forward_deps(event_id)` | an event | events causally downstream of it on the same branch |
| `backward_deps(event_id)` | an event | the causal chain back to root causes |
| `why(predicate, step, branch)` | an observable transition | `backward_deps` of the event that caused that transition |
| `diff(branch_a, branch_b)` | two branches | events unique to each, the first divergent step, the causal-edge difference |

An agent asked "why did stock hit zero" calls `why("stock(widget)=0", 5, "A")`
and gets the chain — not a guess anchored on the last visible `consume`.

## The scenario the agent submits

```json
{
  "initial_facts": ["..."],
  "interventions": [{"label": "...", "changes": ["..."]}],
  "observable": "stock(widget)",
  "direction": "forward",
  "bounds": {"steps": 12, "scheduler": "priority", "seed": 1}
}
```

For a backward query:

```json
{
  "initial_facts": ["..."],
  "target": "stock(widget)=0",
  "direction": "backward",
  "budget": 2,
  "bounds": {"steps": 12}
}
```

The agent chooses the initial facts, the interventions, the observable, and the
bounds. It does **not** choose the rules — those are the authored model, fixed
for the sandbox's lifetime. If a scenario needs a rule the register does not
have, that is a modelling change, reviewed and sourced, not a scenario parameter.

## Inside an `agent-automation` loop

The sandbox is a **read-only tool** in the
[`agent-automation`](../../agent-automation/SKILL.md) sense:

- **Trigger / input** — the agent has a decision to make ("should I apply this
  config change?") and seeds the sandbox's initial facts from the real system's
  current state (a read).
- **Proposal** — the agent proposes a typed action *and*, before it is
  authorized, runs the sandbox forward with that action as the intervention.
- **Policy** — the policy engine can require a sandbox trace as evidence for
  elevated-risk actions: "no `revoke` on a role with an active lease unless a
  sandbox run shows the lease-holder loses write access within N steps".
- **The sandbox itself authorizes nothing and executes nothing.** It changes no
  real state. Its output is an input to the policy decision and the human
  approval view — "here is the predicted causal chain" — never a substitute for
  them.

The division of labour: `agent-automation` owns *whether the action is allowed
and how it is executed and verified*; `causal-sandbox` owns *what the action is
predicted to cause, and why*.

## The discipline in practice

When the agent is about to write a sentence beginning "this will probably…",
"the likely effect is…", "I expect that…" about a domain whose rules are in the
register — that is the moment to run the sandbox instead. The sandbox turns the
sentence into `forward_deps` of the proposed event, with the causal edges shown.

If the rules are *not* in the register and cannot be authored, the honest move is
to say so and route to [`simulation`](../../simulation/SKILL.md) — not to fall
back on narration.
