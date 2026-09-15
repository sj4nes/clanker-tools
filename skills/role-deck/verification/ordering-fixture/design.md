# Fixturing the ordering claim

The premise fixture refuted role-deck's execution-forcing justification: agents
ground cheap claims unprompted, 8/8. That left a **successor hypothesis**,
noted as incidental and explicitly not a finding — none of those eight recorded
a prior or enumerated competing explanations. They went straight to the answer,
and on that task the answer was right.

This fixture tests the sharper version of that, which is not about enumeration
for its own sake:

> Having formed a plausible explanation, does an agent ask **"how do I confirm
> this?"** rather than **"what else would produce this symptom?"**

Confirmatory testing is not laziness — it feels like diligence. You form an
explanation, you test it, the test passes, you ship. The failure is invisible
precisely because the confirmation succeeds.

## Why this one is measurable where "did they enumerate?" is not

"Considered an alternative" is self-report and forgeable. This is scored by
**executing the subject's own fix**. Either their edit makes the gate catch a
stderr-reported failure or it does not.

The fixture is built so that the *confirmatory* path passes its own
confirmation:

| Fix | Presented bug | Stderr-only failure |
|---|---|---|
| unanchor the grep (the visible cause) | exit 1 — confirmed fixed | **exit 0 — bug survives** |
| unanchor **and** capture stderr | exit 1 | exit 1 |

## Protocol

- **Subject:** a fresh agent, no knowledge of role-deck or the hypothesis. The
  author cannot be the subject.
- **Task:** `task.md`, verbatim, identical every trial. It reports the symptom
  ("tests are failing and the gate says ok"), never a specific test.
- **n = 8**, clean copy each.
- **Score:** `score.sh`, committed before any result, applied to the `check.sh`
  they prescribe.
- **One arm.** The deck forces the discriminating question structurally: BLACK
  requires a `discriminator` artifact with `predicted_outcomes` **per
  hypothesis**, and GREEN now requires `candidates` >= 2 (a rule as of diagnose
  v0.8.0 — until then the brief asked for two and the runner took one).

## Pre-registered interpretation

| Outcome | Meaning |
|---|---|
| **6–8 of 8 CONFIRMATORY** | claim supported. Agents confirm rather than discriminate, and the deck's BLACK discipline is its live justification. |
| **3–5** | weakly supported. Reliability, not capability; soften the claim. |
| **1–2** | largely refuted. |
| **0** | refuted. Combined with the premise result, **role-deck would be down to auditability and repeatability alone** — worth keeping for that, and its behavioural justifications would all be gone. That is a real possible outcome and is not to be explained away. |

## Known limits

- **One bug shape.** Two channels, one silent. It does not test premature
  commitment in general — only the stdout/stderr instance of it.
- **Both failures are visible in one run.** The stderr line appears in the
  terminal and is *missing from the echoed `$out`* — a discoverable clue. If
  subjects catch it, the fixture may simply be too easy rather than the claim
  false, and that ambiguity cannot be resolved from the result alone.
- **Contamination.** The repo documents this discipline. Subjects have
  filesystem access; the premise fixture survived that on an unforgeable
  signal, and this one is scored by execution, which is equally unforgeable —
  but a subject who reads `role-deck` may be primed.
- **n=8, one model, one day.**
