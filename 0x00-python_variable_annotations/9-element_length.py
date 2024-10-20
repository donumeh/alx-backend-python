#!/usr/bin/env python3

"""
Type Annotation for function element_length
"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    element_length: iterable sequence generator
    """
    return [(i, len(i)) for i in lst]
