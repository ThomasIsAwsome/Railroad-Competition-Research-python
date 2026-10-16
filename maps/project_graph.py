from __future__ import annotations

from maps.Mercator import Mercator
from typing import Dict, List, Tuple


def project_graph(*, graph: Dict[str, List[Tuple[float, float]]], width: int, height: int) -> Dict[str, Dict]:
    projected_graph: Dict[str, List[Tuple[float, float]]] = {}
    for key, connected_to in graph.items():
        lat = float(key.split("_")[0])
        lon = float(key.split("_")[1])
        coords = Mercator(latitude=lat, longitude=lon)
        x = coords['x'] + 15000
        y = height - coords['y']
        node = [x, y]
        connecting = []
        for conn in connected_to:
            c = Mercator(latitude=float(conn[0]), longitude=float(conn[1]))
            cx = c['x'] + 15000
            cy = height - c['y']
            connecting.append([cx, cy])
        projected_graph[f"{node[0]}_{node[1]}"] = connecting
    return {"projected_graph": projected_graph}
