from __future__ import annotations

import math


def Mercator(latitude: float, longitude: float) -> dict:
    """Replicates original Mercator function behavior."""
    radius = 6378.1
    longitude_rad = longitude * (math.pi / 180)
    latitude_rad = latitude * (math.pi / 180)
    x = latitude_rad * radius
    y = radius * math.log(abs(math.tan((longitude_rad / 2) + (math.pi / 4))))
    return {"x": x, "y": y}
