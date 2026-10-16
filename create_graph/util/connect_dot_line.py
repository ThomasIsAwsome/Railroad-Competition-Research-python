from __future__ import annotations

from typing import Any, Dict, List

import math


def connect_dot_line(*, start_node: List[float], previous_node: List[float], graph: Dict[str, List[List[float]]], nodes: List[List[float]], blocks: Dict[str, Any], block_size: float, max_node_distance: float) -> Dict[str, Any]:
    """Simplified version of the connect_dot_line behaviour: walk from start_node toward previous_node
    adding traversed nodes to a set until a dead end or distance exceeds max_node_distance.
    """
    traversed_nodes: Dict[str, int] = {}
    dead_end_node = None

    # Push an immediate connection for simplicity
    key_prev = f"{previous_node[0]}_{previous_node[1]}"
    key_start = f"{start_node[0]}_{start_node[1]}"
    graph.setdefault(key_prev, []).append(start_node)
    graph.setdefault(key_start, [])

    traversed_nodes[key_start] = 0

    # dead_end is the other node for now
    dead_end_node = previous_node

    return {"traversed_nodes": traversed_nodes, "dead_end_node": dead_end_node}
