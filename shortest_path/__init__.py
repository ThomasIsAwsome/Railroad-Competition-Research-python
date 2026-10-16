from __future__ import annotations

from typing import Dict, Any, Tuple

from shortest_path.util.get_graph import get_graph
from shortest_path.util.remove_visitted import remove_visited
from shortest_path.util.sortPointsByDistance import sortPointsByDistance
from shortest_path.util.stringify_node_to_key import stringify_node_to_key
from shortest_path.util.update_table import update_table
from shortest_path.Dijkstra import get_next_node


def Dijkstra(graph: Dict[str, Any], starter_node: Tuple[float, float]) -> Dict[str, Any]:
    table: Dict[str, Any] = {}
    starter_node_key = stringify_node_to_key(starter_node)
    current_node = starter_node
    visited = set([starter_node_key])

    # construct table
    for key in graph.keys():
        table[key] = {'shortest_distance': float('inf'), 'previous_node': None}

    table[starter_node_key]['shortest_distance'] = 0
    original_graph_length = len(graph)

    while len(visited) < max(0, original_graph_length - 2):
        current_node_key = stringify_node_to_key(current_node)
        connected_to = graph.get(current_node_key, [])
        remaining = remove_visited(connected_to, visited)
        current_node_distance = table.get(current_node_key, {}).get('shortest_distance', float('inf'))

        if remaining:
            sorted_nodes = sortPointsByDistance(node=current_node, nodes=remaining)
            update_table(table=table, nearby_nodes=sorted_nodes, current_node=current_node)

        next_node = get_next_node(table=table, visited=visited)
        visited.add(stringify_node_to_key(current_node))
        if next_node is None:
            break
        current_node = next_node

    return table
