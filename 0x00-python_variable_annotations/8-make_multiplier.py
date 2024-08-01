#!/usr/bin/env python3
"""defines max_multiplier() function"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """returns a function thet multiples an argument by multiplier"""

    def f(n: float) -> float:
        """ multiplies a float by multiplier """
        return float(n * multiplier)

    return f
