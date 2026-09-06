# Analog, digital, and hybrid computing; co-simulation; digital twins

## Analog vs digital vs hybrid

| Aspect | Analog | Digital | Hybrid |
|---|---|---|---|
| Representation | Continuous physical quantities (voltage, current, shaft angle, pressure, fluid level) | Discrete symbols, finite-precision numbers | Continuous physical subsystem + digital coordination / control / capture |
| Natural strength | Continuous-time dynamics, ODEs, real-time behavior | Flexible, reproducible, programmable across model types | Real-time simulation / control where each side covers the other's weakness |
| Primitives | Summation, scaling, integration, multiplication, nonlinear transfer functions | Arithmetic, logic, data structures, solvers, RNG, event scheduling | ADC/DAC, synchronized clocks, plant emulators, FPGA / microcontroller control |
| Error profile | Component tolerance, drift, noise, saturation, scaling / readout error | Discretization, rounding, solver instability, algorithmic / model error | All of the above + coupling delay, sampling, synchronization, interface error |
| Reprogrammability | Historically patch cables, potentiometers, circuit reconfiguration | Usually high | Moderate to high; depends on the hardware interfaces |
| Best use | Fast intuitive exploration of continuous dynamics; low-latency emulation | General-purpose scientific / engineering / operational / software simulation | Hardware-in-the-loop, cyber-physical systems, real-time control, power electronics, robotics |

An electronic analog computer represents variables as continuously varying
voltages (often −10 to +10 V) and wires together integrators, adders, amplifiers,
and potentiometers to solve ODEs **in parallel** — which made dynamic-system
studies very fast (flight control, chemical processes, suspension design), at the
cost of accuracy and flexibility limited by physical imperfections and patching
effort.

### Analog realization of a state-space system

For `ẋ(t) = f(x(t), u(t), θ)`, `y(t) = g(x(t), u(t), θ)`:

- an **integrator** produces `x(t)` by integrating `ẋ(t)`;
- summing amplifiers combine state feedback and forcing terms;
- gains / potentiometers encode coefficients and physical scaling;
- function generators approximate nonlinear relationships;
- initial-condition circuitry loads `x(0)`;
- oscilloscopes / recorders / ADCs observe outputs.

The solution evolves in physical time or in a deliberately scaled version of it.

### Digital realization

State is advanced by a clock, an event agenda, a numerical solver, or repeated
sampling: fixed-step integration; adaptive-step integration; event scheduling
(jump to the next state-changing event); Monte Carlo replication; agent updates
(sequential / synchronous / asynchronous / event-driven); an
optimization / control loop that simulates candidate actions and selects one.

Digital simulation is generally superior for reproducibility, complex data
handling, large scenario ensembles, stochastic models, optimization,
visualization, audit trails, and model composition. Its apparent precision must
not be confused with real-world accuracy.

Analog framing remains conceptually central even in digital tools: many problems
are still expressed as interconnected integrators, gains, summing junctions,
delays, transfer functions, and state-space blocks.

## Co-simulation and model exchange

Large cyber-physical systems often need multiple coupled models: mechanical
plant + embedded software; electrical grid + market dispatch; factory operations
+ robot controls; vehicle dynamics + driver behavior + communications;
climate + energy + economy at different time scales.

- **Model exchange** — a component ships its equations; the importing
  environment's solver integrates them.
- **Co-simulation** — a component ships its own internal solver and advances
  itself between communication points under an orchestrator's coordination.

The Functional Mock-up Interface (FMI) is a tool-independent standard for
exchanging dynamic models in both styles.

### Co-simulation hazards

- Clock mismatch and variable communication step sizes.
- Algebraic loops across the coupling.
- Delay and sampling artifacts introduced by the coupling itself.
- Inconsistent units or sign conventions at the interface.
- Double-counting of dynamics modeled on both sides.
- Nonconvergent coupled solvers (need iteration / waveform relaxation).
- Hidden assumptions baked into vendor-provided model binaries.
- Incorrect mapping between continuous plant values and discrete controller logic.

Verify the interface as carefully as each component: exchange a known signal,
check it arrives with the right units, sign, scale, and delay.

## Simulator vs emulator vs digital twin

These overlap but are not interchangeable:

- **Simulator** — a model that imitates behavior for study, prediction, training,
  or design.
- **Emulator** — a substitute system that reproduces enough behavior or interface
  compatibility for another system to operate against it.
- **Digital twin** — a data-connected digital representation tied to a *particular*
  physical asset or process, updated with current operational data, used for
  monitoring, diagnosis, forecasting, and decision support. The term earns its
  keep only when there is a maintained identity relation to a real asset, a live
  data link, an operational purpose, and an explicit model lifecycle. A dashboard
  with a model behind it is not a digital twin.
- **Hardware-in-the-loop (HIL)** — real hardware runs against a simulated
  environment in real or bounded time.
- **Software-in-the-loop (SIL)** — the real software controller runs against a
  simulated plant before hardware integration.
- **Model-in-the-loop (MIL)** — control / model concepts are evaluated before
  code generation or target deployment.
