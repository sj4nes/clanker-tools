#!/bin/sh
# Mutation check for the LEAN layer: do the checks actually catch an unproved or
# overclaimed core?
#
# `lean file.lean && echo ok` catches a BROKEN file and nothing else. Planted in
# a real capsule file and confirmed at exit 0:
#
#   theorem planted : forall n, n + 0 = n := by sorry   -- warning only, exit 0
#   axiom cheat : forall n, n = n + 1                   -- silent, and 3 = 4 follows
#   theorem "core" : (2:Nat) + 2 = 4 := by decide       -- true, proves nothing general
#
# Only the last of the six mutations below (a genuinely false statement) is
# caught by `lean` itself. The other five are caught by check-lean-cores.py, and
# this file is the regression test proving that it still does.
#
#   Usage: sh lean-mutation-check.sh <capsule-root>
#
# CANONICAL SOURCE: skills/math-theorem-tree/lib/lean-mutation-check.sh
# See docs/verifying-skills.md §5b.
set -eu
lib=$(cd "$(dirname "$0")" && pwd)
cap=$(cd "${1:?usage: lean-mutation-check.sh <capsule-root>}" && pwd)
name=$(basename "$cap")

leanfile=$(ls "$cap"/validation/*.lean 2>/dev/null | head -1 || true)
if [ -z "$leanfile" ]; then
    echo "lean-mutation-check ($name): SKIP -- no validation/*.lean"
    exit 0
fi

work=$(mktemp -d)
trap 'rm -rf "$work"' EXIT INT TERM

reset() {
    rm -rf "$work/cap"; mkdir -p "$work/cap"
    for d in nodes edges results formulas validation indexes sources; do
        [ -e "$cap/$d" ] && cp -R "$cap/$d" "$work/cap/" || true
    done
    mkdir -p "$work/cap/build"
    [ -f "$cap/build/dependencies.sorted.edges" ] && \
        cp "$cap/build/dependencies.sorted.edges" "$work/cap/build/" || true
}
target() { ls "$work/cap"/validation/*.lean | head -1; }

fails=0
planted=0
expect_caught() {
    planted=$((planted + 1))
    if python3 "$lib/check-lean-cores.py" "$work/cap" >/dev/null 2>&1; then
        echo "*** SURVIVED: $1 -- the checks reported success" >&2
        fails=$((fails + 1))
    else
        echo "  caught: $1"
    fi
}

reset
if ! python3 "$lib/check-lean-cores.py" "$work/cap" >/dev/null 2>&1; then
    echo "*** baseline FAILED: the unmutated copy does not pass" >&2
    python3 "$lib/check-lean-cores.py" "$work/cap" >&2 || true
    exit 1
fi
echo "lean-mutation-check ($name): baseline passes; planting defects"

# L1 -- an admitted proof. `lean` exits 0 and only warns.
reset
printf '\ntheorem planted_sorry_mut : ∀ n : Nat, n + 0 = n := by sorry\n' >> "$(target)"
expect_caught "L1 sorry (lean exits 0 for this)"

# L2 -- an axiom. Silent, and it makes anything provable.
reset
printf '\naxiom planted_cheat : ∀ n : Nat, n = n + 1\n' >> "$(target)"
expect_caught "L2 axiom stub (makes 3 = 4 provable, exit 0)"

# L3 -- native_decide moves the trust base off the kernel.
reset
printf '\nexample : (2:Nat) + 2 = 4 := by native_decide\n' >> "$(target)"
expect_caught "L3 native_decide (trusts the compiler, not the kernel)"

# L4 -- a genuinely false statement. The ONE mutation `lean` catches by itself,
# kept as the control that the compile gate is wired up at all.
reset
printf '\ntheorem planted_false_mut : ∀ n : Nat, n + 1 = n := by omega\n' >> "$(target)"
expect_caught "L4 false statement (the control: lean itself rejects this)"

# L5 / L6 need a node that claims machine verification.
claim=$(python3 - "$work/cap" <<'PY'
import glob, os, sys
try:
    import yaml
except ImportError:
    sys.exit(0)
for p in sorted(glob.glob(os.path.join(sys.argv[1], "results/*.yaml"))):
    d = yaml.safe_load(open(p)) or {}
    pr = d.get("proof") if isinstance(d.get("proof"), dict) else {}
    st = pr.get("lean_status", d.get("lean_status"))
    rf = pr.get("lean_ref", d.get("lean_ref"))
    if st in ("core", "dim_core", "instance", "partial") and rf:
        print(os.path.basename(p)[:-5]); break
PY
)

if [ -n "$claim" ]; then
    # L5 -- the ref is emptied: a bare claim of machine verification.
    reset
    python3 - "$work/cap/results/$claim.yaml" <<'PY'
import re, sys
p = sys.argv[1]; s = open(p).read()
open(p, "w").write(re.sub(r"^(\s*lean_ref:).*$", r"\1 null", s, count=1, flags=re.M))
PY
    expect_caught "L5 lean_ref emptied on $claim (claim with nothing behind it)"

    # L6 -- the referenced declaration is renamed out from under the claim. This
    # is the `Prob.markov_finite` failure mode: a header claiming a theorem whose
    # body is no longer there.
    reset
    # rename the declaration THIS claim names -- renaming an unreferenced one
    # proves nothing, and the harness reported a false survivor until it did.
    l6=$(python3 - "$(target)" "$work/cap" <<'PY'
import glob, os, re, sys, yaml
lean, root = sys.argv[1], sys.argv[2]
src = open(lean).read()
decls = set(re.findall(r"^(?:theorem|lemma|def|abbrev)\s+([A-Za-z_][A-Za-z_0-9']*)", src, re.M))
secs = set(re.findall(r"^(?:/-!\s*##|--)\s*([0-9]+)\.", src, re.M))
# L6 needs a ref backed ONLY by declarations: if a section also backs it,
# renaming the declarations leaves the section standing and the claim survives
# legitimately -- that is the checker being right, not a hole.
rf = ""
for p in sorted(glob.glob(os.path.join(root, "results/*.yaml"))):
    d = yaml.safe_load(open(p)) or {}
    pr = d.get("proof") if isinstance(d.get("proof"), dict) else {}
    st = pr.get("lean_status", d.get("lean_status"))
    cand = str(pr.get("lean_ref", d.get("lean_ref")) or "")
    if st not in ("core", "dim_core", "instance", "partial") or not cand:
        continue
    if [x for x in re.findall(r"§\s*([0-9]+)", cand) if x in secs]:
        continue
    if [t for t in re.findall(r"[A-Za-z_][A-Za-z_0-9'.]*", cand) if t.split(".")[-1] in decls]:
        rf = cand
        break
# rename EVERY declaration the ref names. Renaming only the first leaves the
# others resolving, and the check passes -- which is how this harness reported
# a false survivor in three capsules.
hits = {t.split(".")[-1] for t in re.findall(r"[A-Za-z_][A-Za-z_0-9'\.]*", rf)
        if t.split(".")[-1] in decls}
if hits:
    for h in hits:
        src = re.sub(r"\b" + re.escape(h) + r"\b", h + "Renamed", src)
    open(lean, "w").write(src)
else:
    print("L6-NO-TARGET")
PY
)
    if [ "$l6" = "L6-NO-TARGET" ]; then
        echo "  (L6 skipped: this capsule's refs name sections, not declarations)"
    else
        expect_caught "L6 declaration renamed out from under a lean_ref"
    fi
else
    echo "  (L5/L6 skipped: no node in this capsule claims machine verification)"
fi

echo
if [ "$fails" -gt 0 ]; then
    echo "*** lean-mutation-check ($name): $fails of $planted mutations SURVIVED" >&2
    exit 1
fi
echo "lean-mutation-check ($name): ok ($planted/$planted planted defects caught)"
