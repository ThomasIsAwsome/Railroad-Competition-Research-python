from __future__ import annotations


def remove_repeats(nodes: list[list[float]]) -> list[list[float]]:
    seen = set()
    result = []
    for node in nodes:
        key = (float(node[0]), float(node[1]))
        if key not in seen:
            seen.add(key)
            result.append(list(node))
    return result
