#!/usr/bin/env python3

"""
Type annotated for function sum_mixed_list
"""

from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    sum_mixed_list: takes a list of integers and floats and returns their sum

    Args:
        mxd_lst type(list[int|float])
    """

    return sum(mxd_lst)
