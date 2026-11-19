#!/usr/bin/env python3
"""Render every ```mermaid block in a chapter README to images/diagram-N.svg and
insert `![Diagram N](./images/diagram-N.svg)` right after the block (idempotent).

Usage: render_diagrams.py <path/to/README.md> [--no-render]
Needs Node (uses `npx -y @mermaid-js/mermaid-cli`); --no-render only rewrites the markdown.
"""
import re, subprocess, sys, tempfile
from pathlib import Path

BLOCK = re.compile(r"```mermaid\n(.*?)\n```[ \t]*\n?", re.S)


def link_blocks(text):
    """Return (new_text, [mermaid sources]); adds an image link after each block lacking one."""
    sources, out, pos = [], [], 0
    for m in BLOCK.finditer(text):
        n = len(sources) + 1
        sources.append(m.group(1))
        img = f"![Diagram {n}](./images/diagram-{n}.svg)"
        out.append(text[pos:m.end()])
        pos = m.end()
        if not text[pos:].lstrip("\n").startswith(img):
            out.append(f"\n{img}\n\n")
    out.append(text[pos:])
    return "".join(out), sources


def main(argv):
    readme = Path(argv[0])
    new_text, sources = link_blocks(readme.read_text())
    if "--no-render" not in argv:
        img_dir = readme.parent / "images"
        img_dir.mkdir(exist_ok=True)
        for n, src in enumerate(sources, 1):
            with tempfile.NamedTemporaryFile("w", suffix=".mmd", delete=False) as f:
                f.write(src)
            subprocess.run(["npx", "-y", "@mermaid-js/mermaid-cli", "-i", f.name,
                            "-o", str(img_dir / f"diagram-{n}.svg"), "-b", "white"], check=True)
    readme.write_text(new_text)
    print(f"{readme}: {len(sources)} diagram(s)")


if __name__ == "__main__":
    main(sys.argv[1:])
