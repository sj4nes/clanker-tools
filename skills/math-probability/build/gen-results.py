#!/usr/bin/env python3
"""Generate results/<id>.yaml and nodes/<id>.md from a single node spec table.

The authoritative dependency list for each node is read from build/node-deps.txt
(derived from the graph), so a YAML can never drift from the edges.  Run:

    python3 build/gen-results.py            # writes every node with a spec
    python3 build/check-consistency.py      # verify against the graph
    sh build/all.sh

Nodes already having a hand-written results/*.yaml (the 6 headline ones) get
their YAML skipped (unless --force) but still get a generated nodes/<id>.md.
The dependency list in every generated YAML is read from build/node-deps.txt
(itself derived from edges/dependencies.edges), so it cannot drift from the graph.
"""
import os, sys, textwrap

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FORCE = "--force" in sys.argv
HEADLINE = {"kolmogorov_axioms", "bayes_theorem", "markov_inequality",
            "chebyshev_inequality", "expectation_linearity", "central_limit_theorem"}

def load_deps():
    d = {}
    p = os.path.join(ROOT, "build", "node-deps.txt")
    for line in open(p):
        line = line.strip()
        if not line:
            continue
        k, rest = line.split(":", 1)
        rest = rest.strip().strip("[]")
        d[k.strip()] = [x.strip() for x in rest.split(",") if x.strip()]
    return d

DEPS = load_deps()

AREA_TITLE = {
    "logic": "logic", "analysis": "analysis", "measure": "measure",
    "probability_space": "probability_space", "random_variable": "random_variable",
    "independence": "independence", "expectation": "expectation",
    "moments": "moments", "inequalities": "inequalities",
    "distributions": "distributions", "convergence": "convergence",
    "conditional_expectation": "conditional_expectation", "boundary": "boundary",
}

def q(s):
    s = str(s).replace("'", "''")
    return "'" + s + "'"

def block_list(key, items, indent=0):
    pad = " " * indent
    if not items:
        return f"{pad}{key}: []\n"
    out = f"{pad}{key}:\n"
    for it in items:
        out += f"{pad}  - {q(it)}\n"
    return out

def block_map(key, d, indent=0):
    pad = " " * indent
    if not d:
        return f"{pad}{key}: {{}}\n"
    out = f"{pad}{key}:\n"
    for k, v in d.items():
        out += f"{pad}  {q(k)}: {q(v)}\n"
    return out

class N:
    ALL = []
    def __init__(self, nid, ntype, area, display, parseable, symbols,
                 tcn, status_label=None, hyps=None, pre=None,
                 welldef=None, equiv=None, proof=None,
                 choice=False, constructive=True, conv_mode=None,
                 solving_for=None, spec=None, cxd=None, misuse=None,
                 related=None, sources=None, status="draft", tcs="well_formed"):
        self.__dict__.update(locals())
        self.hyps = hyps or []
        self.pre = pre or []
        self.spec = spec or []
        self.cxd = cxd or {}
        self.misuse = misuse or []
        self.related = related or {}
        self.sources = sources or ["billingsley_probability_measure", "durrett_pte"]
        self.symbols = symbols or {}
        if status_label is None:
            self.status_label = {
                "definition": "definition", "axiom": "axiom",
                "notation_convention": "definition", "structure": "definition",
                "primitive": "definition", "construction": "constructive_result",
                "identity": "mathematical_identity", "counterexample": "counterexample",
                "example": "example", "bridge": "proved_theorem",
                "lemma": "proved_lemma", "proposition": "proposition",
                "theorem": "proved_theorem", "corollary": "corollary",
            }.get(ntype, "proved_theorem")
        N.ALL.append(self)

    @property
    def deps(self):
        return DEPS.get(self.nid, [])

    def yaml(self):
        o = f"id: {self.area}.{self.nid}\n"
        o += f"node: {self.nid}\n"
        o += f"status_label: {self.status_label}\n"
        o += f"display: {q(self.display)}\n"
        o += f"parseable: {q(self.parseable)}\n"
        if self.conv_mode:
            o += f"convergence_mode: {self.conv_mode}\n"
        o += block_map("symbols", self.symbols)
        o += f"type_check_status: {self.tcs}\n"
        o += f"type_check_note: {q(self.tcn)}\n"
        o += block_list("hypotheses", self.hyps)
        o += block_list("preconditions", self.pre)
        o += block_list("dependencies", self.deps)
        if self.proof:
            tech, derives, lstat, lref = self.proof
            o += "proof:\n"
            o += f"  technique: {q(tech)}\n"
            o += f"  derives_from: {q(derives) if derives else 'null'}\n"
            o += f"  lean_status: {lstat}\n"
            o += f"  lean_ref: {q(lref) if lref else 'null'}\n"
        if self.welldef:
            o += f"well_definedness: {q(self.welldef)}\n"
        if self.equiv:
            o += block_list("equivalent_forms", self.equiv)
        o += f"uses_choice: {'true' if self.choice else 'false'}\n"
        o += f"constructive: {'true' if self.constructive else 'false'}\n"
        if self.solving_for:
            o += f"solving_for: {q(self.solving_for)}\n"
        o += block_list("specialization_cases", self.spec)
        if self.cxd:
            o += "counterexamples_when_dropped:\n"
            for k, v in self.cxd.items():
                o += f"  {k}: {q(v)}\n"
        else:
            o += "counterexamples_when_dropped:\n  none_all_hypotheses_essential: 'every listed hypothesis is used in the proof; see the block above'\n"
        o += block_list("common_misuse", self.misuse)
        if self.related:
            o += "related:\n"
            for k, v in self.related.items():
                if isinstance(v, list):
                    o += f"  {k}: [{', '.join(q(x) for x in v)}]\n"
                else:
                    o += f"  {k}: {q(v)}\n"
        o += block_list("sources", self.sources)
        o += f"status: {self.status}\n"
        o += "checks:\n"
        o += f"  type: validation/type-checks.md#{self.nid}\n"
        o += f"  specialization: validation/specialization-cases.md#{self.nid}\n"
        o += "  instances: validation/instance-checks.bc\n"
        o += f"  proof: validation/proof-checks.md#{self.nid}\n"
        return o

    def md(self):
        o = f"# {self.nid}\n\n## Type\n{self.ntype}\n\n"
        o += f"## Statement\n{self.display}\n\n"
        o += "## Symbols\n"
        for k, v in self.symbols.items():
            o += f"- `{k}` — {v}\n"
        o += f"\n## Epistemic status\n{self.status_label}"
        o += " (non-constructive)" if not self.constructive else ""
        o += " (uses choice)" if self.choice else ""
        o += "\n\n## Prerequisites (tsort edges into this node)\n"
        o += ", ".join(self.deps) if self.deps else "(root)"
        o += "\n\n## Hypotheses\n" + (", ".join(self.hyps) if self.hyps else "(none — unconditional within scope)")
        if self.proof:
            tech, derives, lstat, lref = self.proof
            o += f"\n\n## Proof provenance\ntechnique: {tech}\n"
            o += f"derives_from: {derives}\n" if derives else ""
            o += f"lean_status: {lstat}" + (f" — {lref}" if lref else "") + "\n"
        if self.welldef:
            o += f"\n\n## Well-definedness\n{self.welldef}\n"
        o += f"\n## Type / well-formedness check\n{self.tcn}\n"
        if self.spec:
            o += "\n## Specialization / boundary cases\n" + "".join(f"- {s}\n" for s in self.spec)
        if self.cxd:
            o += "\n## Hypothesis-dropped counterexamples\n" + "".join(f"- **{k}**: {v}\n" for k, v in self.cxd.items())
        if self.misuse:
            o += "\n## Common misuse\n" + "".join(f"- {m}\n" for m in self.misuse)
        if self.related:
            o += "\n## Related nodes (non-prerequisite)\n"
            for k, v in self.related.items():
                o += f"- {k}: {', '.join(v) if isinstance(v, list) else v}\n"
        o += f"\n## Sources\n{', '.join(self.sources)}\n"
        return o


def emit():
    nr = nm = sk = 0
    for n in N.ALL:
        yp = os.path.join(ROOT, "results", n.nid + ".yaml")
        if n.nid in HEADLINE and not FORCE:
            sk += 1
        else:
            open(yp, "w").write(n.yaml()); nr += 1
        mp = os.path.join(ROOT, "nodes", n.nid + ".md")
        open(mp, "w").write(n.md()); nm += 1
    print(f"gen-results: {nr} yaml written, {nm} md written, {sk} headline yaml skipped")
    spec_ids = {n.nid for n in N.ALL}
    missing = [k for k in DEPS if k not in spec_ids] + \
              [k for k in _registry_ids() if k not in spec_ids]
    missing = sorted(set(missing))
    if missing:
        print(f"  NO SPEC YET ({len(missing)}): {' '.join(missing)}")


def _registry_ids():
    p = os.path.join(ROOT, "nodes", "nodes.tsv")
    out = []
    for i, line in enumerate(open(p)):
        if i == 0:
            continue
        out.append(line.split("\t")[0])
    return out


# ============================================================================
#  NODE SPECS  —  by area.  Dependency lists come from the graph, not from here.
#  Sources shorthand.
# ============================================================================
M = ["billingsley_probability_measure", "folland_real_analysis"]
P = ["billingsley_probability_measure", "durrett_pte"]
W = ["williams_probability_martingales", "durrett_pte"]
G = ["grimmett_stirzaker", "durrett_pte"]

# ---------------------------------------------------------------- roots (logic)
N("set_algebra", "primitive", "logic",
  "The Boolean algebra of subsets of a fixed set: union, intersection, complement, difference, De Morgan's laws, and arbitrary (indexed) unions and intersections.",
  "A cup B, A cap B, A^c, bigcup_i A_i, bigcap_i A_i ; De Morgan ; distributivity",
  {"A, B": "subsets of a set Omega, type: element of 2^Omega",
   "{A_i}": "an indexed family, type: I -> 2^Omega"},
  "operations are on subsets of one fixed Omega; an indexed intersection needs I nonempty for the usual identities. Discharged from math-sets-functions-cardinality.",
  welldef="the powerset 2^Omega is a complete Boolean algebra under subset-or-equal; every identity used downstream (De Morgan, distributivity, A = (A cap B) cup (A cap B^c)) holds there.",
  spec=["two sets: A cup A^c = Omega, A cap A^c = empty",
        "indexed: (bigcup_i A_i)^c = bigcap_i A_i^c (De Morgan, arbitrary)"],
  misuse=["intersecting an empty family (gives Omega, not empty)",
          "assuming a sigma-algebra is closed under ARBITRARY unions -- only countable"],
  related={"developed_in": ["math-sets-functions-cardinality"]},
  sources=["enderton_set_theory", "halmos_naive_set_theory"], status="reviewed")

N("preimage_algebra", "primitive", "logic",
  "For any function f, the preimage operator f^{-1} on sets commutes with arbitrary union, arbitrary intersection, and complement: f^{-1}(bigcup B_i) = bigcup f^{-1}(B_i), etc.",
  "f^{-1}(bigcup_i B_i) = bigcup_i f^{-1}(B_i) ; f^{-1}(B^c) = (f^{-1}(B))^c",
  {"f": "any function X -> Y, type: function",
   "B_i": "subsets of the codomain Y, type: element of 2^Y"},
  "f^{-1} here is the preimage OPERATOR ON SETS, defined for every f (not an inverse function). It is a Boolean-algebra homomorphism 2^Y -> 2^X; the forward image is only a join-homomorphism.",
  welldef="f^{-1}(B) := { x : f(x) in B } is defined for every f and every B; the three commutation identities are immediate from the definition of membership.",
  spec=["f measurable iff f^{-1}(generating sets) are all measurable -- this is why the preimage algebra, not the image, drives measurability",
        "image only satisfies f[A cap B] subset f[A] cap f[B], with equality iff f injective"],
  misuse=["expecting the forward image to commute with intersection or complement"],
  related={"developed_in": ["math-sets-functions-cardinality"], "contrast_with": ["image (weaker laws)"]},
  sources=["enderton_set_theory", "folland_real_analysis"], status="reviewed")

N("countable_set", "primitive", "logic",
  "A set is countable if it injects into the natural numbers. Finite sets are countable; a countable union of countable sets is countable (using countable choice); N x N is countable.",
  "|A| <= |N| ; countable union of countable sets is countable",
  {"A": "a set, type: set", "N": "the natural numbers, type: set"},
  "'countable' includes finite here. A countable union of countable sets needs the axiom of countable choice (noted, not used elsewhere in this capsule). Discharged from math-sets-functions-cardinality.",
  welldef="injectivity into N is a well-defined property; the Cantor pairing N x N -> N is an explicit bijection (see instance-checks in the sibling capsule).",
  spec=["Q is countable; the algebraic numbers are countable",
        "a sigma-algebra is closed under countable unions, so it is the natural domain for a countably additive measure"],
  cxd={"countable_choice": "without countable choice it is consistent that a countable union of countable sets of reals is uncountable (Feferman-Levy)"},
  misuse=["assuming R or 2^N is countable (Cantor's diagonal argument: they are not)",
          "confusing 'countable union' with 'arbitrary union'"],
  related={"developed_in": ["math-sets-functions-cardinality"]},
  sources=["enderton_set_theory", "halmos_naive_set_theory"], status="reviewed")

N("real_field", "primitive", "analysis",
  "R is a complete ordered field: the least-upper-bound property holds, giving the Archimedean property, density of Q, monotone convergence, and the nested-interval theorem.",
  "every nonempty bounded-above S subset R has a supremum in R",
  {"R": "the real numbers, type: complete ordered field"},
  "the completeness axiom (lub property) is taken as given; a construction of R (Dedekind cuts / Cauchy completion) is cited to math-real-analysis, not built.",
  welldef="R is the unique complete ordered field up to isomorphism (math-number-systems); [0, inf] is its two-point compactification, the range of a measure.",
  spec=["[0,1] with its order is where every probability P(A) lives",
        "the extended reals [0, inf] carry measure and integral values"],
  misuse=["using the lub property in Q (fails: sup{ q : q^2 < 2 } does not exist in Q)"],
  related={"developed_in": ["math-real-analysis", "math-number-systems"]},
  sources=["rudin_principles", "tao_analysis_I"], status="reviewed")

N("sequence_limit", "primitive", "analysis",
  "Convergence of a real sequence in the epsilon-N sense, with uniqueness of limits, the algebra of limits, the squeeze theorem, and monotone convergence.",
  "x_n -> L :  for all eps>0 exists N, for all n>=N, |x_n - L| < eps",
  {"(x_n)": "a real sequence, type: N -> R", "L": "the limit, type: real"},
  "the quantifier order is 'for all eps EXISTS N' (N may depend on eps); the uniform form ('exists N for all eps') is a different, stronger statement -- relevant to the difference between the convergence modes downstream. Discharged from math-real-analysis.",
  welldef="limits are unique (a Hausdorff fact for R); the algebra of limits (sum, product, quotient with nonzero denominator) is standard.",
  spec=["P(A_n) -> P(A) statements (continuity of probability) are sequence limits in [0,1]",
        "convergence of a series is convergence of its partial-sum sequence"],
  misuse=["swapping the eps and N quantifiers (that is uniform convergence)",
          "assuming a bounded sequence converges (it has a convergent SUBSEQUENCE -- Bolzano-Weierstrass)"],
  related={"developed_in": ["math-real-analysis"]},
  sources=["rudin_principles", "tao_analysis_I"], status="reviewed")

N("limsup_liminf", "primitive", "analysis",
  "limsup and liminf of a real sequence (always defined in the extended reals); for a sequence of SETS, limsup A_n = { omega in infinitely many A_n } = intersection_N union_{n>=N} A_n.",
  "limsup A_n = bigcap_N bigcup_{n>=N} A_n ;  liminf A_n = bigcup_N bigcap_{n>=N} A_n",
  {"(a_n)": "a real sequence, type: N -> R", "(A_n)": "a sequence of events, type: N -> F"},
  "for sets, 'A_n infinitely often' (i.o.) is limsup A_n; 'A_n eventually / all but finitely often' is liminf A_n. Both are events (countable operations on F). Discharged from math-real-analysis.",
  welldef="limsup a_n = inf_N sup_{n>=N} a_n exists in [-inf, +inf]; the set versions are countable unions and intersections, hence in any sigma-algebra containing the A_n.",
  spec=["Borel-Cantelli lemmas are statements about P(limsup A_n)",
        "a_n -> a iff limsup a_n = liminf a_n = a"],
  misuse=["reading limsup A_n as 'the last A_n' -- it is the i.o. event",
          "forgetting liminf A_n subset limsup A_n always"],
  related={"developed_in": ["math-real-analysis"]},
  sources=["rudin_principles", "billingsley_probability_measure"], status="reviewed")

N("series_convergence", "primitive", "analysis",
  "Convergence of an infinite series of reals via its partial sums; the comparison, ratio, and root tests; absolute convergence; the fact that a series of nonnegative terms either converges or diverges to +inf.",
  "sum_{n} a_n := lim_{N} sum_{n=1}^{N} a_n , when the limit exists",
  {"(a_n)": "the terms, type: N -> R", "sum a_n": "the sum, type: real or +inf"},
  "a series of NONNEGATIVE terms always has a sum in [0, +inf] (monotone partial sums) -- this is what makes countable additivity of a measure well-posed. Discharged from math-real-analysis.",
  welldef="the sum is the limit of the monotone (for nonnegative terms) partial-sum sequence; rearrangement is safe for absolutely convergent series only.",
  spec=["countable additivity: P(bigcup A_n) = sum P(A_n) is a convergent series bounded by 1",
        "sum P(A_n) < inf is the hypothesis of the first Borel-Cantelli lemma"],
  misuse=["rearranging a conditionally convergent series (Riemann rearrangement theorem)",
          "assuming a_n -> 0 implies sum a_n converges (harmonic series)"],
  related={"developed_in": ["math-real-analysis"]},
  sources=["rudin_principles", "tao_analysis_I"], status="reviewed")

N("convex_function", "primitive", "analysis",
  "phi: I -> R is convex if phi(t x + (1-t) y) <= t phi(x) + (1-t) phi(y) for all x,y in I and t in [0,1]; equivalently it lies above each of its tangent/supporting lines on the interior.",
  "phi(t x + (1-t) y) <= t phi(x) + (1-t) phi(y)",
  {"phi": "the function, type: I -> R with I an interval",
   "supporting line at c": "an affine L with L(c)=phi(c), L<=phi, type: affine function"},
  "convexity is on an interval I; at an interior point c there is at least one supporting line phi(x) >= phi(c) + m (x - c). Jensen's inequality is exactly 'take x = X, c = E[X], then integrate'. Discharged from math-real-analysis.",
  welldef="a convex function on an open interval is continuous and has one-sided derivatives everywhere; the supporting-line family is nonempty at every interior point.",
  spec=["phi(x) = x^2, |x|, e^{tx} are convex on R -- the cases used for variance, Jensen, and the Chernoff/Hoeffding bounds",
        "phi affine: Jensen holds with equality"],
  cxd={"convexity": "phi(x) = -x^2 (concave): Jensen reverses, phi(E[X]) >= E[phi(X)]"},
  misuse=["applying Jensen with the inequality the wrong way for a concave phi",
          "assuming strict inequality without strict convexity + a non-degenerate X"],
  related={"developed_in": ["math-real-analysis"], "dual_of": ["concave function"]},
  sources=["rudin_principles", "boucheron_lugosi_massart"], status="reviewed")

# ---------------------------------------------------------------- measure
N("sigma_algebra", "definition", "measure",
  "A family F of subsets of Omega is a sigma-algebra if Omega in F, F is closed under complement, and F is closed under countable unions (hence countable intersections).",
  "Omega in F ; A in F => A^c in F ; A_1,A_2,... in F => bigcup_n A_n in F",
  {"Omega": "the sample space, type: set", "F": "the family of events, type: subset of 2^Omega"},
  "closure is under COUNTABLE unions, not arbitrary; the three axioms give closure under countable intersection and set difference. The pair (Omega, F) is a measurable space.",
  welldef="{empty, Omega} is a sigma-algebra and 2^Omega is a sigma-algebra, so the notion is non-vacuous; an arbitrary intersection of sigma-algebras is a sigma-algebra, which is what makes sigma(C) well-defined.",
  spec=["Omega countable: F = 2^Omega is the usual choice",
        "Omega = R: F = B(R), strictly smaller than 2^R (non-measurable sets exist under AC)"],
  cxd={"countable_union_closure": "the family of finite-or-cofinite subsets of N is closed under complement and FINITE unions but not countable ones -- it is an algebra, not a sigma-algebra"},
  misuse=["assuming closure under arbitrary unions",
          "treating every subset of an uncountable Omega as an event"],
  related={"generalizes": ["algebra of sets (finite closure only)"], "special_case_of": ["Dynkin lambda-system + closure under intersection"]},
  sources=M, status="reviewed")

N("generated_sigma_algebra", "construction", "measure",
  "For any collection C of subsets of Omega, sigma(C) is the smallest sigma-algebra containing C -- the intersection of all sigma-algebras that contain C.",
  "sigma(C) = bigcap { G : G a sigma-algebra, C subset G }",
  {"C": "a collection of subsets, type: subset of 2^Omega", "sigma(C)": "the generated sigma-algebra, type: sigma-algebra"},
  "the intersection is over a nonempty family (2^Omega always qualifies), so sigma(C) exists and is itself a sigma-algebra; it is the unique smallest one.",
  welldef="an arbitrary intersection of sigma-algebras on Omega is a sigma-algebra (each axiom is preserved under intersection); 2^Omega contains C, so the family intersected is nonempty.",
  proof=("intersect all sigma-algebras containing C; verify the intersection is a sigma-algebra and is contained in every other such -- hence smallest", "sigma_algebra", "cited", None),
  spec=["C = { (-inf, x] : x in Q }: sigma(C) = B(R)",
        "C = a single set A: sigma(C) = { empty, A, A^c, Omega }"],
  misuse=["trying to describe sigma(C)'s members explicitly -- usually impossible; work via the pi-lambda theorem instead",
          "confusing 'generated by' with 'the algebra generated by' (finite operations)"],
  related={"used_by": ["borel_sigma_algebra", "independence_sigma_algebras"]},
  sources=M, status="reviewed")

N("borel_sigma_algebra", "definition", "measure",
  "B(R) is the sigma-algebra generated by the open intervals of R (equivalently by the open sets, or by the half-lines (-inf, x]). B(R^d) is generated by the open boxes.",
  "B(R) = sigma({ open intervals }) = sigma({ (-inf, x] : x in R })",
  {"B(R)": "the Borel sets of R, type: sigma-algebra on R", "R^d": "Euclidean d-space, type: set"},
  "the half-lines form a pi-system generating B(R); this is why a CDF (a function of the half-lines) determines the whole law. Every set one can 'write down' -- intervals, countable unions, F-sigma, G-delta -- is Borel.",
  welldef="all listed generating collections yield the same sigma-algebra (each contains a countable subfamily generating the others); B(R) is a proper subset of 2^R (a Vitali set is not Borel, using AC).",
  spec=["singletons {x} = bigcap_n (x-1/n, x+1/n) are Borel, so every countable set is Borel and Borel-null under Lebesgue measure",
        "B(R^d) = B(R) tensor ... tensor B(R), the product sigma-algebra"],
  cxd={"generated_by_a_pi_system": "if one generates from a collection that is not a pi-system, the pi-lambda uniqueness argument for measures fails"},
  misuse=["assuming every subset of R is Borel", "confusing Borel with Lebesgue-measurable (the latter is the completion, strictly larger)"],
  related={"special_case_of": ["generated_sigma_algebra"], "completed_to": ["Lebesgue sigma-algebra"]},
  sources=M, status="reviewed")

N("measurable_space", "structure", "measure",
  "A measurable space is a pair (Omega, F) where F is a sigma-algebra on Omega. Its members are the measurable sets (events).",
  "(Omega, F) with F a sigma-algebra on Omega",
  {"Omega": "underlying set, type: set", "F": "sigma-algebra, type: subset of 2^Omega"},
  "no measure is attached yet; a measurable space is the domain on which measures and measurable functions are defined.",
  welldef="any set with any sigma-algebra on it is a measurable space; morphisms are measurable functions (preimage of measurable is measurable).",
  spec=["(R, B(R)) is the canonical target for a real random variable",
        "(Omega, {empty, Omega}) -- the trivial sigma-algebra: only constants are measurable"],
  misuse=["conflating the measurable space with the probability space (which adds P)"],
  related={"category": ["objects of Meas; morphisms are measurable maps"]},
  sources=M, status="reviewed")

N("measure", "definition", "measure",
  "A measure on (Omega, F) is a function mu: F -> [0, inf] with mu(empty) = 0 that is countably additive: for pairwise-disjoint A_1, A_2, ... in F, mu(bigcup_n A_n) = sum_n mu(A_n).",
  "mu(empty) = 0 ; disjoint (A_n) => mu(bigcup A_n) = sum mu(A_n)",
  {"mu": "the measure, type: F -> [0, inf]", "(A_n)": "a countable disjoint family, type: N -> F"},
  "countable additivity is over a COUNTABLE disjoint family; the sum is a series in [0, inf] and always has a value. mu is sigma-finite if Omega is a countable union of finite-measure sets -- the hypothesis of Radon-Nikodym and Fubini.",
  welldef="mu(empty) = 0 follows from countable additivity unless mu is identically +inf; monotonicity and countable subadditivity are consequences. Counting measure, Lebesgue measure, and Dirac delta_x are the standard examples.",
  spec=["mu(Omega) = 1: a probability measure (kolmogorov_axioms)",
        "mu = counting measure on a countable Omega: mu(A) = |A|",
        "mu = delta_x: mu(A) = 1 if x in A else 0"],
  cxd={"countable_additivity": "a merely finitely additive set function (e.g. a Banach limit / finitely additive extension of density on N) is not a measure and breaks continuity from below and Borel-Cantelli"},
  misuse=["assuming finite additivity is enough", "forgetting sigma-finiteness for Radon-Nikodym / Fubini",
          "treating mu(A) = inf results carelessly in subtractions"],
  related={"specializes_to": ["probability_measure"], "generalizes": ["finitely additive set function"]},
  sources=M, status="reviewed")

N("dynkin_pi_lambda", "theorem", "measure",
  "If P is a pi-system (closed under finite intersection) and L is a lambda-system (contains Omega, closed under proper differences and increasing countable unions) with P subset L, then sigma(P) subset L.",
  "P pi-system, L lambda-system, P subset L  =>  sigma(P) subset L",
  {"P": "a pi-system, type: subset of 2^Omega", "L": "a lambda-system, type: subset of 2^Omega"},
  "the standard uniqueness engine: two measures agreeing on a generating pi-system (and on Omega, if finite) agree on the whole sigma-algebra -- because the agreement set is a lambda-system.",
  proof=("let L' be the smallest lambda-system containing P; show L' is closed under intersection (fix A in L', the sets B with A cap B in L' form a lambda-system containing P), hence L' is a sigma-algebra, so sigma(P) = L' subset L", "sigma_algebra", "cited", "Billingsley Thm 3.2; Durrett A.1.4"),
  spec=["two probability measures equal on { (-inf, x] : x in R } are equal on B(R) -- this proves cdf_determines_law",
        "independence checked on generating pi-systems extends to the generated sigma-algebras (independence_factorization)"],
  cxd={"pi_system": "measures can agree on a generating collection that is NOT a pi-system yet differ: on Omega={1,2,3,4}, uniform vs the measure (3/8,1/8,1/8,3/8) agree on {1,2} and {1,3} but not on {1} = {1,2} cap {1,3}"},
  misuse=["applying it when the generating family is not intersection-closed",
          "forgetting the 'agree on Omega' clause for finite (non-probability) measures"],
  related={"used_by": ["cdf_determines_law", "independence_factorization", "mgf_uniqueness"]},
  sources=["billingsley_probability_measure", "durrett_pte"], status="reviewed")

N("lebesgue_measure_caratheodory", "construction", "measure",
  "There is a unique measure lambda on B(R) with lambda([a,b]) = b - a. It is built by extending interval length to an outer measure lambda* on all of 2^R, then restricting to the Caratheodory-measurable sets, which include B(R).",
  "exists! lambda on B(R) with lambda((a,b]) = b - a ; translation-invariant, sigma-finite",
  {"lambda": "Lebesgue measure, type: measure on B(R)", "lambda*": "Lebesgue outer measure, type: 2^R -> [0, inf]"},
  "CITED. lambda is sigma-finite (R = bigcup [-n, n]) and translation-invariant; it is the reference measure for 'absolutely continuous' random variables and densities. Non-measurable sets (Vitali) exist, using AC.",
  proof=("Caratheodory extension theorem: an outer measure's Caratheodory-measurable sets form a sigma-algebra on which it is a complete measure; interval length is a premeasure on the algebra of finite unions of intervals, so it extends; pi-lambda gives uniqueness on B(R)", "dynkin_pi_lambda", "cited", "Folland Real Analysis 2e Thm 1.14, 1.19; Billingsley Thm 12.4"),
  choice=True, constructive=False,
  spec=["lambda restricted to [0,1] is the uniform probability measure -- the model probability space",
        "lambda({x}) = 0, lambda(Q) = 0, lambda(Cantor set) = 0 -- uncountable null sets exist"],
  cxd={"caratheodory_measurability": "lambda* is only finitely subadditive-not-additive on all of 2^R; a Vitali set V has lambda*(V) > 0 but the translates of V partition [0,1] into countably many congruent pieces, so countable additivity would force a contradiction -- V is not measurable"},
  misuse=["assuming every subset of R has a Lebesgue measure", "confusing lambda (on B(R)) with its completion (Lebesgue sigma-algebra)"],
  related={"uses": ["axiom_of_choice (for non-measurable sets, not for lambda itself)"], "extends": ["interval length"]},
  sources=["folland_real_analysis", "billingsley_probability_measure"], status="reviewed")

