# Railroad Competition Research (Python Port)

This repository is a Python port of the original Node.js project that builds railroad-like graphs, folds/aggregates them, and renders them to image output with Pillow.

The original project structure and approach were preserved as closely as possible while converting from JavaScript to Python.

## Structure

- `create-graph/` - graph construction utilities
- `draw/` - drawing logic, rendered with Pillow
- `fold/` - folding/compression utilities
- `format-data/` - data cleanup and formatting helpers
- `maps/` - Mercator projection and map transformations
- `shortest-path/` - shortest-path research utilities
- `sites/` - browser prototype HTML files
- `main.py` - entry point

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python main.py
```

## Notes

- No `networkx` is used.
- Visual rendering uses `Pillow` instead of `pureimage`.
- The original algorithmic philosophy has been kept: data-first processing, graph generation, graph folding, and image output.
