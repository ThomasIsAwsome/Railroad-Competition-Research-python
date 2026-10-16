from __future__ import annotations

from typing import List


def remove_repeats(nodes: List[List[float]]) -> List[List[float]]:
    seen = set()
    out: List[List[float]] = []
    for node in nodes:
        key = (float(node[0]), float(node[1]))
        if key not in seen:
            seen.add(key)
            out.append([float(node[0]), float(node[1])])
    return out