N("measure_monotonicity", "proposition", "measure",
  "For a measure mu: A subset B implies mu(A) <= mu(B); and mu is countably subadditive: mu(bigcup_n A_n) <= sum_n mu(A_n) for any (not necessarily disjoint) A_n.",
  "A subset B => mu(A) <= mu(B) ;  mu(bigcup A_n) <= sum mu(A_n)",
  {"mu": "a measure, type: F -> [0, inf]", "(A_n)": "any countable family in F, type: N -> F"},
  "monotonicity uses mu(B) = mu(A) + mu(B \\ A) >= mu(A); subadditivity disjointifies B_n = A_n \\ (A_1 cup ... cup A_{n-1}) then uses countable additivity + monotonicity.",
  proof=("monotonicity: B = A disjoint-union (B minus A), additivity, mu >= 0. Subadditivity: replace A_n by disjoint B_n subset A_n with the same union; sum mu(B_n) <= sum mu(A_n)", "measure", "core", "validation/proof-checks.lean Prob.union_bound (the two-set case)"),
  spec=["mu = P: P(A) <= P(B) and P(A) in [0,1]; Boole's inequality is the probability form of subadditivity",
        "equality in subadditivity iff the A_n are pairwise disjoint (mod null sets)"],
  cxd={"nonnegativity_of_mu": "for a signed measure monotonicity fails: a set of negative measure can contain one of positive measure"},
  misuse=["expecting equality in the union bound (usually strict)",
          "using it for mu(A \\ B) = mu(A) - mu(B) without mu(B) < inf and B subset A"],
  related={"used_by": ["boole_inequality", "borel_cantelli_first"]},
  sources=M, status="reviewed")

N("measure_continuity", "proposition", "measure",
  "Continuity from below: A_n increasing to A implies mu(A_n) -> mu(A). Continuity from above: A_n decreasing to A with mu(A_1) < inf implies mu(A_n) -> mu(A).",
  "A_n up A => mu(A_n) -> mu(A) ;  A_n down A, mu(A_1) < inf => mu(A_n) -> mu(A)",
  {"(A_n)": "a monotone sequence of events, type: N -> F", "A": "the limit set bigcup A_n or bigcap A_n, type: element of F"},
  "continuity from below telescopes A = disjoint-union of (A_n \\ A_{n-1}) and applies countable additivity; continuity from above applies it to the complements and needs mu(A_1) < inf to subtract.",
  proof=("from below: write A_n \\ A_{n-1} disjoint, mu(A) = sum = lim of partial sums = lim mu(A_n). From above: apply the from-below result to A_1 \\ A_n up A_1 \\ A", "measure", "cited", "Billingsley Thm 10.2"),
  spec=["mu = P: continuity_of_probability, no finiteness caveat needed (P <= 1)",
        "cdf right-continuity: F_X(x_n) -> F_X(x) for x_n decreasing to x, via { X <= x_n } down { X <= x }"],
  cxd={"finite_measure_for_continuity_from_above": "Lebesgue measure, A_n = [n, inf): A_n down empty but lambda(A_n) = inf for all n, so lambda(A_n) does not converge to lambda(empty) = 0"},
  misuse=["dropping the mu(A_1) < inf hypothesis for continuity from above",
          "assuming continuity for a non-monotone sequence (use limsup/liminf and Fatou-type bounds)"],
  related={"specializes_to": ["continuity_of_probability", "cdf_properties"]},
  sources=M, status="reviewed")

N("null_set", "definition", "measure",
  "A null set (mu-null set) is a set N in F with mu(N) = 0. A property holds mu-almost everywhere (a.e.) if the set where it fails is contained in a null set.",
  "N in F, mu(N) = 0 ;  'P a.e.' :  mu({ omega : not P(omega) }) = 0",
  {"N": "a null set, type: element of F with measure 0", "mu": "the ambient measure, type: measure"},
  "a countable union of null sets is null (countable subadditivity) -- this is why 'a.e.' statements can be combined countably. A measure is complete if every subset of a null set is measurable (Lebesgue measure's completion adds exactly these).",
  welldef="mu(N) = 0 is well-defined; the a.e. quantifier is closed under countable conjunction: if P_n holds a.e. for each n, then all P_n hold simultaneously a.e.",
  spec=["mu = P: a P-null set is the complement of an almost-sure event; 'a.e.' becomes 'almost surely'",
        "Lebesgue: Q is null, so 'x irrational' holds Lebesgue-a.e."],
  cxd={"countability_of_the_union": "an UNCOUNTABLE union of null sets need not be null: R = bigcup_{x} {x}, each {x} Lebesgue-null, but lambda(R) = inf"},
  misuse=["combining uncountably many a.e. statements", "assuming a null set is empty or countable (the Cantor set is uncountable and Lebesgue-null)"],
  related={"used_by": ["almost_sure", "expectation_monotonicity", "conditional_expectation_abstract"]},
  sources=M, status="reviewed")

N("almost_sure", "notation_convention", "measure",
  "An event A holds almost surely (a.s.) if P(A) = 1, equivalently if its complement is a P-null set. Convergence, equality, and inequalities of random variables are all understood in the a.s. sense unless stated otherwise.",
  "A a.s.  <=>  P(A) = 1  <=>  P(A^c) = 0",
  {"A": "an event, type: element of F", "P": "the probability measure, type: F -> [0,1]"},
  "'a.s.' is 'a.e.' for a probability measure. Countably many a.s. events hold simultaneously a.s. (their intersection has probability 1). X = Y a.s. means P(X = Y) = 1; it is an equivalence relation on random variables and is the identification used to define L^p and E[X | G].",
  welldef="P(A) = 1 is well-defined; the a.s. quantifier is closed under countable intersection: P(bigcap A_n) = 1 if P(A_n) = 1 for all n (complement is a countable union of null sets).",
  spec=["X_n -> X a.s. is the strongest of the four convergence modes",
        "E[X | G] is defined only up to a.s. equality"],
  cxd={"countable_intersection_only": "an uncountable family of a.s. events can have intersection of probability 0: on [0,1] uniform, A_x = { omega != x } has P(A_x) = 1 but bigcap_x A_x = empty"},
  misuse=["reading 'a.s.' as 'always' -- a.s. events can fail on a nonempty (null) set",
          "intersecting uncountably many a.s. events (e.g. 'X_t continuous in t' needs a separate argument -- separability / a continuous modification)"],
  related={"specializes": ["null_set"], "used_by": ["convergence_almost_sure", "strong_law_large_numbers"]},
  sources=P, status="reviewed")

N("abstract_integral", "bridge", "measure",
  "For a measure space (Omega, F, mu) and a measurable f: Omega -> [0, inf], integral f dmu is defined as sup over simple 0 <= s <= f of integral s dmu; for general f it is integral f^+ dmu - integral f^- dmu when at least one part is finite. f is integrable if integral |f| dmu < inf.",
  "integral f dmu := sup { integral s dmu : s simple, 0 <= s <= f }  (f >= 0)",
  {"f": "a measurable function, type: Omega -> R (or [0, inf])", "mu": "the measure, type: measure on F", "integral f dmu": "the integral, type: real or +-inf"},
  "CITED, not constructed. The integral is linear, monotone, and satisfies MCT / DCT / Fatou; E[X] is this integral against P. f measurable is required for the sup to be over a well-defined set.",
  proof=("standard three-step construction: indicators -> nonnegative simple functions (finite sums) -> nonnegative measurable via MCT -> integrable via f = f^+ - f^-", None, "cited", "Folland Real Analysis 2e SS2.2-2.4; Billingsley SS15-16"),
  spec=["mu = P: integral X dP = E[X]",
        "mu = counting measure on N: integral f dmu = sum_n f(n) -- series are integrals",
        "f = 1_A: integral 1_A dmu = mu(A)"],
  cxd={"measurability_of_f": "a non-measurable f has no well-defined integral -- the defining sup is over an ill-specified family and Fubini/Tonelli fail"},
  misuse=["swapping limit and integral without MCT/DCT/Fatou justification",
          "assuming integral f dmu is finite for every measurable f"],
  related={"specializes_to": ["expectation"], "developed_in": ["a future math-measure-and-integration capsule"]},
  sources=["folland_real_analysis", "billingsley_probability_measure"], status="reviewed")

for _bn, _disp, _stmt in [
  ("monotone_convergence_theorem",
   "If 0 <= f_n increases pointwise to f (all measurable), then integral f_n dmu increases to integral f dmu.",
   "0 <= f_n up f  =>  integral f_n dmu up integral f dmu"),
  ("dominated_convergence_theorem",
   "If f_n -> f a.e. and |f_n| <= g a.e. for an integrable g, then f is integrable and integral f_n dmu -> integral f dmu (and integral |f_n - f| dmu -> 0).",
   "f_n -> f a.e., |f_n| <= g integrable  =>  integral f_n dmu -> integral f dmu"),
  ("fatou_lemma",
   "For measurable f_n >= 0, integral (liminf f_n) dmu <= liminf integral f_n dmu.",
   "f_n >= 0  =>  integral liminf f_n dmu <= liminf integral f_n dmu"),
  ("fubini_tonelli",
   "For sigma-finite mu, nu: if f >= 0 (Tonelli) or f is (mu x nu)-integrable (Fubini), the double integral equals both iterated integrals.",
   "integral f d(mu x nu) = integral integral f dmu dnu = integral integral f dnu dmu"),
  ("radon_nikodym",
   "If nu << mu (nu(A) = 0 whenever mu(A) = 0) with mu, nu sigma-finite, there is a mu-a.e.-unique measurable h >= 0 with nu(A) = integral_A h dmu. h = dnu/dmu.",
   "nu << mu, sigma-finite  =>  exists h >= 0, nu(A) = integral_A h dmu  (h a.e. unique)"),
]:
  _cx = {
    "monotone_convergence_theorem": {"monotonicity_f_n_up": "f_n = 1_{[n, n+1]} -> 0 pointwise but integral f_n = 1 not -> 0 (not monotone; DCT also fails, no dominating integrable g)"},
    "dominated_convergence_theorem": {"integrable_dominator_g": "f_n = n 1_{(0, 1/n]} on ([0,1], lambda): f_n -> 0 a.e. but integral f_n = 1; no integrable g dominates (sup_n f_n is not integrable)"},
    "fatou_lemma": {"nonnegativity_f_n": "f_n = -1_{[n,n+1]}: liminf f_n = 0 with integral 0, but liminf integral f_n = -1 -- the inequality direction needs f_n >= 0"},
    "fubini_tonelli": {"sigma_finiteness_or_integrability": "f(x,y) = (x^2 - y^2)/(x^2 + y^2)^2 on (0,1)^2: the two iterated integrals are +pi/4 and -pi/4 -- f is not integrable, so Fubini does not apply"},
    "radon_nikodym": {"absolute_continuity_nu_ll_mu": "nu = delta_0, mu = Lebesgue on R: nu({0}) = 1 but mu({0}) = 0, so nu is NOT << mu and has no density; nu is purely singular"},
  }[_bn]
  N(_bn, "bridge", "measure", _disp, _stmt,
    {"f_n, f": "measurable functions, type: Omega -> R", "mu": "a (sigma-finite) measure, type: measure"},
    "CITED. The exchange-of-limit toolkit for the integral; each is stated for a general measure and specialised to P for expectations (MCT/DCT/Fatou for E, Fubini for E[XY] and convolutions).",
    proof=("cited construction from the abstract integral", "abstract_integral", "cited", "Folland Real Analysis 2e ch. 2; Billingsley SS16"),
    spec=["mu = P: the probability form used for E[lim] = lim E, differentiating an MGF, and Scheffe's lemma"],
    cxd=_cx,
    misuse=["applying the wrong theorem for the situation (MCT needs monotone; DCT needs a dominator; Fatou only gives an inequality)"],
    related={"developed_in": ["a future math-measure-and-integration capsule"]},
    sources=["folland_real_analysis", "billingsley_probability_measure"], status="reviewed")

# ---------------------------------------------------------------- probability_space
N("probability_measure", "definition", "probability_space",
  "A probability measure is a measure P on (Omega, F) with P(Omega) = 1. So P: F -> [0,1], P(empty) = 0, and P is countably additive.",
  "P a measure on F with P(Omega) = 1",
  {"P": "the probability measure, type: F -> [0,1]", "(Omega, F)": "a measurable space, type: measurable space"},
  "the only change from a general measure is the normalization P(Omega) = 1, which forces P <= 1 everywhere and removes every finiteness caveat (continuity from above always holds).",
  welldef="a measure with P(Omega) = 1 exists on any measurable space (e.g. a Dirac point mass); the constraint is consistent and non-vacuous.",
  spec=["Omega finite: P given by a pmf on Omega", "P = lambda restricted to [0,1]: the uniform model space"],
  cxd={"normalization": "drop P(Omega)=1 and expectations are no longer weighted averages; Bayes' normalizing constant is meaningless"},
  misuse=["forgetting P is countably (not just finitely) additive", "assuming P(A) > 0 for every nonempty A"],
  related={"specializes": ["measure"], "used_by": ["probability_space", "kolmogorov_axioms"]},
  sources=P, status="reviewed")

N("probability_space", "structure", "probability_space",
  "A probability space is a triple (Omega, F, P): a sample space Omega, an event sigma-algebra F, and a probability measure P on F.",
  "(Omega, F, P) with F a sigma-algebra and P a probability measure",
  {"Omega": "sample space, type: set", "F": "events, type: sigma-algebra", "P": "probability, type: F -> [0,1]"},
  "the single object every probabilistic statement is implicitly relative to. Random variables are measurable maps out of it; independence and conditioning are properties of sub-sigma-algebras of F.",
  welldef="any (Omega, F) with any probability measure P is a probability space; the canonical one for a real random variable with law mu is (R, B(R), mu).",
  spec=["([0,1], B, lambda): supports a random variable of ANY law via the quantile transform (probability_integral_transform)",
        "(Omega, {empty, Omega}, P): only P(empty)=0, P(Omega)=1 -- no non-trivial events"],
  cxd={"F_a_sigma_algebra": "if F is only an algebra, countable additivity has no content and the limit theorems (which are about countable families) cannot even be stated"},
  misuse=["changing Omega mid-argument without a coupling", "assuming a single Omega carries an uncountable family of independent variables without checking (it can, but needs a product construction)"],
  related={"used_by": ["random_variable", "stochastic_process"]},
  sources=P, status="reviewed")

N("finite_additivity", "proposition", "probability_space",
  "For pairwise-disjoint A_1, ..., A_n in F, P(A_1 cup ... cup A_n) = P(A_1) + ... + P(A_n).",
  "disjoint A_1..A_n  =>  P(bigcup_{i=1}^n A_i) = sum_{i=1}^n P(A_i)",
  {"A_i": "pairwise disjoint events, type: element of F", "n": "a fixed positive integer, type: natural number"},
  "the finite case of countable additivity: pad the finite family with A_{n+1} = A_{n+2} = ... = empty and apply the countable axiom (the tail terms are 0).",
  proof=("take the countably additive axiom on (A_1, ..., A_n, empty, empty, ...); the series has finitely many nonzero terms", "kolmogorov_axioms", "core", "validation/proof-checks.lean Prob.incl_excl_2 (n=2)"),
  spec=["n = 2: P(A cup B) = P(A) + P(B) for disjoint A, B",
        "partition of Omega: sum_i P(B_i) = 1"],
  cxd={"disjointness": "P(A cup B) = P(A) + P(B) - P(A cap B) in general; without disjointness the sum overcounts the overlap (inclusion_exclusion)"},
  misuse=["applying it to non-disjoint events", "extending to a countably infinite family (that is the axiom, not this proposition)"],
  related={"special_case_of": ["kolmogorov_axioms"], "generalizes_to": ["inclusion_exclusion"]},
  sources=P, status="reviewed")

N("complement_rule", "identity", "probability_space",
  "P(A^c) = 1 - P(A); consequently P(A) in [0,1], P(empty) = 0, and A subset B implies P(A) <= P(B) (with P(B \\ A) = P(B) - P(A)).",
  "P(A^c) = 1 - P(A) ;  A subset B => P(A) <= P(B)",
  {"A, B": "events, type: element of F"},
  "A and A^c are disjoint with union Omega, so P(A) + P(A^c) = P(Omega) = 1 by finite additivity and normalization.",
  proof=("finite additivity on {A, A^c} plus P(Omega) = 1; monotonicity from B = A cup (B \\ A) disjoint", "finite_additivity", "core", "validation/proof-checks.lean Prob.union_bound / incl_excl_2"),
  spec=["A = Omega: P(empty) = 0", "A = B: P(B \\ B) = 0"],
  cxd={"P_a_probability_measure": "for a general (unnormalized) measure there is no '1 -' form; only mu(B \\ A) = mu(B) - mu(A) with mu(A) < inf survives"},
  misuse=["writing P(A^c) = 1 - P(A) when conditioning: P(A^c | C) = 1 - P(A | C) is fine, but mixing conditioning events is not",
          "subtracting P(A) - P(B) without A superset B"],
  related={"derives_from": ["finite_additivity"], "used_by": ["conditional_probability", "borel_cantelli_second"]},
  sources=P, status="reviewed")

N("inclusion_exclusion", "theorem", "probability_space",
  "P(A_1 cup ... cup A_n) = sum P(A_i) - sum_{i<j} P(A_i cap A_j) + sum_{i<j<k} P(A_i cap A_j cap A_k) - ... + (-1)^{n+1} P(A_1 cap ... cap A_n).",
  "P(bigcup A_i) = sum_k (-1)^{k+1} sum_{|S|=k} P(bigcap_{i in S} A_i)",
  {"A_i": "events, type: element of F", "S": "a subset of {1..n}, type: index set"},
  "an alternating sum over all nonempty subsets S of the indices; the terms are probabilities of intersections, always well-defined.",
  proof=("induction on n using P(A cup B) = P(A) + P(B) - P(A cap B); or take expectations of the indicator identity 1_{bigcup A_i} = 1 - prod (1 - 1_{A_i})", "finite_additivity", "core", "validation/proof-checks.lean Prob.incl_excl_2, Prob.incl_excl_3"),
  spec=["n = 2: P(A cup B) = P(A) + P(B) - P(A cap B)",
        "Bonferroni: truncating after k terms gives an upper bound (k odd) or lower bound (k even)",
        "derangements: P(no fixed point of a uniform random permutation) -> 1/e"],
  cxd={"none_all_terms_needed": "dropping the higher-order terms gives only the Bonferroni one-sided bounds, not equality"},
  misuse=["forgetting the sign alternation", "using only the first two terms as if exact (that is the union bound / a Bonferroni bound)"],
  related={"generalizes": ["finite_additivity"], "special_case_of": ["the Mobius inversion formula on the subset lattice"]},
  sources=G, status="reviewed")

N("boole_inequality", "theorem", "probability_space",
  "P(bigcup_n A_n) <= sum_n P(A_n) for any countable family of events (no disjointness).",
  "P(bigcup_n A_n) <= sum_n P(A_n)",
  {"(A_n)": "any countable family of events, type: N -> F"},
  "the countable subadditivity of P; disjointify B_n = A_n minus (A_1 cup ... cup A_{n-1}), so B_n subset A_n, the B_n are disjoint with the same union, and countable additivity + monotonicity finish it.",
  proof=("disjointify and apply countable additivity: P(bigcup A_n) = P(bigcup B_n) = sum P(B_n) <= sum P(A_n)", "measure_monotonicity", "core", "validation/proof-checks.lean Prob.union_bound (two-set case)"),
  spec=["finitely many A_n: the finite union bound",
        "A_n with sum P(A_n) < 1: P(no A_n occurs) >= 1 - sum P(A_n) > 0 -- the probabilistic method's first-moment argument",
        "if sum P(A_n) < inf then P(A_n i.o.) = 0 (borel_cantelli_first)"],
  cxd={"none_unconditional": "the bound holds for every countable family; it is tight iff the A_n are pairwise disjoint (mod null sets)"},
  misuse=["expecting near-equality when the A_n overlap a lot", "applying to an uncountable family"],
  related={"generalizes": ["finite_additivity (as a bound)"], "used_by": ["borel_cantelli_first", "convergence_implications"]},
  sources=["boucheron_lugosi_massart", "durrett_pte"], status="reviewed")

N("continuity_of_probability", "proposition", "probability_space",
  "If A_n increases to A then P(A_n) -> P(A); if A_n decreases to A then P(A_n) -> P(A). (No finiteness caveat: P <= 1.)",
  "A_n up A => P(A_n) -> P(A) ;  A_n down A => P(A_n) -> P(A)",
  {"(A_n)": "a monotone sequence of events, type: N -> F", "A": "bigcup A_n or bigcap A_n, type: element of F"},
  "the specialisation of measure_continuity to a finite (probability) measure; continuity from above needs no extra hypothesis because P(A_1) <= 1 < inf.",
  proof=("measure_continuity with mu = P; from above via complements", "measure_continuity", "core", None),
  spec=["A_n = { X <= x + 1/n } down { X <= x }: gives right-continuity of the CDF",
        "A_n = { |X_k - X| <= eps for all k <= n }: used to relate a.s. and in-probability convergence",
        "P(bigcup_{n} A_n) = lim_N P(bigcup_{n<=N} A_n)"],
  cxd={"monotonicity_of_A_n": "for a non-monotone sequence only Fatou-type bounds hold: P(liminf A_n) <= liminf P(A_n) <= limsup P(A_n) <= P(limsup A_n)"},
  misuse=["applying to a non-monotone sequence", "confusing set convergence A_n -> A with numerical P(A_n) -> P(A) (the proposition is exactly the bridge)"],
  related={"specializes": ["measure_continuity"], "used_by": ["cdf_properties", "borel_cantelli_first", "borel_cantelli_second"]},
  sources=P, status="reviewed")

N("borel_cantelli_first", "theorem", "probability_space",
  "If sum_n P(A_n) < inf, then P(A_n infinitely often) = 0; i.e. almost surely only finitely many A_n occur.",
  "sum_n P(A_n) < inf  =>  P(limsup_n A_n) = 0",
  {"(A_n)": "any sequence of events (no independence), type: N -> F", "limsup A_n": "the i.o. event, type: element of F"},
  "no independence needed. P(limsup A_n) = P(bigcap_N bigcup_{n>=N} A_n) <= P(bigcup_{n>=N} A_n) <= sum_{n>=N} P(A_n) -> 0 as N -> inf (tail of a convergent series).",
  proof=("monotonicity into the N-th tail union, then Boole, then let N -> inf using that the series tail vanishes", "boole_inequality", "core", "validation/proof-checks.lean Prob.union_bound is the Boole step"),
  choice=False, constructive=True,
  spec=["A_n = { |X_n - X| > eps }: sum P < inf gives X_n -> X a.s. -- the standard route from a rate to a.s. convergence",
        "A_n = { X_n / n > 1 + eps } with sum P < inf: proves a.s. bounds like the SLLN's a.s. o(n) growth"],
  cxd={"none_unconditional_direction": "the converse needs independence (borel_cantelli_second); without it sum P(A_n) = inf gives no lower bound -- take A_n all equal to a fixed A with 0 < P(A) < 1: sum diverges but P(A i.o.) = P(A) < 1"},
  misuse=["thinking it needs independence (it does not)",
          "concluding P(A_n i.o.) > 0 from sum P(A_n) = inf without independence"],
  related={"dual_of": ["borel_cantelli_second"], "used_by": ["strong_law_large_numbers", "convergence_implications"]},
  sources=["billingsley_probability_measure", "durrett_pte"], status="reviewed")

N("borel_cantelli_second", "theorem", "probability_space",
  "If the events A_n are INDEPENDENT and sum_n P(A_n) = inf, then P(A_n infinitely often) = 1.",
  "(A_n) independent, sum_n P(A_n) = inf  =>  P(limsup_n A_n) = 1",
  {"(A_n)": "an independent sequence of events, type: N -> F"},
  "the partial converse to BC1, and it does need independence. P(no A_n for n in [M, N]) = prod (1 - P(A_n)) <= prod e^{-P(A_n)} = e^{-sum} -> 0, so P(some A_n for n >= M) = 1 for every M.",
  proof=("bound prod_{n=M}^{N} (1 - P(A_n)) by exp(-sum P(A_n)) -> 0; hence P(bigcup_{n>=M} A_n) = 1 for all M; intersect over M", "continuity_of_probability", "cited", "Billingsley Thm 4.4"),
  spec=["together with BC1: for INDEPENDENT events, P(A_n i.o.) is 0 or 1 according as sum P(A_n) converges or diverges -- a zero-one law",
        "A_n = { X_n > c_n } for iid X_n: P(X_n > c_n i.o.) is 0 or 1 by whether sum P(X_1 > c_n) converges"],
  cxd={"independence": "A_n = A fixed with 0 < P(A) < 1: sum P(A_n) = inf but P(A i.o.) = P(A) != 1. Pairwise independence is not quite enough in general; mutual (or the Kochen-Stone refinement) is the clean hypothesis."},
  misuse=["applying it to dependent events", "forgetting that BC1 needs NO independence but BC2 does"],
  related={"dual_of": ["borel_cantelli_first"], "special_case_of": ["Kolmogorov's zero-one law"]},
  sources=["billingsley_probability_measure", "durrett_pte"], status="reviewed")

# ---------------------------------------------------------------- random_variable
N("measurable_function", "definition", "random_variable",
  "f: (Omega, F) -> (E, E') is measurable if f^{-1}(B) in F for every B in E'. For E' = B(R) it suffices that { f <= x } in F for every x.",
  "for all B in E', f^{-1}(B) in F   (equivalently { f <= x } in F for all x, when E = R)",
  {"f": "the function, type: Omega -> E", "(E, E')": "the target measurable space, type: measurable space"},
  "measurability is preservation of structure BACKWARD (preimage), which is why the preimage algebra -- not the image -- is the tool. Continuous functions R -> R are Borel measurable; measurable functions are closed under +, x, sup_n, liminf_n, limits.",
  welldef="the collection { B : f^{-1}(B) in F } is a sigma-algebra, so it suffices to check measurability on a generating collection of E' (the half-lines for B(R)).",
  spec=["f = 1_A: measurable iff A in F", "f continuous: Borel measurable", "f = sup_n f_n of measurable f_n: measurable"],
  cxd={"generating_collection_check": "checking f^{-1} of a non-generating family is not enough; and a pointwise limit of measurable functions is measurable but a limit of continuous functions need not be continuous"},
  misuse=["checking the forward image instead of the preimage", "assuming an arbitrary function Omega -> R is measurable"],
  related={"used_by": ["random_variable", "abstract_integral", "conditional_expectation_abstract"], "developed_in": ["math-sets-functions-cardinality (preimage algebra)"]},
  sources=M, status="reviewed")

N("random_variable", "definition", "random_variable",
  "A random variable is a measurable function X: (Omega, F, P) -> (R, B(R)). A random vector is the R^d-valued case. { X in B } := X^{-1}(B) in F for every Borel B, so P(X in B) is defined.",
  "X: Omega -> R measurable ;  P(X in B) := P(X^{-1}(B)) for B in B(R)",
  {"X": "the random variable, type: Omega -> R measurable", "(Omega, F, P)": "the base probability space, type: probability space"},
  "a random variable is not random and not a variable -- it is a fixed measurable function; the randomness is in P. Two random variables can be equal in law without being equal as functions. sigma(X) = X^{-1}(B(R)) is the information X carries.",
  welldef="measurability makes { X <= x } an event for every x, so the CDF and the pushforward law are well-defined; sums, products, and limits of random variables are random variables.",
  spec=["X = 1_A: a Bernoulli random variable",
        "X constant = c: measurable w.r.t. any F; sigma(X) = { empty, Omega }",
        "X = g(Y) for measurable g: sigma(X) subset sigma(Y) (Doob-Dynkin)"],
  cxd={"measurability": "an arbitrary function Omega -> R (e.g. the indicator of a non-measurable set) is not a random variable -- P(X in B) is undefined"},
  misuse=["treating X(omega) as 'the random outcome' rather than a function", "assuming equality in distribution implies equality a.s."],
  related={"used_by": ["distribution_pushforward", "expectation", "independence_random_variables"], "generalizes_to": ["random element of a Polish space"]},
  sources=P, status="reviewed")

