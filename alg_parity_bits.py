"""
Parity of a binary.

The parity of a binary is 1 if the number of 1s in the word is odd.
"""

from __future__ import absolute_import
from __future__ import print_function
from __future__ import division


class BitsIter:
    def parity_bits(self, n: int) -> int:
        pass


def main():
    n = 0b1011
    print(BitsIter().parity_bits(n))


if __name__ == "__main__":
    main()
