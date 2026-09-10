#!/usr/bin/env python3
"""Verification engine for the `causal-sandbox` skill.

A minimal authored-rule state-transition sandbox that exercises every mechanism
SKILL.md prescribes, on two known-answer worlds:

  * inventory  -- consume / reorder / restock, deterministic, confluent
  * roles      -- grant_default / revoke_all, a genuinely non-confluent pair

Stdlib only. No RNG (the scheduler is a fixed priority order), so every run is
deterministic and replay is byte-identical by construction -- which we still
assert. See docs/verifying-skills.md for the shared contract.
"""
from itertools import combinations


# --------------------------------------------------------------------------
# engine
# --------------------------------------------------------------------------
class RState(dict):
    """A state dict that records which keys were read, for read-set enforcement."""

    def __init__(self, *a, **k):
        super().__init__(*a, **k)
        self.reads = set()

    def __getitem__(self, key):
        self.reads.add(key)
        return super().__getitem__(key)

    def get(self, key, default=None):
        self.reads.add(key)
        return super().get(key, default)


def upd(state, changes):
    """Return a copy of `state` with `changes` (a dict of key->value) applied."""
    d = dict(state)
    d.update(changes)
    return d


class Rule:
    def __init__(self, name, types, guard, reads, writes, effect,
                 nondet=False, why="", source=""):
        self.name = name
        self.types = types           # e.g. ["Item"] or ["User"]
        self.guard = guard           # (state, binding) -> bool
        self.reads = reads           # binding -> set of keys
        self.writes = writes         # binding -> set of keys
        self.effect = effect         # (state, binding) -> new plain dict
        self.nondet = nondet
        self.why = why
        self.source = source


class RuleContractError(ValueError):
    pass


def bindings(rule, entities):
    """All parameter bindings for a rule over the entity pools (1 param only here)."""
    if not rule.types:
        return [()]
    pool = entities[rule.types[0]]
    return [(e,) for e in pool]


def enabled(state, rules, entities):
    out = []
    for r in rules:
        for b in bindings(r, entities):
            if r.guard(RState(state), b):
                out.append((r, b))
    return out


def _apply(state, rule, b, next_id, step, branch):
    """Apply one enabled event; enforce the read-set and write-set declarations."""
    # collect reads from guard + effect
    g = RState(state)
    rule.guard(g, b)
    e = RState(state)
    new = rule.effect(e, b)
    seen_reads = g.reads | e.reads
    decl_reads = rule.reads(b)
    if not seen_reads <= decl_reads:
        raise RuleContractError(
            f"{rule.name}{b} read undeclared keys {seen_reads - decl_reads}")
    changed = {k for k in set(new) | set(state) if new.get(k) != state.get(k)}
    decl_writes = rule.writes(b)
    if not changed <= decl_writes:
        raise RuleContractError(
            f"{rule.name}{b} wrote undeclared keys {changed - decl_writes}")
    event = dict(id=next_id, step=step, branch=branch, rule=rule.name, binding=b,
                 reads=frozenset(decl_reads), writes=frozenset(decl_writes),
                 changed=frozenset(changed))
    return new, event


def run(state, rules, entities, max_steps, priority=None, branch="main"):
    """Single-branch forward run under a fixed priority scheduler.

    priority: list of rule names, highest first. Ties broken by binding order.
    Returns (events, states) where states[k] is the state after events[k-1].
    """
    order = {n: i for i, n in enumerate(priority or [r.name for r in rules])}
    states = [dict(state)]
    events = []
    cur = dict(state)
    for step in range(max_steps):
        en = enabled(cur, rules, entities)
        if not en:
            break                              # frozen -- a terminal state
        en.sort(key=lambda rb: (order[rb[0].name], rb[1]))
        rule, b = en[0]
        cur, ev = _apply(cur, rule, b, len(events), step, branch)
        events.append(ev)
        states.append(dict(cur))
    return events, states


def apply_sequence(state, seq, rules_by_name):
    """Apply an explicit sequence of (rule_name, binding); skip a step whose
    guard does not hold at that point. Used by the confluence machinery."""
    cur = dict(state)
    fired = []
    for name, b in seq:
        r = rules_by_name[name]
        if not r.guard(RState(cur), b):
            continue
        cur, ev = _apply(cur, r, b, len(fired), len(fired), "seq")
        fired.append(ev)
    return cur, fired


def causal_edges(events):
    """Edge e_i -> e_j iff e_i is the LAST writer, before j, of a key e_j reads."""
    edges = set()
    for j, ej in enumerate(events):
        for key in ej["reads"]:
            last = None
            for i in range(j):
                if key in events[i]["changed"]:
                    last = i
            if last is not None:
                edges.add((last, j, key))
    return edges