N("indicator_rv", "example", "random_variable",
  "The indicator 1_A of an event A: 1_A(omega) = 1 if omega in A, else 0. It is a random variable iff A in F, and E[1_A] = P(A), Var(1_A) = P(A)(1 - P(A)).",
  "1_A(omega) = [omega in A] ;  E[1_A] = P(A)",
  {"A": "an event, type: element of F", "1_A": "its indicator, type: Omega -> {0,1}"},
  "the bridge between set operations and arithmetic: 1_{A cap B} = 1_A 1_B, 1_{A cup B} = 1_A + 1_B - 1_A 1_B, 1_{A^c} = 1 - 1_A. Turning a probability into an expectation (P(A) = E[1_A]) is the move behind Markov's inequality and the first-moment method.",
  welldef="1_A is measurable exactly when A = 1_A^{-1}({1}) in F; it is bounded, hence in every L^p.",
  spec=["A = Omega: 1_A = 1 constant", "sum_i 1_{A_i} counts how many A_i occur; E of it is sum P(A_i) by linearity"],
  cxd={"A_in_F": "if A is not an event, 1_A is not a random variable and E[1_A] is undefined -- this is the only hypothesis"},
  misuse=["writing 1_{A cup B} = 1_A + 1_B (only for disjoint A, B)"],
  related={"used_by": ["markov_inequality", "expectation", "bernoulli_distribution"]},
  sources=P, status="reviewed")

N("distribution_pushforward", "definition", "random_variable",
  "The distribution (law) of X is the probability measure P_X on (R, B(R)) defined by P_X(B) = P(X in B) = P(X^{-1}(B)). It is the pushforward P o X^{-1}.",
  "P_X(B) := P(X^{-1}(B)) ,  a probability measure on (R, B(R))",
  {"P_X": "the law of X, type: probability measure on B(R)", "X": "a random variable, type: Omega -> R"},
  "P_X packages everything about X that does not depend on the underlying Omega; equality in law is P_X = P_Y. The pushforward of a probability measure by a measurable map is a probability measure (preimage of B(R) is a sigma-algebra, countable additivity transfers).",
  welldef="P_X inherits countable additivity from P via the preimage algebra (X^{-1} commutes with countable disjoint unions); P_X(R) = P(Omega) = 1.",
  spec=["X discrete: P_X = sum_x p_X(x) delta_x", "X absolutely continuous: P_X(B) = integral_B f_X dlambda",
        "X = c constant: P_X = delta_c"],
  cxd={"measurability_of_X": "without it X^{-1}(B) need not be an event and P_X(B) is undefined"},
  misuse=["conflating the law P_X (a measure on R) with the random variable X (a function on Omega)",
          "assuming P_X determines X (it does not -- only up to equality in law)"],
  related={"used_by": ["cdf", "expectation", "lotus"], "equivalent_to": ["the CDF F_X (cdf_determines_law)"]},
  sources=P, status="reviewed")

N("cdf", "definition", "random_variable",
  "The cumulative distribution function of X is F_X(x) = P(X <= x) = P_X((-inf, x]).",
  "F_X(x) := P(X <= x)",
  {"F_X": "the CDF, type: R -> [0,1]", "x": "a real threshold, type: real"},
  "F_X evaluates the law on the half-lines, which form a pi-system generating B(R) -- hence F_X determines P_X (cdf_determines_law). Right-continuity (not left) is the convention, from { X <= x } = bigcap_n { X <= x + 1/n }.",
  welldef="F_X is well-defined for every random variable (the half-lines are Borel); its four characterizing properties are cdf_properties.",
  spec=["X ~ Uniform(0,1): F_X(x) = x on [0,1]", "X = c: F_X = step at c (0 below, 1 from c on)",
        "F_X has an atom at x iff P(X = x) = F_X(x) - F_X(x^-) > 0"],
  cxd={"none_defined_for_every_rv": "F_X always exists; the content is in cdf_properties (which functions are CDFs) and cdf_determines_law"},
  misuse=["using P(X < x) (left-continuous) and P(X <= x) interchangeably -- they differ exactly at atoms",
          "assuming F_X is continuous (it is only right-continuous in general)"],
  related={"equivalent_to": ["the law P_X"], "used_by": ["quantile_function", "convergence_in_distribution", "probability_integral_transform"]},
  sources=P, status="reviewed")

N("cdf_properties", "theorem", "random_variable",
  "F_X is nondecreasing, right-continuous, with lim_{x -> -inf} F_X = 0 and lim_{x -> +inf} F_X = 1. Conversely, every function with these four properties is the CDF of some random variable.",
  "F nondecreasing, right-continuous, F(-inf)=0, F(+inf)=1  <=>  F = F_X for some X",
  {"F_X": "the CDF, type: R -> [0,1]"},
  "nondecreasing: monotonicity of P. Right-continuity and the limits: continuity of probability along { X <= x_n } for x_n decreasing to x (resp. to -inf, +inf). The converse builds X = F^{-1}(U) on ([0,1], lambda) via the quantile function.",
  proof=("forward: monotonicity + continuity_of_probability on the nested half-lines. Converse: on ([0,1], B, lambda) set X(u) = inf{ t : F(t) >= u }; check { X <= x } = { u : u <= F(x) }, so P(X <= x) = F(x)", "continuity_of_probability", "cited", "Billingsley Thm 12.4; Durrett Thm 1.2.2"),
  spec=["a pure-jump F (step function with jumps summing to 1): F_X of a discrete X",
        "F absolutely continuous: F(x) = integral_{-inf}^x f, X has density f",
        "the Cantor function: a continuous F with F' = 0 a.e. -- a singular continuous law, neither discrete nor absolutely continuous"],
  cxd={"right_continuity": "a function that is left-continuous with jumps is not a CDF in this convention -- it would be x |-> P(X < x)",
       "the_limit_conditions": "F(x) = arctan(x)/pi + 1/2 works; F(x) = arctan(x) does not reach 1 (defective / sub-probability distribution -- mass escapes to +inf)"},
  misuse=["forgetting a CDF can have both jumps and a density (mixed) or be singular continuous",
          "assuming F strictly increasing (it is flat wherever the law has no mass)"],
  related={"used_by": ["convergence_in_distribution", "probability_integral_transform"], "characterizes": ["laws on R"]},
  sources=["billingsley_probability_measure", "durrett_pte"], status="reviewed")

N("cdf_determines_law", "theorem", "random_variable",
  "If F_X = F_Y then P_X = P_Y: the CDF determines the entire distribution.",
  "F_X = F_Y  =>  P_X = P_Y  (as measures on B(R))",
  {"F_X, F_Y": "CDFs, type: R -> [0,1]", "P_X, P_Y": "laws, type: probability measure on B(R)"},
  "the half-lines { (-inf, x] } are a pi-system generating B(R); two probability measures agreeing on a generating pi-system (and both giving R measure 1) agree on the whole sigma-algebra by the pi-lambda theorem.",
  proof=("the sets where P_X and P_Y agree form a lambda-system containing the pi-system of half-lines; pi-lambda gives sigma(half-lines) = B(R)", "dynkin_pi_lambda", "cited", "Billingsley Thm 12.4"),
  spec=["hence P(X in B) can always be computed from F_X (by pi-lambda / Caratheodory), even for complicated Borel B",
        "the analogous statement in R^d: the joint CDF F(x_1,...,x_d) = P(X_1<=x_1, ..., X_d<=x_d) determines the joint law"],
  cxd={"pi_system_generates_the_sigma_algebra": "agreeing on a non-generating or non-pi-system family is not enough -- see the dynkin_pi_lambda counterexample"},
  misuse=["believing equal PDFs/PMFs is a weaker condition (it is equivalent, given the type)",
          "in R^d, checking only the one-dimensional marginals -- those do NOT determine the joint law"],
  related={"uses": ["dynkin_pi_lambda"], "equivalent_to": ["P_X = P_Y", "phi_X = phi_Y"]},
  sources=["billingsley_probability_measure", "durrett_pte"], status="reviewed")

N("discrete_rv", "definition", "random_variable",
  "X is discrete if it takes values in a countable set S (its support); equivalently P(X in S) = 1 for some countable S.",
  "exists countable S subset R with P(X in S) = 1",
  {"X": "a random variable, type: Omega -> R", "S": "the countable support, type: countable subset of R"},
  "the law is then a countable sum of point masses P_X = sum_{x in S} p_X(x) delta_x, entirely described by the pmf.",
  welldef="a countable S with P(X in S) = 1 makes P_X purely atomic; the smallest such S is { x : P(X = x) > 0 }.",
  spec=["S finite: a simple random variable, a finite sum of indicators", "S = N: e.g. Poisson, geometric"],
  cxd={"countability_of_S": "if the smallest such S is uncountable then no pmf exists -- e.g. any absolutely continuous X has P(X = x) = 0 for every x"},
  misuse=["assuming every random variable is discrete or continuous (mixed and singular laws exist)"],
  related={"used_by": ["pmf", "conditional_expectation_elementary"], "complement_of": ["absolutely_continuous_rv"]},
  sources=P, status="reviewed")

N("pmf", "definition", "random_variable",
  "The probability mass function of a discrete X is p_X(x) = P(X = x). It satisfies p_X >= 0 and sum_{x in S} p_X(x) = 1, and P(X in B) = sum_{x in B} p_X(x).",
  "p_X(x) := P(X = x) ,  sum_x p_X(x) = 1",
  {"p_X": "the pmf, type: S -> [0,1]", "S": "the countable support, type: countable set"},
  "the pmf is the density of P_X with respect to counting measure on S; it determines the discrete law completely.",
  welldef="sum_{x in S} P(X = x) = P(X in S) = 1 by countable additivity over the disjoint singletons; nonnegativity is immediate.",
  spec=["Bernoulli: p(1) = p, p(0) = 1 - p", "Poisson: p(k) = e^{-lambda} lambda^k / k!"],
  cxd={"discreteness": "for an absolutely continuous X, p_X(x) = P(X = x) = 0 everywhere -- the object that works is the pdf"},
  misuse=["reading p_X(x) as a probability density (it is an actual probability)",
          "forgetting the normalization when constructing a model"],
  related={"analogue_of": ["pdf (counting vs Lebesgue reference measure)"], "used_by": ["lotus", "expectation"]},
  sources=P, status="reviewed")

N("absolutely_continuous_rv", "definition", "random_variable",
  "X is absolutely continuous if its law P_X is absolutely continuous with respect to Lebesgue measure: lambda(B) = 0 implies P_X(B) = 0. Equivalently F_X(x) = integral_{-inf}^x f for some f.",
  "P_X << lambda   <=>   F_X(x) = integral_{-inf}^{x} f_X dt  for some integrable f_X >= 0",
  {"X": "a random variable, type: Omega -> R", "lambda": "Lebesgue measure, type: measure on B(R)"},
  "'absolutely continuous' is a property of the LAW relative to lambda, distinct from F_X being a continuous function (the Cantor function is continuous but its law is singular). Radon-Nikodym then supplies the density f_X = dP_X/dlambda.",
  welldef="P_X << lambda is a well-defined relation between measures; by Radon-Nikodym (P_X finite, lambda sigma-finite) it is equivalent to the existence of a density.",
  spec=["Uniform, exponential, normal, gamma, beta: all absolutely continuous",
        "P(X = x) = 0 for every x (no atoms) is necessary but NOT sufficient (singular continuous laws also have no atoms)"],
  cxd={"absolute_continuity_vs_continuous_cdf": "the Cantor distribution: F_X continuous and strictly increasing on the Cantor set, F_X' = 0 lambda-a.e., P_X concentrated on a lambda-null set -- continuous CDF, no density"},
  misuse=["equating 'continuous random variable' with 'continuous CDF'",
          "assuming a density exists whenever there are no atoms"],
  related={"requires": ["radon_nikodym"], "complement_of": ["discrete_rv"], "third_case": ["singular continuous"]},
  sources=M, status="reviewed")

N("pdf", "definition", "random_variable",
  "The probability density function of an absolutely continuous X is f_X = dP_X/dlambda, the Radon-Nikodym derivative: P(X in B) = integral_B f_X dlambda. f_X >= 0 lambda-a.e. and integral_R f_X = 1.",
  "f_X = dP_X/dlambda ;  P(X in B) = integral_B f_X dlambda ;  integral_R f_X = 1",
  {"f_X": "the density, type: R -> [0, inf), defined lambda-a.e.", "P_X": "the law, type: probability measure << lambda"},
  "f_X is defined only up to a lambda-null set; f_X(x) is NOT a probability (it can exceed 1) but f_X(x) dx is an infinitesimal probability. Where F_X is differentiable, f_X = F_X'.",
  welldef="existence and a.e.-uniqueness of f_X is exactly Radon-Nikodym for P_X << lambda; the normalization integral f_X = P_X(R) = 1.",
  spec=["Uniform(a,b): f_X = 1/(b-a) on [a,b]", "standard normal: f_X(x) = e^{-x^2/2}/sqrt(2 pi)",
        "Exponential(lambda): f_X(x) = lambda e^{-lambda x} for x >= 0"],
  cxd={"absolute_continuity": "a discrete or singular X has no density; writing 'f_X' for them is a type error"},
  misuse=["treating f_X(x) as P(X = x)", "assuming f_X <= 1", "forgetting f_X is only an a.e. equivalence class (pointwise values are not meaningful without a continuity choice)"],
  related={"requires": ["radon_nikodym"], "analogue_of": ["pmf"], "used_by": ["lotus", "transformation_univariate", "convolution_formula"]},
  sources=M, status="reviewed")

N("quantile_function", "definition", "random_variable",
  "The quantile function (generalized inverse CDF) is F_X^{-1}(u) = inf { x : F_X(x) >= u } for u in (0,1).",
  "F_X^{-1}(u) := inf { x in R : F_X(x) >= u }",
  {"F_X^{-1}": "the quantile function, type: (0,1) -> R", "u": "a probability level, type: real in (0,1)"},
  "defined for every CDF, including discrete ones (where it is a step function) -- the inf makes it left-continuous and well-defined even where F_X jumps or is flat. F_X^{-1}(u) <= x iff u <= F_X(x), the Galois connection that powers the probability integral transform.",
  welldef="{ x : F_X(x) >= u } is nonempty (F_X -> 1) and bounded below (F_X -> 0), and closed to the right (F_X right-continuous), so the inf is attained and finite for u in (0,1).",
  spec=["F_X continuous and strictly increasing: F_X^{-1} is the ordinary inverse",
        "median = F_X^{-1}(1/2); quartiles at u = 1/4, 3/4",
        "discrete X: F_X^{-1} is a step function taking values in the support"],
  cxd={"u_in_open_interval": "at u = 0 the inf is over all of R (gives -inf or the essential infimum); at u = 1 it may be +inf -- the transform is stated for u in (0,1)"},
  misuse=["assuming F_X^{-1}(F_X(x)) = x (fails where F_X is flat) or F_X(F_X^{-1}(u)) = u (fails where F_X jumps)",
          "using the right-continuous version inconsistently"],
  related={"used_by": ["probability_integral_transform"], "dual_of": ["the CDF (Galois connection)"]},
  sources=["durrett_pte", "grimmett_stirzaker"], status="reviewed")

N("probability_integral_transform", "theorem", "random_variable",
  "If F_X is continuous, then F_X(X) ~ Uniform(0,1). Conversely, for any CDF F and U ~ Uniform(0,1), the variable F^{-1}(U) has CDF F.",
  "F_X continuous => F_X(X) ~ U(0,1) ;  U ~ U(0,1) => F^{-1}(U) ~ F",
  {"X": "a random variable with continuous CDF, type: Omega -> R", "U": "a uniform variable, type: Omega -> (0,1)", "F": "any target CDF, type: R -> [0,1]"},
  "the inverse direction (F^{-1}(U) ~ F) needs NO continuity and is the basis of simulation: to sample any distribution, sample a uniform and apply the quantile function.",
  proof=("inverse: P(F^{-1}(U) <= x) = P(U <= F(x)) = F(x) by the Galois connection F^{-1}(u) <= x iff u <= F(x). Forward: if F_X continuous, P(F_X(X) <= u) = P(X <= F_X^{-1}(u)) = F_X(F_X^{-1}(u)) = u", "quantile_function", "cited", "Durrett Thm 1.2.2; Devroye Non-Uniform Random Variate Generation ch. 2"),
  solving_for="how to generate a sample from an arbitrary distribution given a uniform RNG",
  spec=["F(x) = 1 - e^{-lambda x} (exponential): F^{-1}(u) = -ln(1-u)/lambda -- inversion sampling for the exponential",
        "F discrete: F^{-1}(U) picks value x_k when U falls in (F(x_{k-1}), F(x_k)] -- the alias/CDF method",
        "goodness-of-fit: if the model F is right, the transformed data F(x_i) should look Uniform(0,1) (the basis of PP-plots and the Kolmogorov-Smirnov test)"],
  cxd={"continuity_of_F_X_for_the_forward_direction": "X ~ Bernoulli(1/2): F_X(X) takes only the values 1/2 and 1, not Uniform(0,1) -- atoms in F_X break the forward transform (the inverse direction still works)"},
  misuse=["applying the forward direction to a discrete or mixed X",
          "forgetting to use the generalized inverse for non-invertible F"],
  related={"used_by": ["simulation (inversion sampling)"], "requires": ["quantile_function"]},
  sources=["durrett_pte", "grimmett_stirzaker"], status="reviewed")

N("transformation_univariate", "theorem", "random_variable",
  "If X has density f_X and g is strictly monotone and C^1 on the range of X, then Y = g(X) has density f_Y(y) = f_X(g^{-1}(y)) |d/dy g^{-1}(y)| on g(range).",
  "Y = g(X), g monotone C^1  =>  f_Y(y) = f_X(g^{-1}(y)) |(g^{-1})'(y)|",
  {"g": "the transformation, type: strictly monotone C^1 function", "Y": "g(X), type: Omega -> R"},
  "derived by differentiating the CDF relation F_Y(y) = F_X(g^{-1}(y)) (increasing g) or 1 - F_X(g^{-1}(y)) (decreasing g); the absolute value handles both.",
  proof=("F_Y(y) = P(g(X) <= y); for increasing g this is F_X(g^{-1}(y)), differentiate via the chain rule; for decreasing g, 1 - F_X(g^{-1}(y)); combine with |.|", "pdf", "cited", "Durrett; Grimmett-Stirzaker 4.7"),
  spec=["g(x) = a x + b, a != 0: f_Y(y) = f_X((y-b)/a) / |a| -- affine rescaling",
        "g(x) = e^x on a normal X: Y is lognormal",
        "g(x) = x^2 (NOT monotone on R): split into x > 0 and x < 0 and add the two branches -- f_Y(y) = [f_X(sqrt y) + f_X(-sqrt y)] / (2 sqrt y)"],
  cxd={"monotonicity_of_g": "g(x) = x^2 with X ~ N(0,1): the naive one-branch formula gives half the correct density; Y ~ chi-squared_1 requires summing both preimages",
       "g_is_C1_with_nonzero_derivative": "if g'(x_0) = 0 the change of variables blows up; the density of Y develops a singularity there"},
  misuse=["forgetting the |Jacobian| factor", "applying the single-branch formula to a non-injective g",
          "using it when X has no density"],
  related={"generalizes_to": ["jacobian_transformation"], "special_case": ["the CDF method"]},
  sources=G, status="reviewed")

N("jacobian_transformation", "theorem", "random_variable",
  "If X is an R^n random vector with density f_X and g: R^n -> R^n is a diffeomorphism on an open set carrying P_X, then Y = g(X) has density f_Y(y) = f_X(g^{-1}(y)) |det J_{g^{-1}}(y)|.",
  "f_Y(y) = f_X(g^{-1}(y)) |det J_{g^{-1}}(y)|",
  {"g": "a diffeomorphism, type: R^n -> R^n, C^1 with C^1 inverse", "J_{g^{-1}}": "the Jacobian matrix of g^{-1}, type: n x n matrix"},
  "the multivariate change-of-variables formula for integrals, applied to P(Y in B) = P(X in g^{-1}(B)) = integral_{g^{-1}(B)} f_X = integral_B f_X(g^{-1}(y)) |det J_{g^{-1}}(y)| dy.",
  proof=("change of variables in the Lebesgue integral (a cited real-analysis theorem) applied to the pushforward identity", "transformation_univariate", "cited", "Folland; Billingsley Thm 17.2"),
  spec=["polar coordinates on (X_1, X_2) ~ iid N(0,1): shows R^2 ~ Exponential and Theta ~ Uniform -- the Box-Muller method",
        "linear map Y = A X, A invertible: f_Y(y) = f_X(A^{-1} y) / |det A|",
        "sum-and-difference: (X+Y, X-Y) to get the distribution of a sum from a joint density"],
  cxd={"g_a_diffeomorphism": "if g is not injective (e.g. (x_1,x_2) -> (x_1^2, x_2)) the preimage has multiple sheets and their Jacobian contributions must be summed",
       "det_J_nonzero": "at a critical point det J_{g^{-1}} = inf and the transformed density is singular"},
  misuse=["using |det J_g| instead of |det J_{g^{-1}}| (they are reciprocals -- getting it backward inverts the density)",
          "applying to a non-injective map without summing sheets"],
  related={"generalizes": ["transformation_univariate"], "used_by": ["convolution_formula", "simulation (Box-Muller)"]},
  sources=["billingsley_probability_measure", "grimmett_stirzaker"], status="reviewed")

N("joint_distribution", "definition", "random_variable",
  "The joint distribution of X_1, ..., X_n is the law of the random vector X = (X_1, ..., X_n) on (R^n, B(R^n)): P_X(B) = P((X_1,...,X_n) in B). Described by the joint CDF, or a joint pmf / pdf.",
  "P_X(B) = P((X_1,...,X_n) in B) ,  a probability measure on B(R^n)",
  {"X": "the random vector, type: Omega -> R^n", "P_X": "the joint law, type: probability measure on B(R^n)"},
  "the joint law carries strictly more information than the collection of marginal laws -- it also encodes the dependence structure (correlation, copula). Rectangles B_1 x ... x B_n form a pi-system generating B(R^n), so the joint CDF determines it.",
  welldef="(X_1,...,X_n) is measurable iff each X_i is (B(R^n) is generated by the coordinate projections); the pushforward is a probability measure on B(R^n).",
  spec=["independent components: P_X = P_{X_1} tensor ... tensor P_{X_n}, joint density factorizes",
        "X_2 = X_1: the joint law is concentrated on the diagonal { x_1 = x_2 }, a lambda_2-null set (no joint density)"],
  cxd={"none_the_marginals_do_not_determine_it": "(X,Y) and (X, X) can have the same marginals (both standard normal) but wildly different joint laws -- Cov 0 vs Cov 1"},
  misuse=["reconstructing the joint law from marginals (impossible without a dependence assumption)",
          "assuming a joint density exists (it does not when components are functionally related)"],
  related={"projects_to": ["marginal_distribution"], "used_by": ["independence_random_variables", "conditional_distribution", "covariance"]},
  sources=P, status="reviewed")

N("marginal_distribution", "definition", "random_variable",
  "A marginal distribution is the law of a subvector of (X_1,...,X_n), obtained by integrating (or summing) the joint density (pmf) over the remaining coordinates: f_{X_1}(x_1) = integral f_{X_1,X_2}(x_1, x_2) dx_2.",
  "f_{X_i}(x_i) = integral_{R^{n-1}} f_X(x) dx_{-i}   (Fubini)",
  {"f_X": "the joint density, type: R^n -> [0, inf)", "f_{X_i}": "a marginal density, type: R -> [0, inf)"},
  "marginalization is projection of the joint law; it discards all dependence information. Fubini-Tonelli justifies the integration (nonnegative integrand).",
  proof=("P(X_1 in B) = P(X in B x R^{n-1}) = integral_B integral_{R^{n-1}} f_X dx_{-1} dx_1 by Tonelli", "fubini_tonelli", "cited", "Billingsley Thm 18.3"),
  spec=["joint uniform on the unit disk: each marginal has a semicircular density, not uniform",
        "bivariate normal: marginals are normal (but normal marginals do not imply joint normal)"],
  cxd={"none_well_defined_always": "the marginal always exists; the caution is that MANY joints share it"},
  misuse=["thinking equal marginals implies equal joints", "assuming joint normality from normal marginals"],
  related={"projection_of": ["joint_distribution"], "used_by": ["conditional_distribution", "independence_factorization"]},
  sources=P, status="reviewed")

N("conditional_distribution", "definition", "random_variable",
  "For jointly continuous (X, Y) with f_X(x) > 0, the conditional density of Y given X = x is f_{Y|X}(y | x) = f_{X,Y}(x, y) / f_X(x). The discrete analogue uses pmfs.",
  "f_{Y|X}(y|x) := f_{X,Y}(x,y) / f_X(x)   (where f_X(x) > 0)",
  {"f_{Y|X}": "the conditional density, type: (R x R) -> [0, inf)", "f_X": "the marginal density of X, type: R -> [0, inf)"},
  "for each fixed x with f_X(x) > 0, y |-> f_{Y|X}(y|x) is a genuine probability density (nonnegative, integrates to 1). Conditioning on the measure-zero event { X = x } is legitimate here because of the density; the general case needs conditional_expectation_abstract / regular conditional distributions.",
  welldef="integral f_{Y|X}(y|x) dy = integral f_{X,Y}(x,y) dy / f_X(x) = f_X(x)/f_X(x) = 1 for a.e. x; the exceptional set { f_X = 0 } is P_X-null.",
  spec=["independence: f_{Y|X}(y|x) = f_Y(y), no dependence on x",
        "bivariate normal: Y | X = x is normal with mean mu_Y + rho (sigma_Y/sigma_X)(x - mu_X) -- the linear regression line",
        "(X,Y) uniform on the triangle 0 < y < x < 1: Y | X = x is Uniform(0, x)"],
  cxd={"positive_marginal_density": "where f_X(x) = 0 the ratio is 0/0 -- conditioning on a value X never takes is undefined",
       "existence_of_a_joint_density": "for singular joints (e.g. Y = X^2) there is no f_{X,Y}; conditioning requires the abstract construction (Borel-Kolmogorov paradox: the answer depends on how the conditioning event is approached)"},
  misuse=["conditioning on { X = x } without a joint density (Borel-Kolmogorov paradox)",
          "treating f_{Y|X}(y|x) as a function of x for fixed y as if it were a density in x"],
  related={"requires": ["joint_distribution", "marginal_distribution"], "generalizes_to": ["conditional_expectation_abstract"], "used_by": ["conditional_expectation_elementary"]},
  sources=["durrett_pte", "grimmett_stirzaker"], status="reviewed")

# ---------------------------------------------------------------- expectation
N("expectation", "definition", "expectation",
  "The expectation of a random variable X is E[X] = integral_Omega X dP. It is defined (finite) when E[|X|] < inf, and in [0, inf] unconditionally when X >= 0.",
  "E[X] := integral_Omega X dP",
  {"X": "a random variable, type: Omega -> R", "E[X]": "its mean, type: real or +-inf or undefined"},
  "E[X] is the Lebesgue integral of X against P; all its properties (linearity, monotonicity, MCT/DCT/Fatou) are the integral's, specialised. E[X] may FAIL to exist (Cauchy: E[X^+] = E[X^-] = inf).",
  welldef="for X >= 0, integral X dP in [0, inf] always exists (sup over simple functions); for signed X, E[X] = E[X^+] - E[X^-] provided not both are +inf. X integrable <=> X in L^1(P).",
  spec=["X = 1_A: E[X] = P(A)", "X discrete: E[X] = sum_x x p_X(x)", "X with density: E[X] = integral x f_X(x) dx",
        "X = c: E[X] = c"],
  cxd={"integrability_E_abs_X_finite": "X ~ Cauchy: E[|X|] = (2/pi) integral_0^inf x/(1+x^2) dx = inf, so E[X] does not exist -- neither the LLN nor the CLT apply"},
  misuse=["assuming E[X] always exists", "writing E[X] for a variable whose positive and negative parts both have infinite integral",
          "confusing E[X] (a number) with X (a function)"],
  related={"specializes": ["abstract_integral"], "used_by": ["variance", "lotus", "markov_inequality"]},
  sources=P, status="reviewed")

