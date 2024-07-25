# This module contains utilities for managing various types.

from typing import Collection, Hashable


def unique(x: Collection[Hashable]) -> bool:
    """
    Determine if the members of a collection are unique.
    """
    return len(x) == len(set(x))
