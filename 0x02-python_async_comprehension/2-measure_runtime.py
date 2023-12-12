#!/usr/bin/env python3
"""
write a measure_runtime coroutine that will execute async_comprehension
four times in parallel using asyncio.gather
"""


import time
from asyncio import gather

async_comprehension = __import__('1-async_comprehension.py').async_comprehension


async def measure_runtime() -> float:
    """Define the measure_runtime coroutine"""
    startTime = time()
    tasks = [async_comprehension() for i in range(4)]
    await gather(*tasks)
    endTime = time()
    return (endTime - startTime)"""measures the total runtime and return it"""
