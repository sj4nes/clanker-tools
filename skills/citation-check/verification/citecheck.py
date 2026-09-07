#!/usr/bin/env python3
"""Minimal implementation of the citation-check workflow, for verifying the skill.

Exercises the prescribed pipeline against the real authoritative APIs:
  parse/normalize -> route by identifier/type -> retrieve -> compare fields
  -> weighted score (never overriding a hard contradiction) -> calibrated status
  -> evidence packet.

Not a production tool: the similarity model is deliberately simple. The point is
to confirm the ladders, the API access patterns, and the decision thresholds in
SKILL.md behave as documented.
"""
from __future__ import annotations
import json, re, sys, time, urllib.parse, urllib.request, unicodedata

UA = "citation-check-verify/0.1 (https://github.com/; mailto:simonjanes@fastmail.com)"
TIMEOUT = 20


def _get(url, parse="json", accept=None):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    if accept:
        req.add_header("Accept", accept)
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
                raw = r.read()
                final = r.geturl()
            if parse == "json":
                return json.loads(raw), final, 200
            return raw.decode("utf-8", "replace"), final, 200
        except urllib.error.HTTPError as e:
            if e.code in (404, 400):
                return None, url, e.code
            time.sleep(2 + attempt * 2)
        except Exception:
            time.sleep(2 + attempt * 2)
    return None, url, None


def _resolve_head(url):
    """Follow a DOI resolver redirect; return the landing URL (or None)."""
    req = urllib.request.Request(url, headers={"User-Agent": UA}, method="HEAD")
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
            return r.geturl(), r.status
    except urllib.error.HTTPError as e:
        return None, e.code
    except Exception:
        return None, None


# ---------------------------------------------------------------- normalization
def norm_text(s):
    if not s:
        return ""
    s = unicodedata.normalize("NFKD", s)
    s = "".join(c for c in s if not unicodedata.combining(c))
    s = s.lower()
    s = s.replace("&", " and ")
    s = re.sub(r"[‐-―\-]", " ", s)
    s = re.sub(r"[^a-z0-9 ]", " ", s)
    return re.sub(r"\s+", " ", s).strip()


def isbn13_valid(digits):
    if len(digits) != 13 or not digits.isdigit():
        return False
    s = sum((1 if i % 2 == 0 else 3) * int(d) for i, d in enumerate(digits))
    return s % 10 == 0


def isbn10_to_13(d):
    core = "978" + d[:9]
    s = sum((1 if i % 2 == 0 else 3) * int(c) for i, c in enumerate(core))
    return core + str((10 - s % 10) % 10)


def normalize_isbn(raw):
    d = re.sub(r"[^0-9Xx]", "", raw)
    out = {"original": raw, "isbn13": None, "isbn10": None, "checksum_valid": False}
    if len(d) == 13:
        out["isbn13"] = d
        out["checksum_valid"] = isbn13_valid(d)
    elif len(d) == 10:
        out["isbn10"] = d
        w = sum((10 - i) * (10 if c in "Xx" else int(c)) for i, c in enumerate(d))
        out["checksum_valid"] = w % 11 == 0
        if out["checksum_valid"]:
            out["isbn13"] = isbn10_to_13(d)
    return out


DOI_RE = re.compile(r"10\.\d{4,9}/[^\s\"'<>&]+", re.I)
ARXIV_RE = re.compile(r"arXiv:\s*(\d{4}\.\d{4,5}(v\d+)?)", re.I)
ISBN_RE = re.compile(r"ISBN[:\s]*([0-9Xx\-– ]{10,20})", re.I)
YEAR_RE = re.compile(r"\b(1[5-9]\d{2}|20\d{2})\b")


