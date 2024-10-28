#!/usr/bin/env python3

"""
Executes multiple co-routines
"""

import asyncio
from typing import List


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    wait_n: multiple co-routine

    Args:
        n type(int): number of routines to work on
        max_delay: type(int): delay to insert
    """
    wait_random = __import__("0-basic_async_syntax").wait_random

    routines = await asyncio.gather(*[wait_random(max_delay) for i in range(n)])
    return sorted(routines)
    # routines


if __name__ == "__main__":
    print(asyncio.run(wait_n(5, 5)))
    print(asyncio.run(wait_n(10, 7)))
    print(asyncio.run(wait_n(10, 0)))
