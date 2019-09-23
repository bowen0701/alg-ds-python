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
            n /= 3.0

        if n == 1:
            return True
        else:
            return False


def main():
    # Output: True
    n = 27
    print SolutionWhile().isPowerOfThree(n)

    # Output: False
    n = 0
    print SolutionWhile().isPowerOfThree(n)

    # Output: True
    n = 9
    print SolutionWhile().isPowerOfThree(n)

    # Output: False
    n = 45
    print SolutionLoop().isPowerOfThree(n)



if __name__ == '__main__':
    main()
