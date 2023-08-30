#!/usr/bin/env python3
""" Write an asynchronous coroutine that takes in an integer argument """
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """ Generates a random float, waits for a delay and returns it """
    random_delay = random.uniform(0, max_delay)
    await asyncio.sleep(random_delay)
    return random_delay
