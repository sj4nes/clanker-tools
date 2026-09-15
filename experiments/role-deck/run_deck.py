#!/usr/bin/env python3
"""Runner for a role deck: draw, play, and an append-only ledger.

The agent never chooses its next hat. The runner computes the legal moves, an
EXTERNAL draw picks one, and the agent's only job is to produce that card's
artifact. That is the whole point -- an agent that picks its own sequence will
pick the one that omits the expensive hat, and no amount of instruction fixes
that because the instruction is the thing being optimised against.

Three properties make the ledger worth trusting:

  1. The draw is a PURE FUNCTION of (seed, step, rerolls-spent-at-that-step).
     Nothing random is stored; `verify` recomputes every draw from scratch. A
     hand-edited ledger, or a play the runner never authorised, does not
     survive replay.

  2. Artifacts are validated against the card's declared fields EXACTLY --
     no missing fields, no extra ones. An extra field is runtime hat bleed:
     an agent still wearing the last hat, or reaching ahead into the next
     one. This is the check that does not depend on the model complying.

  3. `spent` is derived from the play history, never stored. There is no
     mutable counter to corrupt.

Commands:
    init    --deck D --seed N --ledger L
    next    --ledger L                    what the die drew, and what to fill
    play    --ledger L --artifact JSON    submit the drawn card's artifact
    reroll  --ledger L --reason TEXT      spend a reroll token (logged)
    verify  --ledger L                    replay and re-check the whole run
    log     --ledger L                    human-readable history
"""

import argparse
import hashlib
import json
import subprocess
import sys
import time

import budget as B

STDOUT_CAP = 4000        # bytes of captured output stored in the ledger


# ---------------------------------------------------------------- the die
def draw(seed, step, rerolls, legal):
    """Deterministic external draw. Pure in (seed, step, rerolls) so that
    `verify` can recompute it; `legal` is sorted so the result cannot depend
    on dict or file ordering."""
    if not legal:
        return None
    key = f"{seed}:{step}:{rerolls}".encode()
    h = int(hashlib.sha256(key).hexdigest(), 16)
    return sorted(legal)[h % len(legal)]


# ---------------------------------------------------------------- ledger
def load(path):
    with open(path) as f:
        return json.load(f)


def save(path, led):
    with open(path, "w") as f:
        json.dump(led, f, indent=2)
        f.write("\n")


def played_counts(deck, led):
    counts = {c["id"]: 0 for c in deck["cards"]}
    for p in led["plays"]:
        counts[p["played"]] += 1
    return counts


def state_of(deck, led):
    """Everything derivable from the play history. Nothing here is stored."""
    counts = played_counts(deck, led)
    return {
        "counts": counts,
        "spent": B.spent(deck, counts),
        "budget": deck.get("budget"),
        "artifacts": sorted(B.artifacts_of(deck, counts)),
        "terminal": B.is_terminal(deck, counts),
        "legal": sorted(B.legal_moves(deck, counts, lookahead=True)),
        "step": len(led["plays"]) + 1,
    }


def rerolls_spent(led):
    return sum(p.get("rerolls", 0) for p in led["plays"]) + led.get("pending_rerolls", 0)


def current_draw(deck, led):
    st = state_of(deck, led)
    if st["terminal"]:
        return None, st
    return draw(led["seed"], st["step"], led.get("pending_rerolls", 0), st["legal"]), st


# ---------------------------------------------------------------- instruments
def instrument_of(deck, card_id):
    by = {c["id"]: c for c in deck["cards"]}
    return by[card_id].get("instrument")


def digest(text):
    return hashlib.sha256(text.encode("utf-8", "replace")).hexdigest()


def invoke(kind, command, timeout):
    """Run the agent's proposed command and record what actually happened.

    The agent proposes; deterministic code executes and records. The output in
    the ledger is produced by the RUNNER, so the agent cannot forge a result it
    never obtained -- which is the whole difference between an instrument and a
    claim to have used one.

    A nonzero exit is NOT a refusal. A failing test is a result, and EXECUTE
    recording a failure is exactly what the hat is for.
    """
    started = time.time()
    try:
        r = subprocess.run(command, shell=True, capture_output=True,
                           text=True, timeout=timeout)
        out, err, code = r.stdout, r.stderr, r.returncode
    except subprocess.TimeoutExpired:
        out, err, code = "", f"timed out after {timeout}s", 124
    except Exception as e:                                # noqa: BLE001
        out, err, code = "", f"could not execute: {e}", 127
    captured = (out + err)[:STDOUT_CAP]
    return {
        "kind": kind,
        "command": command,
        "exit": code,
        "output": captured,
        "output_sha256": digest(captured),
        "truncated": len(out + err) > STDOUT_CAP,
        "elapsed_s": round(time.time() - started, 3),
    }


