from __future__ import annotations

from typing import List
import random


def find_random_node(nodes: List[List[float]]) -> List[float] | None:
    if not nodes:
        return None
    return random.choice(nodes)
