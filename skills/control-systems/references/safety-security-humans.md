# Safety, security, and humans

Safety is a first-class constraint derived before performance optimisation.
Security changes latency, availability, and safety behaviour, so it is not an
IT afterthought. Human oversight must be real, not nominal.

## Safety as a first-class constraint

Derive, before tuning anything:

- hard physical bounds and the safe operating envelope;
- the set of unsafe states and unsafe actions;
- hazard severity and likelihood (a hazard log / FMEA / STPA-style analysis);
- independent sensors or cross-checks for the safety-critical variables;
- interlocks that act regardless of the nominal controller;
- the fail-safe state and how the plant is driven to it;
- the fail-operational vs fail-safe choice, made explicitly per failure;
- alarm thresholds, prioritised to avoid flooding the operator;
- watchdog timers on the controller and the communication path;
- manual emergency controls that bypass the automation;
- stop, rollback, and recovery procedures.

Following NIST's cyber-physical-systems framing, treat safety as *freedom from
unacceptable risk of physical injury, health damage, property damage, or
environmental harm*, and connect resilience to fault tolerance, graceful
degradation, and predefined fail-safe states.

The nominal controller must be structurally unable to command the plant outside
the safe envelope. Where consequences are high, an independent safety filter or
hardwired interlock enforces the invariant even when the optimiser or a learned
policy requests an unsafe action.

## Security for control systems

Control systems are cyber-physical targets. Per NIST SP 800-82 Rev. 3 (operational
technology security), require:

- an asset inventory and a defined system boundary;
- network segmentation and least privilege between control zones;
- authenticated, authorised control commands;
- secure configuration and update management;
- time-synchronisation integrity (many loops and logs depend on it);
- logging and auditability of commands and overrides;
- anomaly detection tuned to the operational baseline, not a generic IT profile;
- defined safe behaviour on loss of communication;
- incident response coordinated with plant safety, not separate from it;
- vendor and supply-chain exposure review;
- a way to test the security controls without disrupting operations;
- human approval for high-consequence configuration changes.

A security control that adds latency or reduces availability must be evaluated
against the control loop's timing and safety budget before deployment.

## Human-in-the-loop design

"A person can theoretically intervene" is not oversight. Define:

- **Authority** — who may override, and under what conditions;
- **Information** — what the operator sees, and whether the situation is
  understandable in the available response time;
- **Disagreement** — what happens when operator and controller conflict
  (controller yields, or a defined arbitration);
- **Handover** — bumpless transfer in both directions so no transient is
  injected at the switch (initialise the controller's internal state, e.g. the
  integrator, to match the current actuator command);
- **Alarms** — prioritised and rate-limited to prevent alert fatigue;
- **Logging** — every action and override recorded;
- **Training** — realistic simulator drills for the failure and override
  scenarios;
- **Equity** — the automation must not create unsafe incentives or shift
  disproportionate burden or risk onto operators or affected people.

## Bumpless transfer

On any switch between manual/automatic, between controllers, or between
schedules: carry the internal state forward so `u` is continuous. For a PID,
back-calculate the integrator: `integral = (u_current - Kp e - Kd de/dt) / Ki`
at the switch instant. Test the switch in both directions under load.
