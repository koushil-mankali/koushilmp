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

if __name__ == "__main__":
    test_links_and_idempotent(); test_no_blocks(); print("ok")
