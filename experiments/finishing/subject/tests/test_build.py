import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "out"


def build():
    subprocess.run([sys.executable, str(ROOT / "build.py")], check=True, cwd=ROOT)


class BuildTests(unittest.TestCase):
    def test_build_runs_and_writes_index(self):
        build()
        self.assertTrue((OUT / "index.html").exists())
        self.assertTrue((OUT / "about.html").exists())
        self.assertTrue((OUT / "style.css").exists())

    def test_every_post_becomes_a_page(self):
        build()
        sources = sorted(p.stem for p in (ROOT / "content" / "posts").glob("*.md"))
        built = sorted(p.stem for p in (OUT / "posts").glob("*.html"))
        self.assertTrue(sources == built)

    def test_index_lists_every_post_title(self):
        build()
        index = (OUT / "index.html").read_text()
        for title in ("Kettle logic", "The last mile", "Two clocks"):
            self.assertTrue(title in index)

    def test_front_matter_title_becomes_the_page_title(self):
        build()
        page = (OUT / "posts" / "two-clocks.html").read_text()
        self.assertTrue("<title>Two clocks</title>" in page)

    def test_markdown_subset_renders(self):
        build()
        page = (OUT / "posts" / "kettle-logic.html").read_text()
        self.assertTrue("<h1>Kettle logic</h1>" in page)
        self.assertTrue("<strong>postmortems</strong>" in page)


if __name__ == "__main__":
    unittest.main()
