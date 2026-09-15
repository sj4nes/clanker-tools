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

Seventeen gates. See budget.py for why the budget enters through legality rather
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


def gate_min_items(deck):
    """A cardinality demanded in prose must be declared as a rule.

    The `hypothesize` card said "at least two competing explanations" and the
    runner accepted one; only an empty list was refused. Prose is not a gate.
    This asserts every declared `min_items` names a real field and is sane, and
    reports which cards actually carry one."""
    problems = []
    carried = []
    for aname, spec in deck["artifacts"].items():
        mi = spec.get("min_items", {})
        if not isinstance(mi, dict):
            problems.append(f"artifact '{aname}' min_items must be a map")
            continue
        for f, n in mi.items():
            if f not in spec["fields"]:
                problems.append(f"artifact '{aname}' min_items names '{f}', "
                                f"not one of its fields")
            elif not isinstance(n, int) or n < 2:
                problems.append(f"artifact '{aname}'.{f} min_items is {n!r}; "
                                f"a minimum below 2 constrains nothing that "
                                f"the empty-field check does not already")
            else:
                carried.append(f"{aname}.{f}>={n}")
    if problems:
        for pr in problems:
            fail("min-items", pr)
    else:
        ok("min-items", f"{len(carried)} cardinality rule(s): {carried}"
                        if carried else "none declared")


def gate_exclusivity(deck):
    """Hat bleed made mechanical: GREEN shipping a `ranking` field means BLACK
    already ran, silently."""
    # An INDEX field is legitimately shared: `option` on both `support` and
    # `faults` is the same coordinate on two artifacts, not one hat producing
    # another's output. The exemption is narrow on purpose -- it covers exactly
    # the field the deck declares as its option index, on artifacts whose
    # producer is per_option, and nothing else.
    src = B.option_source(deck)
    idx = src.get("index_field") if src else None
    per_option_arts = {c["produces"] for c in deck["cards"] if c.get("per_option")}
    owner = {}
    clash = False
    # The exemption REMOVES the legitimate claims, so an illegitimate one would
    # sit unopposed and collide with nothing. So the index field is also
    # forbidden outright anywhere else -- without this, adding `option` to
    # `evidence` passed cleanly.
    if idx:
        stray = sorted(a for a, sp in deck["artifacts"].items()
                       if idx in sp["fields"] and a not in per_option_arts)
        if stray:
            fail("exclusivity",
                 f"index field '{idx}' appears on {stray}, which no per-option "
                 f"card produces -- the index is only meaningful per option")
            clash = True
    for aname, spec in deck["artifacts"].items():
        for f in spec["fields"]:
            if idx and f == idx and aname in per_option_arts:
                continue
            if f in owner:
                fail("exclusivity",
                     f"field '{f}' is claimed by both '{owner[f]}' and '{aname}' "
                     f"-- one hat is producing another hat's output")
                clash = True
            else:
                owner[f] = aname
    if not clash:
        note = f" (+ index field '{idx}' shared by {sorted(per_option_arts)})" if idx else ""
        ok("exclusivity",
           f"{len(owner)} fields, each owned by exactly one artifact{note}")


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


