# role-deck — checker first, findings from building it

Not a skill yet: no `SKILL.md`, deliberately outside `skills/` so
`tools/check-skills.sh` does not see it.

    sh experiments/role-deck/run.sh     # ~1s

## What exists

| File | What it is |
|---|---|
| `decks/diagnose.json` | the rulebook: artifact types with fields, cards (role, copies, requires, produces, instrument), required roles |
| `check_deck.py` | fourteen static gates over the deck, by exhaustive state-space exploration |
| `budget.py` | the budget model, and why it enters through legality rather than as a wall |
| `mutation-check.sh` | plants one defect per gate and asserts each is caught |
| `run_deck.py` | the runner: external draw, artifact validation, append-only ledger, replay-based `verify` |
| `runner-check.sh` | eight refusals and ten ledger-tamper cases, all asserted caught |
| `decks/decide.json` | the second deck, chosen because diagnose exercises none of: optional hats, multiple terminals, ordering freedom |
| `condition-check.py` | property tests driven by the real die: no commit over an unresolved disputed fact, and no commit/drop before every option has both a steelman and an attack |
| `simulate.py` | what the deck actually generates: every complete path with its exact probability, plus the declared orderings verified |

A deck is a bounded state machine: state is the multiset of cards played, a
card is legal when a copy remains and its required artifacts are present, play
ends at a terminal card. Legality depends on the *set* of artifacts present,
not the order they arrived — which collapses the state space to reachable
subsets of the deck and makes exhaustive checking trivial at any size a human
would author (87 states here).

## The three findings

**1. RED and YELLOW were decorative.** The hand-written v0.1.0 deck passed
every structural gate and failed `no-orphans`: nothing consumed the hunch or
the support. They were in the deck because de Bono prescribes them, not
because the process needed them. Both now have principled consumers rather
than gate-appeasing ones — `falsify` (BLACK) requires `support`, so you cannot
design a *discriminating* test before saying what each hypothesis predicts
(which is also de Bono's yellow-before-black, now enforced rather than
advised); and `close` requires `hunch`, so the verdict must say whether the
opening gut call was borne out, which is the only thing that stops it steering
silently. Tightening those two edges cut the reachable state space **183 → 87**:
fewer ways to wander.

**2. A global budget cannot be a hard wall.** `no-deadlock` and `terminal-live`
were near-vacuous in v0.2.0: artifacts only accumulate, so once a terminal was
reachable it stayed reachable. Adding a budget was meant to fix that. The naive
version — *a move is legal while `spent + cost <= budget`* — does not work. The
agent spends early on optional cards and then cannot afford the mandatory tail,
and the only strand-free wall is the entire deck:

| wall budget | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
|---|---|---|---|---|---|---|---|
| dead ends | 9 | 12 | 14 | 11 | 5 | 1 | **0** |

A budget that only stops binding when it stops constraining is not a budget.
This matters more here than in a game a human plays, because **the draw is
external**: a human who strands themselves made a mistake, but an agent handed
a stranding move by a die was given an illegal position by the rulebook.

So the budget enters through **legality** instead: *a move is legal only if,
after playing it, a terminal is still reachable within the remaining budget.*
You cannot bankrupt yourself. The budget still binds — it prunes the branches
that would waste the tail — but no reachable state is ever a dead end:

| | states | complete runs | dead ends |
|---|---|---|---|
| hard wall at 11 | 74 | — | **7** |
| look-ahead at 11 | 61 | 8 | **0** |

**3. The deck's floor is 9 cards.** Eight cards — `open`, `gather`,
`hunch`, `hypothesize`, `support`, `falsify`, `run`, `close` — but `run` costs
2, because EXECUTE is the hat that spends real resources. The deck runs at
budget **11** against a total deck cost of 14, so there is slack for two extra
plays and **8 distinct complete runs**. This is the number to argue with when
asking whether the process is worth its overhead: not a feeling, a floor.

**4. `no-deadlock` is now an invariant, not a gate.** Look-ahead legality makes
a dead end structurally impossible, so no *deck* defect can fire it — the
mutation that was written for it correctly fires `budget-feasible` instead,
which rejects an unreachable terminal before the state space is even built.
`no-deadlock` is therefore an assertion about the **rule**, and it is verified
by a regression probe that disables the look-ahead and confirms 7 strands
reappear. An assertion that can never fail is worth labelling as one.

## Gates

