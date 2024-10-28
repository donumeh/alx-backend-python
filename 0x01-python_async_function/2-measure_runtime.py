#!/usr/bin/python3

"""
A function measure_time that measures the total execution time
for wait_n function
"""

import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    measure_time: measures total execution time

    Args:
        n type(int): num of times to run
        max_delay type(int): delay time for function

    Return:
        float: (total_time / n)
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    total_time = time.time() - start_time
    return total_time / n


if __name__ == "__main__":
    n = 5
    max_delay = 9

    print(measure_time(n, max_delay))
