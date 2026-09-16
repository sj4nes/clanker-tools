---
name: claim-fixture
description: >-
  Measure whether a claimed default behaviour is real, before building a
  methodology on top of it. Use when a skill, process, runbook, review
  checklist, lint rule, or team convention is justified by an assertion about
  what people or agents do by default — "agents skip verification", "reviewers
  rubber-stamp", "developers don't read the spec", "models confirm rather than
  discriminate" — and that assertion has never been measured. Seven behaviours:
  split the claim into the half a gate already proves and the half that needs
  subjects, recruit subjects who cannot know the hypothesis, prove the control
  did not already receive the treatment before reading any outcome, make the
  measurement unforgeable rather than self-reported, commit the scorer and the
  interpretation bands in a separate commit before any result exists, build the
  fixture from a real failure so the wrong path passes its own confirmation,
  and strike a refuted claim instead of rewording it. NOT a replacement for
  domain evaluation or benchmarking, not a way to prove a methodology works,
  and not applicable to claims that are already structurally provable.
version: 2.0.0
archetype: behaviour
author: Simon Janes
tags: [evaluation, experiments, methodology, agents, pre-registration, falsification]
---

# Measuring a default before you build on it

Most methodology rests on an unmeasured claim about what goes wrong without it.
*Agents skip verification. Reviewers rubber-stamp. People don't read the spec.*
The claim justifies the discipline, the discipline gets built, and nobody ever
checks the claim — because it sounds obviously true, and because checking it
risks finding out the discipline was unnecessary.

That risk is the reason to check. A methodology whose premise is false is not
merely unhelpful; it spends attention and credibility on a problem that is not
there, and it crowds out the problem that is.

This skill is short because the method is short. Its evidence base is four
runs: two that **refuted the claims they were built to support**, and two that
were **invalid** — see [`references/case-studies.md`](references/case-studies.md).
That 50% design-failure rate is why behaviour 3 and the pre-flight gate exist;
both invalid runs were knowable before a subject was spawned.

## The seven behaviours

1. **Split the claim, and fixture only the half that needs subjects.** Most
   "default behaviour" claims are two claims. *"An agent will skip the step, so
   the process must force it"* contains a structural half — does the process in
   fact make skipping impossible, which a gate or an inspection can settle —
   and a behavioural half — would anyone actually skip it. Prove the structural
   half by inspection and it drops out of the experiment entirely, often
   halving the cost and always clarifying the question.

2. **You cannot be the subject.** Knowing the hypothesis destroys the
   measurement, and there is no discipline that repairs it. Subjects must be
   naive: fresh agents with no shared context, or people who have not been told
   what is being measured. If you cannot recruit a naive subject, you cannot
   run the experiment — say so rather than running it on yourself.

3. **Prove the control did not already receive the treatment — before you read
   any outcome.** Naive about the *hypothesis* is not the same as clean of the
   *intervention*. The control arm of this corpus's fourth run had a prompt that
   never mentioned the treatment and an environment that supplied it anyway: the
   `test-writing` skill prescribes the very discipline under test and loads from
   the session, not the working directory. Δ was then structurally zero, and no
   sample size would have fixed it. So: write a **fingerprint list** — strings or
   artifacts whose presence in a control transcript means contamination — and run
   a **manipulation check** against it **before** the pre-registered bands are
   consulted. A failure voids the run rather than annotating it. The ordering is
   the whole point: in that run a respectable pre-registered reading of the null
   fired first and stopped anyone looking for the cause. **Pre-registering how to
   read a null result is not the same as checking the experiment ran.** A corpus
   of installed skills makes its own claims hard to test — assume contamination
   and prove its absence.

4. **Make the measurement unforgeable.** Self-report is worthless: a subject
   asked whether they considered alternatives will say yes. Two forms that
   work, both used in the case studies:
   - **an artefact of doing the work** — a string, a file, a side effect that
     appears only if the work happened and cannot be reached from the material
     the subject was given;
   - **executing the subject's own output** — apply their patch, run their
     query, and score what it does rather than what they said about it.

5. **Commit the scorer and the bands before any result exists — in a separate
   commit.** Write the interpretation for *every* outcome, including the ones
   that refute you, and implement the scoring mechanically. Then commit that
   alone. Pre-registration you cannot prove is pre-registration nobody has to
   believe, and the proof is cheap: the scorer's commit must strictly precede
   the results'. See [`verification/`](verification/) — one of the two case
   studies fails this and is recorded as failing it.

