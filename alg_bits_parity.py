"""
Parity of a binary.

The parity of a binary is 1 if the number of 1s in the word is odd.
"""

from __future__ import absolute_import
from __future__ import print_function
from __future__ import division


class BitsIter:
    def bits_parity(self, n: int) -> int:
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
    def bits_parity(self, n: int) -> int:
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


class BitsCache:
    def __init__(self, cache_size: int = 16):
        # Cache parity for all numbers between 0 - 2^cache_size.
        self.precomputed_parity = dict()
        for n in range(2 ** cache_size):
            self.precomputed_parity[n] = self._precompute_bits_parity(n)

    def _precompute_bits_parity(self, n: int) -> int:
        # Helper function for precomputing bits parity.
        result = 0
        while n:
            result ^= 1
            # Drop the lowest set bit.
            n &= (n - 1)
        return result

    def bits_parity(self, n: int, cache_size: int = 16) -> int:
        """
        Time complexity: O(n/l) = O(1), where 
          - n is the binary word size; and 
          - l is the width of the words for cache.
        Space complexity: O(2^l).
        """
        # Actually bit_mask = 2 ** cache_size - 1.
        bit_mask = 0xFFFF
        return (
            self.precomputed_parity[n >> (3 * cache_size)] ^
            self.precomputed_parity[(n >> (2 * cache_size)) & bit_mask] ^
            self.precomputed_parity[(n >> cache_size) & bit_mask] ^
            self.precomputed_parity[n & bit_mask]
        )


def main():
    # Output: 1
    n = 0b1011
    print(BitsIter().bits_parity(n))
    print(BitsDropLowestSetBit().bits_parity(n))
    print(BitsCache().bits_parity(n))

    # Output: 0
    n = 0b10001000
    print(BitsIter().bits_parity(n))
    print(BitsDropLowestSetBit().bits_parity(n))
    print(BitsCache().bits_parity(n))


if __name__ == "__main__":
    main()
