from __future__ import annotations


def reference_nodes(graph: dict) -> None:
    for key in list(graph.keys()):
        if graph[key] is None:
            graph[key] = []
