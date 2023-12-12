#!/usr/bin/env python3
"""Double co-routines with tasks"""
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """run wait random n times"""
    delay_list: List[float] = []
    for _ in range(n):
        task = task_wait_random(max_delay)
        delay: float = await task
        # print(f"delay: {delay}")
        delay_list.append(delay)
    length = len(delay_list)
    for i in range(length):
        swapped = False
        for j in range(0, n-i-1):
            if delay_list[j] > delay_list[j+1]:
                delay_list[j], delay_list[j+1] = delay_list[j+1], delay_list[j]
                swapped = True
        if not swapped:
            break

    return delay_list
