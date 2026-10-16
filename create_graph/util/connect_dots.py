from __future__ import annotations

from typing import List, Dict, Any

import random
import math

from create_graph.util.get_node_location import get_node_location
from create_graph.util.connect_dot_line import connect_dot_line


def get_random_node_from_map(map_obj: Dict[str, Any]) -> List[float] | None:
    if not map_obj:
        return None
    key = random.choice(list(map_obj.keys()))
    x_str, y_str = key.split("_")
    return [float(x_str), float(y_str)]


def remove_searchable_nodes(nodes_graph: Dict[str, Any], nodes_to_remove: Dict[str, Any]) -> None:
    for key in list(nodes_to_remove.keys()):
        nodes_graph.pop(key, None)


def connect_dots(nodes: List[List[float]], blocks: Dict[str, Any], block_size: float, max_node_distance: float) -> Dict[str, Any]:
    graph: Dict[str, List[List[float]]] = {}
    searchable_graph: Dict[str, int] = {}
    dead_ends: List[Any] = []

    for x, y in nodes:
        graph[f"{x}_{y}"] = []
        searchable_graph[f"{x}_{y}"] = 0

    print("/////////// connecting dots //////////////")

    round_count = 0
    while searchable_graph:
        first_node = get_random_node_from_map(searchable_graph)
        if first_node is not None:
            # Simplified surrounding node lookup: look in same block
            surrounding_nodes = []
            loc = get_node_location(first_node, block_size)
            block_key = f"{loc['x_location']}_{loc['y_location']}"
            block = blocks.get(block_key, {})
            for key in block.keys():
                x_s, y_s = key.split("_")
                surrounding_nodes.append([float(x_s), float(y_s)])

            # find closest
            second_node = None
            min_dist = float('inf')
            for cand in surrounding_nodes:
                dx = cand[0] - first_node[0]
                dy = cand[1] - first_node[1]
                d = math.hypot(dx, dy)
                if 0 < d < min_dist:
                    min_dist = d
                    second_node = cand

            if second_node is not None:
                # create two lines
                line1 = connect_dot_line(start_node=second_node, previous_node=first_node, graph=graph, nodes=nodes, blocks=blocks, block_size=block_size, max_node_distance=max_node_distance)
                line2 = connect_dot_line(start_node=first_node, previous_node=second_node, graph=graph, nodes=nodes, blocks=blocks, block_size=block_size, max_node_distance=max_node_distance)

                graph[f"{first_node[0]}_{first_node[1]}"] .append(second_node)
                dead_ends.append(line1.get("dead_end_node"))
                dead_ends.append(line2.get("dead_end_node"))

                remove_searchable_nodes(searchable_graph, line1.get("traversed_nodes", {}))
                remove_searchable_nodes(searchable_graph, line2.get("traversed_nodes", {}))

                print(f"line1_length: {len(line1.get('traversed_nodes', {}))}, line2_length: {len(line2.get('traversed_nodes', {}))}")

        print(f"round_count: {round_count}, searched_nodes_count: {len(searchable_graph)}, nodes_length: {len(nodes)}")
        round_count += 1

    print(f"dead_ends_length: {len(dead_ends)}")
    return {"graph": graph}
