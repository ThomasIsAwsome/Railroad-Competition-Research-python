from __future__ import annotations

from typing import List


def fold(nodes: List[List[float]], rounds: int) -> List[List[List[float]]]:
    block_size = 0.5
    folded = nodes
    result = []
    for _ in range(rounds):
        # remove repeats
        folded = remove_repeats(folded)
        # blockify and fold once -- simplified: just reduce number of nodes by merging nearest neighbors
        # We'll implement a naive fold_once here
        folded = fold_once(folded, block_size)
        result.append(folded)
    return result


def remove_repeats(nodes):
    seen = set()
    out = []
    for n in nodes:
        key = (float(n[0]), float(n[1]))
        if key not in seen:
            seen.add(key)
            out.append([float(n[0]), float(n[1])])
    return out


def fold_once(nodes, block_size):
    # naive: take every two nodes and average them
    out = []
    i = 0
    while i < len(nodes):
        if i + 1 < len(nodes):
            a = nodes[i]
            b = nodes[i + 1]
            out.append([(a[0] + b[0]) / 2.0, (a[1] + b[1]) / 2.0])
            i += 2
        else:
            out.append(nodes[i])
            i += 1
    return out
