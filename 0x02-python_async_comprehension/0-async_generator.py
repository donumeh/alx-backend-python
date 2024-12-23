#!/usr/bin/env python3

"""
Async Generators
"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    async_generator: loops 10 times awaits for 1 sec an yields a random num
    """

    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
