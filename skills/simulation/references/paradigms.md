# Simulation paradigms — mechanics, concepts, common mistakes

The best paradigm follows from the **system's dominant causal structure**, not
from the preferred software package. Real systems often need a combination.

## Continuous-time dynamic simulation

Quantities that vary over time: velocity, voltage, temperature, concentration,
inventory level, pressure, population, capital.

Mathematical forms:

- ODE: `ẋ = f(x, u, t, θ)`
- DAE: `0 = F(ẋ, x, u, t, θ)` — differential states plus algebraic constraints.
- PDE: `∂u/∂t = 𝓛(u, ∇u, ∇²u, …)` — fields over space.

Core concepts:

- **State** — the minimum information needed to predict future behavior given
  future inputs.
- **Inputs** — exogenous forcing, controls, environment, schedules, disturbances.
- **Parameters** — fixed or slowly varying: masses, coefficients, rates, elasticities.
- **Initial conditions** — state at simulation start.
- **Boundary conditions** — constraints at spatial or interface boundaries.
- **Stiffness** — fast and slow dynamics coexisting; needs implicit or
  specialized solvers, not forward Euler.
- **Conservation laws** — mass, energy, charge, momentum, probability, cash,
  inventory, population balances — check them throughout a run, not just at the end.

Analog framing stays useful even in digital tools: many problems are still
expressed as interconnected integrators, gains, summing junctions, delays,
transfer functions, and state-space blocks. For `mẍ + cẋ + kx = F(t)`, form
acceleration as a weighted sum of force, velocity, displacement, then integrate
twice.

Common mistakes: forward Euler on a stiff or oscillatory system; ignoring a
conservation drift that accumulates over the horizon; treating a visually smooth
plot as evidence of numerical accuracy (do a step-size convergence study).

## Discrete-event simulation (DES)

Built around an **event calendar**. State changes only at events; simulated time
jumps from one event to the next.

Typical events: customer arrival, job enters/leaves a queue, machine failure or
repair, order release, vehicle dispatch/arrival, packet transmission / timeout /
loss, shift change, resource seize / release.

Core concepts:

- **Entity** — the object moving through the system: patient, package, vehicle,
  order, packet.
- **Resource** — capacity-constrained service capability: clinician, truck,
  machine, server, dock.
- **Queue** — waiting population plus its priority / discipline rules.
- **Event** — an instantaneous logical change.
- **Activity** — a time-consuming process between two events.
- **Warm-up period** — initial transient omitted from steady-state statistics.
- **Replication** — an independent run under a distinct random-number stream.
- **Termination condition** — finite horizon, completion count, or steady-state
  criterion.

Most common mistake: treating average arrival and service *rates* as sufficient.
Variability, batching, time-of-day dependence, routing logic, breakdowns, shift
patterns, and correlations routinely dominate queueing outcomes. A system at 85%
average utilization with high service-time variability can have a wildly
different tail than one at 85% with low variability.

## Agent-based modeling (ABM)

Appropriate when behavior arises from local rules, heterogeneity, adaptation, or
network structure rather than a known aggregate equation.

Each agent typically has: attributes and internal state; decision rules; memory
or learning; location or network position; resource constraints; interaction
rules; birth/death or entry/exit or role transitions.

Update schemes: sequential, synchronous, asynchronous, or event-driven — the
choice can change results, so state it and test sensitivity to it.

The central challenge is **behavioral validity**, not coding. Record for each
rule whether it is empirical, theoretical, heuristic, policy-defined, or assumed.
Then test whether plausible micro-behaviors reproduce the relevant aggregate
patterns **without overfitting** — matching one historical curve with a
free-parameter-rich rule set is not validation.

Common mistakes: over-parameterized behavior rules; reading emergent artifacts of
the update order as real phenomena; claiming external validity from a single
calibration.

## System dynamics

Stocks (accumulations), flows (rates), and feedback loops, usually integrated at
a fixed step. Best for strategic / policy questions where delays, accumulations,
and nonlinear feedback dominate: population, supply chains, resource dynamics,
adoption.

Concepts: reinforcing vs balancing loops; material and information delays; the
distinction between a stock (state) and a flow (rate of change); policy functions
that close loops.

Common mistakes: confusing a flow with a stock; omitting a dominant delay;
presenting a single base-case run of a highly nonlinear feedback model as a
forecast rather than as one scenario.

## Monte Carlo / stochastic simulation

Propagate uncertainty by repeatedly sampling uncertain inputs and measuring the
output distribution. If `X ~ p(X)` and `Y = f(X)`, draw `Xᵢ`, compute `Yᵢ =
f(Xᵢ)`, then report: mean, median, variance / SD, percentile intervals,
probability of threshold exceedance, expected shortfall, and the sensitivity of
output uncertainty to each input's uncertainty.

**Model dependence.** Sampling correlated inputs independently can badly
misstate tail risk — usually understating it. Use a covariance structure, a
copula, or an explicit shared driver.

Estimation error: with `n` independent replications, the standard error of the
mean shrinks like `1/√n`. 10× the runs ≈ 3.16× tighter. Percentile and rare-event
estimates need far more runs, or variance-reduction / importance sampling.

Common mistakes: independent sampling of correlated inputs; too few runs for a
reported percentile; stopping after a favorable realization; treating
within-run observations as independent replications.

## Cellular automata

Grid cells with local update rules; usually discrete steps. Wildfire spread, land
use, diffusion-like biological / social processes. Decisions to state and test:
neighborhood definition (von Neumann / Moore / range), update rule, boundary
condition (absorbing / periodic / reflecting), cell size and time step.

Common mistake: conclusions that are artifacts of grid resolution or boundary
treatment — do a resolution study.

## PDE / field simulation

Fields over space and time, discretized on a mesh, grid, basis, or particle set.
CFD, heat, electromagnetics, wave propagation, structural fields.

Tradeoffs: coarse mesh is cheap but misses gradients, shocks, and boundary
layers; fine mesh is expensive and can tighten the stable time step. Boundary
treatment often dominates local accuracy. Turbulence / closure / constitutive
models are frequently the largest model-form uncertainty.

Mandatory: grid-convergence / mesh-refinement study. A smooth-looking contour
plot is not evidence of a converged solution.

## Network simulation

Nodes, links, flows, protocols; event-driven or time-stepped. Communications,
power systems, transport, dependency graphs. State and test: topology, routing /
protocol rules, offered load, and failure modes (single-link, correlated,
cascading).

Common mistake: unrealistic traffic / load model; ignoring correlated failures.

## State-machine / formal simulation

States, transitions, guards; transition/event based. Embedded logic, protocols,
workflows, digital design. The question is coverage: are all modes, guards,
timing constraints, and exceptional states represented? For bounded exhaustive
checking of safety invariants and deadlocks, use the
[`tla-checker`](../../tla-checker/SKILL.md) skill rather than sampling traces.

## Emulation / hardware-in-the-loop (HIL)

Real hardware operates against a simulated environment in real or bounded time.
Automotive, aerospace, robotics, industrial control, power electronics. Decide
what must run physically, what may be simulated, and what coupling latency is
tolerable. See [`analog-digital-hybrid.md`](analog-digital-hybrid.md).

## Surrogate / reduced-order models

A fast learned or simplified approximation of a slow parent model, for design
search, real-time prediction, or optimization loops. The obligation: validate
the speed–fidelity tradeoff **over the entire intended operating region**, and
refuse to query it outside the region where it was validated. A surrogate that
is accurate on average can be dangerously wrong exactly where the optimizer
pushes it.