N("lotus", "theorem", "expectation",
  "Law of the unconscious statistician: for measurable g, E[g(X)] = integral_R g dP_X, which equals sum_x g(x) p_X(x) (discrete) or integral g(x) f_X(x) dx (density) -- no need to find the law of g(X).",
  "E[g(X)] = integral_R g(x) P_X(dx) = sum_x g(x) p_X(x) = integral g(x) f_X(x) dx",
  {"g": "a measurable function, type: R -> R", "X": "a random variable, type: Omega -> R"},
  "the change-of-variables formula for the pushforward: integral_Omega (g o X) dP = integral_R g d(P o X^{-1}). Requires E[|g(X)|] < inf for a finite answer.",
  proof=("change of variables for the pushforward measure: true for indicators g = 1_B (definition of P_X), extend by linearity to simple g, by MCT to g >= 0, by parts to integrable g", "distribution_pushforward", "cited", "Billingsley Thm 16.13"),
  spec=["g(x) = x: E[X] from the law directly", "g(x) = x^k: the k-th moment", "g(x) = e^{tx}: the MGF",
        "g(x) = 1_B(x): E[1_B(X)] = P(X in B)"],
  cxd={"integrability_of_g_X": "g(x) = x on a Cauchy X: E[g(X)] = integral x/(pi(1+x^2)) dx does not converge absolutely -- LOTUS gives no finite value"},
  misuse=["computing the law of g(X) unnecessarily", "applying it when E[|g(X)|] = inf"],
  related={"used_by": ["moment", "mgf", "characteristic_function", "variance"]},
  sources=P, status="reviewed")

N("expectation_monotonicity", "proposition", "expectation",
  "If X <= Y almost surely then E[X] <= E[Y] (when both exist). Also |E[X]| <= E[|X|], and X >= 0 a.s. with E[X] = 0 implies X = 0 a.s.",
  "X <= Y a.s.  =>  E[X] <= E[Y] ;   |E[X]| <= E[|X|]",
  {"X, Y": "integrable random variables, type: L^1(P)"},
  "monotonicity of the Lebesgue integral: Y - X >= 0 a.s. so E[Y - X] = integral (Y-X) dP >= 0, then linearity. The a.s. qualifier is enough (null sets do not affect the integral).",
  proof=("integral of a nonnegative function is >= 0; apply to Y - X; the triangle inequality |E X| <= E|X| from -|X| <= X <= |X|", "abstract_integral", "core", None),
  spec=["X = 1_A <= 1_B = Y when A subset B: recovers P(A) <= P(B)",
        "E[X] = 0 with X >= 0 a.s.: X = 0 a.s. -- the 'no negative mass' rigidity used in L^p norms"],
  cxd={"a_s_inequality": "X <= Y on a null set only is not enough to compare -- but changing X, Y on a null set changes neither expectation, so 'a.s.' is exactly the right hypothesis",
       "existence_of_both_expectations": "if E[Y] = +inf and E[X] = -inf the inequality is vacuous/ill-posed"},
  misuse=["concluding X <= Y a.s. from E[X] <= E[Y] (false -- expectation loses the pointwise order)",
          "using strict monotonicity without a strict a.s. inequality on a positive-probability set"],
  related={"used_by": ["markov_inequality", "jensen_inequality", "cauchy_schwarz_expectation"]},
  sources=P, status="reviewed")

# ---------------------------------------------------------------- moments
N("variance", "definition", "moments",
  "Var(X) = E[(X - E[X])^2], defined when E[X^2] < inf. sd(X) = sqrt(Var(X)). Var(X) >= 0, with Var(X) = 0 iff X is a.s. constant.",
  "Var(X) := E[(X - E[X])^2]",
  {"X": "a random variable with E[X^2] < inf, type: L^2(P)", "sd(X)": "standard deviation, type: nonnegative real"},
  "the mean squared deviation from the mean; needs a finite second moment (which by moment_ladder implies a finite first moment, so E[X] exists). It is the L^2(P) squared distance from X to the constant E[X].",
  welldef="(X - E[X])^2 >= 0 so its expectation is well-defined in [0, inf]; finite iff E[X^2] < inf (expand and use E[X]^2 < inf).",
  spec=["X = 1_A: Var = P(A)(1 - P(A)), maximized at P(A) = 1/2",
        "X = c constant: Var = 0", "X ~ N(mu, sigma^2): Var = sigma^2 (the parameter)"],
  cxd={"finite_second_moment": "X ~ t-distribution with 2 degrees of freedom, or Cauchy: E[X^2] = inf, Var undefined -- the CLT fails, the sample variance does not stabilize"},
  misuse=["reporting Var in the units of X^2 when sd is wanted", "assuming Var(X + Y) = Var(X) + Var(Y) without uncorrelatedness"],
  related={"requires": ["lp_space (L^2)"], "computed_by": ["variance_computational"], "used_by": ["chebyshev_inequality", "covariance"]},
  sources=P, status="reviewed")

N("variance_computational", "identity", "moments",
  "Var(X) = E[X^2] - (E[X])^2.",
  "Var(X) = E[X^2] - (E[X])^2",
  {"X": "a random variable in L^2(P), type: L^2(P)"},
  "expand (X - E[X])^2 = X^2 - 2 E[X] X + E[X]^2 and apply linearity of expectation, treating E[X] as a constant.",
  proof=("E[(X - EX)^2] = E[X^2] - 2 EX E[X] + (EX)^2 = E[X^2] - (EX)^2, by expectation_linearity", "expectation_linearity", "core", "validation/proof-checks.lean Prob.centid (GENUINE, universal list-induction identity Sum p(x-m)^2 = Sum px^2 - 2m Sum px + m^2 Sum p)"),
  spec=["X ~ Bernoulli(p): E[X^2] = p, so Var = p - p^2 = p(1-p)",
        "X ~ Poisson(lambda): E[X^2] = lambda^2 + lambda, Var = lambda",
        "the sample analogue: (1/n) sum x_i^2 - xbar^2 -- but this is biased; divide by n-1 for the unbiased estimator"],
  cxd={"finite_second_moment": "if E[X^2] = inf both sides are +inf (or ill-posed); the identity is only useful when Var is finite"},
  misuse=["the population-vs-sample n vs n-1 confusion (Bessel's correction)",
          "numerical catastrophic cancellation when E[X^2] and E[X]^2 are both large and close -- use a centered/streaming algorithm"],
  related={"derives_from": ["expectation_linearity"], "computes": ["variance"]},
  sources=P, status="reviewed")

N("variance_affine", "identity", "moments",
  "Var(aX + b) = a^2 Var(X). Standard deviation scales as |a|; adding a constant b does not change the variance.",
  "Var(aX + b) = a^2 Var(X)",
  {"a, b": "constants, type: real", "X": "a random variable in L^2(P), type: L^2(P)"},
  "E[aX + b] = a E[X] + b, so (aX + b) - E[aX + b] = a(X - E[X]); square and take expectations.",
  proof=("substitute into the definition; the b cancels, a factors out squared", "expectation_linearity", "core", "validation/proof-checks.lean Prob.var_affine (GENUINE: the 2ab.n.sx and b^2 n^2 terms cancel)"),
  spec=["standardization: Z = (X - mu)/sigma has Var(Z) = 1", "a = -1: Var(-X) = Var(X)"],
  cxd={"none_holds_whenever_Var_X_is_finite": "unconditional given a finite second moment"},
  misuse=["writing Var(aX) = a Var(X) (missing the square)", "thinking b affects the spread"],
  related={"derives_from": ["variance_computational"], "used_by": ["standard_normal", "central_limit_theorem"]},
  sources=P, status="reviewed")

N("covariance", "definition", "moments",
  "Cov(X, Y) = E[(X - E[X])(Y - E[Y])] = E[XY] - E[X]E[Y], defined when X, Y in L^2. Cov(X, X) = Var(X).",
  "Cov(X,Y) := E[(X - EX)(Y - EY)] = E[XY] - EX EY",
  {"X, Y": "random variables in L^2(P), type: L^2(P)"},
  "a measure of linear co-variation; the product XY is integrable by Cauchy-Schwarz when X, Y in L^2. Cov > 0 / < 0 / = 0 means positive / negative / no linear association (NOT independence).",
  welldef="XY in L^1 by Cauchy-Schwarz (|E[XY]| <= ||X||_2 ||Y||_2 < inf); the centered form equals the raw form by linearity.",
  spec=["Y = X: Cov(X, X) = Var(X)", "Y = aX + b: Cov(X, Y) = a Var(X)",
        "X, Y independent: Cov = 0 (independence_expectation)"],
  cxd={"finite_second_moments": "if E[X^2] or E[Y^2] is infinite, E[XY] may not exist and Cov is undefined"},
  misuse=["reading Cov = 0 as independence (uncorrelated_not_independent)",
          "comparing covariances across different unit scales -- use correlation"],
  related={"normalized_to": ["correlation"], "bilinear_via": ["covariance_bilinear"], "used_by": ["variance_of_sum"]},
  sources=P, status="reviewed")

N("covariance_bilinear", "proposition", "moments",
  "Covariance is a symmetric, positive-semidefinite bilinear form on L^2(P): Cov(aX + bZ, Y) = a Cov(X, Y) + b Cov(Z, Y), Cov(X, Y) = Cov(Y, X), Cov(X, X) >= 0.",
  "Cov(aX + bZ, Y) = a Cov(X,Y) + b Cov(Z,Y) ;  Cov symmetric ;  Cov(X,X) = Var(X) >= 0",
  {"X, Y, Z": "random variables in L^2(P), type: L^2(P)", "a, b": "constants, type: real"},
  "bilinearity is linearity of expectation applied in each argument after centering; constants have zero covariance with everything, so Cov(X + c, Y) = Cov(X, Y).",
  proof=("expand the centered products and use expectation_linearity in each slot; symmetry is commutativity of the product; Cov(X,X) = Var(X) >= 0", "expectation_linearity", "core", None),
  spec=["Cov(sum a_i X_i, sum b_j Y_j) = sum_{i,j} a_i b_j Cov(X_i, Y_j) -- the general bilinear expansion behind variance_of_sum",
        "Cov(X, c) = 0 for constant c"],
  cxd={"none_holds_on_all_of_L2": "bilinearity is unconditional on L^2(P); it is the inner-product structure (X, Y) |-> Cov(X, Y) on the quotient by constants"},
  misuse=["forgetting cross terms when expanding Cov of two sums", "treating Cov as an inner product without quotienting out constants (it is only PSD, not PD)"],
  related={"gives": ["the L^2 geometry behind conditional_expectation_l2_projection"], "used_by": ["variance_of_sum", "correlation"]},
  sources=P, status="reviewed")

N("cauchy_schwarz_expectation", "theorem", "inequalities",
  "(E[XY])^2 <= E[X^2] E[Y^2] for X, Y in L^2(P). Equality iff X and Y are a.s. linearly dependent.",
  "(E[XY])^2 <= E[X^2] E[Y^2]",
  {"X, Y": "random variables in L^2(P), type: L^2(P)"},
  "the L^2(P) inner-product Cauchy-Schwarz: the quadratic t |-> E[(X + tY)^2] = E[X^2] + 2t E[XY] + t^2 E[Y^2] is nonnegative for all real t, so its discriminant is <= 0.",
  proof=("nonnegative quadratic in t has discriminant (2 E[XY])^2 - 4 E[Y^2] E[X^2] <= 0; if E[Y^2] = 0 then Y = 0 a.s. and both sides are 0", "expectation_monotonicity", "core", "validation/proof-checks.lean Prob.corr_bound_iff + the 2-point CS/Jensen decide grid; full universal CS over Z is a real-number fact (cited)"),
  spec=["Y = 1: (E[X])^2 <= E[X^2], i.e. Var(X) >= 0",
        "centered X, Y: (Cov(X,Y))^2 <= Var(X) Var(Y), hence |rho| <= 1 (correlation)",
        "Y = X^{p-1} style: a route to Holder / the moment ladder"],
  cxd={"finite_second_moments": "X ~ Cauchy, Y = 1: E[X^2] = inf and E[XY] = E[X] does not exist -- the inequality is between undefined quantities",
       "equality_needs_linear_dependence": "if X, Y are not proportional a.s. the inequality is strict"},
  misuse=["applying it to variables not in L^2", "forgetting equality characterizes a.s. linear dependence"],
  related={"special_case_of": ["holder_inequality (p = q = 2)"], "used_by": ["correlation", "covariance"]},
  sources=["boucheron_lugosi_massart", "durrett_pte"], status="reviewed")

N("correlation", "definition", "moments",
  "rho(X, Y) = Cov(X, Y) / (sd(X) sd(Y)), defined when Var(X), Var(Y) in (0, inf). rho in [-1, 1]; |rho| = 1 iff Y is a.s. an affine function of X.",
  "rho(X,Y) := Cov(X,Y) / (sd(X) sd(Y)) ,  rho in [-1, 1]",
  {"rho": "the correlation coefficient, type: real in [-1,1]", "X, Y": "random variables with positive finite variance, type: L^2(P)"},
  "the scale-invariant, dimensionless version of covariance -- the cosine of the angle between the centered variables in L^2(P). The bound |rho| <= 1 is Cauchy-Schwarz applied to the centered variables.",
  welldef="requires sd(X), sd(Y) > 0 (non-degenerate) and finite; then |Cov(X,Y)| <= sd(X) sd(Y) by Cauchy-Schwarz, so rho in [-1, 1].",
  spec=["Y = aX + b, a > 0: rho = 1; a < 0: rho = -1", "X, Y independent: rho = 0",
        "bivariate normal: rho is the single parameter governing dependence -- and here rho = 0 DOES imply independence"],
  cxd={"positive_finite_variances": "a constant Y has sd(Y) = 0 -- rho is 0/0, undefined",
       "linearity_of_the_relationship": "Y = X^2 with X ~ Uniform(-1,1): perfect functional dependence but rho = 0 -- correlation only sees LINEAR association"},
  misuse=["reading rho = 0 as independence (only true for jointly normal)",
          "reading |rho| near 1 as 'causation' or as a good fit for a nonlinear relationship",
          "comparing rho across samples of very different range (restriction of range attenuates rho)"],
  related={"normalizes": ["covariance"], "bounded_by": ["cauchy_schwarz_expectation"]},
  sources=G, status="reviewed")

N("variance_of_sum", "theorem", "moments",
  "Var(sum_{i=1}^n X_i) = sum_i Var(X_i) + 2 sum_{i<j} Cov(X_i, X_j). If the X_i are pairwise uncorrelated, Var(sum) = sum Var.",
  "Var(sum X_i) = sum Var(X_i) + 2 sum_{i<j} Cov(X_i, X_j)",
  {"X_i": "random variables in L^2(P), type: L^2(P)", "n": "a fixed positive integer, type: natural number"},
  "expand Var(sum X_i) = Cov(sum X_i, sum X_j) by bilinearity; the diagonal terms are Var(X_i), the off-diagonal terms pair up.",
  proof=("bilinearity of covariance: Cov(sum_i X_i, sum_j X_j) = sum_{i,j} Cov(X_i, X_j), split diagonal from off-diagonal", "covariance_bilinear", "core", "validation/proof-checks.lean Prob.var_of_sum_raw and Prob.cov_bilinear_raw (GENUINE raw-moment identities)"),
  spec=["pairwise uncorrelated (in particular independent) X_i: Var(sum) = sum Var(X_i) -- 'variances add'",
        "iid X_i: Var(sum) = n Var(X_1), so Var(sample mean) = Var(X_1)/n -- the 1/n that drives the LLN and the sqrt(n) in the CLT",
        "X_i = X for all i: Var(nX) = n^2 Var(X) -- maximal positive correlation"],
  cxd={"uncorrelatedness_for_the_clean_form": "X_1 ~ N(0,1), X_2 = -X_1: Var(X_1 + X_2) = Var(0) = 0, not Var(X_1) + Var(X_2) = 2 -- the -2 Cov term matters"},
  misuse=["assuming variances add without checking (pairwise) uncorrelatedness",
          "forgetting the factor 2 on the covariance sum"],
  related={"derives_from": ["covariance_bilinear"], "used_by": ["weak_law_large_numbers", "binomial_distribution"]},
  sources=P, status="reviewed")

N("moment", "definition", "moments",
  "The k-th (raw) moment of X is m_k = E[X^k]; the k-th central moment is mu_k = E[(X - E[X])^k]. Skewness = mu_3 / sigma^3, (excess) kurtosis = mu_4 / sigma^4 - 3.",
  "m_k := E[X^k] ;  mu_k := E[(X - E[X])^k]",
  {"X": "a random variable, type: Omega -> R", "k": "a nonnegative integer, type: natural number"},
  "m_k is defined (finite) when E[|X|^k] < inf; by the moment ladder this then implies all lower moments are finite. mu_1 = 0, mu_2 = Var.",
  welldef="E[|X|^k] in [0, inf] always exists; m_k finite iff X in L^k(P). The central moments are polynomials in the raw moments via the binomial expansion.",
  spec=["k = 1: the mean; k = 2 central: the variance",
        "symmetric law: all odd central moments are 0",
        "normal: mu_{2k} = sigma^{2k} (2k-1)!! -- so kurtosis 0 (the baseline for 'excess')"],
  cxd={"finite_k_th_absolute_moment": "Student's t with nu degrees of freedom has E[|X|^k] = inf for k >= nu -- moments beyond a point simply do not exist for heavy-tailed laws"},
  misuse=["assuming a distribution is determined by its moments (the moment problem can be indeterminate -- e.g. the lognormal)",
          "estimating high moments from small samples (enormous variance)"],
  related={"generated_by": ["mgf (mgf_moments)"], "ordered_by": ["moment_ladder"]},
  sources=["billingsley_probability_measure", "grimmett_stirzaker"], status="reviewed")

N("lp_space", "definition", "moments",
  "L^p(P) = { X : E[|X|^p] < inf } for p >= 1, a normed vector space with ||X||_p = E[|X|^p]^{1/p} (identifying X = Y a.s.). It is complete (a Banach space); L^2 is a Hilbert space.",
  "L^p(P) := { X : E[|X|^p] < inf } ,  ||X||_p := (E[|X|^p])^{1/p}",
  {"X": "a random variable, type: Omega -> R", "p": "an exponent, type: real >= 1"},
  "elements are a.s.-equivalence classes, not functions. The triangle inequality is Minkowski; completeness (Riesz-Fischer) is cited. On a PROBABILITY space the L^p are nested (moment_ladder), unlike on infinite measure spaces.",
  welldef="||.||_p is a genuine norm on the quotient by a.s.-equality (||X||_p = 0 iff X = 0 a.s., by expectation_monotonicity); Minkowski gives the triangle inequality.",
  spec=["p = 1: integrable variables, E[X] defined", "p = 2: finite variance, the Hilbert space where E[X|G] is a projection",
        "p = inf: ||X||_inf = ess sup |X|, the a.s.-bounded variables"],
  cxd={"probability_space_for_nesting": "on (R, lambda), 1/x is in L^2(1, inf) but not L^1(1, inf) -- the nesting L^p subset L^q (p > q) needs a FINITE measure"},
  misuse=["treating L^p elements as functions with pointwise values", "assuming L^p nesting on a general measure space"],
  related={"ordered_by": ["moment_ladder"], "normed_by": ["holder_inequality", "minkowski"], "used_by": ["conditional_expectation_l2_projection", "convergence_in_lp"]},
  sources=["folland_real_analysis", "williams_probability_martingales"], status="reviewed")

N("moment_ladder", "theorem", "moments",
  "On a probability space, if 1 <= q <= p then ||X||_q <= ||X||_p, so L^p(P) subset L^q(P): a finite p-th moment implies finite q-th moments for all q <= p.",
  "1 <= q <= p  =>  ||X||_q <= ||X||_p  =>  L^p(P) subset L^q(P)",
  {"X": "a random variable, type: Omega -> R", "p, q": "exponents with 1 <= q <= p, type: real"},
  "apply Jensen's inequality to the convex function phi(u) = |u|^{p/q} and the variable |X|^q: E[|X|^q]^{p/q} = phi(E[|X|^q]) <= E[phi(|X|^q)] = E[|X|^p]. Uses P(Omega) = 1 crucially.",
  proof=("Jensen with phi(u) = u^{p/q} (convex, p/q >= 1) applied to |X|^q; take the (1/p)-th power", "jensen_inequality", "core", "validation/proof-checks.lean Prob.jensen_sq (GENUINE, universal in t,x,y,n) is the p/q = 2 core"),
  spec=["p = 2, q = 1: E[|X|] <= sqrt(E[X^2]) -- finite variance implies finite mean, so Var and E both exist together",
        "the sequence ||X||_q is nondecreasing in q, converging to ||X||_inf"],
  cxd={"finite_total_measure": "on an infinite measure space the inclusion reverses partially and can fail entirely -- the ladder is a probability-space phenomenon (P(Omega) = 1 is the hidden hypothesis)"},
  misuse=["assuming a finite mean implies a finite variance (the ladder only goes DOWN: high moments control low, not vice versa)",
          "using it on a non-probability measure"],
  related={"derives_from": ["jensen_inequality"], "orders": ["lp_space"], "special_case_of": ["Lyapunov's inequality"]},
  sources=["williams_probability_martingales", "durrett_pte"], status="reviewed")

N("mgf", "definition", "moments",
  "The moment generating function of X is M_X(t) = E[e^{tX}], for those real t where the expectation is finite. If M_X is finite on an open interval around 0, it determines the law and all moments.",
  "M_X(t) := E[e^{tX}]",
  {"M_X": "the MGF, type: (subset of R) -> (0, inf]", "t": "a real parameter, type: real"},
  "M_X(0) = 1 always; M_X(t) may be +inf for all t != 0 (e.g. Cauchy, lognormal). The useful hypothesis is 'M_X finite on (-h, h) for some h > 0' (X is then sub-exponential).",
  welldef="e^{tX} > 0 so E[e^{tX}] in (0, inf] is always defined; the set { t : M_X(t) < inf } is an interval containing 0.",
  spec=["X ~ N(mu, sigma^2): M_X(t) = exp(mu t + sigma^2 t^2 / 2), finite for all t",
        "X ~ Exponential(lambda): M_X(t) = lambda/(lambda - t) for t < lambda only",
        "X ~ Poisson(lambda): M_X(t) = exp(lambda(e^t - 1))"],
  cxd={"finiteness_near_0": "X ~ Cauchy or lognormal: M_X(t) = inf for every t != 0, so the MGF carries no information -- use the characteristic function instead"},
  misuse=["assuming the MGF exists", "using it for heavy-tailed distributions where only the CF works",
          "concluding equality in law from agreement at finitely many t"],
  related={"always_replaced_by": ["characteristic_function (which always exists)"], "generates": ["moment (mgf_moments)"], "multiplies": ["mgf_sum_independent"]},
  sources=P, status="reviewed")

N("mgf_moments", "theorem", "moments",
  "If M_X is finite on a neighborhood of 0, then M_X is C^infinity there, X has moments of all orders, and M_X^{(k)}(0) = E[X^k]. Equivalently M_X(t) = sum_k E[X^k] t^k / k! near 0.",
  "M_X finite near 0  =>  M_X^{(k)}(0) = E[X^k]  for all k",
  {"M_X": "the MGF, type: (-h, h) -> R", "k": "a nonnegative integer, type: natural number"},
  "differentiate under the expectation: d^k/dt^k E[e^{tX}] = E[X^k e^{tX}], justified by DCT since finiteness on (-h, h) provides a dominating function e^{h'|X|} for |t| < h' < h.",
  proof=("DCT-justified differentiation under the integral sign, k times, then evaluate at t = 0", "dominated_convergence_theorem", "cited", "Billingsley Thm 21.1; Durrett 3.3"),
  spec=["N(0,1): M(t) = e^{t^2/2}, M''(0) = 1 = E[Z^2], M^{(4)}(0) = 3 = E[Z^4]",
        "Exponential(1): M(t) = 1/(1-t), M^{(k)}(0) = k! = E[X^k]"],
  cxd={"finiteness_of_M_X_near_0": "if M_X is finite only at 0, none of this holds -- a distribution can have all moments finite yet no MGF? no: all-moments-finite does not give an MGF (lognormal: every moment finite, MGF infinite, and the moment sequence does NOT determine the law)"},
  misuse=["computing moments from an MGF that is finite only at isolated points",
          "assuming the Taylor coefficients of any formal series 'M(t)' are moments without checking convergence"],
  related={"requires": ["mgf"], "computes": ["moment"], "cf_analogue": ["phi_X^{(k)}(0) = i^k E[X^k] when E|X|^k < inf"]},
  sources=P, status="reviewed")

N("mgf_uniqueness", "theorem", "moments",
  "If M_X(t) = M_Y(t) < inf for all t in an open interval around 0, then P_X = P_Y.",
  "M_X = M_Y finite on (-h, h)  =>  P_X = P_Y",
  {"M_X, M_Y": "MGFs finite near 0, type: (-h, h) -> R"},
  "finiteness on a neighborhood of 0 forces the law to have exponentially decaying tails, and such laws are determined by their moment sequence (the moment problem is determinate); alternatively the MGF extends to a strip in C and equals the CF, which always determines the law (cf_properties).",
  proof=("analytic continuation of M to the complex strip |Re z| < h; on the imaginary axis it is the characteristic function, whose inversion determines the law", "dynkin_pi_lambda", "cited", "Billingsley Thm 30.1; Curtiss 1942"),
  spec=["sum of independent Poissons: M = product of exp(lambda_i(e^t - 1)) = exp((sum lambda_i)(e^t - 1)) => Poisson(sum lambda_i)",
        "sum of independent N(mu_i, sigma_i^2): M = exp(sum mu_i t + (sum sigma_i^2) t^2 / 2) => N(sum mu_i, sum sigma_i^2)"],
  cxd={"finiteness_on_an_interval": "agreement of M_X and M_Y only AT t = 0 (both equal 1) says nothing; and two different laws can share every moment (lognormal and a discrete perturbation) -- but then neither has an MGF finite near 0"},
  misuse=["concluding P_X = P_Y from M_X = M_Y at finitely many points",
          "using MGF uniqueness for heavy-tailed laws (no MGF -- must use the CF)"],
  related={"cf_analogue": ["phi_X = phi_Y => P_X = P_Y, UNCONDITIONALLY"], "uses": ["dynkin_pi_lambda"], "used_by": ["normal_affine_closure", "poisson_limit_theorem"]},
  sources=["billingsley_probability_measure", "durrett_pte"], status="reviewed")

N("characteristic_function", "definition", "moments",
  "The characteristic function of X is phi_X(t) = E[e^{i t X}] = E[cos tX] + i E[sin tX]. It exists for EVERY random variable and every real t, with |phi_X(t)| <= 1 and phi_X(0) = 1.",
  "phi_X(t) := E[e^{itX}] ,  |phi_X| <= 1 ,  phi_X(0) = 1",
  {"phi_X": "the characteristic function, type: R -> C, |phi_X| <= 1", "t": "a real parameter, type: real"},
  "the Fourier transform of the law P_X. Unlike the MGF it always exists because |e^{itX}| = 1 is bounded. It determines the law (inversion), is uniformly continuous, and turns sums of independents into products.",
  welldef="|e^{itX}| = 1 so e^{itX} is bounded, hence integrable against the probability measure P; phi_X is defined for all t.",
  spec=["N(0,1): phi(t) = e^{-t^2/2}", "Cauchy: phi(t) = e^{-|t|} (exists! even though no moments do)",
        "X = c: phi(t) = e^{itc}", "Bernoulli(p): phi(t) = 1 - p + p e^{it}"],
  cxd={"none_always_defined": "the CF is the tool precisely because it needs no hypothesis -- every law has one"},
  misuse=["expecting phi to be real (it is real iff the law is symmetric about 0)",
          "reading phi_X'(0) as E[X] without E|X| < inf (the derivative may fail to exist)"],
  related={"always_exists_unlike": ["mgf"], "determines": ["the law (cf_properties)"], "used_by": ["levy_continuity_theorem", "central_limit_theorem"]},
  sources=["billingsley_probability_measure", "durrett_pte"], status="reviewed")

N("cf_properties", "theorem", "moments",
  "phi_X is uniformly continuous with |phi_X| <= 1, phi_X(0) = 1, phi_{-X} = conjugate(phi_X). It determines the law (inversion formula). phi_{aX+b}(t) = e^{itb} phi_X(at). If E|X|^k < inf then phi_X is C^k with phi_X^{(k)}(0) = i^k E[X^k].",
  "phi determines P_X ; phi_{aX+b}(t) = e^{itb} phi_X(at) ; E|X|^k < inf => phi^{(k)}(0) = i^k E[X^k]",
  {"phi_X": "the characteristic function, type: R -> C", "a, b": "constants, type: real"},
  "uniform continuity: |phi(t+h) - phi(t)| <= E|e^{ihX} - 1| -> 0 by DCT. Inversion: for a < b continuity points, P_X((a,b]) = lim_T (1/2 pi) integral_{-T}^{T} (e^{-ita} - e^{-itb})/(it) phi_X(t) dt.",
  proof=("uniform continuity by DCT; the inversion formula by Fubini on the Dirichlet kernel; smoothness by differentiating under the integral (DCT) when the moment exists", "dominated_convergence_theorem", "cited", "Billingsley Thm 26.2, 26.1; Durrett 3.3"),
  spec=["phi real-valued <=> P_X symmetric about 0",
        "phi integrable => P_X has a bounded continuous density f(x) = (1/2 pi) integral e^{-itx} phi(t) dt",
        "affine: standardizing X to (X - mu)/sigma multiplies the CF argument by sigma and adds a phase"],
  cxd={"moment_for_smoothness": "Cauchy: phi(t) = e^{-|t|} is NOT differentiable at 0 -- consistent with E|X| = inf",
       "continuity_points_for_inversion": "the inversion formula recovers P_X((a,b]) only at continuity points a, b of F_X"},
  misuse=["assuming phi determines a density (only if phi is integrable)",
          "reading non-smoothness of phi at 0 as pathology -- it just signals a heavy tail"],
  related={"characterizes": ["the law"], "requires": ["characteristic_function"], "used_by": ["levy_continuity_theorem"]},
  sources=["billingsley_probability_measure", "durrett_pte"], status="reviewed")

