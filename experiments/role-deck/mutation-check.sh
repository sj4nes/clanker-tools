#!/bin/sh
# Falsifiability harness for check_deck.py.
#
# A gate that has never been seen to fire is not a gate. This plants one
# defect per gate in a copy of the deck and asserts (a) the checker exits
# nonzero and (b) the SPECIFIC gate names the problem. Other gates may fire
# too -- the defects are not perfectly separable and the report says which.
#
# Same argument as docs/verifying-skills.md §5a/§5b: the hygiene checks pass
# on a deck that is well-formed and wrong.
set -e
cd "$(dirname "$0")"
PY=python3
DECK=decks/diagnose.json
TMP=/tmp/role-deck-mutant.json
fails=0
n=0

plant () {            # plant <name> <expected-gate> <python-mutation>
    n=$((n + 1))
    name="$1"; gate="$2"; mut="$3"
    $PY - "$DECK" "$TMP" <<PYEOF
import json,sys
d=json.load(open(sys.argv[1]))
cards={c["id"]:c for c in d["cards"]}
$mut
json.dump(d,open(sys.argv[2],"w"),indent=2)
PYEOF
    out=$($PY check_deck.py "$TMP" 2>&1) && status=0 || status=$?
    fired=$(printf '%s\n' "$out" | sed -n 's/^\*\*\* FAIL \[\([a-z-]*\)\].*/\1/p' | sort -u | tr '\n' ' ')
    if [ "$status" -eq 0 ]; then
        echo "  *** SURVIVED: $name -- checker exited 0"; fails=$((fails + 1))
    elif ! printf '%s\n' "$fired" | grep -q "$gate"; then
        echo "  *** WRONG GATE: $name -- wanted [$gate], fired [$fired]"; fails=$((fails + 1))
    else
        echo "  caught: $name  ->  [$fired]"
    fi
}

echo "=== baseline: the real deck must PASS ==="
if $PY check_deck.py "$DECK" >/dev/null 2>&1; then
    echo "  ok: decks/diagnose.json passes all gates"
else
    echo "  *** baseline FAILS -- fix the deck before trusting the mutants"; exit 1
fi
echo

echo "=== planted defects ==="

plant "hat bleed: GREEN ships a ranking field owned by the verdict" \
      "exclusivity" \
      'd["artifacts"]["hypotheses"]["fields"].append("ranking")'

plant "precedence cycle: evidence gathering requires the verdict" \
      "acyclic" \
      'cards["gather"]["requires"].append("verdict")'

plant "shortcut card: a terminal that skips the caution hat entirely" \
      "coverage" \
      'd["cards"].append({"id":"guess","role":"BLUE","copies":1,
         "requires":["evidence"],"produces":"verdict","instrument":None,
         "terminal":True,"brief":"just say what it probably is"})
cards["close"]["produces"]="verdict2"
d["artifacts"]["verdict2"]={"fields":["conclusion2","residual2","ranking2"]}'

plant "decorative hat: nothing consumes YELLOW again" \
      "no-orphans" \
      'cards["falsify"]["requires"]=["hypotheses"]'

# Expected `no-deadlock` when first written. It fires `budget-feasible`, which
# is CORRECT and earlier: with no terminal reachable the floor is infinite, so
# the budget gate rejects the deck before the state space is built.
#
# That leaves `no-deadlock` unfirable by any DECK defect, because look-ahead
# legality makes a dead end structurally impossible. It is now an invariant
# assertion on the RULE rather than a gate on the deck -- so it is verified by
# the regression probe below (disable the look-ahead, strands reappear), not by
# a mutation here. An assertion that can never fail is worth labelling as such.
plant "unproducible precondition: the close-out needs an artifact no card makes" \
      "budget-feasible" \
      'd["artifacts"]["signoff"]={"fields":["approver"]}
cards["close"]["requires"].append("signoff")'

plant "undeclared artifact: a card produces a type the deck never declares" \
      "schema" \
      'cards["hunch"]["produces"]="vibes"'

# A card requiring the terminal's own output can never be played, because play
# STOPS at a terminal card. Made terminal itself so it is exempt from the
# orphan gate, and a leaf so it creates no cycle -- which is what isolates
# this defect to `reachable-cards`. The first attempt at this mutation made
# `falsify` require the verdict, which is a CYCLE, so `acyclic` short-circuited
# the state-space gates and the mutation tested nothing it claimed to.
plant "unplayable card: a leaf that requires the terminal's own output" \
      "reachable-cards" \
      'd["artifacts"]["postmortem"]={"fields":["lessons"]}
d["cards"].append({"id":"postmortem","role":"BLUE","copies":1,
   "requires":["verdict"],"produces":"postmortem","instrument":None,
   "terminal":True,"brief":"review the closed diagnosis"})'

plant "budget below the deck's floor: no run can ever complete" \
      "budget-feasible" \
      'd["budget"]=5'

plant "decorative budget: set at or above the whole deck's cost" \
      "budget-binding" \
      'd["budget"]=99'

plant "two producers for one artifact type" \
      "schema" \
      'd["cards"].append({"id":"guess_evidence","role":"WHITE","copies":1,
         "requires":["question"],"produces":"evidence","instrument":None,
         "brief":"assume the observations"})'

