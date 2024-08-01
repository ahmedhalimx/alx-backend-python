#!/usr/bin/env python3
"""defines element_length() function"""

from typing import Sequence, Iterable, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ returns a list of tuples of sequences of integers"""
    return [(i, len(i)) for i in lst]
