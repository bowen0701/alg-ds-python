"""Leetcode 190. Reverse Bits
Easy

URL: https://leetcode.com/problems/reverse-bits/

Reverse bits of a given 32 bits unsigned integer.

Example 1:
Input: 00000010100101000001111010011100
Output: 00111001011110000010100101000000
Explanation: The input binary string 00000010100101000001111010011100
represents the unsigned integer 43261596, so return 964176192 which its
binary representation is 00111001011110000010100101000000.

Example 2:
Input: 11111111111111111111111111111101
Output: 10111111111111111111111111111111
Explanation: The input binary string 11111111111111111111111111111101
represents the unsigned integer 4294967293, so return 3221225471
which its binary representation is 10101111110010110010011101101001.

Note:
- Note that in some languages such as Java, there is no unsigned integer type.
  In this case, both input and output will be given as signed integer type
  and should not affect your implementation, as the internal binary
  representation of the integer is the same whether it is signed or unsigned.
- In Java, the compiler represents the signed integers using 2's complement
  notation. Therefore, in Example 2 above the input represents the
  signed integer -3 and the output represents the signed integer -1073741825.
"""

class SolutionBitsReprIter:
    """
    Time complexity: O(32) = O(1).
    Space complexity: O(32) = O(1).
    """
    def reverseBits(self, n: int) -> int:
        # Edge case.
        if not n:
            return 0

        # Convert n to bits array.
        bits = [0] * 32
        i = 31
        while n:
            bits[i] = n & 1
            n >>= 1
            i -= 1

        # Traverse from back of bits array to accumulate result.
        result = 0
        for i in range(-1, -33, -1):
            result = (result << 1) + bits[i]
        return result


class SolutionBitsIter:
    """
    Time complexity: O(32) = O(1).
    Space complexity: O(32) = O(1).
    """
    def reverseBits(self, n: int) -> int:
        # Edge case.
        if not n:
            return 0

        # Iteratively apply bit AND to lsb and left shift result.
        result = 0
        for i in range(32):
            result = (result << 1) + (n & 1)
            n >>= 1
        return result


class SolutionBin:
    """
    Time complexity: O(1).
    Space complexity: O(1).
    """
    def reverseBits(self, n: int) -> int:
        # Edge case.
        if not n:
            return 0

        # Pad zeros before bin_n to 32 bits, reverse it, and convert to int.
        bin_n = bin(n)[2:]
        return int(('0' * (32 - len(bin_n)) + bin_n)[::-1], 2)


def main():
    # Output: 964176192 (0b00111001011110000010100101000000)
    n = 0b00000010100101000001111010011100
    print(SolutionBitsReprIter().reverseBits(n))
    print(SolutionBitsIter().reverseBits(n))
    print(SolutionBin().reverseBits(n))

    # Output: 3221225471 (10111111111111111111111111111111)
    n = 0b11111111111111111111111111111101
    print(SolutionBitsReprIter().reverseBits(n))
    print(SolutionBitsIter().reverseBits(n))
    print(SolutionBin().reverseBits(n))


if __name__ == '__main__':
    main()
