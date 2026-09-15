# Fixturing behaviour 1

> An agent asked to **"verify this"** produces a weaker artifact than one asked
> to **"make this able to fail, and confirm it fails"**.

`directed-verification` states this and marks it unmeasured. This measures it.

## Two arms, unlike the previous fixtures

The premise and ordering fixtures each had a structural half already settled by
a gate, which left one arm. This claim is **purely behavioural and comparative**
— it is about the difference between two instructions — so both arms must run.

The prompts are identical except for one sentence:

- **A:** *"Write verification for `round_half_up`. Report what you did."*
- **B:** the same, plus *"It must be able to fail: before you finish, confirm it
  actually fails against a wrong implementation, then restore the correct one."*

n = 5 per arm. Subjects are fresh agents with no knowledge of role-deck, of this
corpus's standard, or of what is being measured.

## The measurement is an execution, not a reading

Each subject's verification is **run against a planted defect**: half-up becomes
half-even, which differs from the spec at a remainder of exactly `.5` and
nowhere else. A harness exercising 1.4 and 1.6 passes it. A harness testing the
boundary the docstring names catches it.

| verdict | meaning |
|---|---|
| `CATCHES` | passes clean, fails planted — a harness that can fail |
| `CANNOT-FAIL` | passes clean **and** passes planted |
| `BROKEN` | fails on the correct implementation |
| `NO-HARNESS` | nothing runnable produced |

Nothing about the subject's prose is scored. `score.sh` is self-tested against
all four verdicts before any subject ran.

## Pre-registered interpretation

Let **ΔCATCHES = (B catches) − (A catches)**, out of 5 each.

| Δ | Meaning |
|---|---|
| **≥ +3** | claim supported. The instruction changes the artifact, and behaviour 1 earns its place. |
| **+1 or +2** | weakly supported. Soften to "tends to", and say n=5. |
| **0** | **refuted.** The instruction makes no difference; strike behaviour 1 rather than reword it. |
| **negative** | refuted, and worse — asking for failure produced *weaker* artifacts. Investigate before believing it. |

If arm A scores 5/5 CATCHES, the claim is refuted regardless of arm B, because
there is no headroom for the instruction to matter.

## What this also tests

`claim-fixture` has produced **two refutations and no confirmations**, so
nothing yet shows it can confirm a claim that is true. This is its first
plausible positive. **A supported result here is therefore evidence about the
method, not only about behaviour 1** — and a refutation leaves the method's own
control still missing.

## Known limits

- One subject, one bug shape, one boundary. "Will an agent test a documented
  `.5` boundary" is narrower than "produces a weaker artifact".
- The subject's docstring **names** the half-up rule and says it differs from
  `round()`. A subject that reads carefully has been told where the boundary is,
  which makes arm A's job easier and biases toward refutation.
- n=5 per arm, one model, one day.
