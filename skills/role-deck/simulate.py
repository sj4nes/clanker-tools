#!/usr/bin/env python3
"""What a deck actually generates, as opposed to what its author intended.

The gates in check_deck.py say what is POSSIBLE. They say nothing about how
often. A deck is a generative object, and designers are reliably wrong about
what their generative objects generate -- you intend "BLACK lands after the
second GREEN" and it does, 62% of the time.

This does not sample. It computes every figure EXACTLY by dynamic programming
over the reachable state space, and Monte Carlo runs only as an independent
cross-check through run_deck.draw -- the real hash-based die -- so the
comparison also tests whether that die honours the deck's declared weights
rather than merely being deterministic.

The first version enumerated complete paths instead, which was exact but the
wrong algorithm: THE PATH SPACE IS EXPONENTIAL IN THE STATE SPACE. diagnose has
59 paths and decide 71,098, so it went unnoticed -- but `invent`, a deliberately
generative deck, has 1,182 reachable states and **22,302,788 paths**, and
enumeration simply does not return. DP over states gives the same numbers in
milliseconds at any deck size a human would author, because a state's future
does not depend on how it was reached.

Ordering is the one figure that is not a plain state marginal, so for each pair
the state is augmented with a three-valued latch (neither seen / a first /
b first). Exact, and still linear in the state space.

Sections:
  1. exact enumeration     paths, and the probability mass (must be 1)
  2. process cost          distribution of length and spend
  3. per-card frequency    P(played at all), expected plays per run. Terminal
                           rows assume a uniform agent -- the runner lets the
                           agent choose its exit, so those are not deck facts.
  4. ordering              P(A before B) for every card pair that co-occurs
  5. assertions            the deck's declared `expected_order`, verified
  6. cross-check           exact vs the real die over N sampled seeds

Usage:  python3 simulate.py decks/diagnose.json [trials]
Exits 0 if every declared ordering holds, 1 otherwise.
"""

import json
import random
import sys
from collections import Counter, defaultdict

import budget as B
import run_deck

FAILS = []


def transitions(deck):
    """(state -> [(move, probability, next_state)]) over the reachable space."""
    ids = [c["id"] for c in deck["cards"]]
    start = (tuple(0 for _ in ids), B.no_flags(deck))
    seen = {start}
    out = {}
    stack = [start]
    while stack:
        st = stack.pop()
        counts, flags = st
        pl = dict(zip(ids, counts))
        if B.is_terminal(deck, pl):
            out[st] = []
            continue
        moves = sorted(B.legal_moves(deck, pl, lookahead=True, flags=flags))
        w = B.weights_for(deck, pl, moves)
        tot = sum(w)
        edges = []
        for m, wi in zip(moves, w):
            if wi <= 0:
                continue
            j = ids.index(m)
            nc = tuple(n + 1 if k == j else n for k, n in enumerate(counts))
            branches = B.branch(deck, dict(zip(ids, nc)), flags, m)
            # a condition branch is a property of the ARTIFACT the agent writes,
            # not a chance event, so the deck cannot assign it a probability.
            # Split the mass evenly and say so -- section 2 reports the spread.
            for nf in branches:
                nxt = (nc, nf)
                edges.append((m, wi / tot / len(branches), nxt))
                if nxt not in seen:
                    seen.add(nxt)
                    stack.append(nxt)
        out[st] = edges
    return ids, start, out


def topo(start, trans):
    """States in an order where every predecessor precedes its successors.
    Sound because play counts only ever increase: the graph is a DAG."""
    return sorted(trans, key=lambda st: sum(st[0]))


def reach_prob(start, trans):
    """P(the run passes through each state)."""
    pr = {st: 0.0 for st in trans}
    pr[start] = 1.0
    for st in topo(start, trans):
        base = pr[st]
        if base:
            for _, p, nxt in trans[st]:
                pr[nxt] += base * p
    return pr


def path_count(start, trans):
    """Number of distinct complete paths -- by DP, never materialised."""
    memo = {}
    for st in reversed(topo(start, trans)):
        memo[st] = 1 if not trans[st] else sum(memo[n] for _, _, n in trans[st])
    return memo[start]


def cost_distribution(deck, ids, start, trans):
    """Exact distribution over (plays, spend) at the terminal."""
    by = {c["id"]: c for c in deck["cards"]}
    dist = Counter()
    pr = reach_prob(start, trans)
    for st in trans:
        if trans[st]:
            continue
        counts = dict(zip(ids, st[0]))
        plays = sum(counts.values())
        spend = B.spent(deck, counts)
        dist[(plays, spend)] += pr[st]
    return dist


