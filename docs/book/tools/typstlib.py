#!/usr/bin/env python3
"""Markdown-ish inline text -> Typst content, for the Part IV/V generators.

The corpus is written in Markdown and the book is Typst, and the two disagree
about `*`, `_`, `#`, `@`, `$`, `[`, `]` and backticks.  The README records that
`**bold**` pasted into Typst renders as two EMPTY bolds while compiling
cleanly — a defect found by looking at the PDF, not the exit code.  This module
exists so that defect cannot come back through a generator, and so the escaping
is tested in one place rather than open-coded twice.

    python3 docs/book/tools/typstlib.py    self-test, exit 1 on any failure
"""
import re

# Escaped everywhere: each of these opens Typst syntax in ordinary text.
SPECIAL = "\\#$@*_<>`[]~"


def esc(s):
    """Escape a plain-text run so Typst sets it verbatim.

    Hyphens and quotes are deliberately NOT escaped: `--` should still set an
    en-dash and `"` should still curl.  A leading `-`, `+` or `=` would start a
    list or heading, so only those are escaped, and only at the start.
    """
    out = "".join("\\" + c if c in SPECIAL else c for c in s)
    return re.sub(r"^([-+=])", r"\\\1", out)


def inline(s):
    """Convert `code`, **strong** and *emph* to Typst; escape everything else.

    Returns Typst markup intended for the inside of a content block.

    Bold and italic RECURSE: `**10 are backed only by `docs/`**` is one bold run
    containing a code span, and escaping its inside wholesale printed the
    backticks as literal characters (found by reading page 79, 2026-09-17 —
    it compiled, and looked deliberate).
    """
    tokens = re.split(r"(`[^`]+`|\*\*.+?\*\*|(?<!\*)\*[^*]+\*(?!\*))", s,
                      flags=re.S)
    out = []
    for i, t in enumerate(tokens):
        if not t:
            continue
        if i % 2 == 0:
            out.append(esc(t))
        elif t.startswith("`"):
            # #raw() takes a Python-style string: only \ and " need escaping,
            # and the Typst special characters inside it are inert.
            body = t[1:-1].replace("\\", "\\\\").replace('"', '\\"')
            out.append(f'#raw("{body}")')
        elif t.startswith("**"):
            out.append(f"#strong[{inline(t[2:-2])}]")
        else:
            out.append(f"#emph[{inline(t[1:-1])}]")
    return "".join(out)


def _selftest():
    """Each case is a real string from the corpus, or the defect it caused."""
    cases = [
        # the README's own bug: bold must not survive as Typst-empty stars
        ("**MINOR** bump", "#strong[MINOR] bump"),
        ("the `test-oracle-design` candidate",
         'the #raw("test-oracle-design") candidate'),
        ("*wrong* — the finding", "#emph[wrong] — the finding"),
        # bare specials that would otherwise open syntax
        ("a #hash and a $dollar", "a \\#hash and a \\$dollar"),
        ("see docs/verifying-skills.md §7", "see docs/verifying-skills.md §7"),
        ("x_1 and a@b", "x\\_1 and a\\@b"),
        ("[bracket] <angle>", "\\[bracket\\] \\<angle\\>"),
        ("- leading dash", "\\- leading dash"),
        # a quote inside code: the #raw() string must not be terminated early
        ('use `grep -qF "*** FAIL"`',
         'use #raw("grep -qF \\"*** FAIL\\"")'),
        # em-dash and quotes are left alone for Typst's own smart handling
        ("it's \"fine\" -- really", "it's \"fine\" -- really"),
        # An UNMATCHED star: not emphasis, so it falls through to esc() and
        # must still be escaped.  Added 2026-09-17 after the mutation test
        # found that removing `*` from SPECIAL left this suite at 10/10 —
        # every star in the suite was inside a matched pair.
        ("2 * 3, and a lone ** pair", "2 \\* 3, and a lone \\*\\* pair"),
        ("`x` then a stray * star", '#raw("x") then a stray \\* star'),
        # Markup INSIDE bold or italic: escaping the run wholesale printed the
        # backticks (page 79, 2026-09-17).
        ("**10 are backed only by `docs/`**",
         '#strong[10 are backed only by #raw("docs/")]'),
        ("*see `run.sh` first*", '#emph[see #raw("run.sh") first]'),
        ("**13 `scope` failures**",
         '#strong[13 #raw("scope") failures]'),
    ]
    bad = 0
    for src, want in cases:
        got = inline(src)
        if got != want:
            bad += 1
            print(f"*** FAIL {src!r}\n     want {want!r}\n     got  {got!r}")
    print(f"typstlib self-test: {len(cases) - bad}/{len(cases)} passed")
    return bad


if __name__ == "__main__":
    raise SystemExit(1 if _selftest() else 0)
