#!/usr/bin/env python3
"""Static checker for a role deck.

A deck is a bounded state machine: state is the multiset of cards played, a
card is legal when a copy remains, its required artifacts are present, and the
budget rule allows it; play ends at a terminal card. Legality depends on the
SET of artifacts present rather than the order they arrived, and cost is a
function of the card, so `spent` is determined by the multiset too -- which
keeps the reachable state space to subsets of the deck, small enough to
explore exhaustively at any size a human would author.

That is the point of externalising the draw into a rulebook. A memoryless
choice has nothing to verify; a bounded machine with resources has deadlocks,
unreachable terminals, decorative hats, and paths that skip the hat you most
wanted worn. Those are design bugs you cannot playtest your way to.

Twelve gates. See budget.py for why the budget enters through legality rather
than as a wall.

Usage:  python3 check_deck.py decks/diagnose.json
Exits 0 if every gate passes, 1 otherwise.
"""

import json
import sys
from collections import deque

import budget as B

FAILS = []


def fail(gate, msg):
    print(f"*** FAIL [{gate}] {msg}")
    FAILS.append(gate)


def ok(gate, msg):
    print(f"    ok  [{gate}] {msg}")


# ---------------------------------------------------------------- structural
def gate_schema(deck):
    arts = deck["artifacts"]
    bad = [c["id"] for c in deck["cards"] if c["produces"] not in arts]
    if bad:
        fail("schema", f"cards produce undeclared artifact types: {bad}")
        return
    for c in deck["cards"]:
        for r in c["requires"]:
            if r not in arts:
                fail("schema", f"card '{c['id']}' requires undeclared artifact '{r}'")
                return
    producers = {}
    for c in deck["cards"]:
        producers.setdefault(c["produces"], []).append(c["id"])
    dupes = {a: p for a, p in producers.items() if len(p) > 1}
    if dupes:
        fail("schema", f"artifact types with more than one producer: {dupes} "
                       f"-- the precedence graph assumes one")
        return
    ok("schema", f"{len(deck['cards'])} cards, {len(arts)} artifact types, "
                 f"one producer each")


def gate_exclusivity(deck):
    """Hat bleed made mechanical: GREEN shipping a `ranking` field means BLACK
    already ran, silently."""
    owner = {}
    clash = False
    for aname, spec in deck["artifacts"].items():
        for f in spec["fields"]:
            if f in owner:
                fail("exclusivity",
                     f"field '{f}' is claimed by both '{owner[f]}' and '{aname}' "
                     f"-- one hat is producing another hat's output")
                clash = True
            else:
                owner[f] = aname
    if not clash:
        ok("exclusivity", f"{len(owner)} fields, each owned by exactly one artifact")


def gate_instrument_grounding(deck):
    """Condition 3 from the design: an evaluative hat with no external
    instrument is introspection in costume. The deck names which roles must be
    grounded; this asserts they are, and that no card invents an unknown kind."""
    must = set(deck.get("instrumented_roles", []))
    kinds = set(deck.get("instrument_kinds", []))
    problems = []
    for c in deck["cards"]:
        inst = c.get("instrument")
        if c["role"] in must and inst is None:
            problems.append(f"card '{c['id']}' has role {c['role']}, which the deck "
                            f"requires to be grounded, but declares no instrument")
        if inst is not None and kinds and inst not in kinds:
            problems.append(f"card '{c['id']}' declares unknown instrument "
                            f"'{inst}' (known: {sorted(kinds)})")
    if not must:
        ok("instrument-grounding", "no roles declared as requiring an instrument")
        return
    if problems:
        for pr in problems:
            fail("instrument-grounding", pr)
    else:
        grounded = [c["id"] for c in deck["cards"] if c.get("instrument")]
        ok("instrument-grounding",
           f"roles {sorted(must)} are grounded; {len(grounded)} card(s) carry an "
           f"instrument: {grounded}")


