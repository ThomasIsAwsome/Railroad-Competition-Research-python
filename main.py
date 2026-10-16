import json
from pathlib import Path

from create_graph.create_graph import create_graph
from draw.draw_graph import draw_graph
from draw.draw_nodes import draw_nodes


def main() -> None:
    """Mirror the original Node.js entrypoint logic as closely as possible."""
    path = Path("test-data/test15.json")
    if not path.exists():
        print(f"No input file found at {path}. Expected the original sample data to exist.")
        return

    with path.open("r", encoding="utf-8") as handle:
        nodes = json.load(handle)

    graph_info = create_graph(nodes=nodes)
    graph = graph_info["graph"]

    draw_graph(width=1000, height=1000, graph=graph, save_to="test-pictures/test-graph.png")
    draw_nodes(width=1000, height=1000, nodes=nodes, save_to="test-pictures/test-dotted.png")


if __name__ == "__main__":
    main()
