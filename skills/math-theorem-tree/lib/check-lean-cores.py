#!/usr/bin/env python3
"""Lean TRUTH check: does the capsule's machine-verification claim have anything behind it?

`lean file.lean && echo ok` is the same shape of hole as `bc ... && echo ok`:

    theorem planted : <anything> := by sorry     -->  exit 0, a WARNING on stderr
    axiom cheat : forall n, n = n + 1            -->  exit 0, and now 3 = 4 is provable
    theorem "core" : (2:Nat) + 2 = 4 := by decide -->  exit 0, and it proves nothing general

Verified by planting all three in a real capsule file (see
`validation/lean-mutation-check.sh`). The exit status catches a BROKEN file --
a syntax error, a genuinely false claim -- and never an UNPROVED or OVERCLAIMED
one. The `sorry` warning does not help on its own: it arrives on the same stream
as benign deprecation warnings, so it has to be grepped for by name.

So this script gates five things:

  1. SOURCE HYGIENE  -- no `sorry`, `admit`, `axiom`, or `native_decide` in the
     .lean file. `axiom` makes everything provable; `native_decide` moves the
     trust base from the kernel to the compiler.
  2. COMPILE         -- `lean` exits 0, emits no `error:`, and emits no
     `declaration uses 'sorry'`. Other warnings are counted and reported, not
     failed -- a deprecation is not an unsound proof.
  3. VOCABULARY      -- `lean_status` comes from a fixed set.
  4. LOCATABILITY    -- every status claiming machine verification carries a
     `lean_ref` naming something a machine can FIND in the .lean file: a
     declaration, or a `/-! ## N.` section header (anonymous `example ... := by
     decide` blocks live in sections and cannot be named any other way).
     A ref that is prose, empty, or points only at a non-Lean file is not
     evidence -- that is the Lean form of "annotate, do not assert".
  5. OVERCLAIM       -- `core` means the GENERAL statement is proved, so its ref
     must name a real declaration whose statement is universally quantified.
     A `core` backed only by a section of `decide` instances is an `instance`.

  Usage: python3 check-lean-cores.py <capsule-root> [--report]

CANONICAL SOURCE: skills/math-theorem-tree/lib/check-lean-cores.py
See docs/verifying-skills.md §5b.
"""
import glob
import os
import re
import subprocess
import sys

# `cited` = proved elsewhere and referenced. `none` = no Lean for this node.
# `stated_not_proved` = a boundary node the capsule states and does not prove.
# The four in MACHINE are claims about THIS capsule's .lean file and must resolve.
MACHINE = {"core", "dim_core", "instance", "partial"}
VOCAB = MACHINE | {"cited", "none", "stated_not_proved"}

BANNED = [
    ("sorry", "`sorry` admits the goal; lean still exits 0"),
    ("admit", "`admit` is `sorry` under another name"),
    ("native_decide", "`native_decide` trusts the compiler, not the kernel"),
]
AXIOM_RE = re.compile(r"^axiom\s+", re.M)
# Two section conventions are in use: `/-! ## N.` doc comments in the math
# capsules, and `-- N. <node>:` line comments in the formula capsules. Anonymous
# `example ... := by decide` blocks can only be referenced by their section, so
# both spellings have to be locatable.
SECTION_RE = re.compile(r"^(?:/-!\s*##|--)\s*([0-9]+)\.", re.M)
# a statement is GENERAL if it binds a variable: `(x : T)`, `{x : T}`, or an
# explicit `forall` / unicode forall.
GENERAL_RE = re.compile(r"[(\{]\s*[A-Za-z_][A-Za-z_0-9']*\s*(?:[A-Za-z_0-9'\s]*)?:|∀|\\forall")


def strip_comments(src):
    src = re.sub(r"/-.*?-/", "", src, flags=re.S)
    return re.sub(r"--[^\n]*", "", src)


def declarations(src):
    """name -> its signature line, including every namespace-qualified spelling."""
    out, ns = {}, []
    for line in src.split("\n"):
        m = re.match(r"^namespace\s+(\S+)", line)
        if m:
            ns.append(m.group(1))
            continue
        if re.match(r"^end\b", line) and ns:
            ns.pop()
            continue
        m = re.match(r"^(?:theorem|lemma|def|abbrev|structure|inductive|instance)\s+"
                     r"([A-Za-z_][A-Za-z_0-9'\.]*)", line)
        if m:
            base = m.group(1)
            out.setdefault(base, line)
            for i in range(len(ns)):
                out.setdefault(".".join(ns[i:] + [base]), line)
    return out


def node_claims(root):
    """(node_id, lean_status, lean_ref) for every node that carries one."""
    try:
        import yaml
    except ImportError:
        print("PyYAML required: pip install pyyaml", file=sys.stderr)
        sys.exit(2)
    for path in sorted(glob.glob(os.path.join(root, "results/*.yaml"))):
        d = yaml.safe_load(open(path)) or {}
        pr = d.get("proof") if isinstance(d.get("proof"), dict) else {}
        st = pr.get("lean_status", d.get("lean_status"))
        rf = pr.get("lean_ref", d.get("lean_ref"))
        yield os.path.basename(path)[:-5], st, ("" if rf is None else str(rf))


