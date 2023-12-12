#!/usr/bin/env python3
"""A coroutine called async_generator that takes no arguments"""


import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Loops 10 times through with a time interval interval
    of 1 sec between each iteration
    """
    for num in range(10):
        await asyncio.sleep(1)
        yield radom.random() * 10