def gate_unlocks(deck):
    """A resource unlock must be well formed, must BITE, and must OPEN.

    Same spirit as `conditions` and `no-orphans`: an unlock that never blocks
    anything reads as a constraint while permitting everything, and one that
    never opens makes its card unplayable. Both are checked over the reachable
    state space rather than argued about."""
    carded = [c for c in deck["cards"] if c.get("unlock")]
    if not carded:
        ok("unlocks", "none declared")
        return
    problems = []
    for c in carded:
        u = c["unlock"]
        for k in u:
            if k not in B.UNLOCK_KEYS:
                problems.append(f"card '{c['id']}' declares unknown unlock key "
                                f"'{k}' (known: {list(B.UNLOCK_KEYS)})")
        for k in ("plays_at_least", "spent_at_least", "remaining_at_most"):
            if k in u and (not isinstance(u[k], int) or u[k] < 0):
                problems.append(f"card '{c['id']}' unlock {k}={u[k]!r}; "
                                f"needs a non-negative integer")
        if "remaining_at_most" in u and deck.get("budget") is None:
            problems.append(f"card '{c['id']}' unlocks on remaining budget, "
                            f"but the deck declares no budget")
        pa = u.get("played_at_least")
        if pa is not None:
            for req in (pa if isinstance(pa, list) else [pa]):
                if not isinstance(req, dict) or "card" not in req or "n" not in req:
                    problems.append(f"card '{c['id']}' played_at_least needs "
                                    f"{{card, n}} or a list of them")
                elif req["card"] not in {x["id"] for x in deck["cards"]}:
                    problems.append(f"card '{c['id']}' unlocks on unknown card "
                                    f"'{req['card']}'")
    if problems:
        for pr in problems:
            fail("unlocks", pr)
        return

    ids = [c["id"] for c in deck["cards"]]
    _, seen, _ = B.explore(deck)
    bites = {c["id"]: False for c in carded}
    opens = {c["id"]: False for c in carded}
    for st in seen:
        counts = dict(zip(ids, st[0] if isinstance(st[0], tuple) else st))
        have = B.artifacts_of(deck, counts)
        for c in carded:
            if counts.get(c["id"], 0) >= c["copies"]:
                continue
            # would this card be legal but for the unlock?
            if not all(r in have for r in c["requires"]):
                continue
            if B.unlock_open(deck, c, counts):
                opens[c["id"]] = True
            else:
                bites[c["id"]] = True
    for c in carded:
        if not bites[c["id"]]:
            fail("unlocks", f"card '{c['id']}' has an unlock that never blocks it "
                            f"in any reachable state -- it is decorative")
        elif not opens[c["id"]]:
            fail("unlocks", f"card '{c['id']}' has an unlock that never opens "
                            f"in any reachable state -- the card is unplayable")
    if all(bites.values()) and all(opens.values()):
        desc = ", ".join(f"{c['id']}:{sorted(c['unlock'])}" for c in carded)
        ok("unlocks", f"{len(carded)} resource unlock(s), each both blocks and "
                      f"opens somewhere ({desc})")


def gate_options(deck):
    """A per-option deck must be well formed at every option count it allows.

    `option_source` names the field whose length sets how many copies a
    per-option card gets. The bound is what keeps this checkable: the deck is
    expanded once per count and every gate runs on each expansion."""
    src = B.option_source(deck)
    per = [c["id"] for c in deck["cards"] if c.get("per_option")]
    alls = {r for c in deck["cards"] for r in c.get("requires_all", [])}
    if not src:
        if per or alls:
            fail("options", f"cards use per_option/requires_all but the deck "
                            f"declares no option_source")
        else:
            ok("options", "no per-option cards")
        return
    art = deck["artifacts"].get(src["artifact"])
    if art is None or src["field"] not in art.get("fields", []):
        fail("options", f"option_source names {src['artifact']}.{src['field']}, "
                        f"which is not a declared field")
        return
    if not isinstance(src.get("max"), int) or src["max"] < 1:
        fail("options", f"option_source needs an integer max >= 1 to stay checkable")
        return
    if not per:
        fail("options", "an option_source is declared but no card is per_option")
        return
    producer = {c["produces"]: c["id"] for c in deck["cards"]}
    for r in alls:
        if r not in producer:
            fail("options", f"requires_all names '{r}', which no card produces")
            return
        if not {c["id"] for c in deck["cards"]
                if c["produces"] == r and c.get("per_option")}:
            fail("options", f"requires_all names '{r}', but its producer "
                            f"'{producer[r]}' is not per_option -- 'once per "
                            f"option' is meaningless for a fixed-count card")
            return
    idx = src.get("index_field")
    if not idx:
        fail("options", "option_source needs an index_field: each per-option "
                        "artifact must name which option it addresses, and that "
                        "is what makes distinctness -- and therefore counting -- "
                        "possible")
        return
    for cid in per:
        art_name = {c["id"]: c["produces"] for c in deck["cards"]}[cid]
        if idx not in deck["artifacts"][art_name]["fields"]:
            fail("options", f"per-option card '{cid}' produces '{art_name}', which "
                            f"does not declare the index field '{idx}'")
            return
    ok("options", f"option_source {src['artifact']}.{src['field']} (max "
                  f"{src['max']}); index '{idx}'; per-option cards {per}; "
                  f"requires_all {sorted(alls)}")


