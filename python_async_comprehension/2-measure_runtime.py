#!/usr/bin/env python3
""" Execute async_comprehension four times in parallel using asyncio.gather """
import time
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ measure_runtime should measure the total runtime and return it. """
    start_time = time.time()
    await asyncio.gather(async_comprehension(),
                         async_comprehension(),
                         async_comprehension(),
                         async_comprehension())

    end_time = time.time()
    total_time = end_time - start_time
    return total_time
