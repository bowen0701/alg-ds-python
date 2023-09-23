"""Swap two numbers."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from typing import Tuple


def swap_by_bit_xor(x: float, y: float) -> Tuple[float, float]:
    x = x ^ y
    y = x ^ y
    x = x ^ y
    return x, y


def swap_by_tuple(x: float, y: float) -> Tuple[float, float]:
    x, y = y, x
    return x, y


def main():
    x = 10
    y = 5
    x, y = swap_by_bit_xor(x, y)
    assert(x == 5 and y == 10)

    x = 10
    y = 5
    x, y = swap_by_tuple(x, y)
    assert(x == 5 and y == 10)


if __name__ == "__main__":
    main()