def parse_citation(raw):
    rec = {"raw": raw, "title": None, "authors": [], "year": None,
           "container": None, "identifiers": {"doi": [], "isbn": [], "arxiv": []},
           "suspicious_flags": [], "type_guess": None}
    m = DOI_RE.search(raw.replace("https://doi.org/", " ").replace("doi:", " "))
    if m:
        rec["identifiers"]["doi"].append(m.group(0).rstrip(".,);"))
    m = ARXIV_RE.search(raw)
    if m:
        rec["identifiers"]["arxiv"].append(m.group(1))
    m = ISBN_RE.search(raw)
    if m:
        info = normalize_isbn(m.group(1))
        rec["identifiers"]["isbn"].append(info)
        if not info["checksum_valid"]:
            rec["suspicious_flags"].append(
                "ISBN check digit invalid -- not used for identifier lookup; "
                "fell back to the bibliographic ladder")
    yrs = YEAR_RE.findall(raw)
    if yrs:
        rec["year"] = int(yrs[0])
    # crude title: longest sentence-ish chunk between the year and a following period
    m = re.search(r"\((\d{4})\)\.?\s*([^.]+?)\.", raw)
    if m:
        rec["title"] = m.group(2).strip()
    else:
        m = re.search(r"\d{4}[a-z]?\.\s*([^.]+?)\.", raw)
        if m:
            rec["title"] = m.group(1).strip()
    if rec["title"]:
        # edition/volume belong in their own fields, not the title, or the
        # catalog's exact-ish title search misses.
        rec["edition"] = None
        em = re.search(r",?\s*(\d+)(?:st|nd|rd|th)\s+ed(?:ition)?\.?\s*$", rec["title"], re.I)
        if em:
            rec["edition"] = em.group(1)
            rec["title"] = rec["title"][:em.start()].rstrip(" ,")
    # first author family name = leading token before a comma
    m = re.match(r"\s*([A-Z][A-Za-zÀ-ſ'’-]+)\s*,", raw)
    if m:
        rec["authors"].append({"family": m.group(1)})
    # container: text after title up to a comma/number, if it looks like a journal
    # type inference must NOT hinge on an ISBN being present: books are cited
    # without one all the time. Edition statements, a "Press"/publisher token,
    # and the absence of a journal volume/issue are the signals.
    book_signal = bool(re.search(r"\b\d(st|nd|rd|th)\s+ed(ition)?\b|\bed\.\)?\s*$|"
                                 r"\b(press|publish\w*|verlag|routledge|springer|"
                                 r"wiley|elsevier|penguin|norton)\b", raw, re.I))
    journal_signal = bool(re.search(r"\b\d+\s*\(\d+\)|\bvol\.?\s*\d|\bpp?\.\s*\d+\s*[-–]\s*\d+|"
                                    r"\bjournal\b|\bproceedings\b", raw, re.I))
    if rec["identifiers"]["arxiv"]:
        rec["type_guess"] = "preprint"
    elif rec["identifiers"]["isbn"] or (book_signal and not journal_signal):
        rec["type_guess"] = "book"
    else:
        rec["type_guess"] = "article"
    low = norm_text(raw)
    if len(low.split()) < 4 and not any(rec["identifiers"].values()):
        rec["suspicious_flags"].append("insufficient information to identify a work")
    return rec


# ------------------------------------------------------------------- retrieval
def crossref_by_doi(doi):
    d, _, code = _get("https://api.crossref.org/works/" + urllib.parse.quote(doi))
    if not d:
        return None
    m = d["message"]
    return {"source": "crossref", "id": doi,
            "title": (m.get("title") or [None])[0],
            "authors": [a.get("family", "") for a in m.get("author", [])],
            "year": (m.get("issued", {}).get("date-parts") or [[None]])[0][0],
            "container": (m.get("container-title") or [None])[0],
            "type": m.get("type")}


def crossref_agency(doi):
    d, _, _ = _get("https://api.crossref.org/works/%s/agency" % urllib.parse.quote(doi))
    if d:
        return d["message"].get("agency", {}).get("id")
    return None


