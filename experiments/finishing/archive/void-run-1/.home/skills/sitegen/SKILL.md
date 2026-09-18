---
name: sitegen
description: Use when building or debugging the sitegen site generator.
category: software-development
---

# sitegen

Static site generator for a small blog. Builds `content/` Markdown into `out/` HTML.

## Layout

- `content/posts/*.md` -- blog posts (front-matter: title, date)
- `content/index.md`, `content/about.md` -- top-level pages
- `templates/page.html` -- shared template with `{{title}}`, `{{nav}}`, `{{stylesheet}}`, `{{content}}` placeholders
- `static/style.css` -- shared stylesheet
- `build.py` -- build script (stdlib only)
- `tests/test_build.py` -- unit tests

## Build & test

    python3 build.py
    python3 -m unittest discover -s tests -v

## Key behavior

- Posts go to `out/posts/<slug>.html`; top-level pages to `out/<slug>.html`
- Nav and stylesheet links use relative prefixes (posts use `../`)
- Index lists all posts sorted by date (newest first)
- Markdown subset: headings (#, ##, ###), paragraphs, links, **bold**

## Known pitfall & fix

Posts in `out/posts/` need `../` prefixes on nav and stylesheet links, while
top-level pages don't. `render_page` takes a `prefix` parameter — pass `"../"`
for posts, `""` for top-level pages. The template uses `{{stylesheet}}` and
`{{nav}}` placeholders so the prefix is applied consistently.

**Symptom if it breaks again:** post pages (`out/posts/*.html`) lose their CSS
and nav links 404 — `href="style.css"` resolves to `out/posts/style.css` which
doesn't exist. Build succeeds but the site looks broken in a browser.

## How to verify after editing build.py

Run `python3 build.py` then `python3 -m unittest discover -s tests -v`. Then serve
`out/` with `python3 -m http.server` from inside it and curl every path — all should
return 200.

## Adding a post

1. Create `content/posts/my-post.md` with front-matter header
2. Run `python3 build.py`
3. Link appears on index automatically