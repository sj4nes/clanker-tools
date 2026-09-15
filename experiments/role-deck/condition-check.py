#!/usr/bin/env python3
"""Property test for conditional requirements, driven by the real die.

The model-level proof is in check_deck.py's `conditions` gate: the flag must
change what is legal somewhere. This asserts the consequence actually holds
across real runs rather than in one hand-built state:

    whenever `commit` is on offer, either no disputed fact was declared,
    or the probe was actually played.

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
    rng = random.Random(4242)
    viol = checked = 0
    for _ in range(trials):
        declare = rng.random() < 0.5
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
                if "commit" in exits:
                    seq = [p["played"] for p in led["plays"]]
                    if flags[0] and "probe" not in seq:
                        viol += 1
                        print(f"*** FAIL commit offered with a disputed fact and "
                              f"no probe: {seq}")
            if not work:
                break
            card = run_deck.draw(led["seed"], step, 0, work,
                                 B.weights_for(deck, counts, work))
            art = {f: f"<{f}>"
                   for f in deck["artifacts"][by[card]["produces"]]["fields"]}
            if card == "attack":
                art["disputed_fact"] = "the SLA is unverified" if declare else None
            led["plays"].append({
                "n": step, "drawn": card, "chosen_exit": False, "played": card,
                "rerolls": 0, "artifact": art,
                "instrument": ({"kind": "x", "command": "true", "exit": 0,
                                "output": "", "output_sha256": run_deck.digest("")}
                               if by[card].get("instrument") else None)})
    print(f"   {trials} runs, {checked} exit-decision points, {viol} violation(s)")
    if viol:
        print("*** CONDITION PROPERTY FAILED")
        return 1
    print("   ok: commit is never offered over an unresolved disputed fact")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(int(sys.argv[1]) if len(sys.argv) > 1 else 400))
