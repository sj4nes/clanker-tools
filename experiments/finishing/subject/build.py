#!/usr/bin/env python3
"""sitegen - build content/ into a static site under out/."""

import html
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).parent
CONTENT = ROOT / "content"
TEMPLATES = ROOT / "templates"
STATIC = ROOT / "static"
OUT = ROOT / "out"

NAV = [("Home", "index.html"), ("About", "about.html")]


def read_front_matter(text):
    """Split a '---' delimited header off the top of a document."""
    meta = {}
    if not text.startswith("---"):
        return meta, text
    end = text.find("\n---", 3)
    if end == -1:
        return meta, text
    for line in text[3:end].strip().splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            meta[key.strip()] = value.strip()
    return meta, text[end + 4 :].lstrip("\n")


def render_markdown(text):
    """A deliberately small subset: headings, links, emphasis, paragraphs."""
    out = []
    for block in re.split(r"\n\s*\n", text.strip()):
        block = block.strip()
        if not block:
            continue
        heading = re.match(r"^(#{1,3})\s+(.*)$", block)
        if heading:
            level = len(heading.group(1))
            out.append(f"<h{level}>{inline(heading.group(2))}</h{level}>")
        else:
            out.append(f"<p>{inline(block)}</p>")
    return "\n".join(out)


def inline(text):
    text = html.escape(text)
    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    return text


def nav_html():
    links = [f'<a href="{href}">{label}</a>' for label, href in NAV]
    return '<nav>' + " ".join(links) + '</nav>'


def render_page(title, body):
    template = (TEMPLATES / "page.html").read_text()
    return (
        template.replace("{{title}}", html.escape(title))
        .replace("{{nav}}", nav_html())
        .replace("{{content}}", body)
    )


def slug_of(path):
    return path.stem


def build():
    if OUT.exists():
        shutil.rmtree(OUT)
    (OUT / "posts").mkdir(parents=True)

    posts = []
    for md in sorted((CONTENT / "posts").glob("*.md")):
        meta, body = read_front_matter(md.read_text())
        title = meta.get("title", slug_of(md))
        page = render_page(title, render_markdown(body))
        (OUT / "posts" / f"{slug_of(md)}.html").write_text(page)
        posts.append((meta.get("date", ""), title, f"posts/{slug_of(md)}.html"))

    for md in sorted(CONTENT.glob("*.md")):
        meta, body = read_front_matter(md.read_text())
        title = meta.get("title", slug_of(md))
        content = render_markdown(body)
        if slug_of(md) == "index":
            items = "\n".join(
                f'<li><a href="{href}">{html.escape(title_)}</a> '
                f'<span class="date">{html.escape(date)}</span></li>'
                for date, title_, href in sorted(posts, reverse=True)
            )
            content += f"\n<ul class=\"posts\">\n{items}\n</ul>"
        (OUT / f"{slug_of(md)}.html").write_text(render_page(title, content))

    shutil.copy(STATIC / "style.css", OUT / "style.css")
    print(f"built {len(posts)} posts + {len(list(CONTENT.glob('*.md')))} pages -> {OUT}")


if __name__ == "__main__":
    sys.exit(build())
