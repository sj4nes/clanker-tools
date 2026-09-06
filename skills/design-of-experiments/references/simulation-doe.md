# Simulation-experiment mode

Use this mode when the "experiment" is run against a simulation model rather than
a real system. Pair it with the [`simulation`](../simulation/SKILL.md) skill,
which owns model formulation, verification, and validation; this file owns the
*experiment design* over an already-built, already-validated model.

## Three layers of uncertainty

```
real-world uncertainty  +  model-form uncertainty  +  Monte Carlo uncertainty
```

Manage them separately. A tight Monte Carlo interval around a wrong model is not
a decision-grade result.

## Separate the inputs

- **Design factors** — what you control: policies, configurations, capacities,
  algorithms, environmental settings. These are the factors in the DOE.
- **Model parameters** — uncertain real-world quantities (arrival rate, failure
  rate, elasticity). Propagate their uncertainty; do not fix them silently.
- **Random streams** — stochastic arrivals, demand, failures, behavior, noise.
  Assign each source its own RNG stream so you can reuse it across scenarios.
- **Numerical controls** — time step, solver tolerance, mesh resolution, warm-up
  length, run horizon. Not experimental factors — set them by convergence, not
  by preference.
- **Responses** — throughput, cost, risk, service level, stability, emissions,
  robustness. Report operational tails (95th-percentile delay, deadline-miss
  probability, backlog tail), not just the mean.
- **Validation cases** — real or benchmark scenarios not used to tune the model.

## Workflow

1. **Verify and validate the model before optimizing it** (the `simulation`
   skill). State whether conclusions apply only inside the model or are
   supported for real deployment.
2. Identify controllable factors, uncertain parameters, and noise variables
   separately.
3. **Screen** to drop unimportant design factors — Morris elementary effects, or
   a resolution III/IV fractional factorial over the factor list.
4. Explore the important factors and their interactions with a **space-filling**
   design (Latin hypercube, Sobol sequence) or a factorial / central-composite
   design if the factor count is small.
5. Use **common random numbers** when comparing scenarios: drive each scenario
   with the same stream draws so shared stochastic variation cancels in the
   *difference*, shrinking the variance of the comparison (often 2–5×).
6. Run enough **independent replications** to estimate uncertainty; set the count
   by a target Monte Carlo standard error relative to the smallest difference
   that matters, with a sequential stopping rule.
7. Include a **warm-up** period and a termination rule for steady-state
   discrete-event models; discard warm-up observations (Welch's method to pick
   the cutoff).
8. Check **time-step / mesh / solver-tolerance convergence** for continuous /
   physics models — halve the step and confirm the response is stable.
9. If high-fidelity runs are expensive, fit a **surrogate** (Gaussian process,
   polynomial response surface) on a space-filling design and optimize the
   surrogate, then confirm on the full model.
10. **Confirm the recommended configuration** with fresh random streams and,
    where possible, an independent implementation or a real-world pilot.

## What a useful simulation result looks like

Not "configuration 7 scored 92.4". Instead:

> "Across 500 independent replications with matched random streams,
> configuration 7 reduced mean backlog by 12% (95% interval 8–16%) while holding
> the 95th-percentile delay below the stated service limit in 93% of tested
> demand scenarios. The result is sensitive to failure-repair duration and
> should be confirmed under the planned peak-season arrival distribution."
