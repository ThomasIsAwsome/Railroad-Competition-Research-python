from __future__ import annotations

from typing import Dict, Any, List, Tuple

from shortest_path.util.stringify_node_to_key import stringify_node_to_key


def get_next_node(*, table: Dict[str, Any], visited: set) -> Tuple[float, float] | None:
    smallest = float('inf')
    next_node = None
    for key, value in table.items():
        if key in visited:
            continue
        sd = value.get('shortest_distance', float('inf'))
        if sd < smallest:
            smallest = sd
            parts = key.split('_')
            next_node = (float(parts[0]), float(parts[1]))
    return next_node
