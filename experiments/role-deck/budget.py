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


def raw_moves(deck, played):
    """Legal ignoring budget entirely: a copy remains and requirements are met."""
    have = artifacts_of(deck, played)
    return [c["id"] for c in deck["cards"]
            if played.get(c["id"], 0) < c["copies"]
            and all(r in have for r in c["requires"])]


INF = float("inf")


def min_cost_to_terminal(deck, played, _memo=None):
    """Cheapest additional cost to reach a terminal state, ignoring budget.
    INF when no terminal is reachable at all."""
    if _memo is None:
        _memo = {}
    ids = [c["id"] for c in deck["cards"]]
    by = {c["id"]: c for c in deck["cards"]}

    def go(state, path):
        if is_terminal(deck, dict(zip(ids, state))):
            return 0
        if state in _memo:
            return _memo[state]
        if state in path:                 # guard: artifacts are monotone so
            return INF                    # a revisit cannot help
        path = path | {state}
        best = INF
        pl = dict(zip(ids, state))
        for m in raw_moves(deck, pl):
            j = ids.index(m)
            nxt = tuple(n + 1 if k == j else n for k, n in enumerate(state))
            sub = go(nxt, path)
            if sub is not INF:
                best = min(best, cost_of(by[m]) + sub)
        _memo[state] = best
        return best

    start = tuple(played.get(i, 0) for i in ids)
    return go(start, frozenset())


def legal_moves(deck, played, lookahead=True):
    """Budget-aware legality.

    With `lookahead`, a move is offered only if a terminal remains reachable
    within the remaining budget afterwards -- so the rulebook never hands the
    die a move that strands the run.
    """
    budget = deck.get("budget")
    ids = [c["id"] for c in deck["cards"]]
    by = {c["id"]: c for c in deck["cards"]}
    out = []
    for m in raw_moves(deck, played):
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
        tail = min_cost_to_terminal(deck, nxt_played)
        if tail is not INF and after_spent + tail <= budget:
            out.append(m)
    return out


def explore(deck, lookahead=True):
    """BFS the reachable state space under the budget rule in force."""
    from collections import deque
    ids = [c["id"] for c in deck["cards"]]
    start = tuple(0 for _ in ids)
    seen = {start}
    edges = {}
    q = deque([start])
    while q:
        st = q.popleft()
        played = dict(zip(ids, st))
        if is_terminal(deck, played):
            edges[st] = []
            continue
        moves = legal_moves(deck, played, lookahead=lookahead)
        edges[st] = moves
        for m in moves:
            j = ids.index(m)
            nxt = tuple(n + 1 if k == j else n for k, n in enumerate(st))
            if nxt not in seen:
                seen.add(nxt)
                q.append(nxt)
    return ids, seen, edges


def floor_cost(deck):
    """Cheapest complete run: the deck's hard floor on process overhead."""
    return min_cost_to_terminal(deck, {})
