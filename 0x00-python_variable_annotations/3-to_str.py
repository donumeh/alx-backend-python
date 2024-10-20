#!/usr/bin/env python3

"""
Type annotated function for to_str
"""


def to_str(n: float) -> str:
    """
    to_str: converts float to string

    Args:
        n type(float): value to convert to string
    """
    return str(n)


if __name__ == "__main__":
    to_str(3.14)
