from __future__ import annotations

from typing import Any, Dict, List

from create_graph.util.randomize_array import randomize_array
from create_graph.util.remove_repeats import remove_repeats
from create_graph.util.get_dist_stats import get_dist_stats
from create_graph.util.blockify_nodes import blockify_nodes
from create_graph.util.connect_dots import connect_dots
from create_graph.util.reference_nodes import reference_nodes


def get_median(numbers: List[float]) -> float | None:
    if not numbers:
        return None
    ordered = sorted(numbers)
    center = len(ordered) // 2
    if len(ordered) % 2 == 0:
        return (ordered[center - 1] + ordered[center]) / 2.0
    return float(ordered[center])


def get_top_percentile_value(numbers: List[float], top_percent: float) -> float | None:
    if not numbers:
        return None
    if top_percent <= 0:
        return float(max(numbers))
    if top_percent >= 100:
        return float(min(numbers))

    ordered = sorted(numbers)
    p = (100.0 - top_percent) / 100.0
    index = (len(ordered) - 1) * p
    lower = int(index)
    upper = min(lower + 1, len(ordered) - 1)
    weight = index - lower
    return float(ordered[lower] + weight * (ordered[upper] - ordered[lower]))


def create_graph(nodes: List[List[float]]) -> Dict[str, Any]:
    """Create a graph based on the original Node.js design.

    Nodes is a list of [x, y] points (lat,lon or projected coordinates).
    Returns a dict with key 'graph' mapping node_key -> list of connected nodes.
    """
    # prepare our data before connecting the dots into a graph like structure
    nodes = remove_repeats(nodes)
    nodes = randomize_array(nodes)

    stats = get_dist_stats(nodes)
    average = stats.get("average")
    distances = stats.get("distances", [])
    median = get_median(distances)
    top = get_top_percentile_value(distances, 5)
    largest = distances.pop() if distances else 0
    print(f"average_distance: {average}, median: {median}, top: {top}, largest: {largest}")

    block_size = largest * 10
    print(f"block_size: {block_size}")

    blocks_result = blockify_nodes(nodes=nodes, block_size=block_size)
    blocks = blocks_result["blocks"]

    graph_result = connect_dots(nodes=nodes, blocks=blocks, block_size=block_size, max_node_distance=largest * 1.5)
    graph = graph_result["graph"]

    reference_nodes(graph=graph)

    return {"graph": graph}