| Gate | Catches |
|---|---|
| `schema` | undeclared artifact types |
| `exclusivity` | **hat bleed** — a card's artifact carrying a field owned by another artifact type (GREEN shipping a `ranking` means BLACK already ran, silently) |
| `acyclic` | precedence cycles |
| `reachable-cards` | a card that can never legally be played |
| `budget-feasible` | a budget below the deck's floor, or no reachable terminal at all |
| `budget-binding` | a budget at or above the whole deck's cost — decorative |
| `no-deadlock` | a reachable non-terminal state with no legal move (*invariant — see finding 4*) |
| `terminal-live` | a reachable state from which no terminal is reachable |
| `coverage` | **a path to a terminal that omits a required role** — the structural form of "the agent must not be able to finish without wearing the caution hat" |
| `no-orphans` | an artifact nothing consumes: a decorative hat |

`coverage` is the one that carries the argument from the design conversation.
It makes "the agent routed around Black" impossible by construction rather
than detectable after the fact.

## The runner

    python3 run_deck.py init   --deck decks/diagnose.json --seed 4271 --ledger run.json
    python3 run_deck.py next   --ledger run.json     # what the die drew, and what to fill
    python3 run_deck.py play   --ledger run.json --artifact-file a.json
    python3 run_deck.py reroll --ledger run.json --reason "..."
    python3 run_deck.py verify --ledger run.json     # replay and re-check everything

The agent never chooses its next hat. The runner computes the legal moves, the
draw picks one, and the agent's only job is to produce that card's artifact.

**Three properties make the ledger worth trusting.** The draw is a pure
function of `(seed, step, rerolls-at-that-step)` — nothing random is stored, so
`verify` recomputes every draw from an empty state and a hand-edited ledger does
not survive replay. Artifacts are validated against the card's declared fields
*exactly*: a missing field is an unfinished hat, an extra field is **runtime hat
bleed** — an agent still wearing the last hat or reaching into the next one.
And `spent` is derived from the play history rather than stored, so there is no
mutable counter to corrupt.

That second property is the answer to "some models ignore instructions". The
static `exclusivity` gate checks the *deck* declares its fields cleanly; the
runtime check catches an *agent* that fills in a field belonging to another
hat. Neither depends on the model complying.

`runner-check.sh` asserts six refusals (missing field, hat bleed, empty field,
playing a card the die did not draw, malformed JSON, a reroll past the
allowance) and seven tamper cases (a play deleted from the middle, a field
emptied after the fact, another hat's field spliced in, the recorded draw
rewritten, a play forged and appended, the reroll count inflated, rerolls
beyond the allowance). All thirteen are caught. Four of the seven tamper cases
are caught by the draw failing to reproduce, which is the property doing the
work.

**Finding 5: the reroll log is the behavioural signal.** A reroll is priced and
recorded with the card it was spent avoiding. "The agent rerolled away from
BLACK four times out of five" is then a measurement rather than a suspicion —
the process analogue of `experience-library`'s contribution log.

**Finding 6: grounding has to execute, not attest.** The weak reading of
condition 3 — *"the artifact must cite its source"* — is just another field a
model can fabricate. The real version is `agent-automation`'s split: the agent
**proposes a command**, the runner **executes it and records the result**. The
output in the ledger is produced by the runner, so an agent cannot forge a
result it never obtained.

The deck names which roles must be grounded (`instrumented_roles`: WHITE and
EXECUTE here) and `check_deck.py` asserts they declare an instrument. At play
time a grounded card without `--command` is **refused** — that hat may not be
worn on introspection alone — and a `--command` on an ungrounded card is
refused too, so grounding cannot leak.

Run on the real diagnosis, the EXECUTE hat captured:

    $ printf '*** FAIL: x' | grep -q '*** FAIL'; echo "regex form: $?"; ...
    regex form: 2
    fixed form: 0
    grep: repetition-operator operand invalid

That is the finding of the original audit, produced by the runner rather than
asserted by the model. The stored output is hashed, so editing it after the
fact fails `verify`.

## The simulator

The gates say what is *possible*. They say nothing about how often — and a deck
is a generative object, which designers are reliably wrong about. The state
space is small, so `simulate.py` does not sample: it **enumerates every
complete path with its exact probability** (the product of 1/|legal moves| per
step). Monte Carlo runs only as an independent cross-check, and it goes through
the real hash-based die in `run_deck.draw`, so the comparison also tests whether
that die is uniform. It is: total-variation distance 0.042 over 4000 seeds,
mean length 9.955 exact vs 9.956 sampled.

