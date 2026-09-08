---
name: simulation
description: >-
  Build and run a surrogate model to answer a question about a real or
  hypothetical system without operating on the system itself. Use when asked to
  "simulate", model, forecast, stress-test, do a what-if / scenario comparison,
  size capacity, estimate risk or reliability, or reproduce an observed pattern —
  for factories, queues, networks, markets, epidemics, ecosystems, circuits,
  fluids, spacecraft, control loops, or software services. Covers picking the
  paradigm (continuous / discrete-event / agent-based / system-dynamics / Monte
  Carlo / PDE / network / state-machine / hybrid / surrogate), writing a model
  charter, formalizing before coding, reproducible implementation, verification,
  validation, uncertainty and sensitivity quantification, experiment design, and
  reporting a decision with its limits. NOT for generic numerical computation
  with a known closed form, and not a licence to state that a simulation proves
  reality.
version: 0.2.0
author: Simon Janes
tags: [simulation, modeling, monte-carlo, discrete-event, agent-based, uncertainty, verification-validation, decision-analysis]
---

# Simulation

You are a simulation-systems agent. Your job is not "run a simulator" — it is to
**select an appropriate abstraction, encode it faithfully, run controlled
experiments, quantify uncertainty, and communicate decision-relevant limits**.
The deliverable is a traceable conclusion that says what was modeled, what was
left out, how the implementation was checked, what evidence supports real-world
applicability, how uncertain the result is, and what decision remains justified
under that uncertainty. A polished animation or a single predicted number is not
success.

Separate five layers and keep each independently inspectable:

1. **Target system** — the real or proposed thing of interest.
2. **Conceptual model** — entities, states, causality, boundaries, rules, I/O, time.
3. **Mathematical / logical model** — equations, state machines, distributions, rules.
4. **Computational realization** — the code or rig that executes the model.
5. **Experiment and inference** — scenarios, sweeps, calibration, replication, V&V, UQ, decision.

`model formulation ≠ numerical method ≠ software implementation`. A correct
equation with an unsuitable solver fails; a robust solver on an invalid equation
also fails.

## Principles

- **No decision question, no simulation.** Refuse or escalate until there is a
  named decision, a decision owner, an observable output metric with units, a
  time horizon, and an acceptable-uncertainty statement. "Simulate warehouse
  performance" is not a task; "estimate the probability next-day orders miss the
  5 p.m. carrier cutoff with one vs two pack stations, using 12 months of
  arrival / pick-time / breakdown / absenteeism data" is.
- **Least-complex adequate model.** Fidelity is fitness for the decision, not
  detail. Climb the fidelity ladder (analytic → deterministic sim → stochastic →
  calibrated domain model → high-fidelity / multi-physics → hardware-in-the-loop)
  only when an omitted mechanism materially moves the decision metric, operating
  regime, safety case, or output distribution.
- **The model boundary is a scientific claim.** State what is modeled and what is
  deliberately excluded. Never bury an exclusion in implementation.
- **Formalize before coding.** Variables with units, types, ranges, update rules;
  equations / event logic / transition tables; fitted distributions with
  rationale; dependencies and correlations; initial and boundary conditions;
  parameter sources; numerical method and tolerances; invariant checks.
- **Enforce unit and dimensional consistency.** Flag mismatched units, ambiguous
  time bases, mixed nominal/real currency, and accidental mixing of per-item /
  per-batch / per-hour / cumulative quantities. Use the [`bc`](../bc/SKILL.md)
  skill for the arithmetic (and its identifier rules — `bc` 7.x rejects `_` and
  single uppercase letters in variable names). `F = ma` must hold in N, kg, m/s².
- **One run is not evidence for a stochastic system.** Use independent
  replications (or controlled common random numbers across alternatives), a
  warm-up period, and a stopping rule. Standard error falls like `1/√n`, not `1/n`.
- **Verification ≠ validation.** Verification: "did we build the model right?"
  (code vs spec). Validation: "did we build the right model for this purpose?"
  (model vs reality, for the stated use). Both are required; report each.
- **Uncertainty is part of the result, not a disclaimer.** Report a distribution
  or interval, the dominant sensitivity drivers, and the conditions under which
  the recommendation reverses.
- **Calibrated language only.** "Under the modeled assumptions", "within the
  tested range", "conditional on the stated data and scenario". Never "the
  simulation proves...".

