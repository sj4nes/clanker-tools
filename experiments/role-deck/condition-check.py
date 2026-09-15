#!/usr/bin/env python3
"""Property tests for conditional requirements AND matched depth, driven by the
real die.

The model-level proof is in check_deck.py's `conditions` gate: the flag must
change what is legal somewhere. This asserts the consequence actually holds
across real runs rather than in one hand-built state:

    (1) whenever `commit` is on offer, either no disputed fact was declared
        or the probe was actually played;
    (2) whenever `commit` or `drop` is on offer, EVERY option has both a
        steelman and an attack -- matched depth, which is the constraint the
        card model could not express until options were countable.

Driven by run_deck.draw over many seeds, so the card order is the die's, not a
forced sequence. An earlier hand-forced version of this test was WRONG -- the
runner refuses cards the die did not draw, so most of its plays were silently
rejected and it proved nothing.
"""
import json
import random
import sys

import budget as B
import run_deck

DECK = "decks/decide.json"


def main(trials=400):
    deck = json.load(open(DECK))
    by = {c["id"]: c for c in deck["cards"]}
    if not B.conditions(deck):
        print("  no conditions declared; nothing to check")
        return 0
    src = B.option_source(deck)
    rng = random.Random(4242)
    viol = checked = depth_checked = 0
    for _ in range(trials):
        declare = rng.random() < 0.5
        opts = ["opt%d" % k for k in range(1, rng.randint(1, B.max_options(deck)) + 1)]
        deck = B.expand(json.load(open(DECK)), len(opts))
        by = {c["id"]: c for c in deck["cards"]}
        led = {"deck": deck["deck"], "deck_version": deck["version"],
               "deck_path": DECK, "seed": rng.randrange(1, 2 ** 31),
               "rerolls_allowed": 0, "pending_rerolls": 0, "plays": []}
        for step in range(1, 20):
            counts = run_deck.played_counts(deck, led)
            flags = run_deck.flags_of(deck, led)
            legal = sorted(B.legal_moves(deck, counts, lookahead=True, flags=flags))
            exits = [m for m in legal if by[m].get("terminal")]
            work = [m for m in legal if not by[m].get("terminal")]
            if exits:
                checked += 1
                seq = [p["played"] for p in led["plays"]]
                if "commit" in exits and flags[0] and "probe" not in seq:
                    viol += 1
                    print(f"*** FAIL commit offered with a disputed fact and "
                          f"no probe: {seq}")
                if src and ({"commit", "drop"} & set(exits)):
                    depth_checked += 1
                    idx = src["index_field"]
                    for card, art in (("steelman", "support"), ("attack", "faults")):
                        done = {p["artifact"].get(idx) for p in led["plays"]
                                if p["played"] == card}
                        if set(opts) - done:
                            viol += 1
                            print(f"*** FAIL {sorted(set(exits))} offered with "
                                  f"{card} missing for {sorted(set(opts)-done)}")
            if not work:
                break
            card = run_deck.draw(led["seed"], step, 0, work,
                                 B.weights_for(deck, counts, work))
            art = {f: f"<{f}>"
                   for f in deck["artifacts"][by[card]["produces"]]["fields"]}
            if card == "frame":
                art[src["field"]] = list(opts) if src else art.get("options")
            if src and by[card].get("per_option"):
                idx = src["index_field"]
                used = {p["artifact"].get(idx) for p in led["plays"]
                        if p["played"] == card}
                free = [o for o in opts if o not in used]
                art[idx] = free[0] if free else opts[0]
            if card == "attack":
                art["disputed_fact"] = "the SLA is unverified" if declare else None
            led["plays"].append({
                "n": step, "drawn": card, "chosen_exit": False, "played": card,
                "rerolls": 0, "artifact": art,
                "instrument": ({"kind": "x", "command": "true", "exit": 0,
                                "output": "", "output_sha256": run_deck.digest("")}
                               if by[card].get("instrument") else None)})
    print(f"   {trials} runs, {checked} exit-decision points "
          f"({depth_checked} with commit/drop on offer), {viol} violation(s)")
    if viol:
        print("*** CONDITION PROPERTY FAILED")
        return 1
    print("   ok: commit is never offered over an unresolved disputed fact")
    print("   ok: commit/drop are never offered before every option has both "
          "a steelman and an attack")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(int(sys.argv[1]) if len(sys.argv) > 1 else 400))
