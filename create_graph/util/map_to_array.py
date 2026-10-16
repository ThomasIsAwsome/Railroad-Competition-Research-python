from __future__ import annotations

from typing import List


def map_to_array(graph: dict) -> list:
    return [[key, value] for key, value in graph.items()]
