#!/usr/bin/env python3

"""
Type annotation for function sum_list
"""


def sum_list(input_list: list[float]) -> float:
    """
    sum_list: sums up a list of floats

    Args:
        input_list type(list[float]): list of floats to sum up
    """
    return sum(input_list)