def gate_conditions(deck):
    """A declared condition must actually change something, and must be
    declarable.

    Same spirit as `no-orphans`: a conditional requirement that never alters
    the legal set is decorative, and worse than decorative -- it reads as a
    safeguard while permitting everything. So this asserts the flag makes a
    difference in some reachable state, and that the field it keys on is both
    declared and nullable (a field that can never be null is not a condition,
    it is a requirement)."""
    conds = B.conditions(deck)
    if not conds:
        ok("conditions", "none declared")
        return
    problems = []
    for cond in conds:
        art = deck["artifacts"].get(cond["artifact"])
        if art is None:
            problems.append(f"condition '{cond['id']}' keys on undeclared "
                            f"artifact '{cond['artifact']}'")
            continue
        if cond["field"] not in art["fields"]:
            problems.append(f"condition '{cond['id']}' keys on field "
                            f"'{cond['field']}', not a field of '{cond['artifact']}'")
        if cond["field"] not in art.get("nullable", []):
            problems.append(f"condition '{cond['id']}' keys on '{cond['field']}', "
                            f"which is not nullable -- a field that can never be "
                            f"null is a requirement, not a condition")
        add = cond["adds_requirement"]
        if add["card"] not in {c["id"] for c in deck["cards"]}:
            problems.append(f"condition '{cond['id']}' adds a requirement to "
                            f"unknown card '{add['card']}'")
        if add["artifact"] not in deck["artifacts"]:
            problems.append(f"condition '{cond['id']}' requires undeclared "
                            f"artifact '{add['artifact']}'")
    if problems:
        for pr in problems:
            fail("conditions", pr)
        return

    # does each condition bite? find a state where the flag changes legality
    ids = [c["id"] for c in deck["cards"]]
    _, seen, _ = B.explore(deck)
    bites = {c["id"]: False for c in conds}
    for counts, flags in seen:
        pl = dict(zip(ids, counts))
        for i, cond in enumerate(conds):
            on = tuple(True if k == i else v for k, v in enumerate(flags))
            off = tuple(False if k == i else v for k, v in enumerate(flags))
            if set(B.raw_moves(deck, pl, on)) != set(B.raw_moves(deck, pl, off)):
                bites[cond["id"]] = True
    dead = [k for k, v in bites.items() if not v]
    if dead:
        for k in dead:
            fail("conditions", f"condition '{k}' never changes what is legal "
                              f"in any reachable state -- it is decorative")
    else:
        ok("conditions", f"{len(conds)} condition(s), each alters legality "
                         f"in some reachable state")


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
def succ(deck, ids, st, m):
    """Successor states of (counts, flags) after playing m -- plural, because a
    play that can trigger a condition branches into both outcomes."""
    counts, flags = st
    j = ids.index(m)
    nc = tuple(n + 1 if k == j else n for k, n in enumerate(counts))
    return [(nc, nf) for nf in B.branch(deck, dict(zip(ids, nc)), flags, m)]


def counts_of(st):
    return st[0]



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
        played = dict(zip(ids, counts_of(st)))
        if not moves and not B.is_terminal(deck, played):
            stuck.append({i: n for i, n in played.items() if n})
    if stuck:
        fail("no-deadlock",
             f"{len(stuck)} reachable state(s) with no legal move and no terminal "
             f"card; e.g. after playing {stuck[0] or '{}'}")
    else:
        ok("no-deadlock", f"no dead ends across {len(edges)} reachable states")


def gate_terminal_live(deck, ids, edges):
    term = {st for st in edges if B.is_terminal(deck, dict(zip(ids, counts_of(st))))}
    rev = {st: set() for st in edges}
    for st, moves in edges.items():
        for m in moves:
            for nxt in succ(deck, ids, st, m):
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
        example = {i: n for i, n in zip(ids, counts_of(dead[0])) if n}
        fail("terminal-live",
             f"{len(dead)} reachable state(s) from which NO terminal is reachable; "
             f"e.g. after playing {example or '{}'}")
    else:
        ok("terminal-live", f"a terminal is reachable from all {len(edges)} states")