# ---------------------------------------------------------------- independence
N("conditional_probability", "definition", "independence",
  "For events A, B with P(B) > 0, the conditional probability of A given B is P(A | B) = P(A cap B) / P(B). For fixed B, P(. | B) is itself a probability measure on F.",
  "P(A | B) := P(A cap B) / P(B)   (requires P(B) > 0)",
  {"A, B": "events, type: element of F", "P(. | B)": "the conditioned measure, type: F -> [0,1]"},
  "the positivity P(B) > 0 is a genuine precondition; conditioning on probability-zero events needs conditional_expectation_abstract. P(. | B) restricts and renormalizes P to B.",
  welldef="P(. | B) satisfies the Kolmogorov axioms: nonnegative, P(Omega | B) = P(B)/P(B) = 1, countably additive (inherited from P). So all earlier results apply to it.",
  spec=["B = Omega: P(A | Omega) = P(A)", "A subset B: P(A | B) = P(A)/P(B) >= P(A)",
        "A, B disjoint: P(A | B) = 0"],
  cxd={"positivity_of_P_B": "P(B) = 0 makes the ratio 0/0 -- the Borel-Kolmogorov paradox shows the 'limit' answer depends on the approximating sequence of positive-probability events"},
  misuse=["confusing P(A|B) with P(B|A) (base-rate / prosecutor's fallacy)",
          "conditioning on a measure-zero event without the abstract machinery",
          "assuming P(A|B) >= P(A) (only when A, B positively associated)"],
  related={"used_by": ["multiplication_rule", "bayes_theorem", "law_of_total_probability"], "generalizes_to": ["conditional_expectation_abstract"]},
  sources=P, status="reviewed")

N("multiplication_rule", "identity", "independence",
  "P(A cap B) = P(A | B) P(B) = P(B | A) P(A). Chain rule: P(A_1 cap ... cap A_n) = P(A_1) P(A_2 | A_1) P(A_3 | A_1 cap A_2) ... (each conditioning event having positive probability).",
  "P(A cap B) = P(A|B) P(B) ;  P(cap A_i) = prod_i P(A_i | A_1 cap ... cap A_{i-1})",
  {"A_i": "events with the running intersections of positive probability, type: element of F"},
  "a rearrangement of the definition of conditional probability, iterated. The order of the A_i can be permuted; each requires its predecessor-intersection to have positive probability.",
  proof=("P(A|B) P(B) = [P(A cap B)/P(B)] P(B) = P(A cap B); induct for the n-fold version", "conditional_probability", "core", None),
  spec=["independent A, B: P(A cap B) = P(A) P(B)",
        "drawing without replacement: P(both aces) = (4/52)(3/51) -- the chain rule computes sequential-sampling probabilities",
        "P(A_1 cap ... cap A_n) for a Markov chain telescopes to P(A_1) prod P(A_{i+1} | A_i)"],
  cxd={"positive_probability_of_the_conditioning_events": "if some prefix intersection has probability 0, that conditional factor is undefined -- but then the whole intersection also has probability 0, so the identity is read as 0 = 0"},
  misuse=["assuming P(A cap B) = P(A) P(B) without independence", "chain-rule factors in an order where a conditioning event has probability 0"],
  related={"derives_from": ["conditional_probability"], "used_by": ["law_of_total_probability", "bayes_theorem"]},
  sources=P, status="reviewed")

N("law_of_total_probability", "theorem", "independence",
  "If {B_i} is a countable partition of Omega with P(B_i) > 0, then for any event A: P(A) = sum_i P(A | B_i) P(B_i).",
  "{B_i} a partition, P(B_i) > 0  =>  P(A) = sum_i P(A | B_i) P(B_i)",
  {"A": "an event, type: element of F", "{B_i}": "a countable measurable partition of Omega, type: family in F"},
  "A is the disjoint union of A cap B_i; apply countable additivity, then the multiplication rule to each term.",
  proof=("A = bigsqcup_i (A cap B_i); P(A) = sum_i P(A cap B_i) = sum_i P(A | B_i) P(B_i) by countable additivity and the multiplication rule", "finite_additivity", "core", "validation/proof-checks.lean Prob.bayes_denominator"),
  spec=["two-part partition {B, B^c}: P(A) = P(A|B) P(B) + P(A|B^c) P(B^c)",
        "the denominator of Bayes' theorem is exactly this expansion",
        "first-step analysis: P(gambler ruin) = p P(ruin | up) + (1-p) P(ruin | down)"],
  cxd={"the_B_i_partition_Omega": "if the B_i do not cover Omega, sum_i P(A|B_i) P(B_i) = P(A cap bigcup B_i) < P(A) -- you undercount the part of A outside the B_i"},
  misuse=["using events that overlap or fail to cover Omega", "forgetting a case (a non-exhaustive partition silently loses probability)"],
  related={"used_by": ["bayes_theorem"], "expectation_analogue": ["tower_property / law of total expectation"]},
  sources=P, status="reviewed")

N("independence_events", "definition", "independence",
  "Events A_1, ..., A_n are (mutually) independent if for EVERY subset S of indices, P(bigcap_{i in S} A_i) = prod_{i in S} P(A_i). An infinite family is independent if every finite subfamily is.",
  "for all S subset {1..n}:  P(bigcap_{i in S} A_i) = prod_{i in S} P(A_i)",
  {"A_i": "events, type: element of F", "S": "any subset of the index set, type: index set"},
  "defined by FACTORIZATION, not by conditioning -- this keeps independence available for null events and sigma-algebras, and avoids the independence <-> conditional-probability circularity (see edges/cycles.md). 'P(A|B) = P(A)' is then a theorem, valid when P(B) > 0.",
  welldef="the condition is a finite conjunction of numeric identities per subset; it is preserved under complementation of any subset of the A_i.",
  spec=["two events: independence is the single equation P(A cap B) = P(A) P(B)",
        "A with P(A) in {0, 1}: A is independent of every event",
        "pairwise independence: only the |S| = 2 equations -- strictly weaker (pairwise_not_mutual)"],
  cxd={"all_subsets_not_just_pairs": "pairwise_not_mutual: X, Y iid fair bits, Z = X XOR Y -- each pair independent, but P(X=Y=Z=0) = 1/4 != 1/8",
       "the_empty_and_singleton_S_are_trivial": "the content is in |S| >= 2"},
  misuse=["checking only pairwise independence", "confusing independence with disjointness (disjoint events with positive probability are DEPENDENT: P(A cap B) = 0 != P(A)P(B))"],
  related={"generalizes_to": ["independence_sigma_algebras", "independence_random_variables"], "equivalent_to": ["P(A|B) = P(A) when P(B) > 0"]},
  sources=P, status="reviewed")

N("independence_sigma_algebras", "definition", "independence",
  "Sub-sigma-algebras G_1, ..., G_n of F are independent if P(bigcap_i A_i) = prod_i P(A_i) for every choice of A_i in G_i. Equivalently, generating pi-systems can be checked (via pi-lambda).",
  "for all A_i in G_i:  P(bigcap_i A_i) = prod_i P(A_i)",
  {"G_i": "sub-sigma-algebras, type: sigma-algebra subset F", "A_i": "A_i in G_i, type: element of G_i"},
  "the right level of generality: independence of random variables is independence of the sigma-algebras they generate. By the pi-lambda theorem it suffices to verify the factorization on generating pi-systems (this is what makes it checkable).",
  welldef="the set of A_1 for which the factorization holds (with A_2, ..., A_n fixed in generating pi-systems) is a lambda-system; pi-lambda extends it to all of G_1, then iterate.",
  spec=["G_i = sigma(X_i): recovers independence_random_variables",
        "G = { empty, Omega }: independent of every sigma-algebra",
        "the tail sigma-algebra of an independent sequence is independent of every finite prefix -- Kolmogorov's zero-one law"],
  cxd={"factorization_on_a_pi_system_that_generates": "checking factorization on a generating family that is not intersection-closed does not extend (dynkin_pi_lambda counterexample)"},
  misuse=["verifying independence on a non-pi-system and extending", "conflating independence of G_1, G_2 with G_1 cap G_2 = { empty, Omega }"],
  related={"uses": ["dynkin_pi_lambda"], "specializes_to": ["independence_random_variables"], "generalizes": ["independence_events"]},
  sources=["billingsley_probability_measure", "durrett_pte"], status="reviewed")

N("independence_random_variables", "definition", "independence",
  "Random variables X_1, ..., X_n are independent if the sigma-algebras sigma(X_1), ..., sigma(X_n) are independent; equivalently P(X_1 in B_1, ..., X_n in B_n) = prod_i P(X_i in B_i) for all Borel B_i; equivalently the joint law is the product of the marginals.",
  "P(X_1 in B_1, ..., X_n in B_n) = prod_i P(X_i in B_i)   for all Borel B_i",
  {"X_i": "random variables, type: Omega -> R", "B_i": "Borel sets, type: element of B(R)"},
  "the sets { X_i in B_i } for B_i Borel form a generating pi-system for sigma(X_i), so factorization on rectangles (checked via CDFs or densities) is enough by pi-lambda. Functions of disjoint independent blocks stay independent.",
  welldef="the product measure P_{X_1} tensor ... tensor P_{X_n} exists and is a probability measure on B(R^n); independence says the joint law equals it.",
  spec=["densities factorize: f_{X_1,...,X_n}(x) = prod_i f_{X_i}(x_i) (independence_factorization)",
        "g_1(X_1), ..., g_n(X_n) are independent for any measurable g_i",
        "iid = independent + identically distributed"],
  cxd={"all_n_together_not_just_pairs": "three variables can be pairwise independent but not mutually independent -- e.g. X_1, X_2 iid uniform on {-1,1}, X_3 = X_1 X_2",
       "the_joint_law_not_just_marginals": "same marginals, different dependence: (X, X) vs (X, -X) vs (X, Y independent)"},
  misuse=["inferring independence from zero correlation (uncorrelated_not_independent)",
          "assuming a function of ALL the X_i stays independent of another such function"],
  related={"special_case": ["iid"], "checked_by": ["independence_factorization"], "implies": ["independence_expectation"]},
  sources=P, status="reviewed")

N("independence_factorization", "theorem", "independence",
  "X, Y are independent iff F_{X,Y}(x, y) = F_X(x) F_Y(y) for all x, y; iff (when densities exist) f_{X,Y}(x, y) = f_X(x) f_Y(y) for a.e. (x, y); iff (discrete) p_{X,Y}(x,y) = p_X(x) p_Y(y).",
  "X ⟂ Y  <=>  F_{X,Y} = F_X F_Y  <=>  f_{X,Y} = f_X f_Y  (a.e.)",
  {"F_{X,Y}, f_{X,Y}": "joint CDF / density, type: R^2 -> [0,1] / [0, inf)"},
  "the half-line rectangles (-inf, x] x (-inf, y] are a pi-system generating B(R^2); the factorization of the joint CDF there extends to full independence by the pi-lambda theorem.",
  proof=("factorization on the generating pi-system of rectangles + pi-lambda; for densities, integrate/differentiate the CDF statement", "dynkin_pi_lambda", "cited", "Billingsley Thm 20.1; Durrett Thm 2.1.7"),
  spec=["a joint density that is a product g(x) h(y) (even unnormalized) => X, Y independent with marginals proportional to g, h -- the 'factorization criterion'",
        "checking independence: it is enough that the SUPPORT is a product AND the density factors on it"],
  cxd={"factorization_over_the_full_support": "f_{X,Y}(x,y) = 2 on the triangle 0 < x < y < 1: the density is 'constant' but the support is not a rectangle, so X, Y are NOT independent (Y | X = x is Uniform(x, 1))"},
  misuse=["reading a constant joint density as independence without checking the support is a product",
          "checking factorization at a few points rather than a.e."],
  related={"uses": ["dynkin_pi_lambda"], "operationalizes": ["independence_random_variables"]},
  sources=P, status="reviewed")

N("iid", "definition", "independence",
  "A sequence (X_n) is independent and identically distributed if the X_n are mutually independent and all have the same law. The canonical hypothesis of the laws of large numbers and the classical CLT.",
  "(X_n) mutually independent  AND  P_{X_n} = P_{X_1} for all n",
  {"(X_n)": "an iid sequence, type: N -> (Omega -> R)", "P_{X_1}": "the common law, type: probability measure on B(R)"},
  "'identically distributed' constrains the marginals; 'independent' constrains the dependence. An iid sequence on a single probability space exists for any law (product / Kolmogorov extension construction).",
  welldef="the infinite product measure (P_{X_1})^{tensor N} on (R^N, B(R)^{tensor N}) exists (Kolmogorov extension) and realizes an iid sequence via coordinate projections.",
  spec=["repeated independent trials of one experiment (coin, die, measurement with iid noise)",
        "the empirical distribution of an iid sample converges to P_{X_1} (Glivenko-Cantelli)",
        "a random sample in statistics IS an iid sequence (design permitting)"],
  cxd={"identically_distributed": "independent but not identical: the Lindeberg CLT (lindeberg_clt) is what replaces 'identical' for a non-degenerate limit",
       "independence": "identically distributed but dependent (e.g. a stationary time series): the LLN can still hold (ergodic theorem) but the CLT rate and variance change (long-range dependence)"},
  misuse=["assuming survey / observational data is iid when there is clustering, time trend, or selection",
          "treating 'identically distributed' as 'independent' or vice versa"],
  related={"hypothesis_of": ["weak_law_large_numbers", "strong_law_large_numbers", "central_limit_theorem"], "constructed_by": ["kolmogorov_extension_theorem"]},
  sources=P, status="reviewed")

N("independence_expectation", "theorem", "independence",
  "If X, Y are independent and both integrable, then XY is integrable and E[XY] = E[X] E[Y]. Consequently Cov(X, Y) = 0: independent random variables are uncorrelated.",
  "X ⟂ Y, integrable  =>  E[XY] = E[X] E[Y]  =>  Cov(X, Y) = 0",
  {"X, Y": "independent integrable random variables, type: L^1(P)"},
  "the joint law is the product P_X tensor P_Y; E[XY] = integral integral xy dP_X dP_Y = (integral x dP_X)(integral y dP_Y) by Fubini-Tonelli (applicable since the product |x||y| integrates).",
  proof=("LOTUS on the product law + Fubini-Tonelli: true for indicators of rectangles, extend by linearity and MCT; integrability of XY from E|XY| = E|X| E|Y| < inf", "fubini_tonelli", "cited", "Billingsley Thm 21.2; Durrett Thm 2.1.9"),
  spec=["more generally E[g(X) h(Y)] = E[g(X)] E[h(Y)] for measurable g, h with the products integrable",
        "Var(X + Y) = Var(X) + Var(Y) for independent X, Y",
        "the MGF and CF of a sum of independents factor (mgf_sum_independent)"],
  cxd={"independence_not_merely_uncorrelated": "X ~ Uniform(-1,1), Y = X^2: E[XY] = E[X^3] = 0 = E[X] E[Y], so uncorrelated, but X, Y are strongly dependent -- the converse is FALSE (uncorrelated_not_independent)",
       "integrability": "independent Cauchy X, Y: E[XY] does not exist even though E[X], E[Y] individually fail too"},
  misuse=["using E[XY] = E[X]E[Y] to CONCLUDE independence", "applying it to non-integrable variables"],
  related={"one_way_only": ["uncorrelated_not_independent is the failed converse"], "requires": ["independence_random_variables"], "used_by": ["variance_of_sum", "mgf_sum_independent"]},
  sources=P, status="reviewed")

N("mgf_sum_independent", "identity", "independence",
  "If X, Y are independent, then M_{X+Y}(t) = M_X(t) M_Y(t) (where the MGFs are finite), and phi_{X+Y}(t) = phi_X(t) phi_Y(t) always.",
  "X ⟂ Y  =>  M_{X+Y} = M_X M_Y  and  phi_{X+Y} = phi_X phi_Y",
  {"X, Y": "independent random variables, type: Omega -> R"},
  "e^{t(X+Y)} = e^{tX} e^{tY} is a product of independent (functions of independent) variables, so its expectation factors by independence_expectation. Same for e^{it(X+Y)}.",
  proof=("E[e^{t(X+Y)}] = E[e^{tX} e^{tY}] = E[e^{tX}] E[e^{tY}] by independence_expectation applied to g(X) = e^{tX}, h(Y) = e^{tY}", "independence_expectation", "core", "validation/proof-checks.lean -- binomial MGF^n instance"),
  spec=["sum of n iid: M_{S_n} = M_X^n, phi_{S_n} = phi_X^n -- the engine of the CLT proof",
        "N(mu_1, s_1^2) + N(mu_2, s_2^2) independent = N(mu_1 + mu_2, s_1^2 + s_2^2), by exp adding in the exponent",
        "Poisson(lambda) + Poisson(mu) independent = Poisson(lambda + mu)"],
  cxd={"independence": "X + X = 2X: phi_{2X}(t) = phi_X(2t) != phi_X(t)^2 in general -- the product rule is exactly the independence assumption",
       "finiteness_for_the_MGF_version": "the CF version is unconditional; the MGF version needs both MGFs finite at t"},
  misuse=["multiplying CFs/MGFs of dependent variables", "using the MGF form when an MGF does not exist (use the CF)"],
  related={"derives_from": ["independence_expectation"], "used_by": ["central_limit_theorem", "poisson_limit_theorem", "normal_affine_closure"]},
  sources=P, status="reviewed")

N("convolution_formula", "theorem", "independence",
  "If X, Y are independent with densities f_X, f_Y, then X + Y has density (f_X * f_Y)(z) = integral_R f_X(x) f_Y(z - x) dx. Discrete analogue: p_{X+Y}(k) = sum_j p_X(j) p_Y(k - j).",
  "f_{X+Y}(z) = integral_R f_X(x) f_Y(z - x) dx   (X ⟂ Y)",
  {"f_X, f_Y": "the marginal densities, type: R -> [0, inf)", "*": "convolution, type: binary operation on densities"},
  "P(X + Y <= z) = integral integral_{x + y <= z} f_X(x) f_Y(y) dy dx (product law, Fubini); differentiate in z. Convolution is commutative and associative, matching X + Y = Y + X and sums of three.",
  proof=("push (x, y) -> (x, x + y) through the product density via jacobian_transformation (Jacobian 1), then integrate out x", "fubini_tonelli", "cited", "Grimmett-Stirzaker 4.8; Durrett Thm 2.1.10"),
  spec=["Exponential(lambda) * Exponential(lambda) = Gamma(2, 1/lambda) -- sum of two iid exponentials",
        "N(0, s_1^2) * N(0, s_2^2) = N(0, s_1^2 + s_2^2)",
        "Poisson(a) * Poisson(b) = Poisson(a + b) (discrete convolution of the pmfs)"],
  cxd={"independence": "for dependent X, Y the density of X + Y involves the joint density and is not a convolution -- e.g. Y = -X gives X + Y = 0, a point mass",
       "existence_of_densities": "if X is discrete and Y continuous, X + Y has a density (a mixture of shifted f_Y), but the pure convolution-of-densities formula does not apply directly"},
  misuse=["convolving marginals of dependent variables", "sign error in f_Y(z - x) vs f_Y(x - z) (equal only if f_Y symmetric)"],
  related={"requires": ["independence_random_variables"], "cf_shortcut": ["phi_{X+Y} = phi_X phi_Y (often easier)"], "used_by": ["gamma_distribution", "normal_affine_closure"]},
  sources=["grimmett_stirzaker", "durrett_pte"], status="reviewed")

N("pairwise_not_mutual", "counterexample", "independence",
  "Pairwise independence does not imply mutual independence. Example: X, Y independent fair +-1 variables, Z = XY. Then (X,Y), (X,Z), (Y,Z) are each independent pairs, but P(X = Y = Z = 1) = 1/4 != 1/8 = P(X=1)P(Y=1)P(Z=1).",
  "X, Y iid Uniform{-1,1}, Z = XY:  pairwise independent, NOT mutually independent",
  {"X, Y": "iid Uniform{-1,1}, type: Omega -> {-1,1}", "Z": "XY, type: Omega -> {-1,1}"},
  "each of Z, X, Y is Uniform{-1,1} and any two are independent (checking the four sign combinations), but the three are functionally linked: XYZ = 1 always, so knowing two determines the third.",
  welldef="all three variables are Uniform{-1,1}; the pair (X, Z) is independent because Z = XY with Y an independent fair sign 'rerandomizes' X. Yet Z is sigma(X,Y)-measurable.",
  spec=["the |S| = 2 factorization equations all hold; the |S| = 3 equation P(X=Y=Z=1) = P(X=1)P(Y=1)P(Z=1) fails",
        "consequence: E[XYZ] = E[1] = 1 != 0 = E[X]E[Y]E[Z], so 'expectation factors' can fail even when it holds for every pair"],
  cxd={"this_IS_the_counterexample": "it shows the |S| >= 3 conditions in independence_events are not redundant"},
  misuse=["verifying independence by checking only pairs", "assuming pairwise-independent variables can be treated as a product for a union bound refinement or a CLT (pairwise independence IS enough for the L^2 WLLN, but not for the CLT or the SLLN)"],
  related={"limits": ["independence_events"], "constrasts": ["for the WLLN, pairwise uncorrelated suffices"]},
  sources=["durrett_pte", "grimmett_stirzaker"], status="reviewed")

N("uncorrelated_not_independent", "counterexample", "independence",
  "Zero covariance does not imply independence. Example: X ~ Uniform(-1, 1), Y = X^2. Then Cov(X, Y) = E[X^3] - E[X] E[X^2] = 0 - 0 = 0, but Y is a deterministic function of X.",
  "X ~ Uniform(-1,1), Y = X^2:  Cov(X, Y) = 0  but  X, Y dependent",
  {"X": "Uniform(-1,1), type: Omega -> (-1,1)", "Y": "X^2, type: Omega -> [0,1)"},
  "correlation measures only LINEAR association; the relationship here is purely quadratic (even), so it is invisible to covariance. P(Y < 1/4 | X > 1/2) = 0 != P(Y < 1/4), witnessing dependence.",
  welldef="E[X] = 0 and E[X^3] = 0 by symmetry, so Cov(X, X^2) = 0 exactly; yet sigma(Y) subset sigma(X) non-trivially.",
  spec=["general principle: for any symmetric X with finite third moment, X and |X| (or X^2) are uncorrelated but dependent",
        "the one place the converse DOES hold: (X, Y) jointly Gaussian => uncorrelated implies independent"],
  cxd={"this_IS_the_counterexample": "it shows independence_expectation is a one-way implication"},
  misuse=["concluding independence from a zero sample correlation",
          "using rho as a general dependence measure (it is not -- consider distance correlation / mutual information)",
          "assuming a regression with R^2 = 0 means no relationship"],
  related={"limits": ["independence_expectation"], "exception": ["jointly Gaussian (normal_distribution)"]},
  sources=["grimmett_stirzaker", "durrett_pte"], status="reviewed")

# ---------------------------------------------------------------- inequalities
N("jensen_inequality", "theorem", "inequalities",
  "If phi is convex and X, phi(X) are integrable, then phi(E[X]) <= E[phi(X)]. If phi is strictly convex, equality holds iff X is a.s. constant.",
  "phi convex, X integrable  =>  phi(E[X]) <= E[phi(X)]",
  {"phi": "a convex function, type: R -> R (or on an interval containing the range of X)", "X": "an integrable random variable, type: L^1(P)"},
  "take a supporting line L(x) = phi(E[X]) + m(x - E[X]) <= phi(x) at the point E[X]; then E[phi(X)] >= E[L(X)] = L(E[X]) = phi(E[X]) by linearity and monotonicity of expectation.",
  proof=("supporting-line inequality phi(x) >= phi(c) + m(x - c) with c = E[X], then take expectations", "convex_function", "core", "validation/proof-checks.lean Prob.jensen_sq (phi = square, GENUINE universal in t,x,y,n via the factorization t(n-t)(x-y)^2)"),
  spec=["phi(x) = x^2: E[X]^2 <= E[X^2], i.e. Var(X) >= 0",
        "phi(x) = |x|: |E[X]| <= E[|X|]",
        "phi(x) = e^x: e^{E[X]} <= E[e^X] (used in the Chernoff/entropy bounds)",
        "phi(x) = -log x on X > 0: log E[X] >= E[log X] (AM-GM in expectation form)"],
  cxd={"convexity_of_phi": "phi concave (e.g. sqrt, log): the inequality REVERSES, phi(E[X]) >= E[phi(X)] -- applying Jensen the wrong way is the single most common error",
       "integrability": "phi(x) = x^2 on a Cauchy X: E[phi(X)] = inf, the inequality is vacuous"},
  misuse=["wrong direction for a concave phi", "assuming strict inequality without strict convexity AND a non-degenerate X",
          "applying to phi convex only on part of the range of X"],
  related={"requires": ["convex_function"], "generalizes": ["variance >= 0", "the moment ladder", "AM-GM"], "conditional_version": ["conditional Jensen -- note on tower_property"]},
  sources=["boucheron_lugosi_massart", "durrett_pte"], status="reviewed")

N("holder_inequality", "theorem", "inequalities",
  "If 1/p + 1/q = 1 with p, q > 1 (or the pair 1, inf), then E[|XY|] <= ||X||_p ||Y||_q. The case p = q = 2 is Cauchy-Schwarz.",
  "1/p + 1/q = 1  =>  E[|XY|] <= ||X||_p ||Y||_q",
  {"X": "in L^p(P), type: L^p(P)", "Y": "in L^q(P), type: L^q(P)", "p, q": "conjugate exponents, type: real > 1"},
  "Young's inequality ab <= a^p/p + b^q/q (a convexity fact) applied pointwise to a = |X|/||X||_p, b = |Y|/||Y||_q, then take expectations: E[|XY|]/(||X||_p ||Y||_q) <= 1/p + 1/q = 1.",
  proof=("normalize, apply Young's inequality (from convexity of exp / concavity of log) pointwise, integrate", "jensen_inequality", "core", None),
  spec=["p = q = 2: Cauchy-Schwarz, (E|XY|)^2 <= E[X^2] E[Y^2]",
        "p = 1, q = inf: E[|XY|] <= E[|X|] ess-sup|Y|",
        "Y = 1: E[|X|] <= ||X||_p (part of the moment ladder)",
        "generalized (three factors): E[|XYZ|] <= ||X||_r ||Y||_s ||Z||_t with 1/r + 1/s + 1/t = 1"],
  cxd={"conjugacy_1_over_p_plus_1_over_q_eq_1": "with 1/p + 1/q < 1 the inequality is false in general (dimensional analysis / scaling X -> cX breaks it)",
       "X_in_Lp_and_Y_in_Lq": "if X not in L^p the right side is infinite -- the bound holds but says nothing"},
  misuse=["using non-conjugate exponents", "forgetting the absolute values (Holder bounds E[|XY|], not E[XY])"],
  related={"generalizes": ["cauchy_schwarz_expectation"], "dual_pair_with": ["minkowski (the triangle inequality for ||.||_p)"], "used_by": ["moment_ladder"]},
  sources=["folland_real_analysis", "boucheron_lugosi_massart"], status="reviewed")

N("chernoff_bound", "theorem", "inequalities",
  "For any random variable X with an MGF and any a: P(X >= a) <= inf_{t > 0} e^{-ta} M_X(t). Symmetrically P(X <= a) <= inf_{t < 0} e^{-ta} M_X(t).",
  "P(X >= a) <= inf_{t > 0} e^{-t a} M_X(t)",
  {"X": "a random variable with M_X(t) < inf for some t > 0, type: Omega -> R", "a": "a threshold, type: real"},
  "for fixed t > 0, { X >= a } = { e^{tX} >= e^{ta} }; apply Markov to the nonnegative variable e^{tX}: P(X >= a) <= E[e^{tX}]/e^{ta} = e^{-ta} M_X(t). Then optimize over t.",
  proof=("Markov on e^{tX} with threshold e^{ta}, then take the infimum over t > 0", "markov_inequality", "core", "validation/proof-checks.lean Prob.markov_finite (Markov core; e^{tX} transform is one line)"),
  solving_for="the exponentially small tail bound that Markov/Chebyshev (polynomial) cannot give",
  spec=["X ~ N(0, sigma^2): optimizing gives P(X >= a) <= e^{-a^2 / (2 sigma^2)} -- the Gaussian tail",
        "X = sum of n iid: M_X(t) = M_{X_1}(t)^n, so the bound is exponentially small in n -- the large-deviations rate function I(a) = sup_t (ta - log M_{X_1}(t))",
        "X ~ Poisson(lambda), a = lambda(1 + delta): the multiplicative Chernoff bound e^{-lambda delta^2/(2+delta)}"],
  cxd={"existence_of_the_MGF_for_some_t_gt_0": "heavy-tailed X (Cauchy, power law): M_X(t) = inf for all t > 0, the bound is vacuous -- only polynomial (Markov/Chebyshev/moment) bounds apply"},
  misuse=["forgetting to optimize over t (a single t gives a valid but loose bound)",
          "applying it when the MGF does not exist", "using t <= 0 for an upper-tail bound"],
  related={"derives_from": ["markov_inequality"], "sharpens": ["chebyshev_inequality"], "used_by": ["hoeffding_inequality"], "dual_of": ["Cramer's large-deviations theorem"]},
  sources=["boucheron_lugosi_massart", "durrett_pte"], status="reviewed")