6. **Build the fixture from a real failure, and make the wrong path pass its
   own confirmation.** A contrived trick generalises to nothing; take the
   fixture from something that actually went wrong. And the failing behaviour
   must **succeed on its own terms** — if the subject who stops early gets an
   obviously wrong answer, you have measured competence, not the default. The
   whole point is that the shortcut *feels* sufficient.

7. **Strike a refuted claim; do not reword it.** The reflex on a negative
   result is to substitute a similar-sounding claim that was not tested. That
   is the failure mode the experiment existed to prevent, relocated one level
   up. Remove the claim, state what survives, and leave the space empty until
   something else is measured.

## Before you spend subjects

Run the pre-flight gate. Two of four runs in this corpus were invalid, and both
were knowable in advance — the gate exists so the cost is judgement rather than
a wasted run.

```sh
sh verification/preflight.sh <fixture-dir>
```

It scores the mechanically checkable gates and **blocks on anything it cannot
evaluate**, because a missing manipulation check is exactly how the fourth run
got through. The rubric, and the failure each gate is derived from, is in
[`references/pre-flight.md`](references/pre-flight.md). One gate (does the
shortcut pass its own check?) stays judgement and is reported as owed.

## Before you believe the result

- [ ] The structural half is proven separately, not bundled into the
      experiment.
- [ ] No subject could know the hypothesis; the author is not among them.
- [ ] The manipulation check passed, and it was read **before** the bands.
- [ ] The measurement is an artefact or an execution, never a self-report.
- [ ] The scorer and the bands are in a commit that provably predates the
      first result.
- [ ] A subject who takes the shortcut would have *passed their own check*.
- [ ] Confounds are written down and weighed — and not used to rescue a claim
      the result refuted.

## What this cannot tell you

- **That the methodology is worthless.** Refuting its premise removes a
  justification, not every justification. Say precisely what survives.
- **That the claim is false in general.** A fixture measures one task shape,
  one population, one day. *"Agents run a script handed to them"* is not
  *"agents commission expensive experiments"*.
- **Why.** A behavioural result gives you the what. The mechanism needs a
  different design.
- **Anything, if the fixture was too easy.** If a null result and "the answer
  was handed to them" are indistinguishable, the fixture is not ready — tighten
  it before running, not after.
- **Whether this method can detect anything at all.** Four runs: two
  refutations, two invalid, and **zero positives**. The method has never been
  shown to find an effect it knew was there, so its sensitivity is untested and
  its refutations are weaker than they look. The pre-flight gate demands a
  positive control of every fixture (G4); the method still owes one of itself.

## Verification

[`verification/`](verification/) checks the two parts of this method a machine
can settle. **`preflight.sh`** scores a design against the gates in
[`references/pre-flight.md`](references/pre-flight.md);
`preflight-check.sh` clears a compliant fixture, then breaks one gate at a time
and asserts the **specific** gate fires — and confirms the gate blocks the real
run that failed, on the gate that caused its failure.
**`check_preregistration.sh`** asserts a fixture's scorer was committed before
its results. It runs over the two case studies and **one of them fails** —
the author's own first experiment, where the scorer and the results landed in a
single commit. Recorded as a failure rather than quietly repaired, because it
is the cleanest possible demonstration of why behaviour 5 says *separate
commit*. `sh verification/run.sh`, < 1 s.

## Related skills

- **`evaluator-integrity`** — measurement under optimization pressure. This
  skill is that discipline applied to a claim you are personally invested in.
- **`design-of-experiments`** — the full apparatus when the comparison is the
  deliverable: power, blocking, estimands, randomization.
- **`test-writing`** — behaviour 4 is its independent-oracle rule, applied to
  an experiment instead of a unit test.
- **`docs/verifying-skills.md` §7** — the displacement-table rule demands each
  section name the default it displaces. This skill is how you find out whether
  that default is real.

## Completion report

State, briefly:

- the claim, split into its structural and behavioural halves;
- who the subjects were and why they could not know the hypothesis;
- the measurement, and why it cannot be forged;
- the commit that pre-registered the scoring, and the one that added results;
- the result against the pre-registered bands;
- the confounds, and what you did **not** conclude because of them.
