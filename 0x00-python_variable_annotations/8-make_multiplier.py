#!/usr/bin/env python3


"""
Type annotation for function make_multiplier
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    make_multiplier: takes a float and returns a function
    """

    def mul(m: float) -> float:
        """
        mul: takes a float and squares it

        Args:
            m type(float)
        """
        import math

        return math.pow(multiplier, 2)

    return mul
