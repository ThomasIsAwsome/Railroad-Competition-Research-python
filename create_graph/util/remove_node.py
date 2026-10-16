from __future__ import annotations

from typing import List


def remove_node(graph: dict, node_key: str) -> None:
    graph.pop(node_key, None)