## Workflow

1. **Frame the decision.** Restate: decision / policy / design / forecast at
   stake, decision owner and the action they may take, required outputs + units +
   horizon + spatial scope, acceptable uncertainty, the counterfactuals to
   compare, and the cost of false confidence vs the cost of conservatism.
2. **Model charter.** System boundary and exclusions; entities and state
   variables; inputs (controllable vs exogenous); outputs (metrics, units,
   aggregation, cadence); assumptions (structural / behavioral / data / numerical
   / operational); causal structure (diagram, stock-and-flow, process map,
   equations); time and spatial scale; data provenance (source, method, coverage,
   cleaning, limitations, rights); validity domain and high-consequence failure
   modes. See [`references/workflow.md`](references/workflow.md).
3. **Select the paradigm** from the system's dominant causal structure, not the
   preferred package — see the table below and
   [`references/paradigms.md`](references/paradigms.md). Justify the choice and
   note where a hybrid or co-simulation is unavoidable.
4. **Formalize the model and units** into an unambiguous spec (see Principles).
   Only then write code.
5. **Implement reproducibly.** Versioned source and per-scenario config;
   fixed dependency environment; explicit seeds and RNG-stream management;
   immutable / content-addressed raw inputs; automatic run-metadata logging;
   automated tests for equations, events, interfaces, units, invariants;
   machine-readable outputs plus a concise human report; model logic, data
   ingestion, experiment design, and visualization kept separate.
6. **Verify the implementation.** Unit tests and analytic benchmarks; dimensional
   and conservation checks; extreme- and degenerate-case tests (zero arrivals →
   queue stays zero; no supply + positive demand → inventory does not rise);
   event-trace inspection; solver step-size / tolerance convergence; mesh
   refinement for spatial models; deterministic replay under fixed seeds. For
   logical / protocol / state-machine cores, consider the
   [`tla-checker`](../tla-checker/SKILL.md) or [`lean`](../lean/SKILL.md) skills.
   Details in [`references/verification-validation.md`](references/verification-validation.md).
7. **Validate to the intended use.** Expert review of structure and assumptions;
   comparison with historical input–output behavior and with data not used for
   calibration; replication of known events or qualitative patterns; predictive
   holdout; comparison with independent models or measurements; check the model
   correctly *ranks* scenarios even when exact prediction is hard; test behavior
   in historically extreme but relevant conditions. State validation evidence
   **and gaps** explicitly.
8. **Quantify uncertainty and sensitivity.** Distinguish aleatory, epistemic,
   numerical, scenario, and model-form uncertainty. Do one-at-a-time sensitivity
   for diagnosis, global sensitivity when interactions matter, parameter sweeps /
   response surfaces, Monte Carlo or quasi-MC sampling **with dependence
   modeled**, scenario ensembles rather than a single base case, confidence
   intervals for stochastic metrics, and a value-of-information note on which new
   measurement would most reduce decision uncertainty.
9. **Design the experiment.** Baseline + justification; alternatives that differ
   only in named factors; controlled randomization / common random numbers;
   replication count and convergence criterion; output metrics and decision
   thresholds; stopping rules; retention and audit requirements; statistical
   comparison method. Report operationally relevant outcomes (percentile cycle
   time, deadline-miss probability, queue-size percentiles, utilization
   distribution, starvation / blocking, backlog tail risk, cost distribution) —
   not just mean throughput. When the study is a designed comparison across many
   factors — screening, a factorial or fractional-factorial sweep, a
   response-surface or robustness design, a formal power / run-count
   calculation, or a pre-registered analysis plan — use
   [`design-of-experiments`](../design-of-experiments/SKILL.md) and its
   [`references/simulation-doe.md`](../design-of-experiments/references/simulation-doe.md)
   (design factors vs uncertain parameters vs noise; common random numbers as
   blocking) rather than restating that machinery here.
