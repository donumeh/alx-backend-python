#!/usr/bin/env python3

"""
Async Comprehension
"""

import asyncio
from typing import Generator, List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> Generator[List[float], None, None]:
    """
    async_comprehension: collect 10 random numbers using
    async comprehension over async_generator

    Args:
        None

    Return:

        List of floats
    """

    return [value async for value in async_generator()]
