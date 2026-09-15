#!/bin/sh
# Falsifiability harness for run_deck.py.
#
# Two classes of defect, and the second is the one that matters:
#
#   REFUSALS  -- the runner declines an illegal play at the time it is made.
#   TAMPER    -- someone edits the ledger, or bypasses the runner entirely.
#                `verify` replays from an empty state and recomputes every
#                draw, so these must not survive.
#
# The tamper class exists because a model that ignores the protocol is the
# expected case, not the exceptional one. A guard that only works when the
# agent cooperates is not a guard.
set -e
cd "$(dirname "$0")"
PY=python3
DECK=decks/diagnose.json
LED=/tmp/role-deck-check.json
ART=/tmp/role-deck-art.json
fails=0
n=0

want_refused () {      # want_refused <name> <command...>
    n=$((n + 1))
    name="$1"; shift
    if "$@" >/dev/null 2>&1; then
        echo "  *** ACCEPTED (should have refused): $name"; fails=$((fails + 1))
    else
        echo "  refused: $name"
    fi
}

want_verify_fail () {  # want_verify_fail <name> <python-tamper>
    n=$((n + 1))
    name="$1"; mut="$2"
    cp "$LED" "$LED.bak"
    $PY - "$LED" <<PYEOF
import json,sys
led=json.load(open(sys.argv[1]))
$mut
json.dump(led,open(sys.argv[1],"w"),indent=2)
PYEOF
    out=$($PY run_deck.py verify --ledger "$LED" 2>&1) && status=0 || status=$?
    if [ "$status" -eq 0 ]; then
        echo "  *** SURVIVED verify: $name"; fails=$((fails + 1))
    else
        why=$(printf '%s\n' "$out" | sed -n 's/^\*\*\* FAIL //p' | head -1)
        echo "  caught: $name"
        echo "          -> $why"
    fi
    mv "$LED.bak" "$LED"
}

echo "=== a clean run of the full deck ==="
$PY run_deck.py init --deck "$DECK" --seed 91137 --ledger "$LED" >/dev/null
i=0
while [ $i -lt 20 ]; do
    i=$((i + 1))
    card=$($PY run_deck.py next --ledger "$LED" \
           | $PY -c 'import json,sys;print(json.load(sys.stdin).get("drawn","DONE"))')
    [ "$card" = DONE ] && break
    # fill every declared field with placeholder prose
    $PY - "$DECK" "$card" "$ART" <<'PYEOF'
import json,sys
deck=json.load(open(sys.argv[1])); card=sys.argv[2]
by={c["id"]:c for c in deck["cards"]}
t=by[card]["produces"]
json.dump({f:f"<{f} for {card}>" for f in deck["artifacts"][t]["fields"]},
          open(sys.argv[3],"w"))