def datacite_by_doi(doi):
    d, _, _ = _get("https://api.datacite.org/dois/" + urllib.parse.quote(doi))
    if not d or "data" not in d:
        return None
    a = d["data"]["attributes"]
    return {"source": "datacite", "id": doi,
            "title": (a.get("titles") or [{}])[0].get("title"),
            "authors": [c.get("familyName") or c.get("name", "") for c in a.get("creators", [])],
            "year": a.get("publicationYear"),
            "container": (a.get("publisher") if isinstance(a.get("publisher"), str)
                          else (a.get("publisher") or {}).get("name")),
            "type": (a.get("types") or {}).get("resourceTypeGeneral")}


def openalex_by_doi(doi):
    d, _, _ = _get("https://api.openalex.org/works/doi:%s?mailto=simonjanes@fastmail.com"
                   % urllib.parse.quote(doi))
    if not d or "display_name" not in d:
        return None
    return {"source": "openalex", "id": d.get("id"),
            "title": d.get("display_name"),
            "authors": [ (a["author"]["display_name"].split()[-1])
                         for a in d.get("authorships", []) ],
            "year": d.get("publication_year"),
            "container": (d.get("primary_location") or {}).get("source", {}) and
                         ((d.get("primary_location") or {}).get("source") or {}).get("display_name"),
            "type": d.get("type")}


def arxiv_by_id(aid):
    raw, _, _ = _get("https://export.arxiv.org/api/query?id_list=" + aid, parse="text")
    if not raw:
        return None
    import xml.etree.ElementTree as ET
    ns = {"a": "http://www.w3.org/2005/Atom"}
    try:
        e = ET.fromstring(raw).find("a:entry", ns)
        if e is None or e.find("a:title", ns) is None:
            return None
        return {"source": "arxiv", "id": aid,
                "title": e.find("a:title", ns).text.strip(),
                "authors": [n.find("a:name", ns).text.split()[-1]
                            for n in e.findall("a:author", ns)],
                "year": int(e.find("a:published", ns).text[:4]),
                "container": "arXiv", "type": "preprint"}
    except ET.ParseError:
        return None


def openlibrary_by_isbn(isbn13):
    d, _, _ = _get("https://openlibrary.org/api/books?bibkeys=ISBN:%s&format=json&jscmd=data" % isbn13)
    if not d:
        return None
    v = next(iter(d.values()), None)
    if not v:
        return None
    return {"source": "openlibrary", "id": v.get("key"),
            "title": v.get("title"),
            "authors": [a["name"].split()[-1] for a in v.get("authors", [])],
            "year": int(re.search(r"\d{4}", v.get("publish_date", "")).group())
                    if re.search(r"\d{4}", v.get("publish_date", "")) else None,
            "container": (v.get("publishers") or [{}])[0].get("name"),
            "type": "book"}


def googlebooks_by_isbn(isbn13):
    d, _, _ = _get("https://www.googleapis.com/books/v1/volumes?q=isbn:" + isbn13)
    if not d or not d.get("items"):
        return None
    vi = d["items"][0]["volumeInfo"]
    return {"source": "googlebooks", "id": d["items"][0]["id"],
            "title": vi.get("title") + ((": " + vi["subtitle"]) if vi.get("subtitle") else ""),
            "authors": [a.split()[-1] for a in vi.get("authors", [])],
            "year": int(re.search(r"\d{4}", vi.get("publishedDate", "")).group())
                    if re.search(r"\d{4}", vi.get("publishedDate", "")) else None,
            "container": vi.get("publisher"), "type": "book"}


def crossref_bibsearch(rec):
    q = urllib.parse.quote((rec.get("title") or "") + " " +
                           " ".join(a["family"] for a in rec.get("authors", [])))
    d, _, _ = _get("https://api.crossref.org/works?query.bibliographic=%s&rows=5&mailto=simonjanes@fastmail.com" % q)
    out = []
    if d:
        for m in d["message"]["items"]:
            out.append({"source": "crossref-search", "id": m.get("DOI"),
                        "title": (m.get("title") or [None])[0],
                        "authors": [a.get("family", "") for a in m.get("author", [])],
                        "year": (m.get("issued", {}).get("date-parts") or [[None]])[0][0],
                        "container": (m.get("container-title") or [None])[0],
                        "type": m.get("type")})
    return out


