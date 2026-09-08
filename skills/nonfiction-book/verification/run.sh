#!/bin/sh
# Verification for the nonfiction-book skill.
#
# Exercises the prescribed project system on a worked ~3-chapter mini-book
# ("When Did This Line Change?" -- a guide to reading git history) carried
# through positioning -> claim ledger -> fat outline -> one drafted chapter,
# then:
#   1. asserts the good artifacts PASS every phase gate (check.py, exit 0);
#   2. plants one defect at a time and asserts check.py catches THAT defect
#      (the specific error code appears and the run exits 1);
#   3. confirms the drafted chapter follows the practical-chapter pattern and
#      cites only claim-ledger rows that exist.
#
# Needs: python3 (stdlib only), tsort, sh. ~1 s.

set -eu
here=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
mb="$here/mini-book"
py=${PYTHON:-python3}
pass=0
fail=0

ok()   { pass=$((pass + 1)); printf '  ok    %s\n' "$1"; }
bad()  { fail=$((fail + 1)); printf '  FAIL  %s\n' "$1"; }

echo "1. good mini-book passes every gate"
if out=$("$py" "$here/check.py" "$mb" 2>&1); then
  ok "check.py exits 0"
else
  bad "check.py should exit 0 on the good mini-book"
fi
printf '%s\n' "$out" | sed 's/^/     /'
printf '%s\n' "$out" | grep -q 'PASS: 0 errors' \
  && ok "no errors reported" || bad "expected 'PASS: 0 errors'"

# concept graph is acyclic under the real tsort too
echo
echo "2. concept graph linearises under tsort(1)"
edges=$("$py" - "$mb/fat-outline.json" <<'EOF'
import json, sys
o = json.load(open(sys.argv[1]))
for a, b in o["concept_edges"]:
    print(a, b)
EOF
)
if printf '%s\n' "$edges" | tsort >/dev/null 2>&1; then
  ok "tsort accepts the concept edges (no cycle)"
else
  bad "tsort rejected the concept edges"
fi

echo
echo "3. planted defects are caught"
plant() {   # desc  jq-ish python mutation  expected-code
  desc=$1; mut=$2; code=$3
  tmp=$(mktemp -d)
  cp "$mb"/*.json "$tmp"/
  "$py" - "$tmp" <<EOF
import json, pathlib, sys
d = pathlib.Path(sys.argv[1])
def edit(name, fn):
    p = d / name
    obj = json.loads(p.read_text())
    fn(obj)
    p.write_text(json.dumps(obj, indent=2))
$mut
EOF
  if "$py" "$here/check.py" "$tmp" 2>&1 | grep -q "\[$code\]"; then
    ok "$desc -> [$code]"
  else
    bad "$desc -> expected error code [$code], not found"
    "$py" "$here/check.py" "$tmp" 2>&1 | sed 's/^/       /' || true
  fi
  rm -rf "$tmp"
}

plant "topic-led promise (no reader)" \
  'edit("positioning-brief.json", lambda o: o["promise_check"].__setitem__("who_is_it_for", "everyone interested in git"))' \
  reader-not-concrete

plant "exclusions removed" \
  'edit("positioning-brief.json", lambda o: o.__setitem__("will_not_cover", []))' \
  no-exclusions

plant "only two comps" \
  'edit("positioning-brief.json", lambda o: o.__setitem__("comparable_titles", o["comparable_titles"][:2]))' \
  too-few-comps

plant "unanswered blocking question" \
  'edit("positioning-brief.json", lambda o: o.__setitem__("blocking_questions", ["what git version?"]))' \
  open-blocking-questions

plant "load-bearing claim on a discovery source" \
  'edit("claim-ledger.json", lambda o: (o["claims"][0].__setitem__("source_tier", "discovery")))' \
  discovery-load-bearing

plant "high-confidence cited claim never citation-checked" \
  'edit("claim-ledger.json", lambda o: o["claims"][0].__setitem__("citation_check", "unresolved"))' \
  citation-unverified

plant "claim still blocking enters drafting" \
  'edit("claim-ledger.json", lambda o: o["claims"][1].__setitem__("drafting_status", "blocking"))' \
  claim-blocking

plant "vague chapter outcome (know more about)" \
  'edit("fat-outline.json", lambda o: o["chapters"][0].__setitem__("reader_can_now", "know more about git internals"))' \
  reader-can-now-vague

plant "chapter loses its distinct job" \
  'edit("fat-outline.json", lambda o: o["chapters"][2].__setitem__("distinct_from_neighbours", ""))' \
  chapter-not-distinct

plant "missing through-line transition" \
  'edit("fat-outline.json", lambda o: o["chapters"][1].__setitem__("through_line_transition", ""))' \
  no-through-line

plant "concept graph made cyclic" \
  'edit("fat-outline.json", lambda o: o["concept_edges"].append(["command-choice", "commit-object"]))' \
  concept-cycle

plant "chapter cites a non-existent ledger row" \
  'edit("fat-outline.json", lambda o: o["chapters"][0]["key_evidence"].append("C-99"))' \
  dangling-evidence

plant "two neighbouring chapters make the same claim" \
  'edit("fat-outline.json", lambda o: o["chapters"][1].__setitem__("central_claim_or_skill", o["chapters"][0]["central_claim_or_skill"]))' \
  chapter-repeats-neighbour

echo
echo "4. drafted chapter follows the practical-chapter pattern"
draft="$mb/chapter-2-draft.md"
beats="Hook Problem Principle pickaxe line.log Method Pitfalls Reader.action Transition"
miss=""
for b in $beats; do
  grep -Eiq "$(printf '%s' "$b" | tr '.' ' ')" "$draft" || miss="$miss $b"
done
[ -z "$miss" ] && ok "all expected beats present" || bad "missing beats:$miss"

# every C-xx the draft cites must exist in the ledger
cited=$(grep -oE 'C-[0-9]+' "$draft" | sort -u)
ledger=$("$py" - "$mb/claim-ledger.json" <<'EOF'
import json, sys
print("\n".join(c["id"] for c in json.load(open(sys.argv[1]))["claims"]))
EOF
)
badref=""
for c in $cited; do
  printf '%s\n' "$ledger" | grep -qx "$c" || badref="$badref $c"
done
[ -z "$badref" ] && ok "draft cites only real ledger rows" \
  || bad "draft cites unknown rows:$badref"

echo
echo "-----------------------------------------"
echo "pass=$pass fail=$fail"
[ "$fail" -eq 0 ] || exit 1
