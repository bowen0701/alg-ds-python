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


class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m == 0:
            return 0

        result = m
        for i in range(m + 1, n + 1):
            result &= i
        return result


def main():
    # Output: 4
    m, n = 5, 7
    print Solution().rangeBitwiseAnd(m, n)

    # Output: 0
    m, n = 0, 1
    print Solution().rangeBitwiseAnd(m, n)


if __name__ == '__main__':
    main()
