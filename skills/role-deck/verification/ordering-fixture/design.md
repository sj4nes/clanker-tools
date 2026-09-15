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

## Tightened before running

The first build put **both** failures in the presented output: the stderr line
appeared in the terminal and was visibly absent from the echoed `$out`. That
made a COMPLETE result uninterpretable — "they discriminate by default" and
"the clue was handed to them" would have looked identical, and no result could
separate them.

So the second cause moved **out of the output and into the code**. The suite now
passes both parse tests, so the presented run shows exactly one failure, on
stdout, fully explained by the anchored grep. The stderr path still exists, in
plain sight, in `run_parse_test`:

    printf '  FAIL: %s (parser raised: %s)\n' "$1" "$2" >&2

Finding it requires reading the suite and asking *how else can a test report
failure here* — which is the discriminating question itself, not a clue about
it. Changed before any trial was run; nothing has been tuned toward a result.

## Known limits

- **One bug shape.** Two channels, one silent. It does not test premature
  commitment in general — only the stdout/stderr instance of it.
- **Shell hygiene could score COMPLETE without the reasoning.** A subject might
  add `2>&1` as a reflex — "capture stderr too, why not" — and pass without
  ever thinking about failure channels. The primary score cannot distinguish
  that from discrimination. Their stated cause is recorded as a **secondary
  observation**: does it name the parse-test path? That is self-report and does
  not override the executed score, but a COMPLETE with no mention of the stderr
  path should be reported as hygiene, not discrimination.
- **The presented symptom is fully explained by the visible cause.** This is
  deliberate and is what makes confirmation feel sufficient — but it also means
  a subject who fixes only the anchor has genuinely answered the bug report as
  written. The claim being tested is about thoroughness beyond the literal ask,
  which is a real thing to want and a debatable thing to demand.
- **Contamination.** The repo documents this discipline. Subjects have
  filesystem access; scoring by execution is unforgeable, but a subject who
  reads `role-deck` may be primed.
- **n=8, one model, one day.**
