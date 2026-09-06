# Verification, validation, uncertainty, and calibration

## Verification — "did we build the model right?"

Compares the code / hardware realization against the conceptual and mathematical
specification. High-value methods:

- Unit tests for known function values and limiting cases.
- Analytic benchmarks where a closed-form solution exists (M/M/1 queue length,
  projectile range, RC step response, `x^n` on `[0,1]`).
- Dimensional analysis and unit checks — see the [`bc`](../../bc/SKILL.md) skill.
- Conservation checks (mass / energy / charge / cash / inventory / population).
- Extreme-condition tests: zero, infinite, very large, very small inputs.
- Degenerate-case tests: zero arrivals, zero friction, infinite capacity, one
  agent, no noise. A queueing model with no arrivals must keep queue length 0.
  An inventory model with no supply and positive demand must not gain inventory.
- Event-trace inspection for the first few runs.
- Code review and model walk-throughs with a domain expert.
- Cross-implementation comparison (re-code a core in a second language / tool).
- Solver convergence studies: shrink the step or tighten tolerance; the decision
  metric must stabilize.
- Mesh-refinement / grid-convergence studies for spatial models.
- Deterministic replay under fixed seeds — identical inputs, identical outputs.

For logical / protocol / state-machine cores, use the
[`tla-checker`](../../tla-checker/SKILL.md) skill for bounded exhaustive
invariant and deadlock checking, or the [`lean`](../../lean/SKILL.md) skill to
machine-check an algebraic or inductive core.

## Validation — "did we build the right model for this purpose?"

A model can be perfectly verified and still be an invalid representation of
reality for the stated use. Evidence:

- Expert review of structure and assumptions.
- Comparison with historical input–output behavior.
- Comparison with data **not used** for calibration.
- Replication of known events or qualitative patterns.
- Predictive holdout testing.
- Comparison with independent models or measurements.
- Face-validity workshops with operators and domain experts.
- Testing whether the model correctly **ranks** scenarios, even when exact
  prediction is hard — often the ranking is the decision-relevant property.
- Checking behavior in historically extreme but relevant conditions.

Always state validation **gaps** as explicitly as validation successes. An
unvalidated regime is a non-claim, not a silent assumption.

## Numerical methods and their failure modes

Numerical choices are not implementation trivia — they can change conclusions.

### Time integration

- **Forward Euler** — simple; often unstable or inaccurate for stiff or
  oscillatory systems.
- **Runge–Kutta (explicit)** — general-purpose workhorse for non-stiff systems.
- **Implicit Euler / BDF / implicit RK** — for stiff systems (fast + slow modes).
- **Symplectic integrators** — preserve structure in Hamiltonian / mechanical
  systems over long horizons.
- **Event-aware solvers** — locate discontinuities: collisions, switches,
  thresholds, mode changes.

Checks: step-size convergence (halve Δt — does the metric move?); tolerance
convergence; stability (no nonphysical blow-up, oscillation, or drift);
constraint preservation (positivity, bounds, conservation, algebraic
constraints); event localization (discontinuities detected, not stepped over).

### Spatial discretization

Coarse mesh: cheap, misses gradients / shocks / boundary layers. Fine mesh:
expensive, may constrain the time step and conditioning. Boundary treatment
often dominates local accuracy. Turbulence / closure / constitutive models are
often the dominant model-form uncertainty. Do a grid-convergence study.

### Stochastic estimation error

With `n` independent replications and outputs `Yᵢ`, the sample mean is `Ȳ =
(1/n) Σ Yᵢ`, and its standard error falls like `1/√n`. Common mistakes: treating
within-run observations as independent replications; too short a warm-up;
stopping after a favorable or unfavorable realization; comparing alternatives
with uncontrolled random variation; reporting a percentile from too few runs;
missing rare events that need importance sampling or much larger ensembles.

## Uncertainty quantification

Report uncertainty as part of the result, not as a trailing disclaimer.

| Class | What it is | How to address |
|---|---|---|
| **Aleatory** | Inherent variation — arrivals, failures, weather, demand, randomized behavior | Replications; report the output distribution |
| **Epistemic** | Lack of knowledge — parameters, mechanisms, initial state, inputs | Parameter priors; Bayesian calibration; wider intervals |
| **Numerical** | Discretization, solver tolerance, mesh, rounding, finite sampling | Convergence and refinement studies; Monte-Carlo half-widths |
| **Scenario** | Future policy, behavior, technology, regulation, external conditions | Scenario ensembles, not one base case |
| **Model-form** | Omitted mechanisms, wrong causal structure, regime extrapolation | Alternative model structures; explicit validity domain |

Techniques, roughly in order of effort: one-at-a-time sensitivity (diagnosis);
global sensitivity analysis (Sobol / Morris) when nonlinear interactions matter;
parameter sweeps and response surfaces; Monte Carlo or quasi-Monte Carlo
sampling with dependence modeled; Bayesian calibration and posterior predictive
checks; scenario ensembles; confidence intervals for every stochastic metric
reported; value-of-information analysis to identify which new measurement would
most reduce decision uncertainty.

## Calibration, identifiability, and overfitting

Calibration estimates uncertain parameters so the model agrees with observed
evidence. It is **not** a licence to force agreement with every historical point.

A robust calibration plan:

- Separate calibration and validation data where possible.
- Constrain parameters to physically / behaviorally plausible ranges.
- State the likelihood / error model explicitly.
- Assess parameter **identifiability** — can the data actually pin these
  parameters down, or are there ridges of equally-good fits?
- Report posterior or confidence intervals, not just point estimates.
- Do out-of-sample and regime-specific checks.
- Document which parameters are fixed from theory vs estimated from data.

An unidentifiable model can fit history many different ways, each giving very
different counterfactual predictions. The honest output is then wider
uncertainty or a simpler model — never false precision. Apparent digital
precision (many digits) is not real-world accuracy: the answer can be exact and
still wrong because of bad assumptions, uncertain parameters, thin data, or
numerical artifacts.