def confluence_conflicts(state, rules, entities):
    """Return the set of {rule-name pair} that reach different states under the
    two firing orders -- the non-confluent pairs on this slice."""
    rbn = {r.name: r for r in rules}
    en = enabled(state, rules, entities)
    conflicts = set()
    for (ra, ba), (rb, bb) in combinations(en, 2):
        s_ab, _ = apply_sequence(state, [(ra.name, ba), (rb.name, bb)], rbn)
        s_ba, _ = apply_sequence(state, [(rb.name, bb), (ra.name, ba)], rbn)
        if s_ab != s_ba:
            conflicts.add(tuple(sorted((ra.name, rb.name))))
    return conflicts


def backward_min_intervention(s0, rules, entities, target, candidates,
                              budget, max_steps, priority=None):
    """Smallest set of changes to the INITIAL FACTS (not the event stream) such
    that `target(state)` is never true on the resulting trace.

    candidates: list of (key, [values-to-try]) -- only initial facts.
    Returns a dict of the changes, or None if no fix within `budget` changes.
    """
    keys = [k for k, _ in candidates]
    vals = {k: v for k, v in candidates}
    for k in range(1, budget + 1):
        for combo in combinations(keys, k):
            # cartesian product of the candidate values for the chosen keys
            choices = [{}]
            for key in combo:
                choices = [upd(c, {key: v}) for c in choices for v in vals[key]]
            for delta in choices:
                _, states = run(upd(s0, delta), rules, entities, max_steps,
                                priority)
                if not any(target(st) for st in states):
                    return delta
    return None


# --------------------------------------------------------------------------
# world 1: inventory  (deterministic, confluent)
# --------------------------------------------------------------------------
def _inv_rules():
    def sk(i):
        return ("stock", i)

    consume = Rule(
        "consume", ["Item"],
        guard=lambda st, b: st.get(sk(b[0]), 0) > 0,
        reads=lambda b: {sk(b[0])},
        writes=lambda b: {sk(b[0])},
        effect=lambda st, b: upd(st, {sk(b[0]): st[sk(b[0])] - 5}),
        why="steady draw of 5 units/step", source="inventory-policy.md 3.1")

    reorder = Rule(
        "reorder", ["Item"],
        guard=lambda st, b: (st.get(sk(b[0]), 0) < st.get(("threshold", b[0]), 0)
                             and not st.get(("pending", b[0]), False)),
        reads=lambda b: {sk(b[0]), ("threshold", b[0]), ("pending", b[0])},
        writes=lambda b: {("pending", b[0])},
        effect=lambda st, b: upd(st, {("pending", b[0]): True}),
        why="reorder once when stock first drops below threshold",
        source="inventory-policy.md 3.2")

    restock = Rule(
        "restock", ["Item"],
        guard=lambda st, b: st.get(("pending", b[0]), False),
        reads=lambda b: {sk(b[0]), ("pending", b[0])},
        writes=lambda b: {sk(b[0]), ("pending", b[0])},
        effect=lambda st, b: upd(st, {sk(b[0]): st[sk(b[0])] + 30,
                                         ("pending", b[0]): False}),
        why="delivery of 30 units clears the pending order",
        source="inventory-policy.md 3.3")

    noop = Rule(
        "noop", ["Item"],
        guard=lambda st, b: True,
        reads=lambda b: set(),
        writes=lambda b: set(),
        effect=lambda st, b: dict(st),
        why="the empty-write-set degenerate rule", source="test")

    return dict(consume=consume, reorder=reorder, restock=restock, noop=noop)


INV = _inv_rules()
INV_ENT = {"Item": ["widget"]}
INV_PRIORITY = ["restock", "reorder", "consume", "noop"]


# --------------------------------------------------------------------------
# world 2: roles  (grant_default vs revoke_all -- non-confluent)
# --------------------------------------------------------------------------
def _role_rules():
    def hk(u):
        return ("holds", u, "viewer")

    grant_default = Rule(
        "grant_default", ["User"],
        guard=lambda st, b: (st.get(("new", b[0]), False)
                             and not st.get(hk(b[0]), False)),
        reads=lambda b: {("new", b[0]), hk(b[0])},
        writes=lambda b: {hk(b[0])},
        effect=lambda st, b: upd(st, {hk(b[0]): True}),
        why="a new user is granted the viewer role by default",
        source="rbac-policy.md 2.1")

    revoke_all = Rule(
        "revoke_all", ["User"],
        guard=lambda st, b: st.get(("flagged", b[0]), False),
        reads=lambda b: {("flagged", b[0]), hk(b[0])},
        writes=lambda b: {hk(b[0])},
        effect=lambda st, b: upd(st, {hk(b[0]): False}),
        why="a flagged user has all roles stripped",
        source="rbac-policy.md 5.4")

    return dict(grant_default=grant_default, revoke_all=revoke_all)


