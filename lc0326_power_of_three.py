"""Leetcode 326. Power of Three
Easy

URL: https://leetcode.com/problems/power-of-three/

Given an integer, write a function to determine if it is a power of three.

Example 1:
Input: 27
Output: true

Example 2:
Input: 0
Output: false

Example 3:
Input: 9
Output: true

Example 4:
Input: 45
Output: false

Follow up:
Could you do it without using any loop / recursion?
"""

class SolutionWhile(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool

        Time complexity: O(logn).
        Space complexity: O(1).
        """
        while n > 1:
            if n % 3 != 0:
                return False
            n /= 3.0

        return n == 1


class SolutionLog10(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool

        Time complexity: O(1).
        Space complexity: O(1).
        """
        import math

        if n < 1:
            return False

        if n == 1:
            return True

        # If 3^k = n, k * log10(3) = log10(n) => k is int.
        k = math.log10(n) / math.log10(3)
        return k % 1 == 0


def main():
    # Output: True
    n = 27
    print SolutionWhile().isPowerOfThree(n)
    print SolutionLog10().isPowerOfThree(n)

    # Output: False
    n = 0
    print SolutionWhile().isPowerOfThree(n)
    print SolutionLog10().isPowerOfThree(n)

    # Output: True
    n = 9
    print SolutionWhile().isPowerOfThree(n)
    print SolutionLog10().isPowerOfThree(n)

    # Output: False
    n = 45
    print SolutionWhile().isPowerOfThree(n)
    print SolutionLog10().isPowerOfThree(n)


if __name__ == '__main__':
    main()