# Regression guard for budget.py: the look-ahead is what makes the budget
# safe under an EXTERNAL draw. Turning it off must reintroduce dead ends --
# if this mutation is ever caught by nothing, the look-ahead has stopped
# doing anything and `no-deadlock` has gone vacuous again.
plant "an ungrounded evaluative hat: EXECUTE with no instrument" \
      "instrument-grounding" \
      'cards["run"]["instrument"]=None'

plant "an instrument kind the deck never declares" \
      "instrument-grounding" \
      'cards["gather"]["instrument"]="vibes"'

plant "a zero-weight card: legal for ever, drawn never" \
      "weights" \
      'cards["falsify"]["weight"]=0'

plant "a repeat_decay outside (0, 1]" \
      "weights" \
      'd["repeat_decay"]=1.5'

echo
echo "=== conditional requirements (decks/decide.json) ==="
DEC=decks/decide.json
cplant () {   # cplant <name> <expected-gate> <python-mutation>
    n=$((n + 1))
    name="$1"; gate="$2"; mut="$3"
    $PY - "$DEC" "$TMP" <<PYEOF
import json,sys
d=json.load(open(sys.argv[1]))
cards={c["id"]:c for c in d["cards"]}
$mut
json.dump(d,open(sys.argv[2],"w"),indent=2)
PYEOF
    out=$($PY check_deck.py "$TMP" 2>&1) && status=0 || status=$?
    fired=$(printf '%s\n' "$out" | sed -n 's/^\*\*\* FAIL \[\([a-z-]*\)\].*/\1/p' | sort -u | tr '\n' ' ')
    if [ "$status" -eq 0 ]; then
        echo "  *** SURVIVED: $name"; fails=$((fails + 1))
    elif ! printf '%s\n' "$fired" | grep -q "$gate"; then
        echo "  *** WRONG GATE: $name -- wanted [$gate], fired [$fired]"; fails=$((fails + 1))
    else
        echo "  caught: $name  ->  [$fired]"
    fi
}

cplant "a condition keyed on a field that can never be null" \
       "conditions" \
       'd["artifacts"]["faults"]["nullable"]=[]'

cplant "a decorative condition: it never changes what is legal" \
       "conditions" \
       'd["conditions"][0]["adds_requirement"]={"card":"commit","artifact":"faults"}'

cplant "a condition keyed on a field the artifact does not have" \
       "conditions" \
       'd["conditions"][0]["field"]="imaginary"'

cplant "requires_all on an artifact whose producer is fixed-count" \
       "options" \
       'cards["steelman"].pop("per_option",None)'

cplant "a per-option artifact with no index field" \
       "options" \
       'd["artifacts"]["support"]["fields"]=["steelman"]'

cplant "an option_source with no declared bound" \
       "options" \
       'd["option_source"].pop("max",None)'

cplant "an index field shared by an artifact that is NOT per-option" \
       "exclusivity" \
       'd["artifacts"]["evidence"]["fields"].append("option")'

echo
echo "=== ordering regression (simulate.py) ==="
# The v0.5.0 bug, replanted: with `gather` no longer requiring `hunch`, the die
# is free to schedule the gut call AFTER the evidence -- which every static gate
# passes and which destroys what RED is for. Only the simulator sees it.
$PY - "$DECK" "$TMP" <<'PYEOF'
import json,sys
d=json.load(open(sys.argv[1]))
for c in d["cards"]:
    if c["id"]=="gather": c["requires"]=["question"]
json.dump(d,open(sys.argv[2],"w"),indent=2)
PYEOF
n=$((n + 1))
simout=$($PY simulate.py "$TMP" 400 2>&1) && simstatus=0 || simstatus=$?
if [ "$simstatus" -eq 0 ]; then
    echo "  *** SURVIVED: the hunch may follow the evidence and simulate.py passed"
    fails=$((fails + 1))
else
    echo "  caught: RED scheduled after the evidence"
    printf '%s\n' "$simout" | sed -n 's/^\*\*\* FAIL \[order\] /          -> /p' | head -2
fi

echo
echo "=== regression: disabling look-ahead must reintroduce strands ==="
$PY - <<'PYEOF'
import json, budget as B
d=json.load(open("decks/diagnose.json"))
for la in (True, False):
    ids,seen,edges=B.explore(d, lookahead=la)
    # a state is (counts, flags) since conditional requirements branch the
    # space -- unpacking it as a bare counts tuple made every TERMINAL state
    # look like a strand, which is how this probe reported 8 phantom strands
    strands=sum(1 for st,mv in edges.items()
                if not mv and not B.is_terminal(d,dict(zip(ids,st[0]))))
    print(f"  lookahead={str(la):<5} -> {len(seen):>3} states, {strands:>2} strands")
    if la and strands: raise SystemExit("  *** look-ahead left strands")
    if not la and not strands: raise SystemExit("  *** wall left no strands: gate is vacuous")
print("  ok: the look-ahead rule is load-bearing")
PYEOF

echo
echo "planted $n defect(s)"
if [ "$fails" -eq 0 ]; then
    echo "ALL MUTATIONS CAUGHT"
else
    echo "*** $fails MUTATION(S) NOT CAUGHT CORRECTLY" >&2; exit 1
fi
