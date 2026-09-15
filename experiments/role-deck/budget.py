"""Budget model for a role deck.

A deck declares a global `budget`; each card declares a `cost` (default 1).
Per-card `copies` already bound how often a single hat may be worn -- that is
the "wear Blue at most 3 times" rule. The budget bounds the WHOLE process, and
is what stops a run from turning into planning-for-planning.

The naive reading -- "a move is legal while spent + cost <= budget" -- does not
work, and the checker is what established that. Under a hard wall the agent can
spend early on optional cards and then be unable to afford the mandatory tail.
For the diagnose deck the only strand-free wall is 12, the entire deck:

    budget   6    7    8    9   10   11   12
    strands  9   12   14   11    5    1    0

That matters more here than it would in a game a human plays, because the draw
is EXTERNAL. A human who strands themselves made a mistake; an agent handed a
stranding move by a die was given an illegal position by the rulebook.

So budget enters through LEGALITY instead:

    a move is legal only if, after playing it, a terminal state is still
    reachable within the remaining budget.

You cannot bankrupt yourself. The budget still binds -- it prunes the branches
that would waste the tail -- but no reachable state is ever a dead end. That is
a safety property of the rulebook, and it is computable because the state space
is small.

Because cost is a function of the card, `spent` is determined by the multiset
of cards played. Adding a budget therefore CONSTRAINS the reachable set rather
than adding a dimension to it: no state-space blow-up.
"""


# ---------------------------------------------------------------- conditions
#
# A conditional requirement makes a card's preconditions depend on WHAT AN
# EARLIER ARTIFACT SAID, not on which cards were played. That is outside the
# state model -- legality would depend on prose -- so two things make it
# checkable:
#
#   1. The condition is a DECLARED, TYPED FIELD. The agent writes
#      `disputed_fact` or leaves it null; deterministic code enforces the
#      consequence. The agent can still lie to skip the probe, but that is now
#      an explicit, logged, auditable claim rather than a silent omission.
#      (The agent-automation split again: the model proposes, code enforces.)
#
#   2. The state space BRANCHES on it. State becomes (counts, flags), and
#      every gate is checked on both branches -- the deck must be sound whether
#      or not the condition fires. Flags latch: once a disputed fact is raised
#      it stays raised, so the space is counts x 2^k, bounded.
#
# The look-ahead is PESSIMISTIC: it assumes every condition that can still fire
# does. Otherwise an agent could be stranded by its own honest declaration,
# which is the finding-12 problem wearing a different hat.


# ---------------------------------------------------------------- options
#
# "Steelman and attack each option at matched depth" is a symmetry constraint
# over a list whose length is not known until the run starts. Two things make
# it expressible without losing static checking:
#
#   1. OPTIONS ARE SYMMETRIC to the deck. It does not care WHICH option a
#      steelman addresses, only that every option got one. So if the runner
#      enforces that each per-option play names a DISTINCT option, the static
#      model needs only COUNTS: "all options covered" reduces to
#      "count(producer) >= n_options". Distinctness at runtime is what buys
#      countability at check time.
#
#   2. THE LIST IS BOUNDED. The deck declares a maximum, and the checker
#      expands it once per possible option count and runs every gate on each.
#      Same trick as branching on a condition: enumerate the parameter rather
#      than model it.
#
# `requires_all` is then a threshold on a count, and matched depth is
# `commit` requiring ALL of both `support` and `faults`.


def option_source(deck):
    return deck.get("option_source")


def max_options(deck):
    src = option_source(deck)
    return src["max"] if src else 1


def n_options(deck):
    """Option count this deck instance is expanded for."""
    return deck.get("_n_options", 1)


def expand(deck, n):
    """A concrete deck for exactly n options: per-option cards get n copies."""
    import copy as _copy
    d = _copy.deepcopy(deck)
    d.pop("_memo", None)
    d["_n_options"] = n
    for c in d["cards"]:
        if c.get("per_option"):
            c["copies"] = n
    return d


def conditions(deck):
    return deck.get("conditions", [])


def no_flags(deck):
    return tuple(False for _ in conditions(deck))


def effective_requires(deck, card_id, flags):
    by = {c["id"]: c for c in deck["cards"]}
    req = list(by[card_id]["requires"])
    for i, cond in enumerate(conditions(deck)):
        add = cond["adds_requirement"]
        if flags[i] and add["card"] == card_id and add["artifact"] not in req:
            req.append(add["artifact"])
    return req


def settable(deck, counts, i):
    """Can condition i still become true? Only if its triggering artifact can
    still be produced."""
    cond = conditions(deck)[i]
    for c in deck["cards"]:
        if c["produces"] == cond["artifact"] and counts.get(c["id"], 0) < c["copies"]:
            return True
    return False


