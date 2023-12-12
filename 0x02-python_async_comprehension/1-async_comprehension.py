#!/usr/bin/env python3
"""A coroutine called async_comprehension that takes no arguments"""


from typing import List
async_generator = __import__('0-async_generator.py').async_generator


async def async_comprehension() -> List[float]:
    """returns the 10 random numbers"""
    res = [num async for num in async_generator]
    return res
