#!/usr/bin/env python3
"""define sum_mixed_list() function"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int | float]]) -> float:
    """returns the sum of elements in mxd_lst"""
    return sum(mxd_lst)
