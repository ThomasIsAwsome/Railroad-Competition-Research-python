from __future__ import annotations

from typing import List


def remove_visited(nodes: List[list], visited_set: set) -> List[list]:
    return [n for n in nodes if f"{n[0]}_{n[1]}" not in visited_set]
