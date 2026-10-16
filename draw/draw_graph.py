from __future__ import annotations

from PIL import Image, ImageDraw
from typing import Dict, List, Tuple
from pathlib import Path
import math
import random


def random_rgb() -> Tuple[int, int, int]:
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


def draw_line(draw: ImageDraw.ImageDraw, x1: float, y1: float, x2: float, y2: float, spacing: float = 0.3, radius: float = 1) -> None:
    dx = x2 - x1
    dy = y2 - y1
    distance = math.hypot(dx, dy)
    steps = max(int(distance / spacing), 1)
    color = random_rgb()
    for i in range(steps + 1):
        x = x1 + (dx * (i / steps))
        y = y1 + (dy * (i / steps))
        bbox = [x - radius, y - radius, x + radius, y + radius]
        draw.ellipse(bbox, fill=color)


def draw_graph(*, width: int, height: int, graph: Dict[str, List[List[float]]], save_to: str) -> None:
    print(f"drawing graph to save to: {save_to}")
    img = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(img)

    # draw connecting edges
    for key, connected_to in graph.items():
        if not key:
            continue
        node_x, node_y = map(float, key.split("_"))
        if connected_to:
            for conn in connected_to:
                connected_x = float(conn[0])
                connected_y = float(conn[1])
                draw_line(draw, node_x, node_y, connected_x, connected_y)

    # draw dots
    for key in graph.keys():
        node_x, node_y = map(float, key.split("_"))
        bbox = [node_x - 1, node_y - 1, node_x + 1, node_y + 1]
        draw.ellipse(bbox, fill=(255, 0, 0))

    Path(save_to).parent.mkdir(parents=True, exist_ok=True)
    img.save(save_to, "PNG")
    print(f"Finished drawing graph to {save_to}")
