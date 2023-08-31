#!/usr/bin/env python3
""" The code is nearly identical to wait_n
except task_wait_random is being called. """

from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ Returns a sorted list of floats. """
    new_list = []
    for i in range(n):
        num = await wait_random(max_delay)
        new_list.append(num)
    return sorted(new_list)
