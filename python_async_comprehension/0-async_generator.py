#!/usr/bin/env python3
""" The coroutine will loop 10 times,
wait 1 second, then yield a random number"""
import random
import asyncio
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """ yield: generará valores de forma asincrónica
    a medida que estén disponibles """
    for i in range(0, 10):
        random_number = random.uniform(0, 10)
        await asyncio.sleep(1)
        yield random_number
