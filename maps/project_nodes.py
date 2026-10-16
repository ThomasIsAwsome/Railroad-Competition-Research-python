from __future__ import annotations

from maps.Mercator import Mercator
from typing import List, Tuple, Dict


def project_nodes(*, nodes: List[Tuple[float, float]], width: int, height: int) -> Dict[str, List[Tuple[float, float]]]:
    print('projecting nodes')
    projected: List[Tuple[float, float]] = []

    for latitude, longitude in nodes:
        coords = Mercator(latitude=latitude, longitude=longitude)
        x = coords['x'] + 15000
        y = height - coords['y']
        projected.append([x, y])

    return {"projected": projected}
