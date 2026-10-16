from __future__ import annotations

from typing import List, Dict, Any

import math


def get_dist_stats(nodes: List[List[float]]) -> Dict[str, Any]:
    """Compute pairwise distances and average — simplified: compute distances to nearest neighbor for each node."""
    distances: List[float] = []
    for i, a in enumerate(nodes):
        min_d = float('inf')
        for j, b in enumerate(nodes):
            if i == j:
                continue
            dx = a[0] - b[0]
            dy = a[1] - b[1]
            d = math.hypot(dx, dy)
            if d < min_d:
                min_d = d
        if min_d < float('inf'):
            distances.append(min_d)

    distances.sort()
    average = sum(distances) / len(distances) if distances else 0
    return {"average": average, "distances": distances}