def check_instrument_block(deck, card_id, block):
    """A play record's instrument block must have been written by the runner."""
    want = instrument_of(deck, card_id)
    problems = []
    if want is None:
        if block is not None:
            problems.append(f"card '{card_id}' declares no instrument but the "
                            f"ledger carries an instrument block")
        return problems
    if block is None:
        problems.append(f"card '{card_id}' requires a '{want}' instrument and "
                        f"the ledger has no instrument block")
        return problems
    if block.get("kind") != want:
        problems.append(f"instrument kind is '{block.get('kind')}', "
                        f"card '{card_id}' declares '{want}'")
    if not str(block.get("command", "")).strip():
        problems.append(f"instrument block for '{card_id}' records no command")
    if "exit" not in block:
        problems.append(f"instrument block for '{card_id}' records no exit status")
    got = block.get("output", "")
    if digest(got) != block.get("output_sha256"):
        problems.append(f"instrument output for '{card_id}' does not match its "
                        f"recorded sha256 -- the captured output was edited")
    return problems


# ---------------------------------------------------------------- validation
def validate_artifact(deck, card_id, artifact):
    """Exactly the declared fields, each non-empty. Returns a list of problems."""
    by = {c["id"]: c for c in deck["cards"]}
    if card_id not in by:
        return [f"unknown card '{card_id}'"]
    atype = by[card_id]["produces"]
    declared = set(deck["artifacts"][atype]["fields"])
    if not isinstance(artifact, dict):
        return [f"artifact must be an object, got {type(artifact).__name__}"]
    got = set(artifact)
    problems = []
    for f in sorted(declared - got):
        problems.append(f"missing field '{f}' required by artifact '{atype}'")
    for f in sorted(got - declared):
        owner = next((a for a, s in deck["artifacts"].items() if f in s["fields"]), None)
        if owner:
            problems.append(
                f"field '{f}' belongs to artifact '{owner}', not '{atype}' "
                f"-- HAT BLEED: this card is producing another hat's output")
        else:
            problems.append(f"field '{f}' is not declared by any artifact")
    for f in sorted(declared & got):
        v = artifact[f]
        if v is None or (isinstance(v, (str, list, dict)) and len(v) == 0) \
                or (isinstance(v, str) and not v.strip()):
            problems.append(f"field '{f}' is empty")
    return problems


# ---------------------------------------------------------------- commands
def cmd_init(a):
    deck = load(a.deck)
    led = {
        "deck": deck["deck"],
        "deck_version": deck.get("version"),
        "deck_path": a.deck,
        "seed": a.seed,
        "rerolls_allowed": deck.get("rerolls", 0),
        "pending_rerolls": 0,
        "plays": [],
    }
    save(a.ledger, led)
    print(json.dumps({"ok": True, "ledger": a.ledger, "seed": a.seed,
                      "budget": deck.get("budget"),
                      "floor": B.floor_cost(deck)}, indent=2))
    return 0


def cmd_next(a):
    led = load(a.ledger)
    deck = load(led["deck_path"])
    card, st = current_draw(deck, led)
    if st["terminal"]:
        print(json.dumps({"done": True, "plays": len(led["plays"]),
                          "spent": st["spent"]}, indent=2))
        return 0
    by = {c["id"]: c for c in deck["cards"]}
    c = by[card]
    atype = c["produces"]
    print(json.dumps({
        "step": st["step"],
        "drawn": card,
        "role": c["role"],
        "brief": c["brief"],
        "instrument": c.get("instrument"),
        "command_required": c.get("instrument") is not None,
        "produce_artifact": atype,
        "fields_required": deck["artifacts"][atype]["fields"],
        "cost": B.cost_of(c),
        "spent": st["spent"], "budget": st["budget"],
        "legal_alternatives": st["legal"],
        "rerolls_left": led["rerolls_allowed"] - rerolls_spent(led),
    }, indent=2))
    return 0


