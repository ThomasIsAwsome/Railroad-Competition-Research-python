from __future__ import annotations

from PIL import Image, ImageDraw
from typing import List, Tuple
from pathlib import Path


def draw_nodes(*, width: int, height: int, nodes: List[Tuple[float, float]], save_to: str) -> None:
    """Draw nodes as small filled circles using Pillow."""
    print(f"drawing nodes to save to: {save_to}")
    img = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(img)

    r = 2
    for node in nodes:
        x, y = node[0], node[1]
        bbox = [x - r, y - r, x + r, y + r]
        draw.ellipse(bbox, fill=(0, 128, 0))

    Path(save_to).parent.mkdir(parents=True, exist_ok=True)
    img.save(save_to, "PNG")
    print(f"Finished Drawing the nodes to {save_to}")