def worst_flags(deck, counts, flags):
    """Every condition that is true, or could still become true."""
    return tuple(f or settable(deck, counts, i) for i, f in enumerate(flags))


def branch(deck, counts, flags, card_id):
    """Flag states reachable by playing `card_id`. Two branches for each
    still-open condition this card's artifact can trigger."""
    by = {c["id"]: c for c in deck["cards"]}
    produced = by[card_id]["produces"]
    out = [flags]
    for i, cond in enumerate(conditions(deck)):
        if cond["artifact"] == produced and not flags[i]:
            out = [f for g in out
                   for f in (g, tuple(True if k == i else v
                                      for k, v in enumerate(g)))]
    return out


def cost_of(card):
    return card.get("cost", 1)


def weight_of(deck, card_id, counts):
    """How attractive this card is to the die RIGHT NOW.

    Two separate things, deliberately not conflated:

      `copies`  -- how many times a hat MAY be worn. A resource limit.
      `weight`  -- how likely it is to be drawn when it is legal. A bias.

    A flat weight cannot tell a card's first play from its third -- it is the
    same card. So the weight decays per prior play:

        effective = weight * repeat_decay ** (times already played)

    That is the lever finding 8 named. A uniform draw plays an optional card
    whenever it is legal, so budget slack is always spent; a decay under 1
    makes the second `gather` genuinely optional instead of merely permitted.
    Decay 1.0 (the default) reproduces the uniform draw exactly.

    Weights never affect LEGALITY, only selection -- so the reachable state
    space, the budget look-ahead, and every gate in check_deck.py are unchanged
    by them.
    """
    by = {c["id"]: c for c in deck["cards"]}
    card = by[card_id]
    w = card.get("weight", 1.0)
    decay = card.get("repeat_decay", deck.get("repeat_decay", 1.0))
    return w * (decay ** counts.get(card_id, 0))


def weights_for(deck, counts, legal):
    """Effective weights for the legal moves, in the order given."""
    return [weight_of(deck, c, counts) for c in legal]


def deck_total_cost(deck):
    return sum(cost_of(c) * c["copies"] for c in deck["cards"])


def spent(deck, played):
    by = {c["id"]: c for c in deck["cards"]}
    return sum(cost_of(by[cid]) * n for cid, n in played.items())


def artifacts_of(deck, played):
    by = {c["id"]: c for c in deck["cards"]}
    return {by[cid]["produces"] for cid, n in played.items() if n}


def is_terminal(deck, played):
    by = {c["id"]: c for c in deck["cards"]}
    return any(by[cid].get("terminal") and n for cid, n in played.items())


def raw_moves(deck, played, flags=None):
    """Legal ignoring budget entirely: a copy remains and requirements are met."""
    if flags is None:
        flags = no_flags(deck)
    have = artifacts_of(deck, played)
    n = n_options(deck)
    producer = {c["produces"]: c["id"] for c in deck["cards"]}
    out = []
    for c in deck["cards"]:
        if played.get(c["id"], 0) >= c["copies"]:
            continue
        if not all(r in have for r in effective_requires(deck, c["id"], flags)):
            continue
        # `requires_all`: that artifact must exist ONCE PER OPTION. Because the
        # runner forces distinct options, the count is the coverage.
        if any(played.get(producer.get(r, ""), 0) < n
               for r in c.get("requires_all", [])):
            continue
        out.append(c["id"])
    return out


INF = float("inf")


def min_cost_to_terminal(deck, played, flags=None, _memo=None):
    """Cheapest additional cost to reach a terminal state, ignoring budget,
    assuming the worst case for every condition still open.
    INF when no terminal is reachable at all."""
    if flags is None:
        flags = no_flags(deck)
    wf = worst_flags(deck, played, flags)
    if _memo is None:
        _memo = _cache(deck, f"terminal:{wf}")
    ids = [c["id"] for c in deck["cards"]]
    by = {c["id"]: c for c in deck["cards"]}

    def go(state):
        if is_terminal(deck, dict(zip(ids, state))):
            return 0
        if state in _memo:
            return _memo[state]
        _memo[state] = INF                # artifacts are monotone: no revisit helps
        best = INF
        pl = dict(zip(ids, state))
        for m in raw_moves(deck, pl, wf):
            j = ids.index(m)
            nxt = tuple(n + 1 if k == j else n for k, n in enumerate(state))
            sub = go(nxt)
            if sub is not INF:
                best = min(best, cost_of(by[m]) + sub)
        _memo[state] = best
        return best

    start = tuple(played.get(i, 0) for i in ids)
    return go(start)