def cmd_play(a):
    led = load(a.ledger)
    deck = load(led["deck_path"])
    card, st = current_draw(deck, led)
    if st["terminal"]:
        print("*** run is already complete", file=sys.stderr)
        return 1
    if a.card and a.card != card:
        print(f"*** refused: the die drew '{card}', not '{a.card}'. "
              f"Spend a reroll if you want a different move.", file=sys.stderr)
        return 1
    try:
        artifact = json.loads(a.artifact) if a.artifact else load(a.artifact_file)
    except json.JSONDecodeError as e:
        print(f"*** refused: artifact is not valid JSON -- {e}", file=sys.stderr)
        print("      (inline --artifact is fragile in shell; prefer --artifact-file)",
              file=sys.stderr)
        return 1
    problems = validate_artifact(deck, card, artifact)
    if problems:
        print(f"*** refused: artifact for '{card}' is invalid", file=sys.stderr)
        for p in problems:
            print(f"      - {p}", file=sys.stderr)
        return 1

    kind = instrument_of(deck, card)
    block = None
    if kind is not None:
        if not a.command:
            print(f"*** refused: card '{card}' is grounded in a '{kind}' "
                  f"instrument and no --command was supplied.", file=sys.stderr)
            print("      This hat may not be worn on introspection alone.",
                  file=sys.stderr)
            return 1
        block = invoke(kind, a.command, a.timeout)
        print(f"    [{kind}] $ {a.command}", file=sys.stderr)
        print(f"    [{kind}] exit {block['exit']}, "
              f"{len(block['output'])} bytes captured", file=sys.stderr)
    elif a.command:
        print(f"*** refused: card '{card}' declares no instrument, "
              f"so --command is not accepted", file=sys.stderr)
        return 1

    led["plays"].append({
        "n": st["step"], "drawn": card, "played": card,
        "rerolls": led.get("pending_rerolls", 0),
        "artifact": artifact,
        "instrument": block,
    })
    led["pending_rerolls"] = 0
    save(a.ledger, led)
    new = state_of(deck, led)
    print(json.dumps({"ok": True, "played": card, "spent": new["spent"],
                      "budget": new["budget"], "done": new["terminal"]}, indent=2))
    return 0


def cmd_reroll(a):
    led = load(a.ledger)
    deck = load(led["deck_path"])
    if rerolls_spent(led) >= led["rerolls_allowed"]:
        print(f"*** refused: no rerolls left "
              f"({led['rerolls_allowed']} allowed, all spent)", file=sys.stderr)
        return 1
    before, _ = current_draw(deck, led)
    led["pending_rerolls"] = led.get("pending_rerolls", 0) + 1
    led.setdefault("reroll_log", []).append({
        "step": len(led["plays"]) + 1, "away_from": before, "reason": a.reason})
    save(a.ledger, led)
    after, _ = current_draw(deck, led)
    print(json.dumps({"ok": True, "rerolled_away_from": before, "now": after,
                      "reason": a.reason,
                      "rerolls_left": led["rerolls_allowed"] - rerolls_spent(led)},
                     indent=2))
    return 0