def card_marginals(deck, ids, start, trans):
    """P(card played at least once) and E[plays], exactly."""
    pr = reach_prob(start, trans)
    expect = defaultdict(float)
    atleast = defaultdict(float)
    for st, edges in trans.items():
        for m, p, _ in edges:
            expect[m] += pr[st] * p
    for st in trans:
        if trans[st]:
            continue
        counts = dict(zip(ids, st[0]))
        for cid, n in counts.items():
            if n:
                atleast[cid] += pr[st]
    return atleast, expect


def order_prob(deck, ids, start, trans, a, b):
    """Exact P(a before b) and P(both appear), by latching a three-valued
    marker (neither seen / a first / b first) onto the state.

    The latch alone is not enough: a run where `a` appears and `b` never does
    also latches to "a first". So the mass is accumulated PER TERMINAL STATE
    and then filtered by whether both cards actually appear there.
    """
    pr = {(start, 0): 1.0}
    ends = defaultdict(float)          # (terminal state, latch) -> mass
    for st in topo(start, trans):
        for lat in (0, 1, 2):
            base = pr.get((st, lat), 0.0)
            if not base:
                continue
            if not trans[st]:
                ends[(st, lat)] += base
                continue
            for m, p, nxt in trans[st]:
                nl = lat
                if lat == 0 and m == a:
                    nl = 1
                elif lat == 0 and m == b:
                    nl = 2
                pr[(nxt, nl)] = pr.get((nxt, nl), 0.0) + base * p
    both = a_first = 0.0
    for (st, lat), mass in ends.items():
        counts = dict(zip(ids, st[0]))
        if counts.get(a, 0) and counts.get(b, 0):
            both += mass
            if lat == 1:
                a_first += mass
    return a_first, both


def sample_path(deck, seed):
    """One playthrough driven by the REAL die in run_deck."""
    ids = [c["id"] for c in deck["cards"]]
    counts = {i: 0 for i in ids}
    seq = []
    step = 1
    while not B.is_terminal(deck, counts):
        moves = sorted(B.legal_moves(deck, counts, lookahead=True))
        if not moves:
            return None
        card = run_deck.draw(seed, step, 0, moves,
                             B.weights_for(deck, counts, sorted(moves)))
        counts[card] += 1
        seq.append(card)
        step += 1
    return tuple(seq)


