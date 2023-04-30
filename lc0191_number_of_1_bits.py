"""Leetcode 191. Number of 1 Bits
Easy

URL: https://leetcode.com/problems/number-of-1-bits/

Write a function that takes an unsigned integer and return the number of '1' bits
it has (also known as the Hamming weight).

Example 1:
Input: 00000000000000000000000000001011
Output: 3
Explanation: The input binary string 00000000000000000000000000001011 has a total
of three '1' bits.

Example 2:
Input: 00000000000000000000000010000000
Output: 1
Explanation: The input binary string 00000000000000000000000010000000 has a total
of one '1' bit.

Example 3:
Input: 11111111111111111111111111111101
Output: 31
Explanation: The input binary string 11111111111111111111111111111101 has a total
of thirty one '1' bits.

Note:
Note that in some languages such as Java, there is no unsigned integer type.
In this case, the input will be given as signed integer type and should not affect
your implementation, as the internal binary representation of the integer is the
same whether it is signed or unsigned.
In Java, the compiler represents the signed integers using 2's complement notation.
Therefore, in Example 3 above the input represents the signed integer -3.

Follow up:
If this function is called many times, how would you optimize it?
"""

class SolutionBitsReprIter:
    def hammingWeight(self, n: int) -> int:
        """
        Time complexity: O(32) = O(1).
        Space complexity: O(32) = O(1).
        """
        bits = [0] * 32
        pos = 31
        while n:
            bits[pos] = n & 1
            n >>= 1
            pos -= 1

        return sum(bits)


class SolutionBitsIter:
    def hammingWeight(self, n: int) -> int:
        """
        Time complexity: O(32) = O(1).
        Space complexity: O(1).
        """
        result = 0
        while n:
            result += n & 1
            n >>= 1
        return result


class SolutionBitsDropLowestSetBit:
    def hammingWeight(self, n: int) -> int:
        """
        Time complexity: O(k) = O(1), where k is the number of bits.
        Space complexity: O(1).
        """
        result = 0
        while n:
            result += 1
            # Drop the lowest set bit.
            n &= (n - 1)
        return result


class SolutionBin:
    def hammingWeight(self, n: int) -> int:
        """
        Time complexity: O(1).
        Space complexity: O(1).
        """
        return bin(n).count('1')


def main():
    # Output: 3
    n = 0b00000000000000000000000000001011
    print(SolutionBitsReprIter().hammingWeight(n))
    print(SolutionBitsIter().hammingWeight(n))
    print(SolutionBitsDropLowestSetBit().hammingWeight(n))
    print(SolutionBin().hammingWeight(n))

    # Output: 1
    n = 0b00000000000000000000000010000000
    print(SolutionBitsReprIter().hammingWeight(n))
    print(SolutionBitsIter().hammingWeight(n))
    print(SolutionBitsDropLowestSetBit().hammingWeight(n))
    print(SolutionBin().hammingWeight(n))

    # Output: 31
    n = 0b11111111111111111111111111111101
    print(SolutionBitsReprIter().hammingWeight(n))
    print(SolutionBitsIter().hammingWeight(n))
    print(SolutionBitsDropLowestSetBit().hammingWeight(n))
    print(SolutionBin().hammingWeight(n))


if __name__ == '__main__':
    main()
