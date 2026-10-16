from __future__ import annotations

from typing import List, Tuple


def sortPointsByDistance(*, node: Tuple[float, float], nodes: List[Tuple[float, float]]) -> List[Tuple[float, float]]:
    nx, ny = node
    return sorted(nodes, key=lambda n: ((n[0] - nx) ** 2 + (n[1] - ny) ** 2) ** 0.5)
