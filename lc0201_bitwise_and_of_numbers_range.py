"""Leetcode 201. Bitwise AND of Numbers Range
Medium

URL: https://leetcode.com/problems/bitwise-and-of-numbers-range/

Given a range [m, n] where 0 <= m <= n <= 2147483647,
return the bitwise AND of all numbers in this range, inclusive.

Example 1:
Input: [5,7]
Output: 4

Example 2:
Input: [0,1]
Output: 0
"""


class SolutionBruteForce(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int

        Time limit exceeded.

        Time complexity: O(n-m).
        Space complexity: O(1).
        """
        # Edge case when m = 0.
        if m == 0:
            return 0

        # Apply brute force method.
        result = m
        for i in range(m + 1, n + 1):
            result &= i
        return result


class SolutionCommonPrefixBit(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int

        Time complexity: O(logn).
        Space complexity: O(1).
        """
        # Edge case.
        if m == 0:
            return 0

        # Find common prefix binary code by right-shifting m & n.
        n_shifts = 0
        while m != n:
            m >>= 1
            n >>= 1
            n_shifts += 1

        # Left-shift m by n_shifts digits.
        return m <<= n_shifts


def main():
    # Output: 4
    m, n = 5, 7
    print SolutionBruteForce().rangeBitwiseAnd(m, n)
    print SolutionCommonPrefixBit().rangeBitwiseAnd(m, n)

    # Output: 0
    m, n = 0, 1
    print SolutionBruteForce().rangeBitwiseAnd(m, n)
    print SolutionCommonPrefixBit().rangeBitwiseAnd(m, n)


if __name__ == '__main__':
    main()
