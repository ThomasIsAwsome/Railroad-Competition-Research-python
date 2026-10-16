from __future__ import annotations


def map_to_array(graph: dict) -> list:
    return [[key, value] for key, value in graph.items()]
