from __future__ import annotations

from typing import Dict, List, Tuple


def update_table(*, table: Dict[str, Dict], nearby_nodes: List[Tuple[float, float]], current_node: Tuple[float, float]) -> None:
    current_key = f"{current_node[0]}_{current_node[1]}"
    current_dist = table[current_key]['shortest_distance']
    for node in nearby_nodes:
        key = f"{node[0]}_{node[1]}"
        # simplistic: assume distance is euclidean
        d = ((node[0] - current_node[0]) ** 2 + (node[1] - current_node[1]) ** 2) ** 0.5
        new_dist = current_dist + d
        if new_dist < table.get(key, {'shortest_distance': float('inf')})['shortest_distance']:
            table.setdefault(key, {})['shortest_distance'] = new_dist
            table[key]['previous_node'] = current_node
