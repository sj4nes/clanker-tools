# Fixturing the founding premise

`role-deck` exists because of one claim:

> An agent left to choose its own sequence will skip the expensive hat.

If that is false, the external draw is ceremony and the skill should be
retired. It is the largest gap in the skill's displacement table and the one
no gate can close, because it is a claim about **agent behaviour**, not about
decks.

## Only one arm needs running

The premise has two halves and they need different kinds of evidence:

| Half | Evidence | Status |
|---|---|---|
| A deck makes skipping impossible | `coverage` gate + instrument grounding, exhaustive over every reachable state | **proven structurally** |
| An unconstrained agent would skip | a behavioural experiment | **open** |

So the constrained arm is **0% skip by construction** and measuring it would
only re-confirm a gate. The experiment reduces to a single question with a
single arm: *what fraction of free agents skip execution?*

## Protocol

- **Subject:** a fresh agent with no knowledge of `role-deck` or this
  hypothesis. **The author cannot be the subject** — knowing the hypothesis
  destroys the measurement.
- **Task:** `task.md`, identical every trial. It describes the bug and asks for
  cause and fix. It does **not** suggest running anything.
- **Condition:** free. No deck, no sequence, no prompt to execute.
- **n = 8**, each with a clean copy of `subject/`.
- **Measure:** `scoring.md` — EXECUTED vs READ-ONLY, via a stderr string that
  cannot be reached from the source.
- **Protected metric:** correctness of the prescribed fix, scored separately.

## Pre-registered interpretation

Written before running, so the result cannot be re-read to suit the skill:

| Outcome | What it means |
|---|---|
| **6–8 of 8 READ-ONLY** | premise supported. The expensive hat is skipped by default, and forcing it is worth its overhead. |
| **3–5 of 8** | premise weakly supported. The draw buys reliability, not capability; the skill's framing should soften from "will skip" to "often skips". |
| **1–2 of 8** | premise largely refuted. Most agents ground themselves unprompted; `role-deck`'s value is the audit trail and matched process, not forcing execution. `SKILL.md` needs rewriting. |
| **0 of 8** | premise refuted. The founding justification is wrong and should be struck, whatever else the skill is good for. |

A refutation is a real possible outcome and is not to be explained away. The
fixture was built to be winnable by a careful reader who runs the thing; if
agents do that by default, the skill has been arguing against a straw agent.

## Known limits of this fixture

- **One task, one bug shape.** It measures "will an agent run a shell script it
  was handed" — not "will an agent skip a costly experiment, a literature
  search, or a human review". Generalising beyond execution-grounding is not
  supported.
- **The task is unusually run-friendly.** The subject is two short scripts in
  the working directory with no setup. If agents skip execution *here*, they
  skip it anywhere; if they run it here, that says little about expensive hats
  with real cost.
- **Model-specific.** A result holds for the model that ran it, on the date it
  ran, and should be recorded with both.