def main(path, trials):
    deck = json.load(open(path))
    if B.option_source(deck):
        deck = B.expand(deck, B.max_options(deck))
    by = {c["id"]: c for c in deck["cards"]}
    print(f"=== role-deck simulator: {deck['deck']} v{deck.get('version','?')} ===\n")

    ids, start, trans = transitions(deck)
    npaths = path_count(start, trans)

    # ---------------------------------------------------------- 1. space
    pr = reach_prob(start, trans)
    mass = sum(pr[st] for st in trans if not trans[st])
    print("1. state space")
    print(f"   {len(trans)} reachable states, {npaths:,} distinct complete paths")
    print(f"   terminal probability mass {mass:.12f}")
    if abs(mass - 1.0) > 1e-9:
        print(f"*** FAIL [mass] terminal mass is {mass}, not 1 -- some run "
              f"never finishes")
        FAILS.append("mass")
    print()

    # ---------------------------------------------------------- 2. cost
    dist = cost_distribution(deck, ids, start, trans)
    lens = Counter()
    costs = Counter()
    for (pl, sp), m in dist.items():
        lens[pl] += m
        costs[sp] += m
    exp_len = sum(k * v for k, v in lens.items())
    exp_cost = sum(k * v for k, v in costs.items())
    print("2. process cost  (this is the answer to 'is it just planning for planning')")
    print("   plays per run:  " +
          "  ".join(f"{k}:{v*100:.1f}%" for k, v in sorted(lens.items())) +
          f"   mean {exp_len:.2f}")
    print("   spend per run:  " +
          "  ".join(f"{k}:{v*100:.1f}%" for k, v in sorted(costs.items())) +
          f"   mean {exp_cost:.2f}  (budget {deck.get('budget')}, "
          f"floor {B.floor_cost(deck)})")
    print()

    # ---------------------------------------------------------- 3. frequency
    atleast, expect = card_marginals(deck, ids, start, trans)
    print("3. per-card frequency")
    print("   card           role      P(played)   E[plays]")
    for c in deck["cards"]:
        cid = c["id"]
        flag = ""
        if c.get("terminal"):
            flag = "   <- exit: AGENT-CHOSEN, not drawn"
        elif atleast[cid] < 0.05:
            flag = "   <- almost never played"
        elif atleast[cid] > 0.999:
            flag = "   (every run)"
        print(f"   {cid:<14} {c['role']:<8}  {atleast[cid]*100:>7.1f}%   "
              f"{expect[cid]:>6.2f}{flag}")
    print()

    # ---------------------------------------------------------- 4. ordering
    print("4. ordering: P(A before B), for pairs that are not already forced")
    cards = [c["id"] for c in deck["cards"]]
    undetermined = []
    for i, a in enumerate(cards):
        for b in cards[i + 1:]:
            af, both = order_prob(deck, ids, start, trans, a, b)
            if both < 1e-12:
                continue
            p = af / both
            if 1e-9 < p < 1 - 1e-9:
                undetermined.append((a, b, p, both))
    if not undetermined:
        print("   every co-occurring pair has a forced order")
    for a, b, p, w in sorted(undetermined, key=lambda t: -abs(t[2] - 0.5))[:12]:
        print(f"   {a:<14} before {b:<14} {p*100:>5.1f}%   "
              f"(both appear in {w*100:.0f}% of runs)")
    if len(undetermined) > 12:
        print(f"   ... and {len(undetermined) - 12} more undetermined pair(s)")
    print()

    # ---------------------------------------------------------- 5. assertions
    print("5. declared orderings")
    declared = deck.get("expected_order", [])
    if not declared:
        print("   deck declares none -- see section 4 for what is left to chance")
    for pair in declared:
        a, b = pair[0], pair[1]
        af, both = order_prob(deck, ids, start, trans, a, b)
        if both < 1e-12:
            print(f"*** FAIL [order] '{a}' and '{b}' never co-occur, so the "
                  f"declared ordering is vacuous")
            FAILS.append("order")
            continue
        p = af / both
        if p > 1 - 1e-9:
            print(f"    ok  '{a}' always precedes '{b}' "
                  f"(co-occur in {both*100:.0f}% of runs)")
        else:
            print(f"*** FAIL [order] '{a}' precedes '{b}' in only {p*100:.1f}% of "
                  f"runs -- the deck does not enforce this")
            FAILS.append("order")
    print()

    # ---------------------------------------------------------- 6. cross-check
    print(f"6. cross-check: exact DP vs the real die ({trials} seeds)")
    rng = random.Random(20260915)
    seen = Counter()
    for _ in range(trials):
        sp = sample_path(deck, rng.randrange(1, 2 ** 31))
        if sp is not None:
            seen[sp] += 1
    total = max(1, sum(seen.values()))
    samp_len = sum(len(sq) * n for sq, n in seen.items()) / total
    samp_exp = defaultdict(float)
    for sq, n in seen.items():
        for cid in sq:
            samp_exp[cid] += n / total
    worst_card, worst = None, 0.0
    for c in deck["cards"]:
        gap = abs(samp_exp[c["id"]] - expect[c["id"]])
        if gap > worst:
            worst_card, worst = c["id"], gap
    print(f"   distinct paths seen: {len(seen)} of {npaths:,}")
    print(f"   mean length: exact {exp_len:.3f}, sampled {samp_len:.3f}")
    print(f"   largest per-card gap in E[plays]: {worst_card} {worst:.4f}")
    if worst > 0.10 or abs(samp_len - exp_len) > 0.30:
        print(f"*** FAIL [die] the real die departs from the declared weights "
              f"(worst card gap {worst:.3f})")
        FAILS.append("die")
    else:
        print("   ok: the hash die tracks the weighted model within sampling error")
    print()

    if FAILS:
        print(f"*** {len(FAILS)} SIMULATION FAILURE(S): {', '.join(sorted(set(FAILS)))}")
        return 1
    print("ALL SIMULATION CHECKS PASSED")
    return 0


if __name__ == "__main__":
    sys.setrecursionlimit(10000)
    p = sys.argv[1] if len(sys.argv) > 1 else "decks/diagnose.json"
    t = int(sys.argv[2]) if len(sys.argv) > 2 else 4000
    raise SystemExit(main(p, t))
