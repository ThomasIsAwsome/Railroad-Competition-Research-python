from __future__ import annotations

from typing import List


def randomize_array(array: List[List[float]]) -> List[List[float]]:
    import random

    randomized = array[:]
    random.shuffle(randomized)
    return randomized
