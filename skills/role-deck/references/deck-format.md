# Deck format

Field reference for a deck JSON. Every field here is exercised by
[`../decks/diagnose.json`](../decks/diagnose.json) or
[`../decks/decide.json`](../decks/decide.json) and gated by
[`../check_deck.py`](../check_deck.py). The reasoning behind each is in
[`findings.md`](findings.md).

## Top level

| Field | Required | Meaning |
|---|---|---|
| `deck`, `version` | yes | name and semver of the rulebook |
| `goal_shape` | yes | one line: what kind of goal this deck is for |
| `artifacts` | yes | map of artifact type → `{fields: [...], nullable: [...]}` |
| `cards` | yes | the roles; see below |
| `budget` | yes | total cost a run may spend. Enters through **legality**, not as a wall |
| `required_roles` | yes | list (applies to every exit) **or** map from exit card id → its own list |
| `instrument_kinds` | if grounded | the instrument names a card may declare |
| `instrumented_roles` | if grounded | roles that MUST declare an instrument |
| `repeat_decay` | no | default 1.0. Multiplier on a card's weight per prior play |
| `rerolls` | no | default 0. Reroll tokens the agent may spend |
| `preserve_exit` | no | one exit id whose affordability legality preserves — **yields** rather than stranding |
| `expected_order` | no | `[[a, b], ...]` pairs the simulator asserts always hold |
| `conditions` | no | see *Conditional requirements* |
| `option_source` | no | see *Per-option cards* |

## Cards

| Field | Required | Meaning |
|---|---|---|
| `id`, `role`, `brief` | yes | identity, the hat, and what the agent is being asked for |
| `copies` | yes | how many times this hat MAY be worn — a resource limit |
| `requires` | yes | artifact types that must exist before this card is legal |
| `produces` | yes | the artifact type this card emits. **One producer per type** |
| `instrument` | yes (may be null) | `retrieval` / `execution` / null. Non-null ⇒ `--command` required at play time |
| `cost` | no | default 1. Counts against the budget |
| `weight` | no | default 1.0. How likely the die is to pick it when legal — a bias, *not* a limit |
| `terminal` | no | an exit. **Agent-chosen, never drawn** |
| `unlock` | no | a resource predicate that must hold before the card is legal; see *Resource unlocks* |
| `requires_all` | no | artifact types needed **once per option** |
| `per_option` | no | `copies` becomes the option count |

`copies` and `weight` are deliberately separate: *how many times may I* versus
*how likely am I to be asked*. `repeat_decay` exists because a flat weight
cannot tell a card's first play from its third — it is the same card.

## Resource unlocks

```json
"unlock": {"remaining_at_most": 2, "played_at_least": {"card": "try", "n": 2}}
```

Every other predicate is artifact-based: a card is legal when the artifacts it
requires exist. That cannot say *"you may not stop yet"*, because no artifact's
existence means *enough*. An unlock keys on **resources only** — never on
content, never on judgement:

| Key | Opens when |
|---|---|
| `plays_at_least` | n cards have been played |
| `spent_at_least` | n budget consumed |
| `remaining_at_most` | budget left ≤ n — the **exhaustion** gate |
| `played_at_least` | `{card, n}` — that card played n times |

Keys are ANDed. They cost nothing structurally: plays, spend and per-card
counts are all functions of the counts vector, which is **already the state**,
so unlike conditions (which add a flag dimension) or per-option cards (which
expand the deck) the state space does not grow at all.

The choice of primitive is a design decision. A *judgement*-gated terminal
("stop when it is good enough") hands the agent back the one decision the
external draw exists to remove. A *resource*-gated one cannot be talked out
of — at the cost of not being able to stop early when you got lucky.

**But exhaustion alone measures spend, not work**, and is satisfiable by
padding with the cheapest legal card — see finding 16. Pair
`remaining_at_most` with a `played_at_least` on the card that represents real
work.

## Conditional requirements

```json
"conditions": [{
  "id": "disputed",
  "artifact": "faults",
  "field": "disputed_fact",
  "adds_requirement": {"card": "commit", "artifact": "probe_result"}
}]
```

The field must be declared **nullable** — a field that can never be null is a
requirement, not a condition. The agent writes it or leaves it null; that is a
*declaration*, logged and auditable, and the one place the agent may shorten
its own process. The state space branches on it, so every gate is checked with
the condition fired and not fired, and the look-ahead is pessimistic (it
assumes anything that can still fire will) so an honest declaration can never
strand the run.

## Per-option cards

```json
"option_source": {"artifact": "decision", "field": "options",
                  "index_field": "option", "max": 3}
```

A `per_option` card gets one copy per option. Its artifact must declare the
`index_field`, and the runner refuses a play that names an option already used
by that card — **distinctness at runtime is what makes "every option covered"
countable at check time**. `max` bounds the expansion so the checker can verify
the deck at every option count.

## The gates

| Gate | Rejects |
|---|---|
| `schema` | undeclared artifact types; two producers for one type |
| `exclusivity` | a field owned by two artifacts (**hat bleed**); a stray index field |
| `instrument-grounding` | a role that must be grounded and is not; an unknown instrument kind |
| `weights` | a non-positive weight; a `repeat_decay` outside (0, 1] |
| `options` | per-option cards with no bound, index, or a `requires_all` on a fixed-count producer |
| `conditions` | a condition on a non-nullable field, or one that never changes what is legal |
| `unlocks` | an unknown unlock key; an unlock that never blocks (decorative) or never opens (unplayable) |
| `acyclic` | a precedence cycle |
| `budget-feasible` | a budget below the floor; no reachable terminal |
| `budget-binding` | a budget at or above the whole deck's cost — decorative |
| `reachable-cards` | a card that can never legally be played |
| `no-deadlock` | a reachable non-terminal state with no legal move (*an invariant of the look-ahead rule*) |
| `terminal-live` | a state from which no terminal is reachable |
| `coverage` | **an exit reachable without a role it requires** |
| `no-orphans` | an artifact nothing consumes — a decorative hat |
