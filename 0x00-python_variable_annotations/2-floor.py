#!/usr/bin/env python3

"""
Type annotation for funtion floor
"""


def floor(n: float) -> int:
    """
    floor: Rounds a decimal to whole number

    Args:
        n: type(float): number to round
    """
    import math

    return math.floor(n)


if __name__ == "__main__":
    floor(3.14)
