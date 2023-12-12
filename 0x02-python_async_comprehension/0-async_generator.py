#!/usr/bin/env python3
"""
A coroutine called async_generator that takes no arguments

The coroutine will loop 10 times, each time asynchronously wait 1 second,
then yield a random number between 0 and 10. Use the random module
"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Loops 10 times through with a time interval interval
    of 1 sec between each iteration
    """
    for n in range(10):
        await asyncio.sleep(1)
        yield radom.random() * 10
