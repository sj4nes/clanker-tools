#!/usr/bin/env python3
"""Every LinAlg.* named in a lean_ref must EXIST in validation/proof-checks.lean.

This is the guard against the `lean_status` drift that the sibling capsules had
to be audited for after the fact.  It runs in build/all.sh, so a ref can never
outlive the declaration it names.
"""
import os, re, sys, glob

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

lean = open("validation/proof-checks.lean").read()
declared = set(re.findall(r"^(?:theorem|def|abbrev|structure)\s+([A-Za-z_][A-Za-z_0-9']*)",
                          lean, re.M))
# structure fields and namespaced defs (M2.mul etc.)
declared |= set(re.findall(r"^def\s+M2\.([A-Za-z_][A-Za-z_0-9']*)", lean, re.M))

ALLOWED_STATUS = {"core", "dim_core", "instance", "partial", "cited", "stated_not_proved"}
err = 0
checked = 0
for f in sorted(glob.glob("results/*.yaml")):
    s = open(f).read()
    node = re.search(r"^node: (.+)$", s, re.M).group(1)
    m = re.search(r"^  lean_status: (.+)$", s, re.M)
    if not m:
        continue
    status = m.group(1).strip()
    if status not in ALLOWED_STATUS:
        print(f"FAIL: {node}: unknown lean_status {status!r}"); err += 1
    r = re.search(r"^  lean_ref: (.+)$", s, re.M)
    ref = r.group(1).strip() if r else "null"
    if ref.startswith("'") and ref.endswith("'"):      # unwrap the YAML scalar
        ref = ref[1:-1].replace("''", "'")             # before matching, else the
                                                       # closing quote is eaten by
                                                       # Lean's legal prime suffix
    names = re.findall(r"LinAlg\.([A-Za-z_][A-Za-z_0-9']*)", ref)
    if status in ("core", "dim_core", "instance", "partial"):
        if not names:
            print(f"FAIL: {node}: status {status} but lean_ref names no LinAlg declaration")
            err += 1
        for n in names:
            checked += 1
            if n not in declared:
                print(f"FAIL: {node}: lean_ref names LinAlg.{n}, which is NOT in proof-checks.lean")
                err += 1
    else:
        for n in names:
            print(f"FAIL: {node}: status {status} must not name a LinAlg declaration ({n})")
            err += 1

if err:
    print(f"check-lean-refs: {err} problem(s)"); sys.exit(1)
print(f"check-lean-refs: ok ({checked} LinAlg references, all resolve; {len(declared)} declarations in proof-checks.lean)")
