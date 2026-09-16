---
name: directed-verification
description: >-
  Direct an agent to do verification work in a way that lets it disagree with
  you, and lets you tell when it is wrong. Use when asking an agent to check,
  test, audit, review, or prove something; when its answers are consistently
  agreeable and you cannot tell whether that is because the work is fine; or
  when deciding how much of a verification result to believe. Six behaviours:
  ask for what would prove you wrong rather than for confirmation, demand an
  artifact that can fail rather than prose, suspect the test before the
  subject, keep proposing separate from deciding, re-run what you were told,
  and check what the command was aimed at rather than that it ran. NOT a
  prompting-technique guide, NOT multi-agent orchestration, and NOT a way to
  make an agent's judgement trustworthy — it changes what you can check, never
  how good the thinking was.
version: 1.2.2
archetype: behaviour
author: Simon Janes
tags: [agents, verification, collaboration, sycophancy, evidence, review]
---

# Getting work you can check from an agent that wants to agree

An agent asked to verify something will report that it verified it. The prose
will be fluent, the structure sensible, the conclusion agreeable — and that is
true whether the work was done well, done badly, or not done at all. Fluency is
not a signal, because it is present in every case.

So the question is never *did it verify this?* It is **what did it produce that
could have come out the other way?**

This skill is the collaboration half of building something verified; the
document half is [`skill-authoring`](../skill-authoring/SKILL.md).

## The six behaviours

1. **Ask for what would prove you wrong, not for confirmation.** *"Verify this"*
   gets agreement. *"Make this able to fail, then show me it failing"* gets a
   harness. The instruction that produced every mutation harness in this corpus
   was the second, and the difference is not tone — it changes what artifact
   exists at the end.

2. **Demand something that can fail, not prose.** A number a harness printed. A
   command's captured output. A patch applied and re-run. Reasoning is the one
   thing an agent can always produce, so it is the one thing that carries no
   information. Where an experiment is involved, make the measurement
   unforgeable — see [`claim-fixture`](../claim-fixture/SKILL.md).

3. **Suspect the test before the subject.** When a check behaves surprisingly —
   passing what should fail, or failing what should pass — the *check* is the
   first candidate, not the code. This repository records **at least three**
   occasions where the harness was wrong and the subject was fine
   ([`verification/`](verification/) counts them, and the count is a lower
   bound). A surprising green is not good news, and a surprising red is not
   necessarily a bug found.

4. **Keep proposing separate from deciding.** The agent proposes; deterministic
   code, an external rule, or you decides. The moment the same party does both,
   a result that agrees with the proposer is uninformative. This is
   [`agent-automation`](../agent-automation/SKILL.md)'s principle applied to
   your own working relationship.

5. **Re-run what you were told.** A result you have not reproduced is a claim.
   Ask for the seed, the command, the ledger — anything that lets you get the
   number again yourself. An agent that cannot tell you how to reproduce its
   result has given you prose.

6. **Check what it was aimed at, not that it ran.** Grounding proves a command
   executed; it says nothing about whether the target was alive. A real
   diagnosis in this corpus gathered a status file a month older than the code
   it described, drew only true facts from it, and reached a wrong conclusion.
   Ask *which sources, and how current* before accepting *it checked*.

## Its own premises, unmeasured

The honest position, by this corpus's own standard: **most of the above is an
assumption.** The evidence is one author, one corpus, ten days.

| behaviour | evidence |
|---|---|
| 3 suspect the test | ≥3 recorded incidents, mechanically counted |
| 2, 5 artifact over prose | every skill here traces its numbers to a harness |
| 1, 4, 6 | **argued, not measured** |

Behaviours 1 and 4 are exactly the shape `claim-fixture` exists to test — *an
agent asked to "verify" produces weaker artifacts than one asked to "make it
fail"* is a measurable claim. **Behaviour 1 has been fixtured twice and both runs
were invalid**: run 1's subject was buggy, and run 2's *control arm received the
treatment* — every arm-A agent had `test-writing` in context, which prescribes
the same thing this behaviour does. Δ = 0 there measures nothing, because the two
arms were the same condition. See
[`verification/b1-fixture/RESULT2.md`](verification/b1-fixture/RESULT2.md).

Two premises in this corpus were asserted with this much confidence and refuted
8/8. This one has been neither refuted nor supported — and two failed attempts
are a reason to trust it *less*, not more, because the easy ways of testing it
have now been used up without producing evidence.

## What this cannot do

- **Make the agent's judgement good.** It changes what you can *check*, not the
  quality of the thinking underneath. A well-aimed, reproducible, falsifiable
  check of the wrong thing is still the wrong thing.
- **Detect a confident wrong answer that is also reproducible.** Behaviours 5
  and 6 catch unreproducible and misaimed work. Neither catches work that is
  careful, repeatable, and mistaken.
- **Substitute for reading the result.** Every behaviour here raises the cost of
  a bad answer surviving. None reduces it to zero.

## Before you accept a verification result

- [ ] You asked for the failing case, not for confirmation.
- [ ] Something exists that could have come out the other way.
- [ ] You considered the check itself as the suspect.
- [ ] Whoever proposed the result did not also decide it was good.
- [ ] You can reproduce it — seed, command, or ledger in hand.
- [ ] You know which sources were read, and how current they are.

## Verification

[`verification/`](verification/) counts, from this repository's own commit
history, the occasions where the harness was found wrong rather than the
subject — behaviour 3's evidence. The detector is self-tested in both
directions: four real admissions it must match, four ordinary messages it must
reject, because a detector that only ever says yes is the defect this whole
corpus keeps finding. `sh verification/run.sh`.

## Related skills

- **`skill-authoring`** — the document half of the same job.
- **`claim-fixture`** — behaviours 1 and 4, made measurable rather than argued.
- **`agent-automation`** — behaviour 4 as an architecture, when the agent's
  output triggers real side effects.
- **`evaluator-integrity`** — when the thing being checked is a score, and
  something is optimizing against it.

## Completion report

State: what you asked for and how it could have come out otherwise; the
artifact produced; whether you suspected the check; who decided; how you
reproduced it; which sources were read and how current; and what you still
cannot rule out.