def gate_coverage(deck, ids, edges):
    """Can a terminal be reached without wearing a role it requires?

    `required_roles` is either a LIST (one requirement for every exit) or a
    MAP from terminal card id to its own list. The map form exists because the
    decide deck forced it: with three exits you cannot commit without wearing
    BLACK, but you can legitimately drop a decision without ever running a
    probe. A single global requirement makes every exit as heavy as the
    heaviest, which is how a `defer` card ends up demanding an experiment.
    """
    by_id = {c["id"]: c for c in deck["cards"]}
    spec = deck.get("required_roles")
    terminals = [c["id"] for c in deck["cards"] if c.get("terminal")]
    if not spec:
        ok("coverage", "no required roles declared")
        return
    if isinstance(spec, list):
        per_terminal = {t: list(spec) for t in terminals}
    else:
        per_terminal = {t: list(spec.get(t, [])) for t in terminals}
        unknown = set(spec) - set(terminals)
        if unknown:
            fail("coverage", f"required_roles names non-terminal card(s): "
                             f"{sorted(unknown)}")
            return

    problems = []
    for t, roles in sorted(per_terminal.items()):
        for role in sorted(roles):
            if by_id[t]["role"] == role:
                continue                      # the exit itself wears it
            # can we make `t` legal using only cards of other roles?
            start = (tuple(0 for _ in ids), B.no_flags(deck))
            seen = {start}
            q = deque([start])
            escaped = False
            while q and not escaped:
                st = q.popleft()
                if B.is_terminal(deck, dict(zip(ids, counts_of(st)))):
                    continue
                for m in edges.get(st, []):
                    if m == t:
                        escaped = True
                        break
                    if by_id[m]["role"] == role:
                        continue
                    for nxt in succ(deck, ids, st, m):
                        if nxt not in seen:
                            seen.add(nxt)
                            q.append(nxt)
            if escaped:
                problems.append((t, role))
    if problems:
        for t, role in problems:
            fail("coverage", f"'{t}' is reachable without ever wearing {role} "
                             f"-- the deck permits that exit without it")
    else:
        summary = ", ".join(f"{t}:{len(r)}" for t, r in sorted(per_terminal.items()))
        ok("coverage", f"every exit wears its required roles ({summary})")


def gate_work_floor(deck, ids, edges):
    """The LEAST work a complete run can do while breaking no other gate.

    Every other gate is a safety property -- does anything bad happen on any
    path. This is an extremal query over paths, and it catches a defect class
    none of them can see: a deck that is perfectly well formed and satisfiable
    by doing almost nothing. `invent` v0.1.0 passed all fourteen other gates
    and the simulator, and its laziest legal run padded six `generate` plays to
    reach an exhaustion unlock and ran ONE trial.

    `coverage` is already the n=1 case of this (min_plays(role) >= 1). A deck
    declares `minimum_work` as {card: n}, or as a map from exit id to its own
    {card: n} -- a `defer` owes less than a `commit`, so a single global floor
    can only express what is true of the laziest exit.
    """
    spec = deck.get("minimum_work")
    terminals = [c["id"] for c in deck["cards"] if c.get("terminal")]
    per_exit = {}
    if isinstance(spec, dict) and spec and all(k in terminals for k in spec):
        per_exit = {k: v for k, v in spec.items()}
    elif spec:
        per_exit = {None: spec}

    # always report the table -- it is information whether or not it fails
    lo, hi, wit = B.min_max_plays(deck, ids, edges)
    skippable = [c["id"] for c in deck["cards"]
                 if not c.get("terminal") and lo.get(c["id"]) == 0]
    rng = ", ".join(f"{c['id']} {lo[c['id']]}..{hi[c['id']]}"
                    for c in deck["cards"] if not c.get("terminal"))
    print(f"    --  plays per complete run (min..max): {rng}")
    if skippable:
        print(f"    --  skippable entirely: {skippable}")

    if not per_exit:
        ok("work-floor", "no minimum_work declared -- the min..max line above "
                         "is the laziest run this deck permits")
        return

    bad = False
    for exit_id, want in sorted(per_exit.items(), key=lambda kv: kv[0] or ""):
        elo, _, ewit = (lo, hi, wit) if exit_id is None else \
            B.min_max_plays(deck, ids, edges, exit_id=exit_id)
        for cid, n in sorted(want.items()):
            if cid not in {c["id"] for c in deck["cards"]}:
                fail("work-floor", f"minimum_work names unknown card '{cid}'")
                bad = True
                continue
            got = elo.get(cid, B.INF)
            if got is B.INF:
                fail("work-floor", f"exit '{exit_id}' is unreachable, so its "
                                   f"work floor is vacuous")
                bad = True
            elif got < n:
                where = f"a run ending at '{exit_id}'" if exit_id else "a run"
                fail("work-floor",
                     f"{where} can play '{cid}' only {got}x, floor is {n}x")
                print(f"        laziest witness: {' '.join(ewit.get(cid, ()))}")
                bad = True
    if not bad:
        desc = "; ".join(f"{k or 'every exit'}: {dict(sorted(v.items()))}"
                         for k, v in sorted(per_exit.items(), key=lambda kv: kv[0] or ""))
        ok("work-floor", f"every complete run meets its work floor ({desc})")