def cmd_verify(a):
    """Replay the ledger from an empty state. Every draw is recomputed; every
    artifact is re-validated. This is what makes a hand-edited ledger or a
    bypassed runner detectable."""
    led = load(a.ledger)
    deck = load(led["deck_path"])
    problems = []

    if led.get("deck_version") != deck.get("version"):
        problems.append(f"ledger was written against deck version "
                        f"{led.get('deck_version')}, deck is now {deck.get('version')}")

    replay = {"seed": led["seed"], "plays": [], "pending_rerolls": 0,
              "rerolls_allowed": led["rerolls_allowed"], "deck_path": led["deck_path"]}
    for i, p in enumerate(led["plays"], 1):
        st = state_of(deck, replay)
        if st["terminal"]:
            problems.append(f"play {i} ('{p['played']}') comes after the run ended")
            break
        if p.get("n") != st["step"]:
            problems.append(f"play {i} claims step {p.get('n')}, replay is at {st['step']}")
        expect = draw(led["seed"], st["step"], p.get("rerolls", 0), st["legal"])
        if p.get("drawn") != expect:
            problems.append(f"play {i}: ledger says the die drew '{p.get('drawn')}', "
                            f"replay says '{expect}' -- the draw does not reproduce")
        if p["played"] != p.get("drawn"):
            problems.append(f"play {i}: played '{p['played']}' but drew '{p.get('drawn')}'")
        if p["played"] not in st["legal"]:
            problems.append(f"play {i}: '{p['played']}' was not a legal move "
                            f"(legal were {st['legal']})")
        for bad in validate_artifact(deck, p["played"], p.get("artifact", {})):
            problems.append(f"play {i} ('{p['played']}'): {bad}")
        for bad in check_instrument_block(deck, p["played"], p.get("instrument")):
            problems.append(f"play {i}: {bad}")
        replay["plays"].append(p)

    st = state_of(deck, replay)
    if st["budget"] is not None and st["spent"] > st["budget"]:
        problems.append(f"total spend {st['spent']} exceeds budget {st['budget']}")
    total_rr = sum(p.get("rerolls", 0) for p in led["plays"]) + led.get("pending_rerolls", 0)
    if total_rr > led["rerolls_allowed"]:
        problems.append(f"{total_rr} rerolls spent, only {led['rerolls_allowed']} allowed")

    roles_worn = {next(c["role"] for c in deck["cards"] if c["id"] == p["played"])
                  for p in led["plays"]}
    missing = set(deck.get("required_roles", [])) - roles_worn
    if st["terminal"] and missing:
        problems.append(f"run completed without wearing required roles: {sorted(missing)}")

    print(f"=== verify {a.ledger} ({len(led['plays'])} plays, "
          f"spend {st['spent']}/{st['budget']}, "
          f"{'complete' if st['terminal'] else 'in progress'}) ===")
    if problems:
        for p in problems:
            print(f"*** FAIL {p}")
        print(f"\n*** {len(problems)} LEDGER PROBLEM(S)")
        return 1
    used = [(p["played"], p["instrument"]["kind"], p["instrument"]["exit"])
            for p in led["plays"] if p.get("instrument")]
    print(f"    roles worn: {sorted(roles_worn)}")
    print(f"    instruments invoked: {len(used)}")
    for cid, kind, code in used:
        print(f"      {cid} [{kind}] exit {code}")
    print(f"    rerolls spent: {total_rr}/{led['rerolls_allowed']}")
    print("\nLEDGER VERIFIED")
    return 0


def cmd_log(a):
    led = load(a.ledger)
    deck = load(led["deck_path"])
    by = {c["id"]: c for c in deck["cards"]}
    print(f"=== {led['deck']} v{led['deck_version']}  seed={led['seed']} ===")
    for p in led["plays"]:
        c = by[p["played"]]
        rr = f"  (after {p['rerolls']} reroll)" if p.get("rerolls") else ""
        print(f"  {p['n']:>2}. {c['role']:<8} {p['played']:<12} "
              f"-> {c['produces']}{rr}")
        for k, v in p["artifact"].items():
            s = v if isinstance(v, str) else json.dumps(v)
            print(f"        {k}: {s[:88]}")
    for r in led.get("reroll_log", []):
        print(f"  ! step {r['step']}: rerolled away from '{r['away_from']}' "
              f"-- {r['reason']}")
    st = state_of(deck, led)
    print(f"  spend {st['spent']}/{st['budget']}, "
          f"{'complete' if st['terminal'] else 'in progress'}")
    return 0


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    sub = ap.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("init"); p.set_defaults(fn=cmd_init)
    p.add_argument("--deck", required=True); p.add_argument("--ledger", required=True)
    p.add_argument("--seed", type=int, required=True)

    for name, fn in (("next", cmd_next), ("verify", cmd_verify), ("log", cmd_log)):
        p = sub.add_parser(name); p.set_defaults(fn=fn)
        p.add_argument("--ledger", required=True)

    p = sub.add_parser("play"); p.set_defaults(fn=cmd_play)
    p.add_argument("--ledger", required=True); p.add_argument("--card")
    g = p.add_mutually_exclusive_group(required=True)
    g.add_argument("--artifact"); g.add_argument("--artifact-file")
    p.add_argument("--command", help="required for cards declaring an instrument")
    p.add_argument("--timeout", type=int, default=60)

    p = sub.add_parser("reroll"); p.set_defaults(fn=cmd_reroll)
    p.add_argument("--ledger", required=True); p.add_argument("--reason", required=True)

    a = ap.parse_args()
    return a.fn(a)


if __name__ == "__main__":
    sys.setrecursionlimit(10000)
    raise SystemExit(main())
