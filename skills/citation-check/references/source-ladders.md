# Source ladders and authoritative APIs

Use the source type closest to the publication ecosystem. One general database is
never enough. The first four checks below validate the **reference**; reading the
work validates the **use** of the reference — keep them separate.

## What "existence" can mean

| Level | What it establishes | Example |
|---|---|---|
| Identifier resolution | A supplied DOI / ISBN / PMID / arXiv / OCLC resolves in its authoritative registry | DOI returns a Crossref/DataCite record |
| Bibliographic existence | A catalog/index record supports the work existing | WorldCat or a national-library record lists the book |
| Metadata agreement | Cited title, creators, year, venue, edition, identifiers agree with an authoritative record | Citation says 2nd ed.; catalog confirms 2nd ed. |
| Access / copy exists | A library, repository, publisher, or archive holds or exposes a version | WorldCat holdings, institutional repository |
| Claim support | The work actually supports the nearby factual claim | Requires reading the work or reliable full text/abstract |

## Ladders by citation type

| Citation type | Strong primary checks | Useful corroboration | Key caution |
|---|---|---|---|
| Journal / conference paper | DOI resolver, Crossref, publisher landing page | OpenAlex, PubMed, Europe PMC, Semantic Scholar | DOI metadata can be deposited with errors |
| Dataset / software / thesis / preprint | DOI resolver, DataCite, repository landing page | OpenAlex, institutional repository, arXiv / Zenodo / Figshare | Versions matter; a preprint is not the final article |
| Book / book chapter | National library catalog, publisher page, WorldCat | Library of Congress, Open Library, Google Books | ISBN identifies a manifestation/edition, not the abstract work |
| Government / technical report | Issuing agency repository, report number, national depository | WorldCat, institutional libraries | Agency URLs and series change |
| Standard | Issuer's catalog and standard number | National standards-body / library catalogs | Confirm the exact revision, amendment, and date |
| Legal material | Official court / legislature / code / gazette source | Trusted legal database | Reporters and statute versions must be exact |
| Web source | Original publisher/org page, archived snapshot | Internet Archive, preservation services | "Found online" ≠ established publication date or authorship |

## The APIs

### Crossref — scholarly DOI metadata
- Retrieve a known DOI: `GET https://api.crossref.org/works/{doi}`
- Search registered records by title/author/container as a fallback.
- DOI-agency endpoint (`/works/{doi}/agency`) routes a DOI to its registration
  agency (Crossref vs DataCite vs other).
- Put a contact email in the query (`?mailto=...`) or User-Agent for the polite
  pool. Docs: https://www.crossref.org/documentation/retrieve-metadata/rest-api/
- Caution: Crossref metadata can be incomplete or contain deposit errors — the
  publisher landing page is the tiebreaker for a specific field.

### DataCite — DOIs for datasets, software, theses, preprints
- `GET https://api.datacite.org/dois/{doi}` for metadata.
- Use when Crossref has no record for a resolving DOI.
- Track the version: a DataCite DOI may point to a concept or a specific version.

### OpenAlex — wide scholarly graph (corroboration, not sole authority)
- Covers papers, books, chapters, datasets, dissertations, preprints.
- `GET https://api.openalex.org/works/doi:{doi}` or `?filter=...` searches.
- Use as a second independent pipeline, never as the only source.

### PubMed / Europe PMC — biomedical
- PubMed E-utilities: `esearch` then `efetch`/`esummary` by PMID.
- Europe PMC REST API gives an independent record and often links to full text.

### arXiv
- `GET https://export.arxiv.org/api/query?id_list={arxivid}` (Atom response).
  Use **HTTPS**; the endpoint intermittently returns an empty body — **retry
  with backoff** (2–3 attempts) before concluding anything.
- An arXiv version (`v1`, `v2`, …) is not automatically the journal version of
  record; check for a linked DOI.

### WorldCat — cataloged library resources (books, the strong book check)
- Search API: lookup by OCLC number, ISBN, ISSN; keyword/title/author search.
  https://www.oclc.org/developer/api/oclc-apis/worldcat-search-api.en.html
- Answers: does a cataloged manifestation exist? which ISBN maps to which
  edition / binding / language / year? is there an OCLC number? do records
  distinguish translation / reprint / ebook / revised / large-print? are there
  holdings (i.e. not merely a vendor listing)?
- OCLC also has a Citation API — treat its output as a **formatting aid**, not
  as validation of the record or edition.
- Limits: duplicate / merged / provisional / legacy records; a record may
  describe a *related* edition, not the cited one; **API access requires OCLC
  credentials — there is no keyless path** (confirmed in the verification run;
  the book pipeline fell back to Library of Congress + Open Library + Google
  Books, exactly as this ladder prescribes); **absence from WorldCat does not
  establish nonexistence**.

### Library of Congress
- APIs over LoC collections: https://www.loc.gov/apis/ — strong for US imprints;
  LCCN lookups.

### Open Library
- `https://openlibrary.org/api/books?bibkeys=ISBN:{isbn}&format=json&jscmd=data`
- Also OCLC and LCCN bibkeys. Good structured corroboration for books.

### Google Books
- `GET https://www.googleapis.com/books/v1/volumes?q=isbn:{isbn}` (or
  `intitle:` / `inauthor:`). Returns title, authors, publisher, publication
  date. Corroboration tier.

## Source-routing policy (pseudocode)

```text
if DOI present:
    normalize DOI
    resolve https://doi.org/<doi>
    query Crossref /works/{doi}
    if no Crossref record: query DataCite /dois/{doi}
    fetch the publisher / repository landing page from the resolver redirect
    corroborate in OpenAlex / discipline index
    compare cited fields with retrieved metadata

elif ISBN or OCLC present:
    validate ISBN check digit if present
    if check digit FAILS: flag it, fall through to the no-identifier branch
        (do NOT query catalogs with a known-bad ISBN)
    query WorldCat by OCLC / ISBN
    query a national library catalog (LoC for US imprints)
    query the publisher catalog page
    corroborate with Open Library or Google Books
    match the EDITION-level record, not a title-level work

elif PMID present:
    query PubMed, then publisher / DOI metadata

elif arXiv ID present:
    query arXiv, then DOI / publisher metadata if published

else:
    infer type
    run escalating title -> title+author -> tokens+year -> container+vol/iss/pp
      -> publisher+report-number searches in type-appropriate sources
    require TWO independent corroborating records from different pipelines
```

A DOI resolver redirect is evidence the identifier is *registered* — not that
the citation is correct. It can land on a withdrawn item, an erratum, a generic
landing page, or a version of record different from the one cited. Landing pages
also routinely bounce through cookie walls / `?error=cookies_not_supported` —
the **redirect host** (e.g. `link.springer.com`, `dl.acm.org`) is the useful
signal; an HTTP 200 to a generic or consent page is weak on its own. Get the
authoritative fields from Crossref/DataCite, not by scraping the landing page.