def gate_weights(deck):
    """Weights bias selection; they must never silently remove a card.

    A zero or negative weight makes a card unreachable in practice while
    `reachable-cards` still passes -- it is legal, it is simply never drawn.
    That is the one way weights can lie, so it is gated."""
    problems = []
    for c in deck["cards"]:
        w = c.get("weight", 1.0)
        if not isinstance(w, (int, float)) or w <= 0:
            problems.append(f"card '{c['id']}' has weight {w!r}; a card with no "
                            f"positive weight is legal but never drawn")
        d = c.get("repeat_decay", deck.get("repeat_decay", 1.0))
        if not isinstance(d, (int, float)) or not (0 < d <= 1):
            problems.append(f"card '{c['id']}' has repeat_decay {d!r}; "
                            f"must be in (0, 1]")
    if problems:
        for pr in problems:
            fail("weights", pr)
    else:
        decay = deck.get("repeat_decay", 1.0)
        tuned = [c["id"] for c in deck["cards"] if c.get("weight", 1.0) != 1.0]
        ok("weights", f"all positive; repeat_decay {decay}"
                      + (f"; re-weighted cards: {tuned}" if tuned else
                         "; no per-card weights"))


def gate_acyclic(deck):
    producer = {c["produces"]: c["id"] for c in deck["cards"]}
    adj = {c["id"]: set() for c in deck["cards"]}
    for c in deck["cards"]:
        for r in c["requires"]:
            if r in producer:
                adj[producer[r]].add(c["id"])
    colour = {}

    def visit(n, stack):
        colour[n] = 1
        for m in adj[n]:
            if colour.get(m) == 1:
                fail("acyclic", f"precedence cycle: {' -> '.join(stack + [m])}")
                return True
            if colour.get(m, 0) == 0 and visit(m, stack + [m]):
                return True
        colour[n] = 2
        return False

    for n in adj:
        if colour.get(n, 0) == 0 and visit(n, [n]):
            return
    ok("acyclic", "precedence graph is a DAG")


# ---------------------------------------------------------------- budget
def gate_budget_feasible(deck):
    bud = deck.get("budget")
    floor = B.floor_cost(deck)
    if floor is B.INF:
        fail("budget-feasible", "no terminal state is reachable at any budget")
        return None
    if bud is None:
        fail("budget-feasible", f"deck declares no budget (floor is {floor})")
        return floor
    if bud < floor:
        fail("budget-feasible",
             f"budget {bud} is below the deck's floor of {floor} -- "
             f"no run can ever complete")
        return floor
    ok("budget-feasible", f"budget {bud} >= floor {floor} (slack {bud - floor})")
    return floor


def gate_budget_binding(deck):
    """A budget at or above the whole deck's cost constrains nothing."""
    bud = deck.get("budget")
    total = B.deck_total_cost(deck)
    if bud is None:
        return
    if bud >= total:
        fail("budget-binding",
             f"budget {bud} >= total deck cost {total} -- the budget is "
             f"decorative; every card can always be played")
    else:
        ok("budget-binding", f"budget {bud} < total deck cost {total} "
                             f"(the budget actually binds)")


# ---------------------------------------------------------------- state space
def gate_reachable_cards(deck, ids, edges):
    playable = set()
    for moves in edges.values():
        playable.update(moves)
    dead = [i for i in ids if i not in playable]
    if dead:
        fail("reachable-cards", f"cards that can never be played: {dead}")
    else:
        ok("reachable-cards", f"all {len(ids)} cards are legal in some reachable state")


def gate_no_deadlock(deck, ids, edges):
    """Under look-ahead legality this should be structurally impossible --
    which is exactly why it is worth asserting. It is the check on the RULE,
    not only on the deck."""
    stuck = []
    for st, moves in edges.items():
        played = dict(zip(ids, st))
        if not moves and not B.is_terminal(deck, played):
            stuck.append({i: n for i, n in played.items() if n})
    if stuck:
        fail("no-deadlock",
             f"{len(stuck)} reachable state(s) with no legal move and no terminal "
             f"card; e.g. after playing {stuck[0] or '{}'}")
    else:
        ok("no-deadlock", f"no dead ends across {len(edges)} reachable states")


