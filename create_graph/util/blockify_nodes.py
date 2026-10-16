from __future__ import annotations

from typing import List


def get_node_location(node: List[float], block_size: float) -> dict:
    x, y = node
    x_location = int(x // block_size)
    y_location = int(y // block_size)
    return {"x_location": x_location, "y_location": y_location}


def blockify_nodes(nodes: List[List[float]], block_size: float) -> dict:
    blocks: dict = {}
    print("/////////// blockifying nodes //////////////")
    for index, (x, y) in enumerate(nodes):
        loc = get_node_location([x, y], block_size)
        block_location = f"{loc['x_location']}_{loc['y_location']}"
        blocks.setdefault(block_location, {})[f"{x}_{y}"] = 0
        print(f"{(index / len(nodes)) * 100 if nodes else 0}%")
    return {"blocks": blocks}