def gate_no_orphans(deck):
    consumed = set()
    for c in deck["cards"]:
        consumed.update(c["requires"])
        consumed.update(c.get("requires_all", []))
    # An artifact required only when a condition fires is still consumed --
    # `probe_result` is not decorative just because the probe is optional.
    for cond in B.conditions(deck):
        consumed.add(cond["adds_requirement"]["artifact"])
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
    gate_min_items(deck)
    gate_exclusivity(deck)
    gate_instrument_grounding(deck)
    gate_weights(deck)
    gate_unlocks(deck)
    gate_options(deck)
    gate_conditions(deck)
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
        counts_to_check = (range(1, B.max_options(deck) + 1)
                           if B.option_source(deck) else [1])
        worst = max(counts_to_check)
        if B.option_source(deck):
            print(f"    --  option counts to verify: "
                  f"{list(counts_to_check)}; full detail at n={worst}")
        deck = B.expand(deck, worst) if B.option_source(deck) else deck
        ids, seen, edges = B.explore(deck, lookahead=True)
        _, wall, _ = B.explore(deck, lookahead=False)
        pruned = len(wall) - len(seen)
        term = sum(1 for st in edges
                   if B.is_terminal(deck, dict(zip(ids, counts_of(st)))))
        print(f"    --  {len(seen)} reachable states, {term} distinct complete runs")
        print(f"    --  look-ahead legality prunes {pruned} states a hard wall "
              f"would have allowed\n")
        gate_reachable_cards(deck, ids, edges)
        gate_no_deadlock(deck, ids, edges)
        gate_terminal_live(deck, ids, edges)
        gate_coverage(deck, ids, edges)
        gate_work_floor(deck, ids, edges)
        gate_no_orphans(deck)

        # every other option count must pass the state-space gates too
        if B.option_source(deck) and len(list(counts_to_check)) > 1:
            before = len(FAILS)
            quiet = []
            import contextlib, io
            for n in counts_to_check:
                if n == worst:
                    continue
                dn = B.expand(deck, n)
                idn, seenn, edgn = B.explore(dn, lookahead=True)
                mark = len(FAILS)
                buf = io.StringIO()
                with contextlib.redirect_stdout(buf):
                    gate_reachable_cards(dn, idn, edgn)
                    gate_no_deadlock(dn, idn, edgn)
                    gate_terminal_live(dn, idn, edgn)
                    gate_coverage(dn, idn, edgn)
                if len(FAILS) > mark:        # only a failing count gets detail
                    print(f"    -- at n={n}:")
                    for line in buf.getvalue().splitlines():
                        if line.startswith("***"):
                            print(f"  {line}")
                quiet.append((n, len(seenn), len(FAILS) - mark))
            # collapse the per-n chatter into one line
            print(f"    --  option-count sweep: " +
                  ", ".join(f"n={n}:{st} states"
                            + (f" ({f} FAIL)" if f else "") for n, st, f in quiet))
            if len(FAILS) == before:
                ok("options-sweep", "every option count passes the state-space gates")

    print()
    if FAILS:
        print(f"*** {len(FAILS)} GATE FAILURE(S): {', '.join(sorted(set(FAILS)))}")
        return 1
    print("ALL DECK GATES PASSED")
    return 0


if __name__ == "__main__":
    sys.setrecursionlimit(10000)
    raise SystemExit(main(sys.argv[1] if len(sys.argv) > 1 else "decks/diagnose.json"))