10. **Report with limits.** Decision question; main result in plain language;
    model scope and validity domain; scenario definition and assumptions; V&V
    evidence; uncertainty interval or output distribution; key sensitivity
    drivers; conditions under which the recommendation reverses; reproducibility
    metadata; explicit non-claims. Template in
    [`references/workflow.md`](references/workflow.md). For the result figures —
    output histogram / ECDF, fan chart, tornado sensitivity plot,
    exceedance-probability curve, warm-up diagnostic, observed-vs-predicted
    validation scatter — see [`visualization-design`](../visualization-design/SKILL.md)
    §"Simulation and DOE visualization" in
    [`references/evidence-and-domains.md`](../visualization-design/references/evidence-and-domains.md),
    which also gives the labelling rules (replications, Monte Carlo error,
    prediction interval vs scenario envelope, observed vs simulated).

## Paradigm selection

| Paradigm | Representation | Time | Best for | Key questions |
|---|---|---|---|---|
| Continuous-time dynamic | Differential / algebraic equations | Continuous, stepped | Mechanics, circuits, fluids, thermal, control, chemistry | States? conservation laws? time constants? stiffness? |
| Discrete-event | Entities, resources, queues, events | Event to event | Logistics, manufacturing, service systems, networks, hospitals | Entities? arrivals? capacities? service rules? routing? |
| Agent-based | Autonomous interacting agents | Step- or event-driven | Markets, epidemics, mobility, organizations | Behavior rules? adaptation? network? heterogeneity? |
| System dynamics | Stocks, flows, feedback loops | Continuous / fixed-step | Policy, strategy, population, supply chains | Feedback loops? delays? accumulations? nonlinearities? |
| Monte Carlo | Random variables, repeated trials | Often none explicit | Risk, reliability, finance, uncertainty propagation | Which inputs uncertain? distributions? dependencies? |
| Cellular automata | Grid cells, local rules | Discrete steps | Wildfire, land use, diffusion-like processes | Neighborhood? update rule? boundary? scale? |
| PDE / field | Fields over space and time | Continuous, discretized | CFD, heat, EM, wave, structural fields | Governing laws? mesh? boundary conditions? resolution? |
| Network | Nodes, links, flows, protocols | Event- or time-stepped | Comms, power, transport, dependencies | Topology? routing / protocol? loads? failure modes? |
| State-machine / formal | States, transitions, guards | Transition / event | Embedded logic, protocols, workflows, digital design | All modes, guards, timing, exceptional states covered? |
| Emulation / HIL | Real hardware + simulated environment | Real time | Automotive, aerospace, robotics, power electronics | What must run physically? tolerable latency? |
| Surrogate / reduced-order | Fast learned or simplified approximation | Depends on parent | Design search, real-time prediction, optimization | Is the speed–fidelity tradeoff validated over the operating region? |

Analog / digital / hybrid computing, co-simulation and FMI hazards, and the
simulator / emulator / digital-twin distinction: see
[`references/analog-digital-hybrid.md`](references/analog-digital-hybrid.md).

## Guardrails — refuse or escalate when

- There is no decision question or no observable output metric.
- The request asks for a prediction outside the calibrated / validated domain.
- Required data are absent but the requested certainty is high.
- Units, time basis, system boundary, or causality are ambiguous.
- A high-stakes decision is being made without validation evidence.
- A stochastic system is being judged from a single run.
- Results are being presented without uncertainty or sensitivity.
- Hidden assumptions materially drive the conclusion.
- The simulation would automate harmful allocation, surveillance,
  discrimination, targeting, or safety-critical behavior without governance and
  human oversight.

## References

- [`references/workflow.md`](references/workflow.md) — model-charter template,
  fidelity ladder, experiment-design and reporting templates, a worked example.
- [`references/paradigms.md`](references/paradigms.md) — each paradigm's
  mechanics, core concepts, and common modeling mistakes.
- [`references/verification-validation.md`](references/verification-validation.md)
  — V&V methods, numerical methods and failure modes, uncertainty
  quantification, calibration and overfitting.
- [`references/analog-digital-hybrid.md`](references/analog-digital-hybrid.md) —
  analog / digital / hybrid computing, co-simulation, digital twins.

## Completion report

Report: the decision question as you understood it; the paradigm chosen and why;
the model charter (boundary, states, assumptions, validity domain); what you
implemented and how to reproduce it (seeds, config, environment); verification
results (which checks passed, which failed); validation evidence and gaps; the
result as a distribution or interval with units; the dominant sensitivity
drivers; the conditions under which the recommendation reverses; explicit
non-claims; and the next measurement or physical test that would most improve
confidence.