def gate_terminal_live(deck, ids, edges):
    term = {st for st in edges if B.is_terminal(deck, dict(zip(ids, st)))}
    rev = {st: set() for st in edges}
    for st, moves in edges.items():
        for m in moves:
            j = ids.index(m)
            nxt = tuple(n + 1 if k == j else n for k, n in enumerate(st))
            if nxt in rev:
                rev[nxt].add(st)
    live = set(term)
    q = deque(term)
    while q:
        s = q.popleft()
        for p in rev.get(s, ()):
            if p not in live:
                live.add(p)
                q.append(p)
    dead = [st for st in edges if st not in live]
    if dead:
        example = {i: n for i, n in zip(ids, dead[0]) if n}
        fail("terminal-live",
             f"{len(dead)} reachable state(s) from which NO terminal is reachable; "
             f"e.g. after playing {example or '{}'}")
    else:
        ok("terminal-live", f"a terminal is reachable from all {len(edges)} states")


def gate_coverage(deck, ids, edges):
    """Is there a path to a terminal, under the rules actually in force, that
    omits a required role? If so the agent can finish without wearing it."""
    by_id = {c["id"]: c for c in deck["cards"]}
    required = set(deck.get("required_roles", []))
    if not required:
        ok("coverage", "no required roles declared")
        return
    skipped = []
    for role in required:
        start = tuple(0 for _ in ids)
        seen = {start}
        q = deque([start])
        found = False
        while q and not found:
            st = q.popleft()
            if B.is_terminal(deck, dict(zip(ids, st))):
                found = True
                break
            for m in edges.get(st, []):
                if by_id[m]["role"] == role:
                    continue
                j = ids.index(m)
                nxt = tuple(n + 1 if k == j else n for k, n in enumerate(st))
                if nxt not in seen:
                    seen.add(nxt)
                    q.append(nxt)
        if found:
            skipped.append(role)
    if skipped:
        fail("coverage",
             f"a terminal is reachable WITHOUT these required roles: "
             f"{sorted(skipped)} -- the deck permits finishing without them")
    else:
        ok("coverage", f"every path to a terminal wears all of {sorted(required)}")


def gate_no_orphans(deck):
    consumed = set()
    for c in deck["cards"]:
        consumed.update(c["requires"])
    orphans = [(c["id"], c["role"], c["produces"]) for c in deck["cards"]
               if not c.get("terminal") and c["produces"] not in consumed]
    if orphans:
        for cid, role, art in orphans:
            fail("no-orphans",
                 f"card '{cid}' ({role}) produces '{art}', which NO card requires "
                 f"-- the hat is decorative")
    else:
        ok("no-orphans", "every produced artifact is consumed or is the output")


# ---------------------------------------------------------------- main
def main(path):
    deck = json.load(open(path))
    print(f"=== role-deck checker: {deck['deck']} v{deck.get('version','?')} "
          f"({path}) ===\n")

    gate_schema(deck)
    gate_exclusivity(deck)
    gate_instrument_grounding(deck)
    gate_weights(deck)
    gate_acyclic(deck)
    if any(g in FAILS for g in ("schema", "acyclic")):
        print("\n*** structural gates failed; skipping budget and state-space gates")
        return 1 if FAILS else 0

    floor = gate_budget_feasible(deck)
    gate_budget_binding(deck)

    if "budget-feasible" in FAILS:
        print("\n*** budget is infeasible; skipping state-space gates")
        gate_no_orphans(deck)
    else:
        ids, seen, edges = B.explore(deck, lookahead=True)
        _, wall, _ = B.explore(deck, lookahead=False)
        pruned = len(wall) - len(seen)
        term = sum(1 for st in edges if B.is_terminal(deck, dict(zip(ids, st))))
        print(f"    --  {len(seen)} reachable states, {term} distinct complete runs")
        print(f"    --  look-ahead legality prunes {pruned} states a hard wall "
              f"would have allowed\n")
        gate_reachable_cards(deck, ids, edges)
        gate_no_deadlock(deck, ids, edges)
        gate_terminal_live(deck, ids, edges)
        gate_coverage(deck, ids, edges)
        gate_no_orphans(deck)

    print()
    if FAILS:
        print(f"*** {len(FAILS)} GATE FAILURE(S): {', '.join(sorted(set(FAILS)))}")
        return 1
    print("ALL DECK GATES PASSED")
    return 0


if __name__ == "__main__":
    sys.setrecursionlimit(10000)
    raise SystemExit(main(sys.argv[1] if len(sys.argv) > 1 else "decks/diagnose.json"))