N("hoeffding_lemma", "lemma", "inequalities",
  "If X is a random variable with a <= X <= b a.s. and E[X] = 0, then M_X(t) = E[e^{tX}] <= exp(t^2 (b - a)^2 / 8) for all real t. (X is sub-Gaussian with parameter (b-a)/2.)",
  "a <= X <= b a.s., E[X] = 0  =>  E[e^{tX}] <= exp(t^2 (b - a)^2 / 8)",
  {"X": "a bounded centered random variable, type: Omega -> [a, b]", "t": "a real parameter, type: real"},
  "by convexity of x |-> e^{tx} on [a, b], e^{tX} <= (b - X)/(b - a) e^{ta} + (X - a)/(b - a) e^{tb}; take expectations (E[X] = 0), define psi(t) = log of the result, and show psi''(t) <= (b - a)^2 / 4 by a variance argument, so psi(t) <= t^2 (b-a)^2 / 8.",
  proof=("convex bound of e^{tx} by its chord on [a,b]; take E; the log of the bound has second derivative <= (b-a)^2/4 (it is the variance of a tilted [a,b]-valued law); integrate twice from psi(0) = psi'(0) = 0", "convex_function", "cited", "Hoeffding 1963 Lemma; Boucheron-Lugosi-Massart Lemma 2.2"),
  spec=["X ~ Uniform{-c, c} (or any symmetric law on [-c, c]): recovers the sub-Gaussian bound e^{c^2 t^2 / 2}",
        "the (b - a)^2 / 8 constant is sharp for the two-point law at a, b with mean 0"],
  cxd={"boundedness": "an unbounded centered X (e.g. centered exponential) is not sub-Gaussian -- its MGF grows faster than any e^{ct^2}, only e^{c|t|} for small t (sub-exponential); Hoeffding's inequality is replaced by Bernstein's",
       "E_X_eq_0": "without centering, M_X(t) has an extra e^{t E[X]} factor -- the lemma is stated for the centered variable"},
  misuse=["applying it to unbounded variables", "forgetting to center first"],
  related={"requires": ["convex_function", "mgf"], "used_by": ["hoeffding_inequality"], "generalizes_to": ["sub-Gaussian / Bernstein / sub-exponential concentration"]},
  sources=["boucheron_lugosi_massart", "durrett_pte"], status="reviewed")

N("hoeffding_inequality", "theorem", "inequalities",
  "If X_1, ..., X_n are independent with a_i <= X_i <= b_i a.s., and S = sum X_i, then for s > 0: P(S - E[S] >= s) <= exp(-2 s^2 / sum_i (b_i - a_i)^2), and the two-sided bound doubles the right side.",
  "X_i independent in [a_i, b_i], S = sum X_i  =>  P(S - E[S] >= s) <= exp(-2 s^2 / sum (b_i - a_i)^2)",
  {"X_i": "independent bounded random variables, type: Omega -> [a_i, b_i]", "s": "the deviation, type: positive real"},
  "Chernoff on S - E[S]: P(S - E[S] >= s) <= e^{-ts} prod_i E[e^{t(X_i - E X_i)}] <= e^{-ts} exp(t^2 sum (b_i - a_i)^2 / 8) by independence (MGFs multiply) and Hoeffding's lemma; optimize t = 4s / sum (b_i - a_i)^2.",
  proof=("Chernoff + mgf_sum_independent + hoeffding_lemma per factor, then optimize over t", "hoeffding_lemma", "core", "validation/proof-checks.lean Prob.markov_finite (Markov/Chernoff core); the assembly is algebra"),
  solving_for="a non-asymptotic, distribution-free concentration bound for a sum/average of bounded independent variables",
  spec=["X_i in [0, 1], sample mean Xbar: P(Xbar - E[Xbar] >= eps) <= e^{-2 n eps^2} -- the workhorse bound for empirical means, bandit algorithms, and PAC learning",
        "n coin flips: P(#heads - n/2 >= s) <= e^{-2 s^2 / n}",
        "gives the sample size n >= (1/(2 eps^2)) log(2/delta) for an eps-accurate mean with confidence 1 - delta"],
  cxd={"boundedness_of_each_X_i": "one unbounded X_i (even with tiny variance) breaks the sub-Gaussian MGF bound -- use Bernstein's inequality (needs a variance bound + a one-sided bound) instead",
       "independence": "for dependent X_i the MGF does not factor; McDiarmid's / Azuma's inequality handles bounded-difference dependence"},
  misuse=["applying it to unbounded variables", "using it for dependent data",
          "forgetting the factor 2 in the two-sided version", "ignoring that it can be very loose when the variances are much smaller than the ranges (Bernstein is tighter then)"],
  related={"derives_from": ["hoeffding_lemma", "chernoff_bound"], "sharpens": ["chebyshev_inequality"], "relatives": ["Bernstein, Azuma-Hoeffding, McDiarmid"]},
  sources=["boucheron_lugosi_massart", "durrett_pte"], status="reviewed")

# ---------------------------------------------------------------- distributions
N("bernoulli_distribution", "definition", "distributions",
  "X ~ Bernoulli(p), p in [0,1]: P(X = 1) = p, P(X = 0) = 1 - p. E[X] = p, Var(X) = p(1-p), M_X(t) = 1 - p + p e^t. The indicator of a probability-p event.",
  "P(X=1) = p, P(X=0) = 1-p ;  E = p ;  Var = p(1-p)",
  {"X": "a Bernoulli variable, type: Omega -> {0,1}", "p": "success probability, type: real in [0,1]"},
  "the building block: any event A gives 1_A ~ Bernoulli(P(A)). E[X] = E[X^2] = p (since X^2 = X), so Var = p - p^2.",
  welldef="a two-point law with masses p and 1 - p summing to 1; well-defined for every p in [0,1].",
  spec=["p = 1/2: the fair coin, maximum variance 1/4", "p in {0,1}: degenerate (constant), variance 0",
        "sum of n iid Bernoulli(p) = Binomial(n, p)"],
  cxd={"p_in_0_1": "p outside [0,1] is not a probability"},
  misuse=["confusing the parameter p with the outcome", "forgetting Var is maximized at p = 1/2, not p = 1"],
  related={"generalizes_to": ["binomial_distribution"], "is": ["an indicator random variable (indicator_rv)"]},
  sources=G, status="reviewed")

N("binomial_distribution", "definition", "distributions",
  "X ~ Binomial(n, p): the number of successes in n independent Bernoulli(p) trials. P(X = k) = C(n, k) p^k (1-p)^{n-k}. E[X] = np, Var(X) = np(1-p), M_X(t) = (1 - p + p e^t)^n.",
  "P(X = k) = C(n,k) p^k (1-p)^{n-k} ;  E = np ;  Var = np(1-p)",
  {"X": "a binomial count, type: Omega -> {0,1,...,n}", "n": "number of trials, type: positive integer", "p": "success probability, type: real in [0,1]"},
  "X = sum_{i=1}^n Y_i with Y_i iid Bernoulli(p); the mean and variance follow from linearity and independence (variance_of_sum), not from the combinatorial sum.",
  proof=("mean by expectation_linearity over the indicator sum; variance by variance_of_sum with independence; MGF by mgf_sum_independent", "mgf_sum_independent", "core", "validation/proof-checks.lean -- Binomial(4,1/2) mean/var decide instances + Prob.var_of_sum_raw"),
  spec=["n = 1: Bernoulli(p)", "p = 1/2: symmetric about n/2",
        "n large, p small, np = lambda: approx Poisson(lambda) (poisson_limit_theorem)",
        "n large, p fixed: (X - np)/sqrt(np(1-p)) approx N(0,1) (de Moivre-Laplace, a case of the CLT)"],
  cxd={"independence_of_trials": "correlated trials (e.g. sampling without replacement) give the hypergeometric distribution, with the SAME mean np but SMALLER variance (finite-population correction)",
       "identical_p": "varying p_i per trial gives the Poisson-binomial distribution; mean sum p_i, variance sum p_i(1-p_i)"},
  misuse=["using it for sampling without replacement", "assuming Var = np (that is the Poisson limit; binomial Var = np(1-p) < np)"],
  related={"sum_of": ["bernoulli_distribution"], "limits_to": ["poisson_distribution", "normal_distribution"], "without_replacement": ["hypergeometric"]},
  sources=G, status="reviewed")

N("geometric_distribution", "definition", "distributions",
  "X ~ Geometric(p): the trial index of the first success in iid Bernoulli(p) trials. P(X = k) = (1-p)^{k-1} p for k = 1, 2, .... E[X] = 1/p, Var(X) = (1-p)/p^2. Memoryless.",
  "P(X = k) = (1-p)^{k-1} p ,  k >= 1 ;  E = 1/p ;  Var = (1-p)/p^2",
  {"X": "the first-success index, type: Omega -> {1,2,...}", "p": "success probability, type: real in (0,1]"},
  "the unique memoryless distribution on the positive integers: P(X > m + k | X > m) = P(X > k). (Convention varies: some define X as the number of FAILURES before the first success, support {0,1,2,...}, E = (1-p)/p.)",
  welldef="sum_{k>=1} (1-p)^{k-1} p = p / (1 - (1-p)) = 1 (geometric series); needs p > 0.",
  spec=["p = 1: X = 1 a.s.", "P(X > k) = (1-p)^k -- a clean survival function",
        "min of independent geometrics with rates p_i is geometric with rate 1 - prod(1 - p_i)"],
  cxd={"memorylessness_pins_it_down": "any non-geometric law on {1,2,...} fails P(X > m+k | X > m) = P(X > k) for some m, k",
       "p_gt_0": "p = 0 gives no success ever -- X = inf, not a proper random variable"},
  misuse=["mixing the two conventions (first-trial index vs failure count) -- they differ by 1 in mean",
          "assuming the memoryless property for a non-geometric discrete law"],
  related={"continuous_analogue": ["exponential_distribution"], "characterized_by": ["memorylessness"], "sum_of_r_iid": ["negative binomial"]},
  sources=G, status="reviewed")

N("poisson_distribution", "definition", "distributions",
  "X ~ Poisson(lambda), lambda > 0: P(X = k) = e^{-lambda} lambda^k / k! for k = 0, 1, 2, .... E[X] = Var(X) = lambda. M_X(t) = exp(lambda(e^t - 1)).",
  "P(X = k) = e^{-lambda} lambda^k / k! ;  E = Var = lambda",
  {"X": "a Poisson count, type: Omega -> {0,1,2,...}", "lambda": "the rate / mean, type: positive real"},
  "the law of counts of rare events: the limit of Binomial(n, lambda/n) as n -> inf (poisson_limit_theorem), and the one-parameter family with equal mean and variance. Sums of independent Poissons are Poisson (rates add).",
  proof=("mean: sum k e^{-lambda} lambda^k/k! = lambda sum e^{-lambda} lambda^{k-1}/(k-1)! = lambda. Variance via E[X(X-1)] = lambda^2 then Var = lambda^2 + lambda - lambda^2. MGF: sum e^{tk} e^{-lambda} lambda^k/k! = e^{-lambda} e^{lambda e^t}", "series_convergence", "core", "validation/instance-checks.bc -- Poisson(2) E and Var = 2"),
  spec=["number of decay events per second; typos per page; arrivals in a fixed interval of a Poisson process",
        "lambda large: Poisson(lambda) approx N(lambda, lambda) (a CLT via the sum-of-Poissons representation)",
        "the index of dispersion Var/mean = 1 -- overdispersed count data (Var > mean) needs negative binomial instead"],
  cxd={"lambda_gt_0": "lambda = 0 degenerates to X = 0 a.s.",
       "equal_mean_and_variance": "real count data with Var > mean (contagion, heterogeneity) is NOT Poisson -- fitting Poisson underestimates the variance and overstates significance"},
  misuse=["using Poisson for overdispersed counts", "assuming independence of counts in disjoint intervals without the Poisson-process assumption"],
  related={"limit_of": ["binomial_distribution (poisson_limit_theorem)"], "overdispersed_alternative": ["negative binomial"], "process_version": ["Poisson process (boundary)"]},
  sources=G, status="reviewed")

N("poisson_limit_theorem", "theorem", "distributions",
  "If X_n ~ Binomial(n, p_n) with n p_n -> lambda in (0, inf), then X_n converges in distribution to Poisson(lambda): P(X_n = k) -> e^{-lambda} lambda^k / k! for each k.",
  "Binomial(n, lambda/n)  -->^{d}  Poisson(lambda)   as n -> inf",
  {"X_n": "Binomial(n, p_n), type: Omega -> {0,...,n}", "lambda": "the limiting mean, type: positive real"},
  "the 'law of rare events': many trials, each very unlikely, with a stable expected count. Proof by direct pmf limit, or by MGF: (1 - p_n + p_n e^t)^n = (1 + (n p_n)(e^t - 1)/n)^n -> exp(lambda(e^t - 1)).",
  proof=("pmf: C(n,k) p_n^k (1-p_n)^{n-k} = [n!/(n-k)! n^k] (n p_n)^k/k! (1 - p_n)^{n-k} -> 1 . lambda^k/k! . e^{-lambda}. Or via MGF convergence + mgf_uniqueness", "mgf_uniqueness", "cited", "Durrett Thm 3.6.1; Billingsley Thm 23.2"),
  conv_mode="in_distribution",
  spec=["n = 1000 trials of probability 1/1000: number of successes approx Poisson(1) -- the bc worksheet shows the pmf at k = 3 converging",
        "raisins per cookie, mutations per genome, connection requests per millisecond"],
  cxd={"n_p_n_converges_to_a_finite_positive_limit": "if n p_n -> inf the correct limit is Gaussian (CLT); if n p_n -> 0 the count is 0 a.s. in the limit",
       "p_n_to_0": "with p fixed (not -> 0), Binomial(n, p) has mean np -> inf and is approximately Gaussian, not Poisson"},
  misuse=["using the Poisson approximation when np is large and p is not small (use the normal approximation)",
          "applying it with a fixed p"],
  related={"instance_of": ["convergence_in_distribution"], "connects": ["binomial_distribution", "poisson_distribution"]},
  sources=["durrett_pte", "billingsley_probability_measure"], status="reviewed")

N("continuous_uniform_distribution", "definition", "distributions",
  "X ~ Uniform(a, b): density f_X(x) = 1/(b - a) on [a, b], 0 elsewhere. E[X] = (a+b)/2, Var(X) = (b-a)^2/12. CDF F_X(x) = (x - a)/(b - a) on [a, b].",
  "f_X(x) = 1/(b-a) on [a,b] ;  E = (a+b)/2 ;  Var = (b-a)^2/12",
  {"X": "a uniform variable, type: Omega -> [a,b]", "a < b": "the endpoints, type: real"},
  "the maximum-entropy law on a bounded interval; the target of the probability integral transform (F_X(X) ~ Uniform(0,1)) and the source for inversion sampling (F^{-1}(U) ~ any law).",
  welldef="f_X >= 0 and integral_a^b 1/(b-a) dx = 1; well-defined for any a < b.",
  spec=["Uniform(0,1): the RNG primitive; E = 1/2, Var = 1/12",
        "-log(U) ~ Exponential(1); U^{1/n} ~ Beta(n, 1); (U_1, ..., U_n) order statistics ~ Beta",
        "sum of 12 iid Uniform(0,1) minus 6 is approximately N(0,1) (a crude Gaussian generator)"],
  cxd={"bounded_support": "there is no uniform distribution on R or on (0, inf) -- 'improper uniform' priors are not probability measures (they still yield proper posteriors sometimes)"},
  misuse=["assuming a uniform prior is 'non-informative' (it is not invariant under reparameterization)",
          "using Var = (b-a)^2/4 (that is the range squared over 4, not the variance)"],
  related={"transform_target": ["probability_integral_transform"], "order_statistics": ["beta_distribution"]},
  sources=G, status="reviewed")

N("exponential_distribution", "definition", "distributions",
  "X ~ Exponential(lambda), lambda > 0: density f_X(x) = lambda e^{-lambda x} for x >= 0. E[X] = 1/lambda, Var(X) = 1/lambda^2, M_X(t) = lambda/(lambda - t) for t < lambda. Memoryless.",
  "f_X(x) = lambda e^{-lambda x}, x >= 0 ;  E = 1/lambda ;  Var = 1/lambda^2",
  {"X": "an exponential variable, type: Omega -> [0, inf)", "lambda": "the rate, type: positive real"},
  "the unique memoryless distribution on [0, inf): P(X > s + t | X > s) = P(X > t). The waiting time between events of a rate-lambda Poisson process; the continuous analogue of the geometric.",
  proof=("normalization integral_0^inf lambda e^{-lambda x} dx = 1; E[X] = integral x lambda e^{-lambda x} dx = 1/lambda by parts; memorylessness from P(X > t) = e^{-lambda t}", "pdf", "core", "validation/instance-checks.bc -- Exponential(0.5): E=2, Var=4, memoryless check"),
  spec=["lambda = 1: standard exponential; -log(U) for U ~ Uniform(0,1)",
        "min of independent Exponentials(lambda_i) ~ Exponential(sum lambda_i) -- competing risks",
        "sum of k iid Exponential(lambda) ~ Gamma(k, 1/lambda)"],
  cxd={"memorylessness": "the Weibull, gamma (shape != 1), and lognormal are NOT memoryless -- using an exponential for aging components (increasing hazard) underestimates late failures",
       "constant_hazard_rate": "f_X(x)/P(X > x) = lambda is constant; real lifetimes usually have a bathtub or increasing hazard"},
  misuse=["modeling component lifetimes with wear-out as exponential", "confusing the rate lambda with the mean 1/lambda"],
  related={"discrete_analogue": ["geometric_distribution"], "characterized_by": ["memorylessness"], "sum_gives": ["gamma_distribution"]},
  sources=G, status="reviewed")

N("memorylessness", "proposition", "distributions",
  "P(X > s + t | X > s) = P(X > t) for all s, t >= 0. Among distributions on [0, inf) this holds iff X is exponential; among distributions on {1, 2, ...} iff X is geometric.",
  "P(X > s + t | X > s) = P(X > t)   characterizes exponential (continuous) / geometric (discrete)",
  {"X": "a nonnegative random variable, type: Omega -> [0, inf) or {1,2,...}", "s, t": "nonnegative reals/integers"},
  "the survival function G(x) = P(X > x) satisfies G(s + t) = G(s) G(t) (Cauchy's functional equation); the only monotone solutions are G(x) = e^{-lambda x} (continuous) or G(k) = (1-p)^k (discrete).",
  proof=("P(X > s+t | X > s) = G(s+t)/G(s) = G(t) means G(s+t) = G(s)G(t); with G monotone and G(0) = 1, G(x) = G(1)^x = e^{-lambda x}", "cdf", "cited", "Grimmett-Stirzaker 4.8; Feller I.XIII"),
  spec=["the residual lifetime of an exponential component is exactly a fresh exponential -- no 'aging'",
        "a geometric number of coin flips: given the first m were failures, the additional flips to a success is again Geometric(p)"],
  cxd={"the_characterization_is_exact": "gamma with shape 2: P(X > s + t | X > s) DECREASES in s -- it 'remembers' (positive aging). Weibull with shape > 1 likewise. Pareto: negative aging."},
  misuse=["assuming any 'waiting time' is memoryless", "using memorylessness to justify ignoring elapsed time for a non-exponential process"],
  related={"characterizes": ["exponential_distribution", "geometric_distribution"], "fails_for": ["gamma, Weibull, lognormal, Pareto"]},
  sources=["grimmett_stirzaker", "durrett_pte"], status="reviewed")

N("gamma_distribution", "definition", "distributions",
  "X ~ Gamma(k, theta), shape k > 0, scale theta > 0: density f_X(x) proportional to x^{k-1} e^{-x/theta} on x > 0 (normalizer Gamma(k) theta^k). E[X] = k theta, Var(X) = k theta^2. For integer k it is the sum of k iid Exponential(1/theta).",
  "f_X(x) prop x^{k-1} e^{-x/theta}, x > 0 ;  E = k theta ;  Var = k theta^2",
  {"X": "a gamma variable, type: Omega -> (0, inf)", "k": "shape, type: positive real", "theta": "scale, type: positive real"},
  "the flexible right-skewed family on (0, inf): shape k < 1 gives a pole at 0, k = 1 is exponential, k large approaches normal. Closed under sums with common scale (shapes add). Rate parameterization uses beta = 1/theta.",
  proof=("for integer k, convolution_formula on k iid Exponential(1/theta); E and Var by k-fold sum of the exponential's 1/lambda and 1/lambda^2. General k via the Gamma-function integral", "convolution_formula", "cited", "Grimmett-Stirzaker 4.14"),
  spec=["k = 1: Exponential(1/theta)", "Gamma(k, 2) with 2k = nu integer: chi-squared with nu degrees of freedom",
        "conjugate prior for the rate of a Poisson / the precision of a normal",
        "k -> inf: (X - k theta)/sqrt(k theta^2) -> N(0,1)"],
  cxd={"common_scale_for_the_sum_rule": "Gamma(k_1, theta_1) + Gamma(k_2, theta_2) with theta_1 != theta_2 is NOT gamma -- the sum rule needs a shared scale",
       "shape_and_scale_vs_shape_and_rate": "software differs; mixing them scales the mean by theta^2"},
  misuse=["adding gammas with different scales", "confusing scale theta with rate 1/theta"],
  related={"sum_of": ["exponential_distribution"], "special_case": ["chi-squared, Erlang"], "conjugate_to": ["Poisson rate, normal precision"]},
  sources=G, status="reviewed")

N("beta_distribution", "definition", "distributions",
  "X ~ Beta(a, b), a, b > 0: density f_X(x) proportional to x^{a-1} (1-x)^{b-1} on (0, 1) (normalizer B(a,b) = Gamma(a)Gamma(b)/Gamma(a+b)). E[X] = a/(a+b), Var(X) = ab / ((a+b)^2 (a+b+1)).",
  "f_X(x) prop x^{a-1} (1-x)^{b-1}, 0 < x < 1 ;  E = a/(a+b)",
  {"X": "a beta variable, type: Omega -> (0,1)", "a, b": "shape parameters, type: positive real"},
  "the canonical family for a random PROBABILITY or proportion. Beta(1,1) = Uniform(0,1). It is the conjugate prior for a Bernoulli/binomial rate: prior Beta(a,b) + k successes in n trials -> posterior Beta(a + k, b + n - k).",
  welldef="the Beta function B(a,b) = integral_0^1 x^{a-1}(1-x)^{b-1} dx converges for a, b > 0 and normalizes the density.",
  spec=["a = b = 1: Uniform(0,1)", "a = b: symmetric about 1/2; a = b large: concentrated near 1/2 (approx normal)",
        "a, b < 1: U-shaped, mass near 0 and 1", "the k-th order statistic of n iid Uniform(0,1) is Beta(k, n - k + 1)",
        "if Y_1 ~ Gamma(a, 1), Y_2 ~ Gamma(b, 1) independent, then Y_1/(Y_1 + Y_2) ~ Beta(a, b)"],
  cxd={"support_is_the_unit_interval": "for a proportion that can be exactly 0 or 1, a zero-or-one-inflated beta is needed; plain beta puts zero mass on the endpoints"},
  misuse=["using it for a quantity outside [0,1] without rescaling", "reading Beta(a,b) mean as a/b (it is a/(a+b))"],
  related={"conjugate_to": ["bernoulli_distribution", "binomial_distribution"], "generalizes": ["continuous_uniform_distribution on (0,1)"], "multivariate": ["Dirichlet"]},
  sources=G, status="reviewed")

N("normal_distribution", "definition", "distributions",
  "X ~ N(mu, sigma^2), sigma > 0: density f_X(x) = (1/(sigma sqrt(2 pi))) exp(-(x - mu)^2 / (2 sigma^2)). E[X] = mu, Var(X) = sigma^2, M_X(t) = exp(mu t + sigma^2 t^2 / 2), phi_X(t) = exp(i mu t - sigma^2 t^2 / 2).",
  "f_X(x) = exp(-(x-mu)^2/(2 sigma^2)) / (sigma sqrt(2 pi)) ;  E = mu ;  Var = sigma^2",
  {"X": "a normal variable, type: Omega -> R", "mu": "mean, type: real", "sigma^2": "variance, type: positive real"},
  "parameterized by the VARIANCE sigma^2 (not sigma). The universal limit law (CLT), the maximum-entropy law for a given mean and variance, closed under affine maps and independent sums, and the only law where zero correlation implies independence (jointly).",
  proof=("normalization by the Gaussian integral integral e^{-x^2/2} dx = sqrt(2 pi); MGF by completing the square; E = mu, Var = sigma^2 from M''(0)", "abstract_integral", "core", "validation/instance-checks.bc -- standard normal pdf integrates to 1, second moment 1"),
  spec=["mu = 0, sigma = 1: standard normal Z; X = mu + sigma Z",
        "sum of independent normals is normal (variances add); the sample mean of iid normals is exactly normal",
        "68-95-99.7 within 1-2-3 sigma; tail P(Z > z) approx phi(z)/z"],
  cxd={"light_tails": "financial returns, network delays, and many natural quantities have heavier-than-Gaussian tails -- assuming normality drastically underestimates extreme-event probabilities (a 5-sigma event is ~1 in 3.5 million under normality, far more common in reality)",
       "the_CLT_does_not_make_everything_normal": "the CLT needs iid-ish summands with finite variance; a single dominant term, heavy tails, or strong dependence breaks it"},
  misuse=["assuming normality for skewed or heavy-tailed data", "using sigma where sigma^2 is the parameter",
          "treating a large-sample CLT approximation as exact in the tails (Berry-Esseen: the error is O(1/sqrt n) and worst in the tails)"],
  related={"standardizes_to": ["standard_normal"], "closed_under": ["normal_affine_closure"], "limit_in": ["central_limit_theorem"]},
  sources=P, status="reviewed")

N("standard_normal", "definition", "distributions",
  "Z ~ N(0, 1): density phi(z) = e^{-z^2/2} / sqrt(2 pi), CDF Phi(z) = integral_{-inf}^z phi. E[Z] = 0, Var(Z) = 1, phi_Z(t) = e^{-t^2/2}, all odd moments 0, E[Z^{2k}] = (2k-1)!!.",
  "Z ~ N(0,1) ;  phi(z) = e^{-z^2/2}/sqrt(2 pi) ;  phi_Z(t) = e^{-t^2/2}",
  {"Z": "a standard normal variable, type: Omega -> R", "Phi": "its CDF, type: R -> (0,1)"},
  "the reference point: any N(mu, sigma^2) variable is mu + sigma Z, and any normal probability reduces to Phi. The CLT limit is stated as convergence to Z.",
  proof=("Z = (X - mu)/sigma for X ~ N(mu, sigma^2) via transformation_univariate; phi_Z(t) = e^{-t^2/2} by completing the square in E[e^{itZ}]", "transformation_univariate", "core", "validation/instance-checks.bc -- Phi(1) = 0.8413..."),
  spec=["Phi(0) = 1/2; Phi(1) approx 0.8413; Phi(1.96) approx 0.975 (the 95% two-sided quantile)",
        "Z^2 ~ chi-squared_1; Z_1/Z_2 ~ Cauchy for independent Z_i; sum of k iid Z_i^2 ~ chi-squared_k",
        "Mills ratio: P(Z > z)/phi(z) -> 1/z as z -> inf"],
  cxd={"none_it_is_a_fixed_law": "the standard normal is a single distribution; the caution is downstream (assuming data is standard normal after a bad standardization)"},
  misuse=["using a normal-approximation quantile (1.96) when the sample is small or heavy-tailed (use t)",
          "confusing phi (density) with Phi (CDF)"],
  related={"rescales_to": ["normal_distribution"], "clt_limit": ["central_limit_theorem"], "squares_to": ["chi-squared"]},
  sources=P, status="reviewed")

