---
name: simple-technical-english
description: >-
  Rewrite instructions, prompts, tool descriptions, runbooks, and procedures into
  controlled technical English so a literal reader performs the intended action.
  Use when asked to make instructions clearer or less ambiguous, write or review a
  system prompt / agent policy / tool contract / runbook / incident procedure,
  turn a vague request into an executable spec, tighten acceptance criteria, or
  reduce misreads in text that drives an action. Applies an ASD-STE100-derived
  rule profile (concrete verbs, explicit actor, condition before command, one
  instruction per sentence, defined terms, explicit scope, acceptance criteria in
  place of quality adjectives) and ships an advisory awk checker. NOT a general
  prose editor or a style beautifier, and not for brainstorming, analysis, or
  creative writing where constraint removes useful nuance.
version: 0.1.0
author: Simon Janes
tags: [writing, technical-english, ste, asd-ste100, controlled-language, instructions, prompts, runbooks, specifications]
---

# Writing Instructions in Simple Technical English

You are an autonomous agent asked to make a piece of text **executable**: a
capable but literal reader must identify the actor, the action, the object, the
condition, the constraint, the completion test, and the stopping point, and then
perform the correct action once.

This is controlled writing, not short writing. It fixes meaning, separates
actions, names conditions, and removes stylistic variation. A controlled language
expresses complex work; it removes linguistic complexity, not domain complexity.

The discipline is modeled on **ASD-STE100 Simplified Technical English** (Issue 9,
January 2025: 53 writing rules, ~900-word controlled dictionary), originally for
aviation maintenance documentation. You apply the operational subset, not full
aerospace conformance.

## When this applies -- and when it does not

Apply it where a misread instruction produces a wrong action:

- system prompts and agent policies
- tool and function definitions, API contracts
- runbooks, deployment procedures, incident response
- data transformations and compliance workflows
- evaluation criteria and acceptance tests
- agent-to-human and agent-to-agent handoffs
- prompts reused at scale

Do **not** apply it to brainstorming, exploratory analysis, relationship text,
nuanced persuasion, or creative work. There, over-constraint strips useful
context, personality, and uncertainty. Say so and stop if asked to "simplify"
that kind of text.

## Core model

Treat the rewrite as a controlled derivation, not a copy-edit:

    read the draft -> complete the intent -> rewrite each sentence controlled
    -> run the checker -> review every flag -> deliver with the open questions

The single most important rule:

> One sentence creates one clear operational commitment: one main action, no
> hidden decision.

That does not mean every sentence is tiny. It means it has one action and no
buried condition.

## Method

### 1. Read the draft and name its mode

Classify each paragraph as one of four modes and keep them separate downstream.
A descriptive sentence that reads as a command is the most common defect.

| Mode | Purpose | Form |
|---|---|---|
| Instruction | Tell the agent what to do | Imperative verb, one action, condition first |
| Description | Explain how something works | Present tense, one topic |
| Policy | State what is allowed or forbidden | "must" / "must not", scope, exceptions |
| Decision rule | Choose between actions | If-then with thresholds and tie-breakers |

Full detail: [`references/writing-modes.md`](references/writing-modes.md).

### 2. Complete the intent (pass 1)

Before controlling the language, make the content complete. Prioritize
completeness over brevity here. Resolve the seven questions:

**who** performs the action; **what** object it affects; **what action** occurs;
**when** it is allowed, required, or forbidden; **what constraints** limit it;
**what evidence** proves completion; **what happens** on failure, uncertainty, or
conflict.

For any procedure, define the five execution states: **entry** (preconditions),
**action** (the exact operation), **success** (observable go signal), **failure**
(stop / retry / rollback / escalate), **exit** (required output or final state).

Where the draft cannot answer one of these, record it as an open question. Do not
invent the answer.

### 3. Rewrite each sentence controlled (pass 2)

Apply the rule profile in [`references/rule-profile.md`](references/rule-profile.md):

1. **Concrete verbs.** Use `create, read, list, find, compare, copy, delete,
   send, stop, record, return, ask, verify, report`. Avoid `handle, manage,
   address, leverage, optimize, facilitate, ensure, process` unless you define
   them.
