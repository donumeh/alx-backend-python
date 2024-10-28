#!/usr/bin/env python3

"""
A function that returns asyncio.Task
"""

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    task_wait_random: waits for task

    Args:
        max_delay type(int): max secs to delay

    Return:
        asyncio.Task
    """
    return asyncio.Task(wait_random(max_delay))


if __name__ == "__main__":

    async def test(max_delay: int) -> float:
        task = task_wait_random(max_delay)
        await task
        print(task.__class__)

    asyncio.run(test(5))
