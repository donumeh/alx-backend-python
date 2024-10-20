#!/usr/bin/env python3

"""
Type Annotated function for concat
"""


def concat(str1: str, str2: str) -> str:
    """
    Concat: concatenates two strings together

    Args:
        str1: type(str)
        str2: type(str)
    """
    return str1 + str2


if __name__ == "__main__":
    concat("egg", "shell")
