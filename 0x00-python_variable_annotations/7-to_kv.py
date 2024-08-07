#!/usr/bin/env python3
"""defines to_kv() function"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """returns a tuple containing a string and a float"""
    return (k, v**2)
