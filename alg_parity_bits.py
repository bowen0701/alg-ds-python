"""
Parity of a binary.

The parity of a binary is 1 if the number of 1s in the word is odd.
"""

from __future__ import absolute_import
from __future__ import print_function
from __future__ import division


class BitsIter:
    def parity_bits(self, n: int) -> int:
        result = 0
        while n:
            result ^= n & 1
            n >>= 1
        return result


def main():
    # Output: 1
    n = 0b1011
    print(BitsIter().parity_bits(n))

    # Output: 0
    n = 0b10001000
    print(BitsIter().parity_bits(n))


if __name__ == "__main__":
    main()
