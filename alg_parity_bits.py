"""
Parity of a binary.

The parity of a binary is 1 if the number of 1s in the word is odd.
"""

from __future__ import absolute_import
from __future__ import print_function
from __future__ import division


class BitsIter:
    def parity_bits(self, n: int) -> int:
        """
        Time complexity: O(64) = O(1).
        Space complexity: O(1).
        """
        result = 0
        while n:
            result ^= n & 1
            n >>= 1
        return result


class BitsDropLowestSetBit:
    def parity_bits(self, n: int) -> int:
        """
        Time complexity: O(k) = O(1), where k is the number of bits.
        Space complexity: O(1).
        """
        result = 0
        while n:
            result ^= 1
            # Drop the lowest set bit.
            n &= (n - 1)
        return result 



def main():
    # Output: 1
    n = 0b1011
    print(BitsIter().parity_bits(n))
    print(BitsDropLowestSetBit().parity_bits(n))

    # Output: 0
    n = 0b10001000
    print(BitsIter().parity_bits(n))
    print(BitsDropLowestSetBit().parity_bits(n))


if __name__ == "__main__":
    main()