**Finding 7: the hunch was landing after the evidence, half the time.** In
v0.5.0 the ordering table read:

    gather    before hunch          50.0%
    hunch     before hypothesize    75.0%
    falsify   before hunch           6.2%

RED exists so the gut call is on the table *before* it can be rationalised by
what you have seen. A hunch recorded after the evidence is not a hunch, it is a
post-hoc summary — and in 6% of runs it was recorded after the discriminating
test had already been designed. **Every static gate passed this.** `no-orphans`
confirmed the hunch was consumed; `coverage` confirmed RED was always worn.
Both true, and both blind to *when*.

The fix is one edge: `gather` now requires `hunch`, so no evidence can exist
until the prior is recorded. Paths fell **458 → 59**, states **61 → 36**, and
every co-occurring pair now has a forced order. Decks can declare an
`expected_order` and the simulator verifies it — which turns designer intent
into an assertion instead of a hope. The bug is replanted in
`mutation-check.sh` as a regression.

**Finding 8: budget slack is spent, not saved.** 96% of runs cost exactly 11,
the full budget, against a floor of 9 — mean 10.96. A uniform draw has no
preference for finishing, so an optional card is played whenever it is legal.
The budget is therefore not a ceiling you rarely touch; it *is* the expected
process cost. The honest answer to "what does this deck cost" is **~10 plays,
essentially always**, not "9 to 11 depending". If runs should finish earlier
the lever is the draw (weight it toward terminal-advancing cards) or fewer
optional copies — not a bigger budget.

One consequence worth noticing: the diagnose deck is now a **fixed pipeline
with a variable number of repeats**. The die decides multiplicity, not order.
That is probably right for diagnosis, where evidence really must precede
hypotheses; it would be wrong for an *invent* deck, where ordering freedom is
the point. Ordering rigidity is a design choice the simulator makes visible.

## Weights: what they control, and what they do not

`copies` bounds how many times a hat MAY be worn — a resource limit. `weight`
bounds how likely it is to be drawn when legal — a bias. They were deliberately
not conflated. And because a flat weight cannot tell a card's first play from
its third (it is the same card), weight decays per prior play:

    effective = weight * repeat_decay ** (times already played)

Decay 1.0 reproduces the uniform draw exactly, so the feature is backward
compatible by construction. Weights never affect legality, so the state space,
the budget look-ahead, and every gate are untouched by them.

**Finding 9: the budget sets the cost, the weights set the shape.** Finding 8
named weighting as the lever for process cost. It is not. Measured head to head:

| lever | paths | E[spend] | P(minimal run) |
|---|---|---|---|
| baseline, budget 11 | 59 | 10.96 | 0.3% |
| `repeat_decay` 0.35 | 59 | 10.67 | 5.2% |
| budget 11 → 10 | 12 | **10.00** | 0.3% |
| budget 11 → 9 (the floor) | 1 | **9.00** | 100% |
| `gather`/`hypothesize` copies 2 → 1 | 4 | 10.00 | 16.7% |

A 65% weight reduction on every repeat moves expected spend by **0.29**. Cutting
the budget by one moves it by **0.96**, exactly. Two reasons, both structural:

- **Suppressing one repeat frees budget for another.** As decay falls from 1.0
  to 0.35, P(a second `falsify`) *rises* from 14.8% to 24.3%. The draw
  redistributes the slack rather than returning it.
- **The budget is spent before the exit is legal.** Weighting `close` up to 12
  only moves expected spend from 10.67 to 10.45, because by the time `close`
  becomes legal the optional cards have already been played. You cannot fix
  process cost by making the exit attractive; the decision that cost you
  happened five steps earlier.

So there is a variety/cost frontier, and every unit of budget on it is fully
spent: **budget 9 → 1 path**, budget 10 → 12 paths, budget 11 → 59 paths. Pick
the budget for the cost you will accept, then use weights to shape which of the
runs you get.

The diagnose deck ships at `repeat_decay` 0.5 and `falsify` weight 2 — a claim
*about diagnosis*, now expressible: a second discriminating test is worth more
than a second round of evidence-gathering, because it can separate hypotheses
the first test left tied. Expected spend 10.84, and P(a minimal run) rises from
0.3% to 2.1%.

## The decide deck, and what a second deck was for

`diagnose` exercises one capability: multiplicity. All eight cards play in
100% of runs, there is one terminal, and since v0.6.0 every ordering is forced.
`decide` was chosen to hit the three untested ones — optional hats, multiple
exits, ordering freedom — and it broke something on each.

