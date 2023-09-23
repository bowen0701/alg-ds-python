"""Right propagate the rightmost set bit in x.

Example: Turns (01010000)2 to (01011111)2.
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


def bit_right_propagate(x: float) -> float:
    """Bit right propagate by bit operation:
    (x - 1) OR isolated lowest set bit.

    - Time complexity: O(1).
    - Space complexity: O(1).    
    """
    return (x - 1) | (x & ~(x - 1))


def main():
    x = 0b01010000
    assert(bit_right_propagate(x) == 0b01011111)

    x = 0b01010010
    assert(bit_right_propagate(x) == 0b01010011)


if __name__ == "__main__":
    main()
