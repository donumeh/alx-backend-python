#!/usr/bin/env python3

"""
Type annotation for function safely_get_value
"""

from typing import Any, Dict, Union, Mapping, TypeVar

T = TypeVar("T")


def safely_get_value(
    dct: Mapping, key: Any, default: Union[T, None] = None
) -> Union[Any, T]:
    """
    safely_get_value: the function to annotate

    Args:
        dct type(dict)
        key type(any)
        default type(T | None)
    """
    if key in dct:
        return dct[key]
    else:
        return default
