#!/usr/bin/env python3
""" Type-annotated function make_multiplier that
takes a float multiplier as argument"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ Returns a function that multiplies a float by multiplier. """
    def funcion_multiplicadora(x: float) -> float:
        return x * multiplier
    return funcion_multiplicadora