ROLE = _role_rules()


# --------------------------------------------------------------------------
# assertions
# --------------------------------------------------------------------------
def main():
    fail = 0

    def check(name, got, want):
        nonlocal fail
        ok = got == want
        print(f"  {'PASS' if ok else 'FAIL'}  {name}: got {got!r} want {want!r}")
        if not ok:
            fail += 1

    def check_true(name, cond, detail=""):
        nonlocal fail
        print(f"  {'PASS' if cond else 'FAIL'}  {name}{(' -- ' + detail) if detail else ''}")
        if not cond:
            fail += 1

    rules = [INV[n] for n in ("consume", "reorder", "restock", "noop")]

    # 1. forward run: the causal chain consume -> reorder -> restock ---------
    print("=== 1. forward run: causal graph of the reorder cycle ===")
    s0 = {("stock", "widget"): 40, ("threshold", "widget"): 25}
    events, states = run(s0, rules, INV_ENT, max_steps=8, priority=INV_PRIORITY)
    seq = [(e["rule"], e["step"]) for e in events]
    print(f"  events: {seq}")
    print(f"  stock by step: {[st.get(('stock','widget')) for st in states]}")
    edges = causal_edges(events)
    simple = {(i, j) for (i, j, _) in edges}
    # consume#3 (idx 3, the one that drops stock to 20) feeds reorder (idx 4)
    check_true("reorder fires at event 4", events[4]["rule"] == "reorder")
    check_true("last consume before reorder -> reorder edge present (via stock)",
               (3, 4) in simple)
    check_true("earlier consume #0 is NOT the causal parent of reorder "
               "(last-writer wins)", (0, 4) not in simple)
    check_true("reorder -> restock edge present (via pending)", (4, 5) in simple)
    check("restock brings stock 20 -> 50", states[6][("stock", "widget")], 50)

    # 2. backward: minimal intervention for 'stock hit zero' ----------------
    print("\n=== 2. backward: smallest initial-condition change that avoids "
          "stock == 0 ===")
    s0z = {("stock", "widget"): 40, ("threshold", "widget"): 3}
    _, zstates = run(s0z, rules, INV_ENT, max_steps=12, priority=INV_PRIORITY)
    hit = [k for k, st in enumerate(zstates) if st.get(("stock", "widget")) == 0]
    print(f"  under threshold=3, stock reaches 0 at state index {hit[0]}")
    check("stock hits 0 at state index 8", hit[0], 8)

    target = lambda st: st.get(("stock", "widget"), 1) == 0
    candidates = [(("threshold", "widget"), [25, 10, 40, 5]),
                  (("stock", "widget"), [45, 50, 60, 80])]
    fix = backward_min_intervention(s0z, rules, INV_ENT, target, candidates,
                                    budget=2, max_steps=12, priority=INV_PRIORITY)
    print(f"  minimal intervention found: {fix}")
    check("1-change fix is raise-the-threshold", fix,
          {("threshold", "widget"): 25})
    # the search space is initial facts, never the event stream:
    cand_keys = {k for k, _ in candidates}
    check_true("candidate space is initial facts only (no events)",
               all(k in s0z for k in cand_keys))
    check_true("'skip the day-4 consume' is not a candidate "
               "(not an initial fact)",
               ("event", 3) not in cand_keys and ("consume", 3) not in cand_keys)

    # 3. confluence: flag the real conflict, pass the commuting pair --------
    print("\n=== 3. confluence pass on the role slice ===")
    role_rules = [ROLE["grant_default"], ROLE["revoke_all"]]
    slice_state = {("new", "alice"): True, ("flagged", "alice"): True,
                   ("holds", "alice", "viewer"): False,
                   ("new", "bob"): True, ("holds", "bob", "viewer"): False}
    conflicts = confluence_conflicts(slice_state, role_rules,
                                     {"User": ["alice", "bob"]})
    print(f"  conflicting rule pairs: {sorted(conflicts)}")
    check_true("grant_default / revoke_all on the SAME user is flagged",
               ("grant_default", "revoke_all") in conflicts)
    # two grant_defaults on different users touch disjoint facts:
    twogrant = confluence_conflicts(
        {("new", "alice"): True, ("holds", "alice", "viewer"): False,
         ("new", "bob"): True, ("holds", "bob", "viewer"): False},
        [ROLE["grant_default"]], {"User": ["alice", "bob"]})
    check("two independent grant_defaults do NOT conflict", twogrant, set())

    # 4. the causal claim flips with firing order on the non-confluent slice
    print("\n=== 4. a causal claim on the non-confluent slice is order-dependent ===")
    rbn = ROLE
    alice = {("new", "alice"): True, ("flagged", "alice"): True,
             ("holds", "alice", "viewer"): False}
    s_gr, ev_gr = apply_sequence(
        alice, [("grant_default", ("alice",)), ("revoke_all", ("alice",))], rbn)
    s_rg, ev_rg = apply_sequence(
        alice, [("revoke_all", ("alice",)), ("grant_default", ("alice",))], rbn)
    hk = ("holds", "alice", "viewer")
    last_writer = lambda evs: next(
        (e["rule"] for e in reversed(evs) if hk in e["changed"]), None)
    print(f"  order <grant, revoke>: holds={s_gr[hk]}  last writer={last_writer(ev_gr)}")
    print(f"  order <revoke, grant>: holds={s_rg[hk]}  last writer={last_writer(ev_rg)}")
    check_true("final holds(alice,viewer) differs by order",
               s_gr[hk] != s_rg[hk], f"{s_gr[hk]} vs {s_rg[hk]}")
    check_true("the claim 'revoke_all caused holds=False' is true under one "
               "order and false under the other",
               (last_writer(ev_gr) == "revoke_all" and s_gr[hk] is False)
               and not (last_writer(ev_rg) == "revoke_all" and s_rg[hk] is False))

    # 5. degenerate cases + replay ----------------------------------------
    print("\n=== 5. degenerate cases and replay ===")
    no_noop = [INV[n] for n in ("consume", "reorder", "restock")]
    frozen_s = {("stock", "widget"): 0, ("threshold", "widget"): 0}
    fev, fst = run(frozen_s, no_noop, INV_ENT, max_steps=5, priority=INV_PRIORITY)
    check("no enabled rule -> state frozen, zero events", len(fev), 0)

    nev, nst = run({("stock", "widget"): 7}, [INV["noop"]], INV_ENT,
                   max_steps=1, priority=["noop"])
    check_true("empty-write-set rule leaves the state unchanged",
               nst[0] == nst[1] and nev[0]["changed"] == frozenset())

    e1, s1 = run(s0, rules, INV_ENT, max_steps=8, priority=INV_PRIORITY)
    e2, s2 = run(s0, rules, INV_ENT, max_steps=8, priority=INV_PRIORITY)
    check_true("replay under the same seed is byte-identical",
               [(e["rule"], e["binding"]) for e in e1]
               == [(e["rule"], e["binding"]) for e in e2] and s1 == s2)

    # 6. read/write-set enforcement --------------------------------------
    print("\n=== 6. read-set / write-set enforcement ===")
    leaky = Rule(
        "leaky", ["Item"],
        guard=lambda st, b: True,
        reads=lambda b: set(),
        writes=lambda b: set(),                       # declares NO writes ...
        effect=lambda st, b: upd(st, {("stock", b[0]): 999}),  # ... but writes
        why="deliberately mis-declared", source="test")
    raised = False
    try:
        run({("stock", "widget"): 10}, [leaky], INV_ENT, max_steps=1,
            priority=["leaky"])
    except RuleContractError as exc:
        raised = True
        print(f"  engine rejected the rule: {exc}")
    check_true("a rule that writes an undeclared field is rejected", raised)

    peeker = Rule(
        "peeker", ["Item"],
        guard=lambda st, b: st.get(("secret", b[0]), 0) >= 0,   # reads 'secret'
        reads=lambda b: {("stock", b[0])},                      # ... undeclared
        writes=lambda b: {("stock", b[0])},
        effect=lambda st, b: upd(st, {("stock", b[0]): 1}),
        why="deliberately mis-declared", source="test")
    raised = False
    try:
        run({("stock", "widget"): 10, ("secret", "widget"): 3}, [peeker],
            INV_ENT, max_steps=1, priority=["peeker"])
    except RuleContractError as exc:
        raised = True
        print(f"  engine rejected the rule: {exc}")
    check_true("a rule that reads an undeclared field is rejected", raised)

    print()
    if fail:
        print(f"{fail} CHECK(S) FAILED")
        raise SystemExit(1)
    print("ALL SANDBOX CHECKS PASSED")


if __name__ == "__main__":
    main()
