---
name: role-deck
description: >-
  Run a goal-directed process as an executable rulebook whose next step is
  drawn EXTERNALLY, so the agent cannot route around the expensive phase. Use
  when a multi-phase procedure has to be followed the same way every time and
  the record has to be trustworthy afterwards — a diagnosis, a decision, a
  review, an incident walkthrough, an intake — or when designing, auditing, or
  debugging such a procedure. A deck is roles as cards, each declaring the
  typed artifact it produces and the artifacts it requires; a bounded state
  machine that can be checked exhaustively before anyone runs it. Six
  behaviours: an externally drawn sequence so a run is auditable and
  repeatable, a phase grounded in an instrument that executes rather than
  attests, a process bounded through legality, a ledger that replays, typed
  artifacts that catch a hat bleeding into the next, and a deck simulated
  before it is used. Measured, not assumed: agents do NOT skip cheap grounding
  unprompted (8/8 ran it), so this buys auditability and repeatability, not
  work that would otherwise go undone. NOT a workflow engine,
  not a task queue, and not a way to make a model's judgement trustworthy —
  it constrains WHEN and WHETHER, never how good the thinking is.
version: 2.2.0
author: Simon Janes
tags: [process, thinking-hats, state-machine, verification, agents, decision, diagnosis]
---

# Running a process you can audit afterwards

A procedure an agent follows on its own honour leaves no evidence that it was
followed. It may have gone straight to the answer, skipped the step that would
have caught the error, or done the work perfectly — and the transcript reads
the same either way.

**What this skill does not claim.** An earlier version of this page asserted
that an unconstrained agent *will* skip the expensive step. That was measured
and is false: eight fresh agents, given a bug whose true cause is only visible
by running the code, all ran it unprompted, with no deck and no prompting
([`verification/premise-fixture/RESULT.md`](verification/premise-fixture/RESULT.md)).
For cheap grounding, agents self-ground. The claim is struck rather than
rewritten into something that sounds similar and is equally untested.

A **role deck** makes the procedure an object: roles are cards, each card
declares the artifact it produces and the artifacts it requires, and **the next
card is drawn externally**. The agent's job is to fill in the drawn card's
artifact. That is the whole mechanism, and everything below follows from it.

Because a deck is a bounded state machine, it can be checked *before* anyone
runs it — exhaustively, over every reachable state.

## The six behaviours

1. **Externalise the draw; never let the agent pick its own next step.** Not
   because an agent would otherwise skip the work — it demonstrably does the
   cheap work unasked — but because a self-chosen sequence is **unauditable and
   unrepeatable**: nothing distinguishes a run that considered three
   explanations from one that committed to the first, and two runs of the same
   question need not resemble each other. `python3 run_deck.py next` computes the legal moves and
   the die picks one. **But the die decides what work to do next, never what
   the answer is** — terminal cards are agent-chosen, from the exits it has
   actually earned. A random verdict would be absurd; a random *order of work*
   is the point.

2. **Ground evaluative phases in an instrument that runs.** A card declaring an
   instrument may not be played without `--command`; the runner executes it and
   records the output, so the agent cannot forge a result it never obtained.
   The weak version of this — "cite your source" — is another field a model can
   fabricate. A nonzero exit is not a refusal: a failing test is a result.

3. **Bound the process through legality, not a wall.** A budget enforced as
   "stop when you hit it" strands the run: the agent spends early and cannot
   afford the mandatory tail. A move is legal only if a terminal remains
   reachable within the remaining budget afterwards — **you cannot bankrupt
   yourself.** The budget is what stops planning-for-planning, and the deck's
   *floor* is the number to argue with when someone asks if the process is
   worth its overhead.

4. **Keep a ledger that replays.** The draw is a pure function of
   `(seed, step, rerolls)`, so `verify` recomputes every draw from an empty
   state. A hand-edited ledger, a bypassed runner, or a play the runner never
   authorised does not survive replay. Rerolls are *priced and logged with the
   card they avoided* — "rerolled away from the caution hat four times in five"
   is then a measurement, not a suspicion.

5. **Type every artifact, and let the schema catch the bleed.** Each card's
   artifact is validated against its declared fields **exactly**. A missing
   field is an unfinished hat; an **extra** field is hat bleed — an agent still
   wearing the last hat or reaching into the next. This is the check that does
   not depend on the model complying, which matters because non-compliance is
   the expected case, not the exceptional one.

6. **Check and simulate a deck before you run it — and ask what its laziest
   legal run does.** The gates say what is
   possible; the simulator says what actually happens, and designers are
   reliably wrong about what their generative objects generate. Every deck in
   [`decks/`](decks/) was hand-written naive first and was wrong — decorative
   hats, an exit reachable with no evidence, a gut call recorded *after* the
   evidence in half of all runs. None of that was visible by reading. And the
   check that a deck **passes** is not the end of it: `invent` v0.1.0 passed
   every gate and every simulator check and was still wrong, because nothing
   asked what its **laziest legal run** looked like. `check_deck.py` now always
   prints the min..max plays per card; that line *is* the laziest run the deck
   permits, and `minimum_work` turns what you intended into an assertion.

## Workflow

