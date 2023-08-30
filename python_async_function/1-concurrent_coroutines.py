#!/usr/bin/env python3
""" """

from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:

    new_list = []
    for i in range(n):
        num = await wait_random(max_delay)
        new_list.append(num)
    return sorted(new_list)