def openlibrary_search(rec):
    q = urllib.parse.quote((rec.get("title") or ""))
    au = rec["authors"][0]["family"] if rec.get("authors") else ""
    d, _, _ = _get("https://openlibrary.org/search.json?title=%s&author=%s&limit=5" % (q, urllib.parse.quote(au)))
    out = []
    if d:
        for m in d.get("docs", []):
            out.append({"source": "openlibrary-search", "id": m.get("key"),
                        "title": m.get("title"),
                        "authors": [a.split()[-1] for a in m.get("author_name", [])],
                        "year": m.get("first_publish_year"),
                        "container": (m.get("publisher") or [None])[0], "type": "book"})
    return out


# --------------------------------------------------------------------- scoring
def sim(a, b):
    a, b = norm_text(a), norm_text(b)
    if not a or not b:
        return 0.0
    if a == b:
        return 1.0
    ta, tb = set(a.split()), set(b.split())
    j = len(ta & tb) / len(ta | tb)
    # substring bonus only when the shorter title is most of the longer one --
    # "nothing in particular" inside "a framework for nothing in particular" is
    # NOT a title match.
    if (a in b or b in a) and min(len(a), len(b)) / max(len(a), len(b)) >= 0.6:
        j = max(j, 0.9)
    return j


def author_sim(cited, rec_authors):
    if not cited:
        return 0.5
    fam = norm_text(cited[0]["family"])
    return 1.0 if any(fam == norm_text(x) or fam in norm_text(x) for x in rec_authors) else 0.0


def score(rec, cand, identifier_exact):
    I = 1.0 if identifier_exact else 0.0
    T = sim(rec.get("title") or "", cand.get("title") or "")
    A = author_sim(rec.get("authors"), cand.get("authors") or [])
    Y = 1.0 if rec.get("year") and cand.get("year") and rec["year"] == cand["year"] else (
        0.6 if rec.get("year") and cand.get("year") and abs(rec["year"] - cand["year"]) == 1 else 0.0)
    C = sim(rec.get("container") or "", cand.get("container") or "") if rec.get("container") else 0.5
    D = 0.5
    return round(0.40 * I + 0.25 * T + 0.15 * A + 0.08 * Y + 0.07 * C + 0.05 * D, 3)


def field_diffs(rec, cand):
    d = []
    if rec.get("year") and cand.get("year") and rec["year"] != cand["year"]:
        d.append({"field": "year", "cited": rec["year"], "authoritative": cand["year"]})
    if rec.get("container") and cand.get("container") and sim(rec["container"], cand["container"]) < 0.5:
        d.append({"field": "container", "cited": rec["container"], "authoritative": cand["container"]})
    return d


def hard_conflicts(rec, cand, identifier_exact):
    c = []
    if identifier_exact and rec.get("title") and cand.get("title"):
        if sim(rec["title"], cand["title"]) < 0.35:
            c.append("supplied identifier resolves to a different title: cited %r vs record %r"
                     % (rec["title"], cand["title"]))
    if rec.get("type_guess") == "article" and cand.get("type") in (
            "book-review", "editorial", "correction", "peer-review"):
        c.append("cited as article; record type is %r" % cand["type"])
    return c


