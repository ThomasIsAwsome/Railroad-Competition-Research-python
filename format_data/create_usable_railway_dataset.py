from __future__ import annotations

import json
from pathlib import Path
from maps.project_nodes import project_nodes
from draw.draw_nodes import draw_nodes


def create_usable_railway_dataset(file_path: str, railway_name: str) -> None:
    # placeholder: read geojson and extract coordinates
    print(f"Creating usable dataset for {railway_name} from {file_path}")
    # Implementation depends on the geojson structure; provide a pass-through for now
    Path('railways').mkdir(parents=True, exist_ok=True)