N("normal_affine_closure", "proposition", "distributions",
  "If X ~ N(mu, sigma^2) then aX + b ~ N(a mu + b, a^2 sigma^2) for a != 0. If X ~ N(mu_1, s_1^2), Y ~ N(mu_2, s_2^2) are independent, then X + Y ~ N(mu_1 + mu_2, s_1^2 + s_2^2).",
  "aX + b ~ N(a mu + b, a^2 sigma^2) ;  independent normals sum to a normal (means and variances add)",
  {"X, Y": "normal random variables, type: Omega -> R", "a, b": "constants, a != 0, type: real"},
  "affine closure by transformation_univariate; the sum by multiplying MGFs: exp(mu_1 t + s_1^2 t^2/2) exp(mu_2 t + s_2^2 t^2/2) = exp((mu_1+mu_2) t + (s_1^2 + s_2^2) t^2/2), then mgf_uniqueness.",
  proof=("affine: change of variables on the density. Sum: mgf_sum_independent then mgf_uniqueness -- the exponents add", "mgf_sum_independent", "core", None),
  spec=["standardization Z = (X - mu)/sigma ~ N(0,1) is the a = 1/sigma, b = -mu/sigma case",
        "sample mean of n iid N(mu, sigma^2) is exactly N(mu, sigma^2/n) -- the CLT holds with no error for normal data",
        "any linear combination sum a_i X_i of jointly normal X_i is normal -- the definition of a Gaussian vector"],
  cxd={"independence_for_the_sum": "X ~ N(0,1), Y = -X ~ N(0,1): X + Y = 0, a point mass, NOT N(0, 2) -- the sum rule needs independence (or joint normality with the right covariance)",
       "joint_normality_for_linear_combos": "X ~ N(0,1) and Y = X if |X| < 1 else -X: each is N(0,1) but X + Y is not normal -- marginal normality is not joint normality"},
  misuse=["adding variances of dependent normals", "assuming a sum of normal marginals is normal without joint normality"],
  related={"defines": ["the Gaussian vector / multivariate normal"], "uses": ["mgf_sum_independent", "mgf_uniqueness"]},
  sources=P, status="reviewed")

N("cauchy_no_mean", "counterexample", "distributions",
  "X ~ Cauchy: density f_X(x) = 1/(pi(1 + x^2)) on R. E[|X|] = inf, so E[X] does not exist and Var is undefined. The sample mean of n iid Cauchy variables is again Cauchy(0,1) -- it does not concentrate. The LLN and CLT both fail.",
  "f_X(x) = 1/(pi(1+x^2)) :  E[|X|] = inf ;  (X_1 + ... + X_n)/n ~ Cauchy for every n",
  {"X": "a standard Cauchy variable, type: Omega -> R", "f_X": "its density, type: R -> (0, inf)"},
  "the canonical finite-density law with no mean: the tails decay only like 1/x^2, so integral |x| f_X(x) dx = (2/pi) integral_0^inf x/(1+x^2) dx = inf. Its characteristic function phi_X(t) = e^{-|t|} exists (and is non-differentiable at 0, consistent with the missing mean).",
  welldef="f_X integrates to 1 (arctan), so Cauchy is a bona fide probability law; it is E[X] that fails to exist, not the distribution.",
  spec=["ratio Z_1/Z_2 of independent standard normals is standard Cauchy",
        "the sample mean stays Cauchy(0,1) (phi_{Xbar}(t) = phi_X(t/n)^n = e^{-|t|}) -- averaging does not help",
        "the sample MEDIAN of n iid Cauchy DOES concentrate (median is well-defined) and is asymptotically normal"],
  cxd={"this_IS_the_counterexample": "it shows the finite-mean hypothesis of the WLLN/SLLN and the finite-variance hypothesis of the CLT are not removable"},
  misuse=["applying the LLN or CLT to ratios, or to data with power-law tails of index <= 1 (no mean) or <= 2 (no variance)",
          "reporting a sample mean and its standard error for heavy-tailed data (both are meaningless)",
          "assuming a symmetric unimodal density implies a mean exists"],
  related={"breaks": ["weak_law_large_numbers", "strong_law_large_numbers", "central_limit_theorem"], "stable_law": ["index 1"], "arises_as": ["ratio of normals, tan of a uniform angle"]},
  sources=["durrett_pte", "grimmett_stirzaker"], status="reviewed")

# ---------------------------------------------------------------- convergence
def _cmode(nid, disp, parse, mode, tcn, deps_note, spec, cxd, misuse, related, proof=None, src=None):
    N(nid, "definition", "convergence", disp, parse,
      {"(X_n)": "a sequence of random variables on one probability space, type: N -> (Omega -> R)",
       "X": "the limit random variable (or law), type: Omega -> R (or a law)"},
      tcn, conv_mode=mode, proof=proof, spec=spec, cxd=cxd, misuse=misuse, related=related,
      sources=src or ["durrett_pte", "billingsley_probability_measure"], status="reviewed")

_cmode("convergence_almost_sure",
  "X_n -> X almost surely if P({omega : X_n(omega) -> X(omega)}) = 1.",
  "P(X_n -> X) = 1",
  "almost_sure",
  "the convergence set { omega : X_n(omega) -> X(omega) } is an event (a countable combination of { |X_n - X| < 1/k }); a.s. convergence requires it to have probability 1. This is the strongest of the four modes together with L^p.",
  "requires the X_n and X on a COMMON probability space (pointwise statement).",
  ["the SLLN delivers this mode: sample mean -> E[X_1] a.s.",
   "a.s. convergence is preserved by continuous functions (continuous_mapping_theorem) and is equivalent to P(sup_{m >= n} |X_m - X| > eps) -> 0 for all eps"],
  {"common_probability_space": "a.s. convergence is meaningless for X_n and X defined on different spaces -- only the WEAKER convergence in distribution makes sense then"},
  ["confusing 'X_n -> X a.s.' with 'P(X_n -> X) can be computed pointwise' -- it needs the whole trajectory",
   "assuming a.s. convergence from convergence in probability (only a SUBSEQUENCE converges a.s.)"],
  {"implies": ["convergence_in_probability"], "delivered_by": ["strong_law_large_numbers"], "tag": ["a.s. -- the choice_grade analogue"]})

_cmode("convergence_in_probability",
  "X_n -> X in probability if for every eps > 0, P(|X_n - X| > eps) -> 0 as n -> inf.",
  "for all eps > 0:  P(|X_n - X| > eps) -> 0",
  "in_probability",
  "a statement about the MARGINAL of |X_n - X| for each n -- no joint trajectory needed beyond a common space. Weaker than a.s. (which controls the whole tail at once) and than L^p (Markov), stronger than in distribution.",
  "requires a common probability space; quantifier order is 'for all eps, the sequence P(...) -> 0'.",
  ["the WLLN delivers this mode: sample mean -> E[X_1] in probability",
   "X_n -> X in probability iff every subsequence has a further subsequence converging a.s. -- the 'subsequence principle'",
   "X_n -> c (a constant) in probability <=> X_n -> c in distribution"],
  {"eps_quantifier": "P(|X_n - X| > eps) -> 0 for ONE eps is not enough; it must hold for every eps > 0"},
  ["reading it as a.s. convergence (typewriter sequence: converges in probability, not a.s.)",
   "assuming a rate -- convergence in probability alone gives no n at which P(|X_n - X| > eps) < delta"],
  {"implied_by": ["convergence_almost_sure", "convergence_in_lp"], "implies": ["convergence_in_distribution"], "delivered_by": ["weak_law_large_numbers"], "tag": ["p"]})

_cmode("convergence_in_lp",
  "X_n -> X in L^p (p >= 1) if E[|X_n - X|^p] -> 0, i.e. ||X_n - X||_p -> 0.",
  "E[|X_n - X|^p] -> 0",
  "in_lp",
  "convergence in the L^p(P) norm; requires X_n, X in L^p. By Markov's inequality (applied to |X_n - X|^p) it implies convergence in probability; the converse needs uniform integrability.",
  "X_n, X must lie in L^p(P); p = 2 (mean square) is the common case.",
  ["L^2 convergence of the sample mean under finite variance (a one-line Chebyshev bound), giving the L^2 WLLN",
   "in a Hilbert space (L^2) it is convergence in norm; Cauchy sequences converge (Riesz-Fischer)"],
  {"uniform_integrability_for_the_converse": "X_n = n 1_{(0, 1/n]} on ([0,1], lambda): X_n -> 0 in probability and a.s., but E[|X_n|] = 1 not -> 0 -- convergence in probability does NOT imply L^1 without a dominating / uniformly integrable family"},
  ["forgetting the p (L^1 and L^2 convergence are different)",
   "assuming L^p convergence from a.s. convergence (needs domination -- DCT)"],
  {"implies": ["convergence_in_probability"], "via": ["markov_inequality"], "strongest_with": ["convergence_almost_sure"], "tag": ["L^p"]})

_cmode("convergence_in_distribution",
  "X_n -> X in distribution if F_{X_n}(x) -> F_X(x) at every x where F_X is continuous. Equivalently E[g(X_n)] -> E[g(X)] for every bounded continuous g (portmanteau).",
  "F_{X_n}(x) -> F_X(x)  at every continuity point x of F_X",
  "in_distribution",
  "the WEAKEST mode: it is a statement about the LAWS, not the random variables, so X_n and X need not live on the same space. The 'continuity point' clause is essential -- CDFs can converge everywhere except at jumps of the limit.",
  "only the laws P_{X_n}, P_X matter; the limit is often written as a distribution (X_n -> N(0,1)).",
  ["the CLT delivers this mode: standardized sample mean -> N(0,1) in distribution",
   "equivalent forms (portmanteau_theorem): E[g(X_n)] -> E[g(X)] for bounded continuous g; limsup P(X_n in C) <= P(X in C) for closed C; phi_{X_n}(t) -> phi_X(t) for all t (Levy)"],
  {"continuity_points_only": "X_n = 1/n (constant): F_{X_n} is a step at 1/n, F_X a step at 0; F_{X_n}(0) = 0 for all n but F_X(0) = 1 -- convergence fails AT the jump but X_n -> 0 in distribution is still true"},
  ["expecting F_{X_n}(x) -> F_X(x) at jump points of F_X",
   "concluding X_n -> X in probability (only true when X is a constant)",
   "reading 'X_n -> X in distribution' as any statement about X_n(omega)"],
  {"implied_by": ["convergence_in_probability"], "characterized_by": ["portmanteau_theorem", "levy_continuity_theorem"], "delivered_by": ["central_limit_theorem"], "tag": ["d"]})

N("convergence_implications", "theorem", "convergence",
  "The lattice of modes: (a.s.) => (in probability); (L^p) => (in probability); (in probability) => (in distribution); (in probability) => (a.s. along a subsequence); (in distribution to a CONSTANT) => (in probability). No other implication holds in general.",
  "a.s. => p ;  L^p => p ;  p => d ;  p => a.s. subsequence ;  d-to-constant => p",
  {"X_n, X": "random variables on a common space (except the d-only statements), type: N -> (Omega -> R)"},
  "each arrow is a short proof; the content is equally in the NON-arrows, witnessed by standard counterexamples (the typewriter sequence, escaping mass, a symmetric two-point law).",
  proof=("a.s.=>p: dominated convergence of indicators / continuity of P. L^p=>p: Markov on |X_n - X|^p. p=>d: portmanteau via a bounded-Lipschitz test function. p=>a.s. subsequence: pick n_k with P(|X_{n_k} - X| > 2^{-k}) < 2^{-k}, apply Borel-Cantelli 1. d-to-constant=>p: F of a constant is a step, so F_{X_n} -> it everywhere but the jump.", "portmanteau_theorem", "core", "validation/proof-checks.lean Prob.markov_finite + Prob.union_bound (the Boole/BC1 step)"),
  spec=["finite-dimensional summary: a.s. and L^p each imply p; p implies d; that is all",
        "Scheffe's lemma: if densities converge a.e. then L^1 (hence p, hence d) convergence follows -- a bridge that skips the counterexamples",
        "if X_n -> X in distribution and X_n -> Y in probability then X = Y in distribution"],
  cxd={"a_s_does_not_imply_L_p": "X_n = n 1_{(0,1/n]}: X_n -> 0 a.s. but E|X_n| = 1 (escaping mass)",
       "L_p_does_not_imply_a_s": "the typewriter sequence (indicators of [j/2^k, (j+1)/2^k] in order): -> 0 in every L^p but converges a.s. for NO omega",
       "p_does_not_imply_a_s": "same typewriter sequence -- in probability but not a.s.",
       "d_does_not_imply_p": "X ~ N(0,1), X_n = (-1)^n X: each X_n ~ N(0,1) so X_n -> N(0,1) in distribution, but |X_n - X_{n+1}| = 2|X| does not -> 0, so not in probability",
       "d_to_a_nonconstant_does_not_imply_p": "the same example -- the limit must be a CONSTANT for the reverse arrow"},
  misuse=["assuming convergence in distribution says anything about the variables jointly",
          "assuming a.s. => L^p (needs uniform integrability / a dominator)",
          "using 'converges in probability' as if it gave an a.s. limit"],
  related={"organizes": ["convergence_almost_sure", "convergence_in_probability", "convergence_in_lp", "convergence_in_distribution"], "uses": ["markov_inequality", "borel_cantelli_first"]},
  sources=["durrett_pte", "williams_probability_martingales"], status="reviewed")

N("portmanteau_theorem", "theorem", "convergence",
  "The following are equivalent to X_n -> X in distribution: (i) E[g(X_n)] -> E[g(X)] for all bounded continuous g; (ii) for all bounded Lipschitz g; (iii) limsup P(X_n in C) <= P(X in C) for all closed C; (iv) liminf P(X_n in U) >= P(X in U) for all open U; (v) P(X_n in A) -> P(X in A) for all A with P(X in boundary A) = 0.",
  "X_n -->^{d} X  <=>  E[g(X_n)] -> E[g(X)] for all bounded continuous g  (and 4 more forms)",
  {"g": "a test function, type: R -> R bounded and continuous", "C, U, A": "closed / open / continuity Borel sets, type: element of B(R)"},
  "the CDF definition is the special case A = (-inf, x] with P(X = x) = 0. Form (i) is the working definition of weak convergence on general metric spaces; forms (iii)-(v) are what make it a topology on laws.",
  proof=("CDF => (i) by approximating 1_{(-inf,x]} by Lipschitz functions and using continuity points; (i) => (iii) by g_k decreasing to 1_C; (iii) <=> (iv) by complements; (v) from both one-sided bounds when the boundary is null; (i) => CDF by (v) with A = (-inf, x]", "convergence_in_distribution", "cited", "Billingsley Convergence of Probability Measures Thm 2.1; Durrett Thm 3.2.5"),
  spec=["A = (-inf, x], P(X = x) = 0: the CDF form",
        "g bounded uniformly continuous is enough (form ii) -- the class can be shrunk",
        "the Levy metric / bounded-Lipschitz metric metrizes this convergence on laws over R"],
  cxd={"boundedness_of_g": "g(x) = x is continuous but unbounded: E[X_n] -> E[X] can FAIL under X_n -> X in distribution (escaping mass) -- convergence of unbounded moments needs uniform integrability",
       "continuity_of_g": "g = 1_{(-inf, 0]} (discontinuous): P(X_n <= 0) -> P(X <= 0) fails when X has an atom at 0",
       "P_of_boundary_zero_in_(v)": "A = {0}, X ~ N(0,1) (so P(X in bd A) = P(X = 0) = 0) is fine; A = {0}, X = 0 constant is not"},
  misuse=["applying form (i) to an unbounded g (moments)", "using P(X_n in A) -> P(X in A) for a set whose boundary carries mass"],
  related={"characterizes": ["convergence_in_distribution"], "used_by": ["continuous_mapping_theorem", "slutsky_theorem"]},
  sources=["billingsley_probability_measure", "durrett_pte"], status="reviewed")

N("continuous_mapping_theorem", "theorem", "convergence",
  "If X_n -> X (a.s., or in probability, or in distribution) and g is measurable with P(X in D_g) = 0 where D_g is g's discontinuity set, then g(X_n) -> g(X) in the same mode.",
  "X_n -> X (in mode M), P(X in disc(g)) = 0  =>  g(X_n) -> g(X)  (in mode M)",
  {"g": "a measurable function continuous P_X-a.e., type: R -> R^k", "D_g": "the set of discontinuities of g, type: Borel set"},
  "for a.s. and in-probability, pointwise/along-subsequence continuity carries the limit through; for in-distribution, use the portmanteau form (bounded continuous test functions compose with g to bounded a.e.-continuous functions).",
  proof=("a.s.: X_n(omega) -> X(omega) and g continuous at X(omega) (a.e.) => g(X_n(omega)) -> g(X(omega)). p: via the subsequence principle. d: portmanteau -- for bounded continuous h, h o g is bounded and continuous P_X-a.e.", "portmanteau_theorem", "cited", "Billingsley CPM Thm 2.7; Durrett Thm 3.2.10"),
  spec=["g(x) = x^2: X_n -> X in distribution => X_n^2 -> X^2 in distribution (e.g. sqrt(n) Xbar -> N(0, sigma^2) gives n Xbar^2 -> sigma^2 chi-squared_1)",
        "g continuous everywhere: the a.e. hypothesis is automatic",
        "combined with Slutsky to build asymptotic distributions of test statistics (t-statistic, Wald statistic)"],
  cxd={"P_X_gives_the_discontinuity_set_measure_zero": "g(x) = 1_{x >= 0}, X_n = -1/n -> 0, but g(X_n) = 0 for all n while g(0) = 1 -- g is discontinuous exactly at the limit point, which here has full mass",
       "same_mode_out": "if the input is only in distribution, the output is only in distribution -- you cannot upgrade"},
  misuse=["applying it across a discontinuity that the limit law charges",
          "expecting the output mode to be stronger than the input mode"],
  related={"uses": ["portmanteau_theorem"], "pairs_with": ["slutsky_theorem", "delta_method"]},
  sources=["billingsley_probability_measure", "durrett_pte"], status="reviewed")

N("slutsky_theorem", "theorem", "convergence",
  "If X_n -> X in distribution and Y_n -> c in probability (c a constant), then X_n + Y_n -> X + c, X_n Y_n -> cX, and X_n / Y_n -> X / c (c != 0), all in distribution.",
  "X_n -->^{d} X , Y_n -->^{p} c  =>  X_n + Y_n -->^{d} X + c , X_n Y_n -->^{d} cX",
  {"X_n": "sequence converging in distribution, type: N -> (Omega -> R)", "Y_n": "sequence converging in probability to a constant c, type: N -> (Omega -> R)", "c": "a constant, type: real"},
  "the key asymmetry: one sequence may converge only in distribution, but the OTHER must converge in probability to a CONSTANT (not a random variable). Then (X_n, Y_n) -> (X, c) jointly in distribution and the continuous map applies.",
  proof=("Y_n -> c in probability => (X_n, Y_n) -> (X, c) jointly in distribution (the constant limit removes the dependence problem), then continuous_mapping_theorem on +, x, /", "continuous_mapping_theorem", "cited", "Durrett Thm 3.2.8 (Ex); Billingsley Thm 25.4"),
  spec=["studentization: sqrt(n)(Xbar - mu)/S_n -> N(0,1), because sqrt(n)(Xbar - mu)/sigma -> N(0,1) and sigma/S_n -> 1 in probability",
        "if a_n -> a and b_n -> b (deterministic) and Z_n -> Z in distribution then a_n Z_n + b_n -> a Z + b"],
  cxd={"the_limit_c_must_be_a_constant": "X_n = Z ~ N(0,1) for all n (so X_n -> Z in distribution), Y_n = -Z (so Y_n -> -Z in distribution, NOT to a constant): X_n + Y_n = 0, not N(0,1) + N(0,1). Slutsky needs Y_n -> constant.",
       "convergence_in_probability_not_just_distribution_for_Y_n": "if Y_n -> c only in distribution (c constant) that is equivalent to in probability, so this is automatically fine -- but Y_n -> non-constant in distribution is not enough"},
  misuse=["applying it when both sequences converge only in distribution",
          "letting the 'constant' limit actually be a non-degenerate random variable"],
  related={"special_case_of": ["continuous_mapping_theorem (joint)"], "used_by": ["delta_method"]},
  sources=["durrett_pte", "billingsley_probability_measure"], status="reviewed")

N("weak_law_large_numbers", "theorem", "convergence",
  "If X_1, X_2, ... are iid with E|X_1| < inf and mean mu, then the sample mean Xbar_n = (X_1 + ... + X_n)/n -> mu IN PROBABILITY.",
  "X_i iid, E|X_1| < inf  =>  Xbar_n -->^{p} mu",
  {"X_i": "an iid sequence, type: N -> L^1(P)", "mu": "the common mean E[X_1], type: real", "Xbar_n": "the sample mean, type: Omega -> R"},
  "convergence mode: IN PROBABILITY (weaker than the SLLN's a.s.). Finite mean is enough; the classical finite-variance proof is a one-line Chebyshev bound, the general case uses truncation or characteristic functions.",
  proof=("finite-variance route: Var(Xbar_n) = sigma^2/n, so P(|Xbar_n - mu| > eps) <= sigma^2/(n eps^2) -> 0 (Chebyshev). General route: truncate X_i at n, control the mean shift and the variance of the truncated part; or phi_{Xbar_n}(t) = phi_{X_1}(t/n)^n -> e^{i mu t}, the CF of the constant mu", "chebyshev_inequality", "core", "validation/proof-checks.lean Prob.chebyshev_reduction_fwd + Prob.var_of_sum_raw"),
  conv_mode="in_probability",
  spec=["X_i ~ Bernoulli(p): the relative frequency of successes -> p in probability (Bernoulli's theorem, 1713)",
        "pairwise independence and finite variance are ENOUGH for this mode (the Chebyshev proof only uses pairwise uncorrelatedness)",
        "Monte Carlo integration: (1/n) sum g(U_i) -> integral g in probability"],
  cxd={"finite_mean": "X_i ~ Cauchy: Xbar_n ~ Cauchy for every n -- no convergence to any constant (cauchy_no_mean)",
       "identically_distributed_ish": "for non-identical independent X_i, Xbar_n -> the average of the means in probability provided (1/n^2) sum Var(X_i) -> 0"},
  misuse=["claiming a.s. convergence (that is the SLLN, which also only needs a finite mean)",
          "a rate: the WLLN gives no explicit n; use Chebyshev/Hoeffding for that",
          "the gambler's fallacy: Xbar_n -> mu does NOT mean the SUM sum(X_i - mu) stays bounded (it grows like sqrt(n))"],
  related={"strengthened_by": ["strong_law_large_numbers"], "uses": ["chebyshev_inequality"], "tag": ["p"]},
  sources=["durrett_pte", "billingsley_probability_measure"], status="reviewed")

N("strong_law_large_numbers", "theorem", "convergence",
  "If X_1, X_2, ... are iid with E|X_1| < inf and mean mu, then Xbar_n -> mu ALMOST SURELY. If E|X_1| = inf, then limsup |Xbar_n| = inf a.s.",
  "X_i iid, E|X_1| < inf  =>  Xbar_n -->^{a.s.} mu",
  {"X_i": "an iid sequence, type: N -> L^1(P)", "mu": "the common mean, type: real"},
  "convergence mode: ALMOST SURELY -- strictly stronger than the WLLN. A finite mean is necessary AND sufficient. Etemadi's proof needs only pairwise independence and uses truncation + a fourth-moment-free Borel-Cantelli argument (choice-free).",
  proof=("Etemadi: reduce to X_i >= 0 by splitting into positive/negative parts; truncate Y_i = X_i 1_{X_i <= i}; show sum Var(Y_i)/i^2 < inf so Xbar along a geometric subsequence n_k ~ alpha^k converges a.s. (Chebyshev + Borel-Cantelli 1); fill gaps by monotonicity; let alpha -> 1", "borel_cantelli_first", "cited", "Durrett Thm 2.4.1 (Etemadi); Williams 12.10 (martingale proof)"),
  conv_mode="almost_sure",
  spec=["X_i ~ Bernoulli(p): the relative frequency -> p for almost every infinite sequence of trials (Borel's normal number theorem is the p = 1/2, base-2 case)",
        "the empirical CDF F_n(x) -> F(x) a.s. for each x (and uniformly -- Glivenko-Cantelli)",
        "renewal theory: N(t)/t -> 1/E[interarrival] a.s."],
  cxd={"finite_mean": "X_i ~ Cauchy or any law with E|X_1| = inf: limsup |Xbar_n| = inf a.s. -- the sample mean has no a.s. limit and in fact oscillates unboundedly",
       "identically_distributed": "Kolmogorov's SLLN for independent non-identical X_i needs sum Var(X_i)/i^2 < inf"},
  misuse=["assuming a rate of a.s. convergence (the law of the iterated logarithm gives the a.s. envelope +- sqrt(2 sigma^2 n log log n))",
          "believing the SLLN needs a finite variance (it does not -- only a finite mean)",
          "the gambler's fallacy again"],
  related={"strengthens": ["weak_law_large_numbers"], "uses": ["borel_cantelli_first"], "refined_by": ["law of the iterated logarithm"], "tag": ["a.s."]},
  sources=["durrett_pte", "williams_probability_martingales"], status="reviewed")

N("levy_continuity_theorem", "theorem", "convergence",
  "If phi_{X_n}(t) -> phi(t) for every t and phi is continuous at t = 0, then phi is the characteristic function of some random variable X and X_n -> X in distribution. Conversely X_n -> X in distribution implies phi_{X_n} -> phi_X pointwise.",
  "phi_{X_n}(t) -> phi(t) for all t, phi continuous at 0  <=>  X_n -->^{d} X  with phi_X = phi",
  {"phi_{X_n}": "characteristic functions, type: R -> C", "phi": "the pointwise limit, type: R -> C"},
  "the workhorse for proving convergence in distribution: reduce to a pointwise limit of characteristic functions (which factor over sums). The continuity of phi at 0 rules out mass escaping to infinity (tightness).",
  proof=("continuity of phi at 0 gives tightness of (X_n) (a CF-tail bound); every subsequential distributional limit has CF phi (by the converse direction + the pointwise convergence); phi determines the limit uniquely, so the whole sequence converges", "cf_properties", "cited", "Billingsley Thm 26.3; Durrett Thm 3.3.6"),
  conv_mode="in_distribution",
  spec=["CLT: phi_{S_n}(t) = phi_{X_1}(t/sqrt n)^n -> e^{-t^2/2}, continuous at 0, hence S_n -> N(0,1)",
        "Poisson limit: (1 + (lambda/n)(e^{it} - 1))^n -> exp(lambda(e^{it} - 1))"],
  cxd={"continuity_of_the_limit_phi_at_0": "X_n ~ N(0, n): phi_{X_n}(t) = e^{-n t^2/2} -> 1_{t = 0}, which is NOT continuous at 0 -- and indeed X_n has no distributional limit (mass escapes to +-inf). The continuity condition is exactly the tightness check.",
       "pointwise_convergence_for_all_t": "convergence of phi_{X_n}(t) on a bounded interval of t is not enough in general"},
  misuse=["skipping the continuity-at-0 check (it is where tightness lives)",
          "concluding convergence from CF agreement on a finite set of t"],
  related={"uses": ["characteristic_function", "cf_properties"], "used_by": ["central_limit_theorem", "poisson_limit_theorem"]},
  sources=["billingsley_probability_measure", "durrett_pte"], status="reviewed")

N("lindeberg_clt", "theorem", "convergence",
  "For each n let X_{n,1}, ..., X_{n,k_n} be independent, mean 0, with s_n^2 = sum_i Var(X_{n,i}). If the Lindeberg condition holds -- for every eps > 0, (1/s_n^2) sum_i E[X_{n,i}^2 1_{|X_{n,i}| > eps s_n}] -> 0 -- then (sum_i X_{n,i})/s_n -> N(0,1) in distribution.",
  "Lindeberg condition  =>  (sum_i X_{n,i}) / s_n  -->^{d}  N(0,1)",
  {"X_{n,i}": "a triangular array of row-independent, mean-0 variables, type: array of L^2(P)", "s_n^2": "the row variance sum, type: positive real"},
  "the definitive CLT for NON-identically-distributed independent summands: the Lindeberg condition says no single term contributes a non-negligible fraction of the total variance. It implies (and under a uniform-asymptotic-negligibility assumption, is equivalent to) asymptotic normality; Lyapunov's (2 + delta)-moment condition is a convenient sufficient case.",
  proof=("CF expansion of prod_i phi_{X_{n,i}}(t/s_n); the Lindeberg condition controls the third-order remainder uniformly, giving -> e^{-t^2/2}; then Levy", "levy_continuity_theorem", "cited", "Billingsley Thm 27.2; Durrett Thm 3.4.5"),
  conv_mode="in_distribution",
  spec=["X_{n,i} iid mean 0 variance sigma^2: Lindeberg reduces to E[X_1^2 1_{|X_1| > eps sqrt n}] -> 0, true by DCT -- recovers the classical CLT",
        "Lyapunov: if (1/s_n^{2+delta}) sum E|X_{n,i}|^{2+delta} -> 0 for some delta > 0, then Lindeberg holds",
        "regression residuals, weighted sums with bounded weights, m-dependent sequences"],
  cxd={"lindeberg_condition": "X_{n,1} ~ N(0, n), X_{n,2}, ..., X_{n,n} ~ iid N(0,1): s_n^2 = 2n - 1 but the first term carries ~half the variance; the normalized sum is NOT asymptotically normal (it stays a 50-50 mix). One dominant term breaks the CLT.",
       "independence_within_rows": "strong dependence needs a different CLT (martingale CLT, mixing conditions)"},
  misuse=["applying the classical CLT to non-identical summands without checking a Lindeberg/Lyapunov condition",
          "ignoring a single heavy-weighted observation"],
  related={"generalizes": ["central_limit_theorem"], "sufficient_condition": ["Lyapunov"], "uses": ["levy_continuity_theorem"]},
  sources=["billingsley_probability_measure", "durrett_pte"], status="reviewed")

