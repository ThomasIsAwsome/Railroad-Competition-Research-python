from __future__ import annotations

from pathlib import Path


def get_node_location(node: list[float], block_size: float) -> dict:
    """Translate the original JS helper to Python."""
    x, y = node
    x_location = int(x // block_size)
    y_location = int(y // block_size)
    return {"x_location": x_location, "y_location": y_location}


def blockify_nodes(nodes: list[list[float]], block_size: float) -> dict:
    """Keep the same high-level behavior as the original file."""
    blocks = {}
    for index, (x, y) in enumerate(nodes):
        location = get_node_location([x, y], block_size)
        key = f"{location['x_location']}_{location['y_location']}"
        if key in blocks:
            blocks[key][f"{x}_{y}"] = 0
        else:
            blocks[key] = {f"{x}_{y}": 0}
        print(f"{(index / len(nodes)) * 100 if nodes else 0}%")
    return {"blocks": blocks}


def calculate_dist(a: list[float], b: list[float]) -> float:
    """Distance between two points."""
    dx = a[0] - b[0]
    dy = a[1] - b[1]
    return (dx * dx + dy * dy) ** 0.5


def already_has_array(obj: list, candidate: object) -> bool:
    return any(item == candidate for item in obj)


def randomize_array(array: list) -> list:
    import random

    randomized = array[:]
    random.shuffle(randomized)
    return randomized


def map_to_array(graph: dict) -> list:
    result = []
    for key, value in graph.items():
        result.append([key, value])
    return result


def reference_nodes(graph: dict) -> None:
    for key in list(graph.keys()):
        if graph[key] is None:
            graph[key] = []


def remove_node(graph: dict, node_key: str) -> None:
    if node_key in graph:
        del graph[node_key]
