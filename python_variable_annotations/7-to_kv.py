#!/usr/bin/env python3
""" Type-annotated function to_kv that takes a string k and
an int OR float v as arguments and returns a tuple."""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ Return a tuple """
    square_v = v ** 2
    new_tuple = (k, square_v)
    return new_tuple
