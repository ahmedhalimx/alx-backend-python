#!/usr/bin/env python3
"""defiens sum_list() function"""


def sum_list(input_lst: list[float]) -> float:
    """returns the sum of the list"""
    fsum: float = 0
    for i in input_lst:
        fsum += i

    return fsum
