# Probes and value of information

Discovery has to move from reflection to a learning action. This is how the
learning backlog is built and ranked.

## Value of information

Rank candidate investigations by expected decision value, not curiosity:

```
VoI ≈ E[decision value after learning] − E[decision value before learning] − cost of learning
```

The expected-value-of-perfect-information (EVPI) special case is a useful upper
bound and is exactly computable for a small decision: it is the expected payoff
if you could know the true state before acting, minus the payoff of the best
fixed action now. If EVPI is below the cost of the cheapest informative probe,
do not run the probe — act on the current best action and monitor.

Worked shape (two actions `a1, a2`, two states `s1, s2` with probabilities
`p, 1−p`, payoff matrix `v(a, s)`):

```
value_now      = max( p·v(a1,s1) + (1−p)·v(a1,s2) ,  p·v(a2,s1) + (1−p)·v(a2,s2) )
value_perfect  = p·max(v(a1,s1), v(a2,s1)) + (1−p)·max(v(a1,s2), v(a2,s2))
evpi           = value_perfect − value_now
```

`verification/checks.bc` computes this for a concrete case. A partial-information
probe (imperfect signal) is worth at most EVPI and is valued with the same
structure using the signal's likelihoods.

High-value questions are: decision-relevant; genuinely uncertain; capable of
changing the action; answerable at reasonable cost and time; connected to a
large or irreversible downside.

## Probe-selection guide

| Unknown type | Best learning action |
|---|---|
| Missing factual information | Primary-source / records search, instrumentation, audit |
| Uncertain parameter | Measurement campaign, calibration study, Bayesian update, DOE |
| Competing causal explanations | Controlled or natural experiment, causal analysis, process tracing |
| Model-form uncertainty | Compare independent models, residual analysis, external validation, stress test |
| Rare failure | Fault tree, FMEA, simulation, stress test, fault injection, analogous-case search |
| Human behaviour / adoption | Interviews, ethnography, usability study, field pilot, segmentation |
| Adversarial behaviour | Threat modelling, red team, penetration test, game-theoretic scenarios |
| Future change | Horizon scan, scenarios, signposts, options / reversible commitments |
| Measurement blind spot | Add logging / sensors, data-quality audit, manual observation, reconciliation |
| Complex interactions | Factorial DOE, sensitivity analysis, agent-based / system simulation |
| Operational feasibility | Shadow mode, limited pilot, tabletop exercise, workflow observation |

## Safe-to-fail experimentation

Prefer probes that are: limited in scope; reversible; bounded by explicit safety
constraints; observable; instrumented *before* they start; protected by a stop
rule; designed to teach at least one discriminating lesson; followed by a
decision review.

### Learning-backlog entry

```yaml
learning_item:
  question: ""
  unknown_type: ""              # from the guide above
  probe_or_method: ""
  discriminates: []             # which hypotheses / assumptions it separates
  expected_decision_value: "low | medium | high  (+ rationale, or EVPI if computed)"
  cost_and_duration: ""
  reversible: true
  safety_boundary: ""
  success_criteria: ""
  disconfirming_outcome: ""     # what result would falsify the hypothesis
  stop_rule: ""
  owner: ""
  review_after: ""
```

An item with no `disconfirming_outcome` is not a probe — it is a search for
confirmation, and it goes back for redesign.

## Hand-offs to the sibling skills

- **[`simulation`](../../simulation/SKILL.md)** — explore the consequences of a
  scenario or a failure chain before touching the real system; quantify
  uncertainty and sensitivity.
- **[`design-of-experiments`](../../design-of-experiments/SKILL.md)** — when the
  probe is a real comparison: charter, estimand, least-complex-adequate design,
  power, pre-registered analysis plan.
- **[`control-systems`](../../control-systems/SKILL.md)** — when a live probe
  runs on an actuated system: an independent safety filter and a human override
  enforce the safety boundary regardless of what the probe requests.
- **[`tla-checker`](../../tla-checker/SKILL.md)** / **[`lean`](../../lean/SKILL.md)**
  — when the unknown is whether an invariant or protocol can be violated:
  bounded state exploration or a machine-checked core.
- **[`bc`](../../bc/SKILL.md)** — the VoI / EVPI and calibration arithmetic
  (lowercase identifiers; no `_` or single uppercase letters).
