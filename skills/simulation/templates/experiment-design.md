# Experiment-design template

How the runs are structured so the output supports the decision. For a designed
comparison across many factors — screening, factorial / fractional-factorial,
response-surface, robustness, formal power / run-count, a pre-registered
analysis plan — use [`design-of-experiments`](../../design-of-experiments/SKILL.md)
and its [`references/simulation-doe.md`](../../design-of-experiments/references/simulation-doe.md)
instead of extending this block.

```
BASELINE      : <scenario, and why it is the reference>
ALTERNATIVES  : <each differs from baseline only in: factor = value>
FACTORS       : <full-factorial | fractional | one-at-a-time | Latin hypercube>
RANDOMIZATION : <independent streams | common random numbers>  seed log: <path>
REPLICATIONS  : n = <...>   convergence criterion : <half-width < X on metric M>
WARM-UP       : <duration discarded; how chosen>
TERMINATION   : <horizon | completion count | steady-state test>
METRICS       : <primary + secondary, each with units and decision threshold>
COMPARISON    : <paired t / Welch / bootstrap CI / ranking + probability best>
STOPPING RULE : <fixed n | sequential with error control>
RETENTION     : <what is kept for audit; for how long>
```