# ------------------------------------------------------------------- assessment
def assess(raw):
    rec = parse_citation(raw)
    ev, queries = [], []
    ids = rec["identifiers"]

    if "insufficient information to identify a work" in rec["suspicious_flags"]:
        return rec, {"status": "not_applicable", "confidence": 0.0,
                     "reason": "insufficient information to identify a candidate work"}, ev, queries

    cands = []
    identifier_exact = False

    if ids["doi"]:
        doi = ids["doi"][0]
        land, hcode = _resolve_head("https://doi.org/" + doi)
        queries.append({"step": "resolve", "url": "https://doi.org/" + doi,
                        "landing": land, "http": hcode})
        agency = crossref_agency(doi)
        queries.append({"step": "doi-agency", "agency": agency})
        cr = crossref_by_doi(doi)
        if cr:
            ev.append(cr); cands.append(cr); identifier_exact = True
        else:
            dc = datacite_by_doi(doi)
            if dc:
                ev.append(dc); cands.append(dc); identifier_exact = True
        oa = openalex_by_doi(doi)
        if oa:
            ev.append(oa); cands.append(oa)
        if not cr and not (ids["doi"] and datacite_by_doi(doi)):
            queries.append({"step": "doi-unregistered",
                            "note": "identifier as cited did not resolve in Crossref or DataCite"})

    if ids["arxiv"]:
        ax = arxiv_by_id(ids["arxiv"][0])
        if ax:
            ev.append(ax); cands.append(ax); identifier_exact = True

    if ids["isbn"]:
        info = ids["isbn"][0]
        if info["checksum_valid"] and info["isbn13"]:
            for fn in (openlibrary_by_isbn, googlebooks_by_isbn):
                r = fn(info["isbn13"])
                if r:
                    ev.append(r); cands.append(r); identifier_exact = True
        else:
            queries.append({"step": "isbn-malformed",
                            "note": "ISBN check digit invalid -- NOT used for a lookup "
                                    "(a coincidental hit would not be this book); "
                                    "this is not proof of nonexistence"})

    if not cands:  # identifier-free or identifiers failed -> bibliographic ladder
        if rec["type_guess"] == "book":
            ev_search = openlibrary_search(rec)
        else:
            ev_search = crossref_bibsearch(rec)
        queries.append({"step": "bibliographic-search", "hits": len(ev_search)})
        cands.extend(ev_search)
        # a second independent pipeline
        other = crossref_bibsearch(rec) if rec["type_guess"] == "book" else openlibrary_search(rec)
        queries.append({"step": "second-pipeline", "hits": len(other)})
        ev.extend(other)
        cands.extend(other)

    if not cands:
        return rec, {"status": "unresolved", "confidence": 0.0,
                     "reason": "no adequate record found after the applicable source ladder"}, ev, queries

    scored = sorted(((score(rec, c, identifier_exact and c["source"] in
                            ("crossref", "datacite", "arxiv", "openlibrary", "googlebooks")), c)
                     for c in cands), key=lambda x: -x[0])
    best_score, best = scored[0]

    hc = hard_conflicts(rec, best, identifier_exact)
    if hc:
        return rec, {"status": "contradicted", "confidence": 0.97, "conflicts": hc}, ev, queries

    pipelines = {c["source"].split("-")[0] for _, c in scored if score(rec, c, False) >= 0.5 or c is best}
    corr = len(pipelines - {best["source"].split("-")[0]}) if not identifier_exact else \
        len([c for c in cands if c is not best and sim(c.get("title") or "", best.get("title") or "") > 0.6])
    diffs = field_diffs(rec, best)

    if identifier_exact and best_score >= 0.4 and not diffs:
        st = {"status": "verified", "confidence": 0.99}
    elif identifier_exact and best_score >= 0.4 and diffs:
        st = {"status": "verified_metadata_correction_needed", "confidence": 0.95, "corrections": diffs}
    elif best_score >= 0.80 and corr >= 1 and diffs:
        st = {"status": "verified_metadata_correction_needed", "confidence": 0.9, "corrections": diffs}
    elif best_score >= 0.80 and corr >= 1:
        st = {"status": "verified", "confidence": 0.9}
    elif best_score >= 0.55 and (len(scored) == 1 or scored[0][0] - scored[1][0] > 0.15):
        st = {"status": "likely_match", "confidence": 0.7,
              "warnings": ["no unique authoritative identifier match"]}
    else:
        # `ambiguous` means SEVERAL PLAUSIBLE records -- at least two candidates
        # that each clear a plausibility floor. Weak search noise with nothing
        # near the citation is `unresolved`, not `ambiguous`.
        plausible = [c for s, c in scored
                     if s >= 0.55 or sim(rec.get("title") or "", c.get("title") or "") >= 0.7]
        # several records that are all the SAME work at different manifestation
        # levels (editions, translations, reprints) is `likely_match` at work
        # level -- not `ambiguous`, which is for genuinely different candidates.
        same_work = (len(plausible) >= 2 and
                     all(sim(plausible[0].get("title") or "", c.get("title") or "") >= 0.7
                         for c in plausible[1:]) and
                     sim(rec.get("title") or "", plausible[0].get("title") or "") >= 0.7)
        if same_work:
            st = {"status": "likely_match", "confidence": 0.7,
                  "warnings": ["work found; the cited edition/manifestation is "
                               "not confirmed without an identifier"],
                  "frbr_level": "work"}
        elif len(plausible) >= 2:
            st = {"status": "ambiguous", "confidence": 0.4,
                  "candidates": [{"title": c.get("title"), "id": c.get("id")}
                                 for c in plausible[:3]]}
        else:
            st = {"status": "unresolved", "confidence": 0.0,
                  "reason": "source ladder returned only weak, non-matching records "
                            "(not evidence of nonexistence -- coverage may be incomplete)"}
    st["match_score"] = best_score
    st["matched_record"] = {"source": best["source"], "id": best.get("id"),
                            "title": best.get("title"), "year": best.get("year")}
    return rec, st, ev, queries


