#!/usr/bin/env python3
"""defines task_wait_random function"""
import asyncio
import random

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """takes in an integer as argument and returns an asyncio.Task"""
    loop = asyncio.get_event_loop()
    return loop.create_task(wait_random(max_delay))