2. **Explicit actor.** Active voice. Name who is responsible. For a human-agent
   workflow, say whether the agent acts or asks a person.
3. **Condition before command.** `If the backup completes, delete the temporary
   files.` -- never the reverse. Add the failure branch.
4. **One instruction per sentence.** Split ordered steps into a numbered list.
5. **Defined terms.** Turn "high risk", "active customer", "production-ready"
   into a stated predicate at first use.
6. **Explicit scope and exclusions.** Say what to do and what not to do; name the
   directories, orgs, or record types in and out of bounds; forbid inference of
   missing values.
7. **Acceptance criteria, not quality adjectives.** Replace "robust", "correct",
   "clean", "complete" with the test that proves them.

Keep terminology fixed: if `delete` means permanent removal, never later write
`clear`, `purge`, or `clean up` for the same operation.

Sentence-length guidance: about 20 words procedural, about 25 descriptive, as
warnings not laws.

### 4. Run the checker and review every flag

```sh
skills/simple-technical-english/verification/run.sh YOUR_FILE.md
```

Add `--canon "verify,delete,create"` to name the verbs you standardized on; the
checker then flags every other synonym at its line. Add `--strict` for a
non-zero exit on any finding (CI).

The checker is **advisory**: it flags surface patterns, not meaning. `PASSIVE?`
and `MULTI-ACTION?` produce false positives by design. Review each flag; fix or
consciously keep it. See [`verification/README.md`](verification/README.md).

### 5. Deliver

Return the rewritten text, the list of open questions from step 2 (the intent
the draft did not specify), and a short note of any checker flags you kept and
why.

## Patterns

[`references/prompt-patterns.md`](references/prompt-patterns.md) has reusable
shapes for research tasks, code-change tasks, and incident-triage tasks, plus the
two-pass editing method.

## Refuse / escalate

- Do not "simplify" brainstorming, analysis, or creative text -- explain that
  constraint removes nuance the text needs.
- Do not invent an actor, threshold, scope, or acceptance criterion the source
  does not provide. List it as an open question instead.
- Do not treat a clean checker run as proof the instruction is correct -- the
  checker sees surface form, not meaning or assumptions.
- Do not add detail that does not resolve a decision, set a boundary, define a
  term, or enable verification. Excess detail dilutes priority.

## Minimum standard

1. Every paragraph is one mode; no descriptive sentence reads as a command.
2. The seven questions are answered or listed as open.
3. Every procedure has its five execution states.
4. Every verb is concrete; terminology is fixed across the document.
5. Every condition precedes its command; every failure branch is stated.
6. Scope, exclusions, and permission boundaries are explicit.
7. Completion has an observable acceptance test, not a quality adjective.
8. The checker was run and every flag was reviewed.
9. Open questions are delivered with the text, not silently resolved.

## References

- [`references/rule-profile.md`](references/rule-profile.md) -- the seven rules,
  weak-versus-strong instruction tables, length guidance, sources.
- [`references/writing-modes.md`](references/writing-modes.md) -- the four modes,
  the five execution states, where strictness helps, common misconceptions.
- [`references/prompt-patterns.md`](references/prompt-patterns.md) -- reusable
  task shapes and the two-pass method.

## Templates

- [`templates/instruction-checklist.md`](templates/instruction-checklist.md) --
  copy-paste pre-publish checklist.

## Verification

- [`verification/ste-check.awk`](verification/ste-check.awk),
  [`verification/run.sh`](verification/run.sh) -- the advisory checker.
- [`verification/test.sh`](verification/test.sh) -- 18-assertion battery over
  `verification/fixtures/`, one file per tag, no network.
- [`verification/README.md`](verification/README.md) -- tags, options, limits,
  and Vale as the CI-grade upgrade path.

## Completion report

State: which text was rewritten; the mode of each section; the open questions the
draft did not answer; the execution states you had to add; the terminology you
fixed and the synonyms you removed; the checker findings and which you kept and
why; and whether any part was left unchanged because STE does not apply to it.
