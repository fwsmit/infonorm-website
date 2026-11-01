#!/usr/bin/env python3
"""Build the static pages by inlining shared partials.

Usage:
    python3 build.py

Edit the pages in src/ and shared fragments in partials/, then run this script.
The generated HTML is written to the project root so it can be opened directly
or uploaded to any static host.
"""

from pathlib import Path
import re
import textwrap

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "src"

INCLUDE_RE = re.compile(
    r"^([ \t]*)<!--\s*include:\s*([^\s]+)\s*-->[ \t]*\n?",
    re.MULTILINE,
)


def inline_includes(html: str) -> str:
    def replace(match: re.Match[str]) -> str:
        indent, partial_path = match.groups()
        partial = (ROOT / partial_path).read_text(encoding="utf-8")
        partial = textwrap.dedent(partial).rstrip("\n")
        return textwrap.indent(partial, indent) + "\n"

    return INCLUDE_RE.sub(replace, html)


def main() -> None:
    for source in sorted(SRC.glob("*.html")):
        output = ROOT / source.name
        output.write_text(inline_includes(source.read_text(encoding="utf-8")), encoding="utf-8")
        print(f"built {output.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
