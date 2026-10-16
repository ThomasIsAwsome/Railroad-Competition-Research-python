from __future__ import annotations

from typing import Dict


def reference_nodes(graph: Dict[str, list]) -> None:
    for key in list(graph.keys()):
        if graph.get(key) is None:
            graph[key] = []
