from __future__ import annotations

import json
from typing import Dict, Any


def get_graph(file_location: str) -> Dict[str, Any]:
    with open(file_location, 'r', encoding='utf-8') as fh:
        data = json.load(fh)
    return data
