# sitegen

Builds `content/` into a small browsable site under `out/`: an index listing the
posts, an about page, and one page per post, sharing navigation and a stylesheet.

    python3 build.py

Content is Markdown with a `---` front-matter header (`title`, `date`). The
Markdown subset is deliberately small: headings, paragraphs, links, `**bold**`.

    python3 -m unittest discover -s tests

Handing this over shortly; it should be ready for someone to write posts in.
