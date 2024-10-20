#!/usr/bin/env python3

"""
Type annotated for function to_kv
"""

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    to_kv: Takes in string and int OR float and ret tuple

    Args:
        k: type(str)
        v: type(int | float)
    """
    import math

    squared: float = math.pow(v, 2)

    ret_tuple: Tuple[str, float] = (k, squared)

    return ret_tuple
