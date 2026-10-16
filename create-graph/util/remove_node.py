from __future__ import annotations


def remove_node(graph: dict, key: str) -> None:
    if key in graph:
        del graph[key]
