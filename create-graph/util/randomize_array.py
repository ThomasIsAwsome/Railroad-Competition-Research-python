from __future__ import annotations

import random
from typing import List


def randomize_array(array: List[List[float]]) -> List[List[float]]:
    randomized = array[:]
    random.shuffle(randomized)
    return randomized
