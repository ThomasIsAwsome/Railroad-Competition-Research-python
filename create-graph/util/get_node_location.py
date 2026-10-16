from __future__ import annotations


def get_node_location(node: list[float], block_size: float) -> dict:
    x, y = node
    x_location = int(x // block_size)
    y_location = int(y // block_size)
    return {"x_location": x_location, "y_location": y_location}
