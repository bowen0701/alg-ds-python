"""Leetcode 231. Power of Two
Easy

URL: https://leetcode.com/problems/power-of-two/

Given an integer, write a function to determine if it is a power of two.

Example 1:
Input: 1
Output: true 
Explanation: 2^0 = 1

Example 2:
Input: 16
Output: true
Explanation: 2^4 = 16

Example 3:
Input: 218
Output: false
"""

class SolutionIter(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool

        Time complexity: O(logn).
        Space complexity: O(1).
        """
        i = 1
        while i < n:
            i *= 2
        return i == n


def main():
    # Output: True
    n = 1
    print SolutionIter().isPowerOfTwo(n)

    # Output: True
    n = 16
    print SolutionIter().isPowerOfTwo(n)

    # Output: False
    n = 218
    print SolutionIter().isPowerOfTwo(n)


if __name__ == '__main__':
    main()