TESTS = [
    ("T1  verified / paper+DOI",
     "Dijkstra, E. W. (1959). A note on two problems in connexion with graphs. "
     "Numerische Mathematik, 1, 269-271. https://doi.org/10.1007/BF01386390"),
    ("T2  wrong year / paper+DOI",
     "Dijkstra, E. W. (1968). A note on two problems in connexion with graphs. "
     "Numerische Mathematik, 1, 269-271. https://doi.org/10.1007/BF01386390"),
    ("T3  DOI -> different work",
     "Smith, J. (2015). Deep learning for feline facial recognition. Nature. "
     "https://doi.org/10.1007/BF01386390"),
    ("T4  hallucinated, no identifier",
     "Marlowe, T. R. (2013). Quantum coherence in avian magnetoreception revisited. "
     "Journal of Theoretical Ornithology, 45(2), 88-104."),
    ("T5  not enough information",
     "See the classic paper on quicksort."),
    ("T6  verified / book+ISBN",
     "Abelson, H., & Sussman, G. J. (1996). Structure and Interpretation of Computer "
     "Programs, 2nd ed. MIT Press. ISBN 0262011530."),
    ("T7  well-formed but unregistered DOI",
     "Nguyen, P. (2020). A framework for nothing in particular. Journal of Placeholders, "
     "8(1), 1-10. https://doi.org/10.9999/jplh.2020.999999"),
    ("T8  invalid ISBN check digit",
     "Roe, B. (2019). Example Book: A Study, 2nd ed. Northstar Press. "
     "ISBN 978-1-234-56789-9."),
    ("T9  verified / arXiv preprint",
     "Vaswani, A., et al. (2017). Attention is all you need. arXiv:1706.03762."),
    ("T10 identifier-free real book",
     "Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2009). "
     "Introduction to Algorithms, 3rd ed. MIT Press."),
]


def main():
    rows = []
    for label, raw in TESTS:
        print("=" * 78)
        print(label)
        print("  " + raw)
        rec, st, ev, queries = assess(raw)
        print("  parsed  : title=%r year=%s ids=%s flags=%s"
              % (rec.get("title"), rec.get("year"),
                 {k: v for k, v in rec["identifiers"].items() if v}, rec["suspicious_flags"]))
        for q in queries:
            print("  query   :", json.dumps(q, default=str))
        for e in ev:
            print("  record  : [%s] %r (%s) authors=%s type=%s"
                  % (e["source"], e.get("title"), e.get("year"),
                     e.get("authors"), e.get("type")))
        print("  STATUS  :", json.dumps({k: v for k, v in st.items()
                                         if k != "matched_record"}, default=str))
        rows.append((label, st["status"], st.get("match_score", "")))
        time.sleep(1)
    print("=" * 78)
    print("SUMMARY")
    for label, status, sc in rows:
        print("  %-34s -> %-34s %s" % (label, status, sc))


if __name__ == "__main__":
    main()
