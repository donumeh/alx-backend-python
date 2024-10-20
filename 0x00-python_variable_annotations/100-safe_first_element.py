#!/usr/bin/env python3

"""
Type Annotation of function safe_first_element
"""


from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    safe_first_element: returns first element of list
    """
    if lst:
        return lst[0]
    else:
        return None
