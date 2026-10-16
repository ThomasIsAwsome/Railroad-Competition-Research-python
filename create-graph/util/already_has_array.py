from __future__ import annotations


def already_has_array(items: list, candidate: object) -> bool:
    return any(item == candidate for item in items)