def main(argv):
    report = "--report" in argv
    root = os.path.abspath([a for a in argv[1:] if not a.startswith("-")][0])
    leans = sorted(glob.glob(os.path.join(root, "validation/*.lean")))
    if not leans:
        print("check-lean-cores: SKIP -- no validation/*.lean in this capsule")
        return 0

    err, warncount = 0, 0
    def fail(msg):
        nonlocal err
        err += 1
        print("FAIL:", msg)

    src_all, decls, secs = "", {}, set()
    for lean in leans:
        raw = open(lean).read()
        body = strip_comments(raw)
        name = os.path.basename(lean)

        for tok, why in BANNED:
            for m in re.finditer(r"\b" + re.escape(tok) + r"\b", body):
                fail(f"{name}: contains `{tok}` at offset {m.start()} -- {why}")
        for m in AXIOM_RE.finditer(body):
            fail(f"{name}: declares an `axiom` -- it makes every downstream claim provable")

        if os.environ.get("SKIP_LEAN"):
            print(f"  {name}: compile SKIPPED (SKIP_LEAN set)")
        else:
            p = subprocess.run(["lean", lean], capture_output=True, text=True)
            out = p.stdout + p.stderr
            if p.returncode != 0:
                fail(f"{name}: lean exited {p.returncode}\n{out.strip()[:800]}")
            for line in out.splitlines():
                if "error:" in line:
                    fail(f"{name}: {line.strip()}")
                elif "declaration uses 'sorry'" in line or "declaration uses `sorry`" in line:
                    fail(f"{name}: {line.strip()} -- lean still exits 0 for this")
                elif "warning:" in line:
                    warncount += 1

        src_all += raw
        decls.update(declarations(raw))
        secs |= set(SECTION_RE.findall(raw))

    claims = list(node_claims(root))
    if not claims:
        # Formula capsules have no results/*.yaml; they cite Lean from the entry
        # text as "Lean check N", which must name a section that exists.
        cited = set()
        for md in sorted(glob.glob(os.path.join(root, "formulas/*.md"))):
            for m in re.finditer(r"Lean check ([0-9]+)", open(md).read()):
                cited.add(m.group(1))
                if m.group(1) not in secs:
                    fail(f"{os.path.basename(md)}: cites `Lean check {m.group(1)}`, which is not a "
                         f"section of the .lean file (it has {len(secs)})")
        if err:
            print(f"\n{err} problem(s)")
            return 1
        print(f"check-lean-cores: ok ({len(leans)} file(s) compile, {len(secs)} numbered checks, "
              f"{len(cited)} cited from the entries, {warncount} non-sorry warnings)")
        return 0

    counts = {}
    for nid, st, rf in claims:
        key = str(st)
        counts[key] = counts.get(key, 0) + 1
        if st is None:
            continue
        if st not in VOCAB:
            fail(f"{nid}: lean_status {st!r} is not in the vocabulary {sorted(VOCAB)}")
            continue
        if st not in MACHINE:
            continue

        named = [t for t in re.findall(r"[A-Za-z_][A-Za-z_0-9'\.]*", rf)
                 if t in decls or t.split(".")[-1] in decls]
        sections = [s for s in re.findall(r"§\s*([0-9]+)", rf) if s in secs]

        if not rf.strip():
            fail(f"{nid}: lean_status `{st}` with an EMPTY lean_ref -- a claim of machine "
                 f"verification with nothing behind it")
        elif not named and not sections:
            nonlean = re.findall(r"\S+\.(?:bc|md|py|sh)\b", rf)
            if nonlean:
                fail(f"{nid}: lean_status `{st}` but the ref points only at {nonlean[0]} -- "
                     f"that is not Lean evidence")
            else:
                fail(f"{nid}: lean_status `{st}` but the ref names no declaration and no "
                     f"existing section: {rf[:70]!r}")
        elif st in ("core", "dim_core") and not named:
            fail(f"{nid}: `{st}` claims the general statement is proved but its ref names only "
                 f"a section, not a declaration: {rf[:70]!r}")
        elif st == "core":
            general = [n for n in named
                       if GENERAL_RE.search(decls.get(n, decls.get(n.split(".")[-1], "")))]
            if not general:
                fail(f"{nid}: `core` names {named[0]}, whose statement binds no variable -- a "
                     f"closed claim is an `instance`, not a general proof")

    if report:
        print(f"# lean-core triage for {os.path.basename(root)}")
        print(f"# {len(claims)} nodes, statuses: {counts}")
        print(f"# {len(decls)} declaration names, {len(secs)} sections, {warncount} warnings")
        return 0

    if err:
        print(f"\n{err} problem(s) across {len(claims)} nodes")
        return 1
    machine = sum(v for k, v in counts.items() if k in MACHINE)
    print(f"check-lean-cores: ok ({machine} of {len(claims)} nodes claim machine verification, "
          f"all refs resolve; {len(decls)} declarations, {warncount} non-sorry warnings)")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
