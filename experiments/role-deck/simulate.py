#!/usr/bin/env python3
"""What a deck actually generates, as opposed to what its author intended.

The gates in check_deck.py say what is POSSIBLE. They say nothing about how
often. A deck is a generative object, and designers are reliably wrong about
what their generative objects generate -- you intend "BLACK lands after the
second GREEN" and it does, 62% of the time.

The state space is small, so this does not sample: it enumerates EVERY complete
path with its exact probability (the product of the drawn card's
share of the legal weight at each step). Monte Carlo is used only as an
independent cross-check, and it runs through run_deck.draw -- the real hash-based
die -- so the comparison also tests whether that die honours the deck's
declared weights rather than merely being deterministic.

Sections:
  1. exact enumeration     paths, and the probability mass (must be 1)
  2. process cost          distribution of length and spend
  3. per-card frequency    P(played at all), expected plays per run
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


def enumerate_paths(deck):
    """Every complete path, with its exact probability under the declared weights."""
    ids = [c["id"] for c in deck["cards"]]
    paths = []

    def walk(counts, seq, prob):
        if B.is_terminal(deck, counts):
            paths.append((tuple(seq), prob))
            return
        moves = sorted(B.legal_moves(deck, counts, lookahead=True))
        if not moves:
            return
        w = B.weights_for(deck, counts, moves)
        total = sum(w)
        if total <= 0:
            return
        for m, wi in zip(moves, w):
            if wi <= 0:
                continue                       # a zero-weight card is never drawn
            nxt = dict(counts)
            nxt[m] = nxt.get(m, 0) + 1
            walk(nxt, seq + [m], prob * wi / total)

    walk({i: 0 for i in ids}, [], 1.0)
    return paths


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
    by = {c["id"]: c for c in deck["cards"]}
    print(f"=== role-deck simulator: {deck['deck']} v{deck.get('version','?')} ===\n")

    # ---------------------------------------------------------- 1. enumerate
    paths = enumerate_paths(deck)
    mass = sum(p for _, p in paths)
    print(f"1. exact enumeration")
    print(f"   {len(paths)} distinct complete paths, probability mass {mass:.12f}")
    if abs(mass - 1.0) > 1e-9:
        print(f"*** FAIL probability mass is {mass}, not 1 -- some path does not terminate")
        FAILS.append("mass")
    print()

    # ---------------------------------------------------------- 2. cost
    lens = Counter()
    costs = Counter()
    for seq, pr in paths:
        lens[len(seq)] += pr
        costs[sum(B.cost_of(by[c]) for c in seq)] += pr
    exp_len = sum(k * v for k, v in lens.items())
    exp_cost = sum(k * v for k, v in costs.items())
    print("2. process cost  (this is the answer to 'is it just planning for planning')")
    print(f"   plays per run:  " +
          "  ".join(f"{k}:{v*100:.1f}%" for k, v in sorted(lens.items())) +
          f"   mean {exp_len:.2f}")
    print(f"   spend per run:  " +
          "  ".join(f"{k}:{v*100:.1f}%" for k, v in sorted(costs.items())) +
          f"   mean {exp_cost:.2f}  (budget {deck.get('budget')})")
    print()

    # ---------------------------------------------------------- 3. frequency
    print("3. per-card frequency")
    print("   card           role      P(played)   E[plays]")
    atleast = defaultdict(float)
    expect = defaultdict(float)
    for seq, pr in paths:
        c = Counter(seq)
        for cid, n in c.items():
            atleast[cid] += pr
            expect[cid] += pr * n
    for c in deck["cards"]:
        cid = c["id"]
        flag = ""
        if atleast[cid] < 0.05:
            flag = "   <- almost never played"
        elif atleast[cid] > 0.999:
            flag = "   (every run)"
        print(f"   {cid:<14} {c['role']:<8}  {atleast[cid]*100:>7.1f}%   "
              f"{expect[cid]:>6.2f}{flag}")
    print()

    # ---------------------------------------------------------- 4. ordering
    print("4. ordering: P(A before B), for pairs that are not already forced")
    before = defaultdict(float)
    both = defaultdict(float)
    for seq, pr in paths:
        first = {}
        for i, c in enumerate(seq):
            first.setdefault(c, i)
        for a in first:
            for b in first:
                if a >= b:
                    continue
                both[(a, b)] += pr
                if first[a] < first[b]:
                    before[(a, b)] += pr
    undetermined = []
    for (a, b), w in sorted(both.items()):
        if w < 1e-12:
            continue
        p = before[(a, b)] / w
        if 1e-9 < p < 1 - 1e-9:
            undetermined.append((a, b, p, w))
    if not undetermined:
        print("   every co-occurring pair has a forced order")
    for a, b, p, w in sorted(undetermined, key=lambda t: -abs(t[2] - 0.5)):
        print(f"   {a:<14} before {b:<14} {p*100:>5.1f}%   "
              f"(both appear in {w*100:.0f}% of runs)")
    print()

    # ---------------------------------------------------------- 5. assertions
    print("5. declared orderings")
    declared = deck.get("expected_order", [])
    if not declared:
        print("   deck declares none -- see section 4 for what is left to chance")
    for pair in declared:
        a, b = pair[0], pair[1]
        key = (a, b) if a < b else (b, a)
        w = both.get(key, 0.0)
        if w < 1e-12:
            print(f"*** FAIL [order] '{a}' and '{b}' never co-occur, so the "
                  f"declared ordering is vacuous")
            FAILS.append("order")
            continue
        p = before[key] / w if a < b else 1 - before[key] / w
        if p > 1 - 1e-9:
            print(f"    ok  '{a}' always precedes '{b}' "
                  f"(co-occur in {w*100:.0f}% of runs)")
        else:
            print(f"*** FAIL [order] '{a}' precedes '{b}' in only {p*100:.1f}% of "
                  f"runs -- the deck does not enforce this")
            FAILS.append("order")
    print()

    # ---------------------------------------------------------- 6. cross-check
    print(f"6. cross-check: exact enumeration vs the real die ({trials} seeds)")
    exact = defaultdict(float)
    for seq, pr in paths:
        exact[seq] += pr
    rng = random.Random(20260915)
    seen = Counter()
    for _ in range(trials):
        s = sample_path(deck, rng.randrange(1, 2**31))
        if s is not None:
            seen[s] += 1
    tv = 0.5 * sum(abs(seen[s] / trials - exact.get(s, 0.0))
                   for s in set(seen) | set(exact))
    samp_len = sum(len(s) * n for s, n in seen.items()) / max(1, sum(seen.values()))
    print(f"   distinct paths seen: {len(seen)} of {len(paths)}")
    print(f"   mean length: exact {exp_len:.3f}, sampled {samp_len:.3f}")
    print(f"   total-variation distance: {tv:.4f}")
    if tv > 0.15:
        print(f"*** FAIL [die] the real die's path distribution is far from uniform "
              f"(TV {tv:.3f}) -- the exact model does not describe it")
        FAILS.append("die")
    else:
        print(f"   ok: the hash die tracks the weighted model within sampling error")
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
