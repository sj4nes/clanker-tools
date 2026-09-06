# Verification, validation, and deployment

Following NASA systems-engineering usage: **verification** shows the system
satisfies its specified requirements ("built it right"); **validation** shows it
fulfils its intended purpose in the intended environment ("built the right
thing"). Both are required and reported separately. Passing simulation is
neither — it is one rung on the deployment ladder.

## Verification activities

- dimensional and unit tests;
- symbolic / model review of the control-law and observer equations;
- static analysis and code review of the implementation;
- requirements traceability (each requirement maps to a test);
- gain and stability-margin calculations reproduced independently;
- constraint and saturation tests (does the output ever exceed limits?);
- hardware-interface tests (scaling, sign, units at every boundary);
- deterministic replay under fixed seeds / recorded inputs;
- worst-case execution time measured on the target processor;
- numerical precision and overflow checks (fixed-point ranges, integrator
  growth);
- state-machine transition coverage;
- formal methods where feasible ([`lean`](../../lean/SKILL.md) for invariant /
  algebraic cores, [`tla-checker`](../../tla-checker/SKILL.md) for bounded
  mode-transition logic);
- software-in-the-loop (SIL), processor-in-the-loop (PIL),
  hardware-in-the-loop (HIL) as available;
- fault injection.

## Validation activities

- compare model response to real plant input–output data;
- pilot in representative operating conditions;
- evaluate the **full operating envelope**, not only nominal;
- test disturbances, faults, operator interventions, degraded sensing;
- confirm the stakeholder performance requirements are met;
- confirm the safety outcomes and the usability of the override in the time
  available;
- validate the predicted tradeoffs (energy, quality, delay, throughput,
  comfort) against measurement;
- test generalisation to new loads, environments, sites, equipment lots;
- staged deployment and shadow-mode evaluation.

State the validation evidence **and the gaps** explicitly.

## The test scenario matrix

Cover, for every candidate controller:

- nominal tracking and disturbance rejection;
- worst-case disturbance magnitude and rate;
- uncertain-parameter corners (all combinations of the envelope extremes);
- sensor noise, bias, latency, dropout, stuck-at;
- actuator saturation, rate limit, dead zone, partial and total failure;
- communication delay, jitter, packet loss, reordering;
- mode transitions, simultaneous events, transition-during-fault;
- model mismatch (structure, not just parameters);
- operator override mid-manoeuvre and handback;
- restart, recovery, and cold-start;
- cyber-disruption modes (spoofed measurement, delayed command, replay);
- extreme environmental or demand conditions within scope;
- solver / numerical failure and the fallback path;
- simultaneous independent faults.

Use the [`simulation`](../../simulation/SKILL.md) skill for the plant and its
uncertainty and [`design-of-experiments`](../../design-of-experiments/SKILL.md)
to lay out the sweep (space-filling over the envelope, common random numbers
across controller candidates, a replication and stopping rule for stochastic
metrics).

## Performance metrics to report

Not just "stable" and "mean tracking error": rise time, settling time, overshoot
/ undershoot, steady-state error, disturbance-rejection magnitude and recovery
time, noise sensitivity, peak and RMS control effort, energy, actuator duty /
wear, constraint-violation count and margin, worst-case computation time and
deadline misses, and — where people are affected — fairness / distributional
impact. Report worst-case and percentile values across the scenario matrix, not
just the nominal-run number.

## The deployment ladder

1. paper / model review;
2. mathematical analysis (stability, margins, robustness);
3. offline simulation;
4. Monte-Carlo uncertainty study;
5. software-in-the-loop;
6. processor- / hardware-in-the-loop;
7. shadow mode — recommendations logged, not applied;
8. constrained pilot with conservative limits and close monitoring;
9. staged rollout with monitoring and rollback;
10. continuous assurance — drift detection, re-identification governance,
    periodic safety review.

State which level has actually been reached. A controller that has passed
simulation is at level 3–4, not "verified for deployment".
