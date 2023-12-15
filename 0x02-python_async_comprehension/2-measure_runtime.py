#!/usr/bin/env python3
"""
write a measure_runtime coroutine that will execute async_comprehension
four times in parallel using asyncio.gather
"""


import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Define the measure_runtime coroutine"""
    start = time.time()
    await asyncio.gather(*[async_comprehension() for i in range(4)])
    end = time.time()

    lag = end - start
    return lag