def _cache(deck, name):
    """Per-deck memo, attached to the loaded dict.

    Safe because nothing serialises a deck after calling into this module --
    check_deck, simulate and run_deck all load decks read-only. Without it
    `min_cost_to_exit` rebuilt its table on every candidate move and the suite
    took 71s; with it, 8s.
    """
    return deck.setdefault("_memo", {}).setdefault(name, {})


def min_cost_to_exit(deck, played, exit_id, flags=None):
    """Cheapest additional cost to reach a terminal state VIA a named exit,
    assuming the worst case for every condition still open."""
    ids = [c["id"] for c in deck["cards"]]
    by = {c["id"]: c for c in deck["cards"]}
    if flags is None:
        flags = no_flags(deck)
    wf = worst_flags(deck, played, flags)
    memo = _cache(deck, f"exit:{exit_id}:{wf}")

    def go(state):
        pl = dict(zip(ids, state))
        if is_terminal(deck, pl):
            return 0 if pl.get(exit_id) else INF
        if state in memo:
            return memo[state]
        memo[state] = INF                    # artifacts are monotone: no revisit helps
        best = INF
        for m in raw_moves(deck, pl, wf):
            j = ids.index(m)
            nxt = tuple(n + 1 if k == j else n for k, n in enumerate(state))
            sub = go(nxt)
            if sub is not INF:
                best = min(best, cost_of(by[m]) + sub)
        memo[state] = best
        return best

    return go(tuple(played.get(i, 0) for i in ids))


def legal_moves(deck, played, lookahead=True, flags=None):
    """Budget-aware legality.

    With `lookahead`, a move is offered only if a terminal remains reachable
    within the remaining budget afterwards -- so the rulebook never hands the
    die a move that strands the run.
    """
    if flags is None:
        flags = no_flags(deck)
    budget = deck.get("budget")
    ids = [c["id"] for c in deck["cards"]]
    by = {c["id"]: c for c in deck["cards"]}
    out = []
    for m in raw_moves(deck, played, flags):
        if budget is None:
            out.append(m)
            continue
        after_spent = spent(deck, played) + cost_of(by[m])
        if after_spent > budget:
            continue
        if not lookahead:
            out.append(m)
            continue
        j = ids.index(m)
        state = tuple(played.get(i, 0) for i in ids)
        nxt = tuple(n + 1 if k == j else n for k, n in enumerate(state))
        nxt_played = dict(zip(ids, nxt))
        if is_terminal(deck, nxt_played):
            out.append(m)
            continue
        tail = min_cost_to_terminal(deck, nxt_played, flags)
        if tail is INF or after_spent + tail > budget:
            continue
        out.append(m)

    # A deck may name ONE exit whose affordability must be preserved. Without
    # it the look-ahead only promises that SOME exit remains reachable, so a
    # run can wander until the strongest exit is priced out -- which is how
    # the decide deck spent itself out of `commit`.
    #
    # But preservation must YIELD rather than strand. Enforcing it strictly
    # deadlocked decide v0.5.0: it pruned `alternatives` because commit would
    # no longer be affordable afterwards, and every exit requires `alternative`,
    # so nothing at all was legal. A preference that can produce a dead end is
    # not a preference, it is a bug.
    keep = deck.get("preserve_exit")
    if keep:
        kept = []
        for m in out:
            if by[m].get("terminal"):
                kept.append(m)
                continue
            nxt_played = dict(played)
            nxt_played[m] = nxt_played.get(m, 0) + 1
            need = min_cost_to_exit(deck, nxt_played, keep, flags)
            if need is not INF and spent(deck, played) + cost_of(by[m]) + need <= budget:
                kept.append(m)
        if kept:
            return kept
    return out


def explore(deck, lookahead=True):
    """BFS the reachable state space. A state is (counts, flags): a play that
    can trigger a condition branches into both outcomes, so every gate sees
    the deck with the condition fired and not fired."""
    from collections import deque
    ids = [c["id"] for c in deck["cards"]]
    start = (tuple(0 for _ in ids), no_flags(deck))
    seen = {start}
    edges = {}
    q = deque([start])
    while q:
        st = q.popleft()
        counts, flags = st
        played = dict(zip(ids, counts))
        if is_terminal(deck, played):
            edges[st] = []
            continue
        moves = legal_moves(deck, played, lookahead=lookahead, flags=flags)
        edges[st] = moves
        for m in moves:
            j = ids.index(m)
            nc = tuple(n + 1 if k == j else n for k, n in enumerate(counts))
            for nf in branch(deck, dict(zip(ids, nc)), flags, m):
                nxt = (nc, nf)
                if nxt not in seen:
                    seen.add(nxt)
                    q.append(nxt)
    return ids, seen, edges


def floor_cost(deck):
    """Cheapest complete run: the deck's hard floor on process overhead."""
    return min_cost_to_terminal(deck, {})