```sh
# design-time — run both, always, before a deck is used
python3 check_deck.py decks/<name>.json      # 16 gates, exhaustive
python3 simulate.py  decks/<name>.json       # exact marginals, by DP over states

# run-time
python3 run_deck.py init --deck decks/<name>.json --seed N --ledger run.json
python3 run_deck.py next   --ledger run.json                  # what to do, and what to fill
python3 run_deck.py play   --ledger run.json --artifact-file a.json [--command '...']
python3 run_deck.py reroll --ledger run.json --reason '...'   # priced, logged
python3 run_deck.py verify --ledger run.json                  # replay and re-check
```

`next` returns the drawn card, its brief, the exact fields to fill, whether a
`--command` is required, which options remain for a per-option card, and any
exits you have earned. Fill the fields; play; repeat. Pick an exit when one is
offered and you are ready.

Three decks ship: [`diagnose`](decks/diagnose.json) (something is wrong and the
cause is unknown), [`decide`](decks/decide.json) (several options, one has to be
chosen, deferred, or refused), and [`invent`](decks/invent.json) (something new
is wanted and nobody knows what it is yet).

## Writing a deck

The full field reference is in
[`references/deck-format.md`](references/deck-format.md). The parts that carry
the design:

- **`requires` is precedence, and precedence is the real constraint.** Order is
  not a suggestion you write in a brief; it is which artifacts must exist.
- **Every non-terminal card's output must be consumed by something.** An
  artifact nothing requires means a decorative hat — a role present in the deck
  whose output feeds nothing. Two of the first draft's roles were decorative.
- **Each exit earns its own preconditions** (`required_roles` as a map). With
  several exits, only the *shortest* one's requirements bind, so a cheap escape
  hatch silently voids the rest of the process.
- **Conditional requirements go through a declared nullable field.** The agent
  writes it or leaves it null; code enforces the consequence. The agent can
  still lie — but the lie is now logged and auditable instead of silent.
- **Per-option cards need an index field and a declared maximum.** Distinctness
  at runtime is what makes "every option covered" a countable thing.
- **Declare a `minimum_work` floor and keep a mutation that breaks it.** The
  floor *describes*; an `unlock` is what *enforces* it. Strip the unlock and
  confirm the floor fails, or the declaration may be describing what the deck
  would have done anyway.
- **An `unlock` gates a card on resources, never on judgement.** It is the only
  way to say *"you may not stop yet"*, because no artifact's existence means
  *enough*. Exhaustion alone is not sufficient: it measures **spend, not
  work**, and is satisfiable by padding with the cheapest card — pair
  `remaining_at_most` with a `played_at_least` on the card that is the real
  work.

## What a deck cannot do

Everything here constrains **when** and **whether**. None of it touches quality:

- **Field presence is not field quality.** Nothing checks that a discriminator
  discriminates, or that an attack is as serious as its steelman. Matched depth
  is matched *count*.
- **A command is not the right command.** `--command true` satisfies grounding.
- **A condition is only as honest as its declaration.** Nothing verifies a
  nullable field was left null truthfully.
- **Tamper-evident, not tamper-proof.** `verify` catches drift, editing and a
  bypassed runner. It does not stop someone who runs the same draw algorithm
  and forges a consistent ledger. The threat model is a model that wanders, not
  one that attacks.
- **The runner executes what it is given** (`shell=True`, with a timeout). It
  is not a sandbox.

## Guardrails — stop and escalate when

- the deck's **floor** is a larger process than the task deserves — a six-phase
  deck on a trivial question is pure cost, and the floor is printed so you can
  see it;
- the min..max line shows a card can be played once, or not at all, and you
  expected more — declare the floor and find out whether the deck delivers it;
- `check_deck.py` fails and the fix is to relax a gate rather than the deck;
- you want the die to choose an **outcome** rather than a step;
- the procedure's steps cannot be written down and defended — then this is the
  wrong tool, and `unknown-discovery` or plain judgement is the right one.

## Verification

[`verification/`](verification/) runs four harnesses: 16 gates over three decks,
30 planted deck defects each asserted caught by the gate that claims it, three
simulators, two die-driven property tests, and 20 runner refusal/tamper cases.
107 assertions. `sh verification/run.sh`, ~50 s.

Nineteen findings from building it — including three cases where *the test was
broken rather than the thing under test*, and one where the skill itself
shipped a broken check — are in
[`references/findings.md`](references/findings.md).

## Related skills

- **`agent-automation`** — the principle underneath behaviours 1, 2 and the
  conditional field: the model proposes, deterministic code authorises and
  records.
- **`tla-checker`** — the same bounded-state-machine argument, for concurrent
  systems rather than processes. The gates here are safety properties in its
  sense; the **work floor is neither safety nor liveness** but an extremal
  query over paths, which is the one thing a model checker is not usually
  asked for.
- **`causal-sandbox`** — authored-rule transitions an agent drives; a deck is
  that shape applied to its own process.
- **`unknown-discovery`** — supplies the *content* of a diagnose deck's cards
  (ACH, diagnosticity, premortem) where this supplies the sequencing.
- **`evaluator-integrity`** — why the draw must be external: the selector is
  otherwise optimising against the thing being measured.
- **`experience-library`** — the deck is a capped library; cards compete, and
  the contribution log is the reroll log's sibling.

## Completion report

State, briefly:

- the deck, its floor, and the budget the run was given;
- the sequence actually played, and any rerolls with the card each avoided;
- every instrument invoked, with its exit status;
- which conditions fired and which exits were earned;
- the exit chosen and why that one;
- that `verify` passed — and what the ledger still cannot tell you.