**Finding 10: multiple terminals make orphaning easy.** The naive v0.1.0 had
*three* decorative hats (WHITE, GREEN and EXECUTE all produced artifacts
nothing consumed) and a floor of **5**: `frame → criteria → steelman → attack →
defer`. You could defer a decision having gathered no evidence, considered no
alternatives and run no probe. With one exit, the precedence chain to the
terminal pulls most cards in behind it; with three, **only the shortest exit's
requirements bind**, and everything else floats free.

The fix made each exit earn its own preconditions, which forced a machinery
change: **`coverage` had to become per-terminal.** You cannot commit without
wearing BLACK, but you can legitimately drop a decision without ever running a
probe. A single global requirement makes every exit as heavy as the heaviest,
which is how a `defer` card ends up demanding an experiment. `required_roles`
now accepts a map from exit to its own list; the list form still means "all
exits", so diagnose is unchanged.

Two of the fixes are substantive claims about deciding, now expressible:
you may not say *"none of these work"* without having tried to invent one that
does (`drop` requires GREEN's alternative), and you may not commit over a
disputed fact the attack turned up (`commit` requires the probe result).

**Finding 11: the die must never choose the answer.** v0.2.0 committed in only
**14.5%** of runs — a magic 8-ball that says "ask again later" 85% of the time.
Weighting `commit` up to 8 only reached 26.4%, because `defer` and `drop`
become legal the moment `attack` lands while `commit` needs one more card: the
die ends the run before committing is even an option.

But the real error was upstream. Exits are not interchangeable moves — they are
the **output the process exists to produce**, and which one is right depends on
what the analysis found, which is exactly what a state-independent draw cannot
see. So terminal cards are now **agent-chosen, never drawn**. This does not
reopen the route-around-the-caution-hat problem, because `coverage` already
guarantees each exit's preconditions: the agent may only choose among exits it
has *earned*. The die decides what work to do next; only the conclusion is free.

The simulator's exit rows are now labelled `AGENT-CHOSEN, not drawn`, because
those percentages describe a hypothetical uniform agent and are not facts about
the deck.

**Finding 12: the look-ahead preserves *an* exit, not *your* exit.** A real
playthrough spent 10 of 12 on repeats and arrived with `commit` priced out —
probe costs 2, and 2 remained. Not a strand: `defer` and `drop` were still
reachable, so every gate was satisfied. The die had simply spent the run out of
its best ending. A deck may now name `preserve_exit`, and legality additionally
requires that exit to stay affordable. On decide it cut the space from 149
states / 25,767 paths to **88 / 4,613**, and `commit` is affordable from every
reachable state.

**Finding 13: a cross-check that trips on size is not a check.** The
exact-vs-die comparison used total-variation distance over paths, and fired on
decide at TV 0.557 — not because the die was biased but because 25,767 paths
cannot be populated by 3,000 draws. TV is the wrong statistic when paths ≫
samples. It now compares **marginals** (mean length, per-card expected plays)
below that threshold: largest per-card gap 0.014. The die was always fine; the
gate was measuring deck size.

## Conditional requirements

`commit` required a probe result unconditionally, though not every attack
raises a fact worth probing. Making that conditional breaks something
fundamental: **legality would depend on artifact content**, which is outside
the state model, and that kills exhaustive enumeration. Two things make it
checkable anyway.

**The condition is a declared, typed field.** `faults` gains a nullable
`disputed_fact`; the agent writes it or leaves it null, and deterministic code
enforces the consequence. The agent can still lie to skip the probe — but that
is now an explicit, logged, auditable claim rather than a silent omission. It
is the `agent-automation` split once more: the model proposes, code enforces.
A nullable field left empty is a **declaration**, not an oversight, and it is
the one place the agent may shorten its own process.

**The state space branches on it.** State becomes `(counts, flags)`; a play
that can trigger a condition branches into both outcomes, so every gate is
checked with the condition fired *and* not fired. Flags latch, so the space is
`counts × 2^k` — decide went 88 → 167 states. Nothing about a flag is stored in
the ledger: `verify` recomputes them from what the artifacts say, so forging a
flag means forging a field, which the existing checks already cover.

The look-ahead is deliberately **pessimistic** — it assumes every condition
that can still fire does. Otherwise an agent could be stranded by its own
honest declaration, which is finding 12 wearing a different hat.

**Finding 14: a preference that can strand is a bug.** Enforcing `preserve_exit`
strictly deadlocked decide v0.5.0. It pruned `alternatives` because `commit`
would no longer be affordable afterwards — and *every* exit requires
`alternative`, so nothing at all was legal. `preserve_exit` now **yields**:
if preserving the named exit would leave no legal move, the plain
terminal-reachability rule applies instead. Preserve the best ending where
possible, never at the cost of having none.

Two gates came out of it. `conditions` asserts a declared condition is
well-formed *and* that it **actually changes what is legal in some reachable
state** — same spirit as `no-orphans`, because a conditional requirement that
never bites reads as a safeguard while permitting everything. And `no-orphans`
now counts conditional requirements as consumption: `probe_result` is not
decorative just because the probe is optional.

Proof it bites, at the model level:

| after the full analysis, no probe played | `commit` legal? |
|---|---|
| attack declared **no** disputed fact | **yes** |
| attack declared a disputed fact | **no** |

and at the runner level, `condition-check.py` drives 300–400 real runs through
the die and checks the invariant at every exit-decision point: 1218 points,
**0 violations**.

## Per-option cards and matched depth

*"Steelman and attack each option at matched depth"* is a symmetry constraint
over a list whose length is unknown until the run starts. It looked
inexpressible. Two observations made it checkable:

**Options are symmetric to the deck.** It does not care *which* option a
steelman addresses, only that every option got one. So if the runner enforces
that each per-option play names a **distinct** option, the static model needs
only counts: *all options covered* reduces to `count(producer) >= n_options`.
Distinctness at runtime is what buys countability at check time.

**The list is bounded.** `option_source` declares a maximum, and the checker
**expands the deck once per possible option count and runs every gate on
each** — the same move as branching on a condition: enumerate the parameter
rather than model it. decide verifies at n=1 (59 states), n=2 (135) and n=3
(259).

Matched depth is then just `commit` and `drop` declaring
`requires_all: [support, faults]`. `defer` deliberately does not — the one
exit that does not need every option examined, because "not yet" is a
legitimate thing to say halfway through. And you may not **refuse** a field you
have not examined, which is why `drop` carries the same burden as `commit`.

**Finding 15: an exemption that removes the legitimate claims leaves the
illegitimate one unopposed.** A per-option artifact needs an index field
(`option`) naming which option it addresses, and two of them carrying the same
field is not hat bleed — it is one coordinate on two artifacts. So
`exclusivity` exempts the declared index field on per-option artifacts. That
exemption *silently permitted* adding `option` to `evidence`: exempting
`support` and `faults` meant nothing was left to collide with. The gate now
also forbids the index field outright anywhere a per-option card does not
produce. The planted mutation survived until it did.

A run of three options, watched through the runner:

    6. steelman  [opts left: buy,build,partner]
    9. steelman  [opts left: build,partner]
   10. steelman  [opts left: partner]
   12. attack    [opts left: build,partner]
   13. attack    [opts left: partner]
       exits: commit,defer,drop

`commit` appears only after the thirteenth play — the moment the last option
has both. `condition-check.py` asserts that as a property over 300 die-driven
runs: 1195 exit-decision points, 485 with commit or drop on offer,
**0 violations**.

## Resource unlocks, and the `invent` deck

`invent` was the shape the machinery could not express: every legality
predicate was artifact-based, and invent's terminal condition is *"good
enough"* — a judgement, with no artifact whose existence means stop.

The primitive that fixes it turned out to need **no new machinery at all**.
Plays, spend and per-card counts are functions of the counts vector, and the
counts vector is already the state — so unlike conditions (a flag dimension) or
per-option cards (expansion), an `unlock` does not grow the state space by a
single node. The design decision was the whole of the work: a *judgement*-gated
terminal hands back the one decision the external draw exists to remove, so
unlocks key on **resources only**.

**Finding 16: exhaustion measures spend, not work.** `invent` v0.1.0 gated
`harvest` on `remaining_at_most: 2` and **passed every gate and every simulator
check on the first draft** — the only deck of the three to do so. It was still
wrong. Searching for the laziest legal complete run:

    frame generate generate generate generate generate generate
    oblique oblique survey develop try cull harvest

Six `generate` plays — its entire copy limit — to burn budget down to the
unlock, and **exactly one trial**. The exhaustion gate is satisfiable by
padding with the cheapest legal card. This refutes the claim written into
`BACKLOG.md` when the deck was deferred, that "terminating by exhaustion is at
least incorruptible": it cannot be *talked* out of stopping early, but it can
be *padded* into it. The fix pairs exhaustion with work:
`played_at_least: {card: try, n: 2}`, after which the laziest run does two real
trials.

Note what found this. Not a gate, not the simulator — an explicit search for
the run that does the least work while staying legal. That search is worth
running on any deck with an unlock, and it is the thing to add next.

**Finding 17: the path space is exponential in the state space.** The simulator
enumerated every complete path, which was exact and fine at 59 paths
(`diagnose`) and 261,243 (`decide`) — and simply did not return for `invent`,
which has **1,182 reachable states and 22,302,788 paths**. The fix is a
different algorithm for the same numbers: dynamic programming over the state
space, exact rather than sampled, because a state's future does not depend on
how it was reached. Ordering is the one figure that is not a plain state
marginal, so each pair gets a three-valued latch (neither seen / a first /
b first) — still linear in the state space. `invent` now reports in **0.66 s**,
and `diagnose`'s numbers are reproduced to the digit.

**Finding 18: a check that has never run is not a check — including this
harness's own.** The completed `invent` run failed `verify` with *"run
completed without wearing required roles: ['harvest']"*. `required_roles` is a
list or a map, and `set(a_dict)` yields the **keys** — card ids — which were
then compared against role names. Latent since `coverage` became per-terminal:
`diagnose` is list-form, and **no map-form deck had ever been played to a
terminal**, because every `decide` playthrough stopped at the exits rather than
taking one. The skill shipped at 1.0.0 with it. A completed map-form run is now
part of `runner-check.sh`.

## Known limitations

- **Monotone artifacts.** Cards are consumed; artifacts are not. The budget now
  supplies the exhaustible resource that makes the state space interesting, but
  no card ever *invalidates* an earlier artifact — a diagnosis cannot go stale.
- **One producer per artifact type** — now checked (`schema`), after the
  mutation harness found that two producers would silently collapse the
  precedence map.
- **Tamper-evident, not tamper-proof.** `verify` catches drift, hand-editing,
  and a bypassed runner. It does not stop an adversary who runs the same draw
  algorithm and forges a self-consistent ledger. The threat model is a model
  that wanders, not one that attacks.
- **Field presence is not field quality.** The runner checks that every
  declared field is present and non-empty. Nothing checks that `discriminator`
  actually discriminates — that stays human, or needs the instrument.
- **A command is not the right command.** Grounding proves a command ran and
  records what it printed. Nothing checks it was *relevant* — `--command true`
  satisfies the gate. This is the same boundary as field presence vs field
  quality, one level down, and it is where the human stays.
- **The runner executes what it is given**, with `shell=True` and a timeout.
  Fine for a local tool whose deck and operator you trust; it is not a sandbox.
- **Three decks.** `build` would likely be *more* forced than diagnose and test
  little. `improve` is the one shape this machinery structurally **cannot**
  express — L5 means the process revises itself, and every gate assumes the
  deck is fixed for the duration of a run.
- **No laziness search in the harness.** Finding 16 was found by hand, by
  searching for the legal run that does the least work. Nothing runs that
  search automatically, so the next deck with an unlock can repeat the mistake.
- **An unlock cannot key on artifact content**, deliberately — that is what
  keeps it incorruptible, and it is also why it cannot express "stop when the
  result is good", which remains outside the model.
- **Matched depth is matched COUNT, not matched effort.** The deck can require
  every option to have a steelman and an attack. It cannot tell a two-line
  attack from a page of one, which is the sense in which a steelman is usually
  unfair. Field presence is not field quality, once more.
- **One index only.** A card can be per-option; it cannot be per-option-per-
  criterion. Nested indices are unmodelled.
- **A condition is only as honest as the declaration.** Nothing verifies that
  `disputed_fact` is null *truthfully*. The gate moves the lie from silent to
  logged; it does not prevent it. That is the same boundary as "a command is
  not the right command", one level up.
- **Conditions key on presence, not value.** `is the field non-null` is the
  only predicate. There is no *"if cost > X"* or comparison of any kind.
- **The suite is 48s**, over the repo's seconds-not-minutes bar. Most of it is
  process spawn across ~80 python invocations in the mutation harnesses; user
  time is 10s.
- **Weights are state-independent.** `weight * decay^plays` depends only on how
  often a card has been played, not on what else is in the artifact set. A card
  cannot become more attractive *because* a particular result came back — which
  is exactly what an adaptive process would want, and what finding 9 says the
  budget cannot give you either.

