from __future__ import annotations

from typing import Tuple


def stringify_node_to_key(node: Tuple[float, float]) -> str:
    return f"{node[0]}_{node[1]}"
