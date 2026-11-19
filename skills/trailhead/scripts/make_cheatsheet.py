#!/usr/bin/env python3
"""Build a one-page SVG cheatsheet (grid of numbered cards) from a JSON file.

Usage: make_cheatsheet.py <input.json> <output.svg>
JSON: {"title": str, "subtitle": str, "accent": "#dark", "tint": "#light", "items": [{"num": str, "title": str, "summary": str}]}
"""
import json, sys
from xml.sax.saxutils import escape

COLS, W, CARD_W, CARD_H, GAP, PAD, HEAD = 3, 1480, 460, 110, 20, 30, 80


def build(data):
    items, accent = data["items"], data.get("accent", "#312e81")
    tint = data.get("tint", "#c7d2fe")
    rows = -(-len(items) // COLS)
    h = HEAD + 30 + rows * (CARD_H + GAP) + PAD
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{h}" viewBox="0 0 {W} {h}" font-family="-apple-system,Segoe UI,Roboto,sans-serif">',
           '<rect width="100%" height="100%" fill="#f8fafc"/>',
           f'<rect width="{W}" height="{HEAD}" fill="{accent}"/>',
           f'<text x="30" y="50" font-size="32" font-weight="700" fill="white">{escape(data["title"])}</text>',
           f'<text x="30" y="74" font-size="14" fill="#cbd5e1">{escape(data.get("subtitle", ""))}</text>']
    for i, it in enumerate(items):
        x = PAD + (i % COLS) * (CARD_W + GAP)
        y = HEAD + 30 + (i // COLS) * (CARD_H + GAP)
        out += [f'<rect x="{x}" y="{y}" width="{CARD_W}" height="{CARD_H}" rx="10" fill="{tint}" stroke="{accent}" stroke-width="1.5"/>',
                f'<rect x="{x}" y="{y}" width="46" height="{CARD_H}" rx="10" fill="{accent}"/>',
                f'<text x="{x + 23}" y="{y + CARD_H / 2 + 6}" font-size="18" font-weight="700" fill="white" text-anchor="middle">{escape(str(it["num"]))}</text>',
                f'<text x="{x + 58}" y="{y + 38}" font-size="15" font-weight="700" fill="#0f172a">{escape(it["title"])}</text>',
                f'<text x="{x + 58}" y="{y + 62}" font-size="12" fill="#334155">{escape(it["summary"])}</text>']
    return "\n".join(out + ["</svg>"])


if __name__ == "__main__":
    open(sys.argv[2], "w").write(build(json.load(open(sys.argv[1]))))