PYEOF
    # cards declaring an instrument may not be played on introspection alone
    inst=$($PY -c 'import json,sys;d=json.load(open(sys.argv[1]));
print(next((c.get("instrument") or "") for c in d["cards"] if c["id"]==sys.argv[2]))' \
        "$DECK" "$card")
    if [ -n "$inst" ]; then
        $PY run_deck.py play --ledger "$LED" --artifact-file "$ART" \
            --command "echo grounded-$card" >/dev/null 2>&1
    else
        $PY run_deck.py play --ledger "$LED" --artifact-file "$ART" >/dev/null
    fi
done
$PY run_deck.py verify --ledger "$LED" >/dev/null \
    && echo "  ok: $(($i - 1)) plays, ledger verifies" \
    || { echo "  *** baseline run does not verify"; exit 1; }
echo

echo "=== refusals (checked mid-run, on a fresh ledger) ==="
$PY run_deck.py init --deck "$DECK" --seed 91137 --ledger "$LED" >/dev/null
DRAWN=$($PY run_deck.py next --ledger "$LED" \
        | $PY -c 'import json,sys;print(json.load(sys.stdin)["drawn"])')

echo '{"scope":"s","symptom":"y"}' > "$ART"
want_refused "an artifact missing a declared field" \
    $PY run_deck.py play --ledger "$LED" --artifact-file "$ART"

echo '{"scope":"s","symptom":"y","stop_condition":"c","candidates":["a","b"]}' > "$ART"
want_refused "HAT BLEED: an artifact carrying another hat's field" \
    $PY run_deck.py play --ledger "$LED" --artifact-file "$ART"

echo '{"scope":"s","symptom":"","stop_condition":"c"}' > "$ART"
want_refused "an empty field (present but unfilled)" \
    $PY run_deck.py play --ledger "$LED" --artifact-file "$ART"

echo '{"scope":"s","symptom":"y","stop_condition":"c"}' > "$ART"
want_refused "playing a card the die did not draw" \
    $PY run_deck.py play --ledger "$LED" --card close --artifact-file "$ART"

echo 'not json at all' > "$ART"
want_refused "an artifact that is not valid JSON" \
    $PY run_deck.py play --ledger "$LED" --artifact-file "$ART"

# burn both rerolls, then ask for a third
$PY run_deck.py reroll --ledger "$LED" --reason "first" >/dev/null
$PY run_deck.py reroll --ledger "$LED" --reason "second" >/dev/null
want_refused "a reroll past the deck's allowance" \
    $PY run_deck.py reroll --ledger "$LED" --reason "third"
echo

echo "=== instrument grounding (refusals at play time) ==="
# advance to a WHITE card, which the deck grounds in `retrieval`
$PY run_deck.py init --deck "$DECK" --seed 91137 --ledger "$LED" >/dev/null
while :; do
    card=$($PY run_deck.py next --ledger "$LED" \
           | $PY -c 'import json,sys;print(json.load(sys.stdin).get("drawn","DONE"))')
    [ "$card" = gather ] && break
    [ "$card" = DONE ] && break
    $PY - "$DECK" "$card" "$ART" <<'PYEOF'
import json,sys
deck=json.load(open(sys.argv[1])); card=sys.argv[2]
t={c["id"]:c for c in deck["cards"]}[card]["produces"]
json.dump({f:f"<{f}>" for f in deck["artifacts"][t]["fields"]}, open(sys.argv[3],"w"))
PYEOF
    $PY run_deck.py play --ledger "$LED" --artifact-file "$ART" >/dev/null
done
echo '{"observations":"o","provenance":"p"}' > "$ART"

want_refused "a grounded hat worn with no --command (introspection in costume)" \
    $PY run_deck.py play --ledger "$LED" --artifact-file "$ART"

$PY run_deck.py play --ledger "$LED" --artifact-file "$ART" --command "true" >/dev/null
echo '{"candidates":["a","b"]}' > "$ART"
want_refused "--command supplied to a card that declares no instrument" \
    $PY run_deck.py play --ledger "$LED" --artifact-file "$ART" --command "true"
echo

echo "=== tamper (the ledger is edited behind the runner's back) ==="
$PY run_deck.py init --deck "$DECK" --seed 91137 --ledger "$LED" >/dev/null
i=0
while [ $i -lt 20 ]; do
    i=$((i + 1))
    card=$($PY run_deck.py next --ledger "$LED" \
           | $PY -c 'import json,sys;print(json.load(sys.stdin).get("drawn","DONE"))')
    [ "$card" = DONE ] && break
    $PY - "$DECK" "$card" "$ART" <<'PYEOF'
import json,sys
deck=json.load(open(sys.argv[1])); card=sys.argv[2]
by={c["id"]:c for c in deck["cards"]}
t=by[card]["produces"]
json.dump({f:f"<{f} for {card}>" for f in deck["artifacts"][t]["fields"]},
          open(sys.argv[3],"w"))
PYEOF
    # cards declaring an instrument may not be played on introspection alone
    inst=$($PY -c 'import json,sys;d=json.load(open(sys.argv[1]));
print(next((c.get("instrument") or "") for c in d["cards"] if c["id"]==sys.argv[2]))' \
        "$DECK" "$card")
    if [ -n "$inst" ]; then
        $PY run_deck.py play --ledger "$LED" --artifact-file "$ART" \
            --command "echo grounded-$card" >/dev/null 2>&1
    else
        $PY run_deck.py play --ledger "$LED" --artifact-file "$ART" >/dev/null
    fi
done

want_verify_fail "a play deleted from the middle of the run" \
    'del led["plays"][3]
for i,p in enumerate(led["plays"],1): p["n"]=i'

want_verify_fail "a field quietly emptied after the fact" \
    'k=sorted(led["plays"][0]["artifact"])[0]
led["plays"][0]["artifact"][k]=""'

want_verify_fail "another hat's field spliced into a stored artifact" \
    'led["plays"][0]["artifact"]["ranking"]="H2 wins"'

want_verify_fail "the recorded draw rewritten to a card the die never showed" \
    'led["plays"][2]["drawn"]=led["plays"][2]["played"]="close"'

want_verify_fail "a whole play forged and appended" \
    'import copy
p=copy.deepcopy(led["plays"][-1]); p["n"]=len(led["plays"])+1
led["plays"].append(p)'

want_verify_fail "the reroll count inflated to justify a different draw" \
    'led["plays"][1]["rerolls"]=5'

want_verify_fail "the instrument block stripped from a grounded play" \
    'for p in led["plays"]:
    if p.get("instrument"): p["instrument"]=None; break'

want_verify_fail "captured instrument output edited after the fact" \
    'for p in led["plays"]:
    if p.get("instrument"): p["instrument"]["output"]="whatever I wanted it to say"; break'

want_verify_fail "an instrument block forged onto an ungrounded card" \
    'for p in led["plays"]:
    if not p.get("instrument"):
        p["instrument"]={"kind":"execution","command":"true","exit":0,
                         "output":"","output_sha256":
                         "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"}
        break'

want_verify_fail "rerolls spent beyond the allowance" \
    'led["rerolls_allowed"]=0
led["plays"][1]["rerolls"]=1'

echo
echo "checked $n case(s)"
if [ "$fails" -eq 0 ]; then
    echo "ALL RUNNER CHECKS PASSED"
else
    echo "*** $fails RUNNER CHECK(S) FAILED" >&2; exit 1
fi
