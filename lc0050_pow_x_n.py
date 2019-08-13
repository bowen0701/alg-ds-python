"""Leetcode 50. Pow(x, n).
Medium

URL: https://leetcode.com/problems/powx-n/

Implement pow(x, n), which calculates x raised to the power n (x^n).

Example 1:
Input: 2.00000, 10
Output: 1024.00000

Example 2:
Input: 2.10000, 3
Output: 9.26100

Example 3:
Input: 2.00000, -2
Output: 0.25000
Explanation: 2^-2 = 1/2^2 = 1/4 = 0.25

Note:
- -100.0 < x < 100.0
- n is a 32-bit signed integer, within the range [-2^31, 2^31 - 1].
"""

class SolutionNaive(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float

        Note: Underflow or Overflow.

        Time complexity: O(n).
        Space complexity: O(1).
        """
        if n < 0:
            x = 1 / x
            n = -n
        elif n == 0:
            return 1

        # Iteratively product x for n times. 
        res = 1
        for i in range(n):
            res *= x
        return res


class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float

        Time complexity: O(logn).
        Space complexity: O(1).
        """
        if n < 0:
            x = 1 / x
            n = -n
        elif n == 0:
            return 1

        res = 1
        
        while n > 0:
            # If n is odd, product x once.
            if n & 1:
                res *= x

            # Obtain x to the power of 2, then shift n to n/2.
            x *= x
            n >>= 1
        
        return res


def main():
    # Should be 1024.
    x, n = 2.00000, 10
    print SolutionNaive().myPow(x, n)
    print Solution().myPow(x, n)

    # Should be 9.26100.
    x, n = 2.10000, 3
    print SolutionNaive().myPow(x, n)
    print Solution().myPow(x, n)

    # Should be 0.25.
    x, n = 2.00000, -2
    print SolutionNaive().myPow(x, n)
    print Solution().myPow(x, n)


if __name__ == '__main__':
    main()
