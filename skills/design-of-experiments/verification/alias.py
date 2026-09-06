"""Fractional-factorial alias structure for a 2^(4-1) design, two ways.

The design-of-experiments SKILL requires that a fractional factorial is never
proposed without its defining relation, resolution, and full alias structure
(references/factorial-and-screening.md). This script derives the alias structure
of the 2^(4-1) design with generator D = ABC by:

  (1) algebra on the defining relation  I = ABCD  (word multiplication mod 2), and
  (2) building the 8-run design matrix and finding which effect columns are
      numerically identical.

Both methods must agree, and the result must show resolution IV: every main
effect clear of every other main effect, two-factor interactions aliased only
in pairs.
"""

import itertools

FACTORS = ["A", "B", "C", "D"]
DEFINING_WORD = frozenset("ABCD")  # I = ABCD


def _word(symbols):
    """Symmetric difference of factor letters == multiplication mod 2 (X^2 = I)."""
    acc = frozenset()
    for s in symbols:
        acc ^= frozenset(s)
    return acc


def alias_of(effect):
    """The alias partner of `effect` under I = ABCD."""
    return "".join(sorted(_word([effect, "".join(sorted(DEFINING_WORD))]))) or "I"


def algebraic_alias_sets():
    effects = []
    for k in range(1, 5):
        for combo in itertools.combinations(FACTORS, k):
            effects.append("".join(combo))
    seen = set()
    sets = []
    for e in effects:
        if e in seen:
            continue
        partner = alias_of(e)
        group = tuple(sorted({e, partner}, key=lambda s: (len(s), s)))
        sets.append(group)
        seen.update(group)
    return sorted(sets, key=lambda g: (len(g[0]), g[0]))


def design_matrix():
    """8 runs: A,B,C full factorial at +/-1; D = A*B*C."""
    rows = []
    for a, b, c in itertools.product((-1, 1), repeat=3):
        rows.append({"A": a, "B": b, "C": c, "D": a * b * c})
    return rows


def column(rows, effect):
    out = []
    for r in rows:
        v = 1
        for ch in effect:
            v *= r[ch]
        out.append(v)
    return tuple(out)


def empirical_alias_sets():
    rows = design_matrix()
    effects = []
    for k in range(1, 5):
        for combo in itertools.combinations(FACTORS, k):
            effects.append("".join(combo))
    by_col = {}
    for e in effects:
        by_col.setdefault(column(rows, e), []).append(e)
    identity_col = tuple([1] * 8)
    groups = []
    for col, es in by_col.items():
        tag = " = ".join(sorted(es, key=lambda s: (len(s), s)))
        if col == identity_col:
            tag = "I = " + tag
        groups.append((sorted(es, key=lambda s: (len(s), s))[0], tag, col))
    return sorted(groups, key=lambda g: (len(g[0]), g[0]))


def resolution(alias_sets):
    """Shortest word in the defining relation == resolution."""
    return len(DEFINING_WORD)


def main():
    print("generator            : D = ABC")
    print("defining relation    : I = ABCD")
    print(f"resolution           : {resolution(None)}  (IV)")
    print()

    algebra = algebraic_alias_sets()
    print("alias sets by algebra (I = ABCD):")
    for g in algebra:
        print("  " + " = ".join(g))
    print()

    empirical = empirical_alias_sets()
    print("alias sets by design-matrix column equality:")
    for _, tag, _ in empirical:
        print("  " + tag)
    print()

    # cross-check: the two methods must produce the same partition of effects
    emp_part = sorted(sorted(tag.split(" = ")) for _, tag, _ in empirical)
    alg_part = sorted(sorted(g) for g in algebra)
    ok_match = alg_part == emp_part
    print(f"algebra == design-matrix partition : {ok_match}")

    # resolution IV checks
    # no main effect aliased with another main effect
    no_main_main = all(
        sum(1 for e in grp if len(e) == 1) <= 1 for grp in alg_part
    )
    # no main effect aliased with a two-factor interaction
    no_main_2fi = all(
        not (any(len(e) == 1 for e in grp) and any(len(e) == 2 for e in grp))
        for grp in alg_part
    )
    print(f"no main effect aliased with another main effect : {no_main_main}")
    print(f"no main effect aliased with a 2-factor interaction: {no_main_2fi}")

    all_ok = ok_match and no_main_main and no_main_2fi
    print()
    print("RESULT:", "PASS" if all_ok else "FAIL")
    return 0 if all_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
