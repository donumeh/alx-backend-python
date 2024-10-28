#!/usr/bin/env python3

"""
    An asynchronous co-routine task 0
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    wait_random: Takes an integer args and wait for a random secs

    Args:
        max_delay type(int): maximun delay of secs
    """
    wait_secs = random.uniform(0, max_delay + 1)
    await asyncio.sleep(wait_secs)
    return wait_secs


if __name__ == "__main__":

    print(asyncio.run(wait_random()))
    print(asyncio.run(wait_random(5)))
    print(asyncio.run(wait_random(15)))
