#!/usr/bin/env python3

"""
A type annotated function to add to floats
"""


def add(a: float, b: float) -> float:
    """
    add: adds to floats

    Args:
        a: float
        b: float
    """
    return a + b


if __name__ == "__main__":
    add(1.11, 2.22)
