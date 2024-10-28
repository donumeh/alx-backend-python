#!/usr/bin/env python3

"""
Executes Tasks
"""

import asyncio
from typing import List


task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    wait_n: multiple co-routine

    Args:
        n type(int): number of routines to work on
        max_delay: type(int): delay to insert
    """
    routines = await asyncio.gather(
            *[task_wait_random(max_delay) for i in range(n)]
            )
    return sorted(routines)


if __name__ == "__main__":

    n = 5
    max_delay = 6
    print(asyncio.run(task_wait_n(n, max_delay)))
