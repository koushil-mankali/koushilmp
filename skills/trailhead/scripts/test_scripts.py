from render_diagrams import link_blocks

SRC = "a\n```mermaid\ngraph TD\nA-->B\n```\n\ntext\n```mermaid\ngraph LR\nC-->D\n```\nend\n"

def test_links_and_idempotent():
    once, srcs = link_blocks(SRC)
    assert srcs == ["graph TD\nA-->B", "graph LR\nC-->D"]
    assert "![Diagram 1](./images/diagram-1.svg)" in once and "![Diagram 2](./images/diagram-2.svg)" in once
    twice, _ = link_blocks(once)
    assert twice == once

def test_no_blocks():
    assert link_blocks("plain") == ("plain", [])


def test_cheatsheet():
    import xml.dom.minidom as m
    from make_cheatsheet import build
    svg = build({"title": "A & B", "subtitle": "2 concepts", "tint": "#dbeafe", "items": [{"num": "00", "title": "<x>", "summary": "s"}] * 4})
    m.parseString(svg)  # well-formed XML, special chars escaped
    assert svg.count("<rect") == 2 + 4 * 2 and svg.count("#dbeafe") == 4

if __name__ == "__main__":
    test_links_and_idempotent(); test_no_blocks(); test_cheatsheet(); print("ok")
