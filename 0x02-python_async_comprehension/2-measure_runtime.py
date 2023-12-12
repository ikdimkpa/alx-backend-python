#!/usr/bin/env python3
"""
write a measure_runtime coroutine that will execute async_comprehension
four times in parallel using asyncio.gather
"""


import time
import asyncio
from typing import List
async_comprehension = __import__('1-async_comprehension.py').async_comprehension


async def measure_runtime() -> float:
    """measures the total runtime and return it"""
    start_time = time.time()

    await asyncio.gather(*(async_comprehension() for num in range(4)))

    end_time = time.time()
    return end_time - start_time
