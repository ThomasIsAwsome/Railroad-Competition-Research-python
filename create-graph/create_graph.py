from __future__ import annotations

from typing import Any, Dict, List

from create_graph.util.randomize_array import randomize_array
from create_graph.util.remove_repeats import remove_repeats
from fold.util.remove_repeats import remove_repeats as fold_remove_repeats


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
    percentile = (100.0 - top_percent) / 100.0
    index = (len(ordered) - 1) * percentile
    lower = int(index)
    upper = min(lower + 1, len(ordered) - 1)
    weight = index - lower
    return float(ordered[lower] + weight * (ordered[upper] - ordered[lower]))


def create_graph(nodes: List[List[float]]) -> Dict[str, Any]:
    """Create a graph based on the original Node.js design."""
    nodes = remove_repeats(nodes=nodes)
    nodes = randomize_array(array=nodes)

    stats = get_dist_stats(nodes=nodes)
    average = stats["average"]
    distances = stats["distances"]
    median = get_median(distances)
    top = get_top_percentile_value(distances, 5)
    largest = distances.pop()
    print(f"average_distance: {average}, median: {median}, top: {top}, largest: {largest}")

    block_size = largest * 10
    print(f"block_size: {block_size}")

    from create_graph.util.blockify_nodes import blockify_nodes
    blocks_result = blockify_nodes(nodes=nodes, block_size=block_size)
    blocks = blocks_result["blocks"]

    from create_graph.util.connect_dots import connect_dots
    graph_result = connect_dots(nodes=nodes, blocks=blocks, block_size=block_size, max_node_distance=largest * 1.5)
    graph = graph_result["graph"]

    from create_graph.util.reference_nodes import reference_nodes
    reference_nodes(graph=graph)

    return {"graph": graph}


def get_dist_stats(nodes: List[List[float]]) -> Dict[str, Any]:
    """Load the helper from the original remove-wild-nodes directory.

    The Node.js repo had this helper under a path with a hyphen. The Python version keeps
    the same directory name but loads it through Python's importlib to preserve the repo's
    original structure.
    """
    import importlib.util
    from pathlib import Path

    spec = importlib.util.spec_from_file_location(
        "remove_wild_nodes_get_dist_stats",
        Path(__file__).resolve().parent / "util" / "remove-wild-nodes" / "get_dist_stats.py",
    )
    module = importlib.util.module_from_spec(spec)
    assert spec and spec.loader
    spec.loader.exec_module(module)
    return module.get_dist_stats(nodes=nodes)