N("delta_method", "theorem", "convergence",
  "If sqrt(n)(T_n - theta) -> N(0, sigma^2) in distribution and g is differentiable at theta with g'(theta) != 0, then sqrt(n)(g(T_n) - g(theta)) -> N(0, g'(theta)^2 sigma^2).",
  "sqrt(n)(T_n - theta) -->^{d} N(0, sigma^2) , g differentiable at theta  =>  sqrt(n)(g(T_n) - g(theta)) -->^{d} N(0, g'(theta)^2 sigma^2)",
  {"T_n": "an asymptotically normal estimator, type: N -> (Omega -> R)", "g": "a transformation differentiable at theta, type: R -> R", "theta": "the true parameter, type: real"},
  "a first-order Taylor expansion g(T_n) approx g(theta) + g'(theta)(T_n - theta), made rigorous by Slutsky: sqrt(n)(g(T_n) - g(theta)) = [g'(theta) + o_p(1)] sqrt(n)(T_n - theta).",
  proof=("Taylor with remainder: g(T_n) - g(theta) = g'(xi_n)(T_n - theta) with xi_n between; T_n -> theta in probability so g'(xi_n) -> g'(theta) in probability; Slutsky gives the product limit", "slutsky_theorem", "cited", "Durrett; van der Vaart Asymptotic Statistics Thm 3.1"),
  conv_mode="in_distribution",
  spec=["g(x) = x^2 at theta: asymptotic variance 4 theta^2 sigma^2 (degenerate at theta = 0 -- then a chi-squared limit at rate n, the SECOND-order delta method)",
        "g = log: stabilizes a variance that scales with the mean (log-transform for count / ratio data)",
        "the asymptotic variance of a sample correlation, an odds ratio, an R^2 -- all standard delta-method calculations"],
  cxd={"g_prime_theta_nonzero": "g(x) = x^2 at theta = 0: g'(0) = 0, the first-order limit is degenerate; n(g(T_n) - g(theta)) -> sigma^2 chi-squared_1 instead (a different rate AND a non-normal limit)",
       "differentiability_at_theta": "g with a kink at theta (e.g. |x - theta|): no single derivative, the limit is a folded normal"},
  misuse=["applying it where g'(theta) = 0 (wrong rate and wrong limit shape)",
          "using it far from the asymptotic regime (the linearization error dominates in small samples)"],
  related={"uses": ["slutsky_theorem", "central_limit_theorem"], "second_order": ["when g'(theta) = 0"]},
  sources=["durrett_pte", "grimmett_stirzaker"], status="reviewed")

# ---------------------------------------------------------------- conditional_expectation
N("conditional_expectation_elementary", "definition", "conditional_expectation",
  "For discrete Y, E[X | Y = y] = sum_x x P(X = x | Y = y) (or the density analogue integral x f_{X|Y}(x|y) dx), defined for y with P(Y = y) > 0 (resp. f_Y(y) > 0). The function y |-> E[X | Y = y] is g(y); then E[X | Y] := g(Y).",
  "E[X | Y = y] := sum_x x p_{X|Y}(x | y) ;  E[X | Y] := g(Y) where g(y) = E[X | Y = y]",
  {"X": "an integrable random variable, type: L^1(P)", "Y": "the conditioning variable, type: Omega -> R", "g": "the regression function y |-> E[X|Y=y], type: R -> R"},
  "the concrete, computational conditional expectation. E[X | Y] is a RANDOM VARIABLE (a function of Y); E[X | Y = y] is a NUMBER for each y. Matches the abstract E[X | sigma(Y)] where both are defined.",
  welldef="for each y with positive mass/density, x |-> p_{X|Y}(x|y) is a probability distribution, so its mean g(y) is a well-defined number when E|X| < inf; the exceptional y-set is P_Y-null.",
  spec=["X, Y independent: E[X | Y] = E[X] (constant)",
        "X = Y: E[X | Y] = Y", "bivariate normal: E[Y | X] = mu_Y + rho (sigma_Y/sigma_X)(X - mu_X) -- linear regression",
        "E[X | Y] is the best predictor of X from Y in mean square (conditional_expectation_l2_projection)"],
  cxd={"positive_mass_or_density_at_y": "conditioning on { Y = y } with P(Y = y) = 0 and no joint density is ambiguous (Borel-Kolmogorov) -- needs the abstract construction",
       "integrability_of_X": "E[X | Y = y] can fail to exist for each y if E|X| = inf"},
  misuse=["treating E[X | Y] as a number", "conditioning on a measure-zero value without a joint density",
          "assuming E[X | Y] is linear in Y (only for jointly normal or by construction)"],
  related={"generalizes_to": ["conditional_expectation_abstract"], "requires": ["conditional_distribution"]},
  sources=["durrett_pte", "grimmett_stirzaker"], status="reviewed")

N("conditional_expectation_abstract", "definition", "conditional_expectation",
  "For X in L^1(Omega, F, P) and a sub-sigma-algebra G subset F, E[X | G] is any random variable Z such that (i) Z is G-measurable and (ii) integral_A Z dP = integral_A X dP for every A in G. It is unique up to P-a.s. equality.",
  "E[X | G] is the a.s.-unique G-measurable Z with  integral_A Z dP = integral_A X dP  for all A in G",
  {"X": "an integrable random variable, type: L^1(P)", "G": "a sub-sigma-algebra (the conditioning information), type: sigma-algebra subset F", "Z": "the conditional expectation E[X | G], type: L^1(Omega, G, P)"},
  "the defining property is (i) measurability + (ii) matching integrals on G-sets; conditioning on a variable is E[X | sigma(Y)]. This handles conditioning on probability-zero events, which the elementary definition cannot.",
  proof=("existence and uniqueness are conditional_expectation_existence (Radon-Nikodym or L^2 projection); this node is the DEFINITION via the two properties", None, "cited", "Williams ch. 9; Durrett ch. 4"),
  spec=["G = { empty, Omega }: E[X | G] = E[X] (a constant)",
        "G = F: E[X | G] = X", "X G-measurable: E[X | G] = X; X independent of G: E[X | G] = E[X]",
        "pull-out: E[Y X | G] = Y E[X | G] when Y is G-measurable and bounded"],
  cxd={"integrability_of_X": "for X >= 0 not integrable one defines E[X | G] in [0, inf] by monotone approximation; for signed non-integrable X it need not exist",
       "measurability_condition_(i)": "dropping (i) makes Z = X trivially satisfy (ii) -- the content is that Z is COARSER (G-measurable), a genuine projection / averaging"},
  misuse=["computing integral_A Z = integral_A X only for A generating G, without checking it is a pi-system (then pi-lambda is needed)",
          "treating E[X | G] as defined pointwise (it is an a.s. equivalence class)"],
  related={"exists_by": ["conditional_expectation_existence"], "generalizes": ["conditional_expectation_elementary", "law_of_total_probability"], "is_a": ["projection (conditional_expectation_l2_projection)"]},
  sources=["williams_probability_martingales", "durrett_pte"], status="reviewed")

N("conditional_expectation_existence", "theorem", "conditional_expectation",
  "For every X in L^1(Omega, F, P) and every sub-sigma-algebra G subset F, E[X | G] exists and is P-a.s. unique.",
  "X in L^1, G subset F  =>  E[X | G] exists, a.s. unique",
  {"X": "an integrable random variable, type: L^1(P)", "G": "a sub-sigma-algebra, type: sigma-algebra subset F"},
  "two standard constructions: (a) Radon-Nikodym -- nu(A) = integral_A X dP is a (signed) measure on (Omega, G) with nu << P|_G, so nu has a G-measurable density, which is E[X|G]; (b) for X in L^2, orthogonal projection onto the closed subspace L^2(G), then extend to L^1 by density and monotonicity.",
  proof=("Radon-Nikodym on (Omega, G, P|_G) applied to the finite signed measure A |-> integral_A X dP; uniqueness because two versions Z_1, Z_2 have integral_A (Z_1 - Z_2) = 0 for all A in G, forcing Z_1 = Z_2 a.s. (take A = {Z_1 > Z_2})", "radon_nikodym", "cited", "Williams Thm 9.2; Durrett Thm 4.1.1"),
  spec=["X in L^2: E[X | G] is the L^2-orthogonal projection of X onto L^2(Omega, G, P) -- the geometric picture",
        "X = 1_B: E[1_B | G] is the 'conditional probability' P(B | G), a G-measurable [0,1]-valued random variable"],
  cxd={"integrability_of_X": "without X in L^1 (or X >= 0), the signed measure A |-> integral_A X dP may not be finite and Radon-Nikodym does not apply directly",
       "sigma_finiteness_is_automatic": "P|_G is a probability measure, so the sigma-finiteness hypothesis of Radon-Nikodym is free here"},
  misuse=["assuming a REGULAR conditional distribution always exists (it does on Polish spaces; the a.s.-unique random variable E[X|G] always exists, the measure-valued version needs more)",
          "expecting a canonical pointwise version"],
  related={"uses": ["radon_nikodym", "lp_space"], "defines": ["conditional_expectation_abstract"]},
  sources=["williams_probability_martingales", "durrett_pte"], status="reviewed")

N("tower_property", "theorem", "conditional_expectation",
  "If H subset G subset F then E[E[X | G] | H] = E[X | H]. In particular E[E[X | G]] = E[X] (the law of total expectation / iterated expectation).",
  "H subset G  =>  E[ E[X | G] | H ] = E[X | H] ;   E[E[X | G]] = E[X]",
  {"X": "an integrable random variable, type: L^1(P)", "H, G": "nested sub-sigma-algebras H subset G subset F, type: sigma-algebra"},
  "the smaller sigma-algebra wins: conditioning on more then less information equals conditioning on less. Proof: E[X | H] is H-measurable (hence G-measurable) and its integral matches X on H-sets; check that E[X|G] has the same integrals on H-sets (it does, since H subset G).",
  proof=("for A in H subset G: integral_A E[E[X|G]|H] = integral_A E[X|G] = integral_A X = integral_A E[X|H]; both outer terms are H-measurable with equal integrals on all H-sets, so equal a.s.", "conditional_expectation_existence", "core", "validation/proof-checks.lean -- linearity core; the tower is the defining-property chase"),
  spec=["H = { empty, Omega }: E[E[X | G]] = E[X] -- compute a mean by conditioning (first-step analysis, LOTUS for expectations)",
        "E[X] = sum_i E[X | B_i] P(B_i) for a partition -- the law-of-total-probability analogue",
        "martingale: E[X_{n+1} | F_n] = X_n gives E[X_m | F_n] = X_n for m > n by iterating"],
  cxd={"nesting_H_subset_G": "if H and G are not nested, E[E[X | G] | H] need NOT equal E[X | H]: with X, G, H chosen so G and H are independent and both informative about X, iterating loses information both ways and the two sides differ",
       "integrability": "needs X in L^1 for all the conditional expectations to exist"},
  misuse=["applying it to non-nested conditioning sigma-algebras",
          "writing E[E[X|G]|H] = E[X|G] (wrong -- the OUTER, smaller one wins)"],
  related={"generalizes": ["law_of_total_probability"], "used_by": ["law_of_total_variance", "martingale"]},
  sources=["williams_probability_martingales", "durrett_pte"], status="reviewed")

N("law_of_total_variance", "theorem", "conditional_expectation",
  "For X in L^2 and a sub-sigma-algebra G: Var(X) = E[Var(X | G)] + Var(E[X | G]), where Var(X | G) = E[(X - E[X|G])^2 | G].",
  "Var(X) = E[ Var(X | G) ] + Var( E[X | G] )",
  {"X": "a square-integrable random variable, type: L^2(P)", "G": "a sub-sigma-algebra, type: sigma-algebra subset F"},
  "'within-group + between-group variance'. Decomposes total variability into the average conditional (unexplained) variance plus the variance of the conditional means (explained). Proof: apply variance_computational and the tower property.",
  proof=("E[Var(X|G)] = E[E[X^2|G]] - E[(E[X|G])^2] = E[X^2] - E[(E[X|G])^2] (tower); Var(E[X|G]) = E[(E[X|G])^2] - (E X)^2; add -- the middle terms cancel", "tower_property", "core", "validation/proof-checks.lean Prob.centid + Prob.expectation_linearity (GENUINE)"),
  spec=["G = sigma(Y): Var(X) = E[Var(X | Y)] + Var(E[X | Y]) -- the ANOVA / random-effects decomposition; R^2 = Var(E[X|Y])/Var(X) is the fraction 'explained' by Y",
        "hierarchical models: total variance = measurement variance + between-unit variance",
        "compound distributions: Var(sum_{i=1}^N Y_i) = E[N] Var(Y) + Var(N) (E Y)^2 for N ⟂ iid Y_i"],
  cxd={"finite_second_moment": "X must be in L^2 for all three variances to be finite",
       "both_terms_nonnegative": "E[Var(X|G)] >= 0 and Var(E[X|G]) >= 0, so conditioning can only REDUCE expected variance: E[Var(X|G)] <= Var(X)"},
  misuse=["forgetting the Var(E[X|G]) term (assuming Var(X) = E[Var(X|G)])",
          "using it with X not in L^2"],
  related={"uses": ["tower_property", "variance_computational"], "decomposes": ["variance"], "analogue": ["law of total expectation"]},
  sources=["williams_probability_martingales", "grimmett_stirzaker"], status="reviewed")

N("conditional_expectation_l2_projection", "theorem", "conditional_expectation",
  "For X in L^2(P), E[X | G] is the orthogonal projection of X onto the closed subspace L^2(Omega, G, P): it is the G-measurable random variable minimizing E[(X - Z)^2] over all G-measurable Z in L^2.",
  "E[X | G] = argmin_{Z in L^2(G)} E[(X - Z)^2]   (orthogonal projection in L^2(P))",
  {"X": "a square-integrable random variable, type: L^2(P)", "G": "a sub-sigma-algebra, type: sigma-algebra subset F"},
  "the geometric meaning of conditioning: E[X | G] is the BEST PREDICTOR of X using only G-information, in mean-square. The residual X - E[X | G] is orthogonal to every G-measurable function (E[(X - E[X|G]) W] = 0 for W in L^2(G)).",
  proof=("L^2(G) is a closed subspace of the Hilbert space L^2(P); the projection theorem gives a unique closest point Z*, characterized by X - Z* orthogonal to L^2(G), i.e. E[(X - Z*) 1_A] = 0 for all A in G -- exactly the defining property of E[X | G]", "conditional_expectation_existence", "core", "validation/proof-checks.lean Prob.jensen_sq (the L^2 convexity core)"),
  spec=["G = sigma(Y): E[X | Y] = argmin_{g measurable} E[(X - g(Y))^2] -- nonparametric regression is estimating this",
        "restricting Z to AFFINE functions of Y gives the best LINEAR predictor mu_X + (Cov(X,Y)/Var Y)(Y - mu_Y) -- equals E[X|Y] iff (X,Y) jointly normal",
        "the Pythagorean identity: E[X^2] = E[(E[X|G])^2] + E[(X - E[X|G])^2]"],
  cxd={"finite_second_moment": "the projection picture needs X in L^2; for X in L^1 only, E[X | G] still exists (conditional_expectation_existence) but is not a projection and is not a mean-square minimizer",
       "G_measurable_predictors_only": "allowing Z to depend on more than G lets Z = X drive the error to 0 -- the constraint Z in L^2(G) is the whole point"},
  misuse=["assuming the best predictor is linear (only for jointly Gaussian)",
          "using the L^2 characterization when X is not square-integrable"],
  related={"uses": ["lp_space", "conditional_expectation_existence"], "special_case": ["linear regression / best linear predictor"], "gives": ["the Pythagorean / ANOVA identity"]},
  sources=["williams_probability_martingales", "durrett_pte"], status="reviewed")

# ---------------------------------------------------------------- boundary
N("martingale", "bridge", "boundary",
  "A sequence (X_n) adapted to a filtration (F_n) with E|X_n| < inf and E[X_{n+1} | F_n] = X_n for all n. (Supermartingale: <= ; submartingale: >= .) STATED here as the doorway to stochastic processes; not developed in this release.",
  "E[X_{n+1} | F_n] = X_n   (X_n adapted, integrable)",
  {"(X_n)": "an adapted integrable sequence, type: N -> L^1(P)", "(F_n)": "a filtration, type: increasing sequence of sub-sigma-algebras"},
  "the model of a fair game: the best forecast of tomorrow given everything known today is today's value. By the tower property E[X_n] = E[X_0] for all n. The convergence theorem, optional stopping, and the maximal / Doob inequalities are the content of a future release.",
  proof=("definition only; the theory (Doob's convergence theorem, optional stopping, L^p maximal inequalities, the martingale CLT) is CITED to Williams / Durrett ch. 5 and deferred to Release 0.2", "tower_property", "cited", "Williams Probability with Martingales chs. 10-14; Durrett ch. 5"),
  spec=["S_n = sum of iid mean-0 increments: a martingale w.r.t. its natural filtration",
        "M_n = E[Y | F_n] for a fixed integrable Y (a Doob martingale): converges a.s. and in L^1 to E[Y | F_inf]",
        "the likelihood ratio prod (q(X_i)/p(X_i)) under p: a nonnegative martingale"],
  cxd={"adaptedness_and_integrability": "if X_n is not F_n-measurable or not integrable the conditional expectation is ill-posed",
       "the_equality_(fair_game)": "E[X_{n+1} | F_n] > X_n (submartingale) models a favorable game -- convex functions of a martingale are submartingales (conditional Jensen)"},
  misuse=["assuming a martingale converges without an L^1-boundedness or uniform-integrability condition",
          "applying optional stopping without a boundedness / integrability side condition (the St Petersburg / doubling paradox)"],
  related={"uses": ["conditional_expectation_abstract", "tower_property"], "developed_in": ["Release 0.2 / a stochastic-processes capsule"]},
  sources=["williams_probability_martingales", "durrett_pte"], status="draft")

N("stochastic_process", "bridge", "boundary",
  "A stochastic process is a collection (X_t)_{t in T} of random variables on one probability space, indexed by a set T (time). Its law lives on the product space R^T via the finite-dimensional distributions. STATED as a boundary node.",
  "(X_t)_{t in T} :  a T-indexed family of random variables on (Omega, F, P)",
  {"(X_t)": "the process, type: T -> (Omega -> R)", "T": "the index set (e.g. N, [0, inf)), type: set"},
  "for fixed omega, t |-> X_t(omega) is a sample path; for fixed t, X_t is a random variable. The finite-dimensional distributions (laws of (X_{t_1}, ..., X_{t_k})) are the observable data; Kolmogorov's extension theorem builds the process from consistent f.d.d.s.",
  proof=("definition only; existence from consistent finite-dimensional distributions is kolmogorov_extension_theorem; path regularity (continuity, cadlag) requires the Kolmogorov-Chentsov criterion -- all deferred", "random_variable", "cited", "Billingsley SS36; Durrett ch. 6-8; Karatzas-Shreve ch. 1-2"),
  spec=["T = N: a discrete-time sequence (e.g. a Markov chain, a time series)",
        "T = [0, inf), continuous paths: Brownian motion, diffusions",
        "T = [0, inf), piecewise-constant paths: the Poisson process, continuous-time Markov chains"],
  cxd={"one_common_probability_space": "a process is more than its marginals -- the joint law across times (the dependence) is the object of interest",
       "path_regularity_is_extra": "the f.d.d.s do not determine path properties; { X_t continuous } may not even be measurable without choosing a good modification"},
  misuse=["confusing the process with its one-dimensional marginals",
          "assuming a version with continuous (or measurable) paths exists without a regularity criterion"],
  related={"constructed_by": ["kolmogorov_extension_theorem"], "special_cases": ["martingale, Markov chain, Poisson process, Brownian motion"], "developed_in": ["a future stochastic-processes capsule"]},
  sources=["billingsley_probability_measure", "durrett_pte"], status="draft")

N("kolmogorov_extension_theorem", "bridge", "boundary",
  "Given a family of finite-dimensional distributions mu_{t_1,...,t_k} on R^k that is CONSISTENT (marginalizing mu over a coordinate gives the lower-dimensional mu, and permuting coordinates permutes the measure), there is a probability space carrying a process (X_t) with exactly those finite-dimensional distributions. STATED and CITED.",
  "consistent finite-dimensional distributions  =>  exists a process (X_t) realizing them  (on R^T, product sigma-algebra)",
  {"mu_{t_1..t_k}": "the prescribed finite-dimensional laws, type: probability measures on R^k", "(X_t)": "the resulting process, type: T -> (Omega -> R)"},
  "the existence theorem underlying every stochastic-process construction (iid sequences, Markov chains from a transition kernel, Gaussian processes from a covariance function). Consistency is exactly the compatibility needed; the built measure lives on the product sigma-algebra of R^T.",
  proof=("Caratheodory extension: the consistent f.d.d.s define a premeasure on the algebra of cylinder sets of R^T; consistency makes it well-defined and countably additive on that algebra (using compactness of R and inner regularity), so it extends to the product sigma-algebra", "lebesgue_measure_caratheodory", "cited", "Billingsley Thm 36.1; Durrett Thm 6.1.1 (Kolmogorov); Tao"),
  spec=["iid sequences: mu_{t_1,...,t_k} = mu^{tensor k} is trivially consistent -- gives the infinite product measure",
        "Markov chains: mu built from an initial law and a transition kernel via Chapman-Kolmogorov consistency",
        "Gaussian processes: any symmetric positive-semidefinite covariance function K(s,t) yields a centered Gaussian process"],
  cxd={"consistency_of_the_f_d_d_s": "an inconsistent family (e.g. mu_{1,2} with a marginal on coordinate 1 disagreeing with mu_1) realizes no process -- consistency is necessary and sufficient",
       "the_product_sigma_algebra_only": "the resulting measure only sees cylinder events; { t |-> X_t continuous } is NOT in the product sigma-algebra -- path properties need a separate modification argument (Kolmogorov-Chentsov)"},
  misuse=["expecting path regularity (continuity, boundedness) from the extension -- it gives only the f.d.d.s",
          "applying it to an index set where the underlying space is not standard Borel (the theorem needs Polish coordinate spaces)"],
  related={"uses": ["lebesgue_measure_caratheodory (Caratheodory extension)"], "constructs": ["iid", "stochastic_process"], "companion": ["Kolmogorov-Chentsov continuity criterion"]},
  sources=["billingsley_probability_measure", "durrett_pte"], status="draft")

# --- headline nodes: md pages only (yaml is hand-written) ---
N("kolmogorov_axioms", "axiom", "probability_space",
  "P(A) >= 0 ; P(Omega) = 1 ; countable additivity on disjoint events. See results/kolmogorov_axioms.yaml.",
  "P >= 0 ; P(Omega) = 1 ; disjoint (A_n) => P(bigcup A_n) = sum P(A_n)",
  {"P": "a probability measure, type: F -> [0,1]"},
  "see the hand-written results/kolmogorov_axioms.yaml for the full treatment.",
  spec=["Omega finite: P is a pmf"], cxd={"countable_additivity": "finite-additive density on N is not a probability measure"},
  misuse=["assuming only finite additivity"], related={"full_entry": ["results/kolmogorov_axioms.yaml"]},
  sources=P, status="reviewed")
N("bayes_theorem", "theorem", "independence",
  "P(B_j | A) = P(A | B_j) P(B_j) / sum_i P(A | B_i) P(B_i). See results/bayes_theorem.yaml.",
  "P(B_j|A) = P(A|B_j) P(B_j) / sum_i P(A|B_i) P(B_i)",
  {"{B_i}": "a partition with positive priors, type: family in F"},
  "see the hand-written results/bayes_theorem.yaml for the full treatment.",
  proof=("definition of P(B_j|A) with the law of total probability in the denominator", "law_of_total_probability", "core", "validation/proof-checks.lean Prob.bayes_denominator"),
  spec=["two hypotheses: odds form, posterior odds = likelihood ratio x prior odds"],
  cxd={"partition_of_Omega": "a non-exhaustive partition loses probability mass"},
  misuse=["confusing P(A|B) with P(B|A)"], related={"full_entry": ["results/bayes_theorem.yaml"]},
  sources=P, status="reviewed")
N("markov_inequality", "theorem", "inequalities",
  "X >= 0, a > 0 => P(X >= a) <= E[X]/a. See results/markov_inequality.yaml.",
  "X >= 0, a > 0 => P(X >= a) <= E[X] / a",
  {"X": "a nonnegative random variable, type: Omega -> [0, inf)"},
  "see the hand-written results/markov_inequality.yaml for the full treatment.",
  proof=("a 1_{X>=a} <= X pointwise, take expectations", "expectation_monotonicity", "core", "validation/proof-checks.lean Prob.markov_finite"),
  spec=["X = (Y - EY)^2, a = k^2: Chebyshev", "X = e^{tY}: Chernoff"],
  cxd={"X_nonnegative": "a mean-0 symmetric two-point X has P(X >= a) = 1/2 while E[X]/a = 0"},
  misuse=["applying to a signed variable"], related={"full_entry": ["results/markov_inequality.yaml"]},
  sources=P, status="reviewed")
N("chebyshev_inequality", "theorem", "inequalities",
  "Var(X) < inf, k > 0 => P(|X - E[X]| >= k) <= Var(X)/k^2. See results/chebyshev_inequality.yaml.",
  "P(|X - E[X]| >= k) <= Var(X) / k^2",
  {"X": "a random variable with finite variance, type: L^2(P)"},
  "see the hand-written results/chebyshev_inequality.yaml for the full treatment.",
  proof=("Markov applied to (X - EX)^2 with threshold k^2", "markov_inequality", "core", "validation/proof-checks.lean Prob.chebyshev_reduction"),
  spec=["k = c sd(X): P(|X - EX| >= c sd) <= 1/c^2", "sample mean: gives the WLLN"],
  cxd={"finite_variance": "Cauchy has 1/k tails, not 1/k^2 -- no variance bound"},
  misuse=["using it when Chernoff/Hoeffding apply"], related={"full_entry": ["results/chebyshev_inequality.yaml"]},
  sources=P, status="reviewed")
N("expectation_linearity", "theorem", "expectation",
  "E[aX + bY] = a E[X] + b E[Y] for integrable X, Y. No independence needed. See results/expectation_linearity.yaml.",
  "E[aX + bY] = a E[X] + b E[Y]",
  {"X, Y": "integrable random variables, type: L^1(P)"},
  "see the hand-written results/expectation_linearity.yaml for the full treatment.",
  proof=("linearity of the Lebesgue integral", "abstract_integral", "core", "validation/proof-checks.lean Prob.expectation_additivity"),
  spec=["indicators: E[sum 1_{A_i}] = sum P(A_i) -- mean of a count", "binomial mean np with no combinatorial sum"],
  cxd={"integrability": "X ~ Cauchy, Y = -X: X + Y = 0 has mean 0 but E[X], E[Y] undefined"},
  misuse=["believing independence is required"], related={"full_entry": ["results/expectation_linearity.yaml"]},
  sources=P, status="reviewed")
N("central_limit_theorem", "theorem", "convergence",
  "X_i iid, mean mu, variance sigma^2 in (0, inf) => sqrt(n)(Xbar_n - mu)/sigma -> N(0,1) in distribution. See results/central_limit_theorem.yaml.",
  "sqrt(n)(Xbar_n - mu)/sigma  -->^{d}  N(0,1)",
  {"X_i": "an iid sequence with finite nonzero variance, type: N -> L^2(P)"},
  "see the hand-written results/central_limit_theorem.yaml for the full treatment. Convergence mode: IN DISTRIBUTION (not a.s. or in probability).",
  proof=("CF of the standardized sum -> e^{-t^2/2}, then Levy's continuity theorem", "levy_continuity_theorem", "cited", "Billingsley Thm 27.1"),
  conv_mode="in_distribution",
  spec=["Bernoulli(p): de Moivre-Laplace", "normal X_i: exact for every n"],
  cxd={"finite_nonzero_variance": "Cauchy: Xbar_n stays Cauchy -- no normal limit"},
  misuse=["claiming a rate (that is Berry-Esseen)", "treating finite n as exactly normal in the tails"],
  related={"full_entry": ["results/central_limit_theorem.yaml"], "uses": ["levy_continuity_theorem"]},
  sources=P, status="reviewed")

# <<SPECS>>

if __name__ == "__main__":
    emit()
