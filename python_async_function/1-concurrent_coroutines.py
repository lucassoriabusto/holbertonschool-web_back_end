#!/usr/bin/env python3
""" Importa la funcion wait_random """

from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ Espera n veces utilizando wait_random con
    un tiempo de espera máximo especificado. """
    new_list = []
    for i in range(n):
        num = await wait_random(max_delay)
        new_list.append(num)
    return sorted(new_list)
