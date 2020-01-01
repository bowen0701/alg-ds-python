"""Leetcode 7. Reverse Integer
Easy

URL: https://leetcode.com/problems/reverse-integer/description/

Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321

click to show spoilers.

Note:
The input is assumed to be a 32-bit signed integer. 
Your function should return 0 when the reversed integer overflows.
"""

class SolutionNegativeOverflow(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int

        Time complexity: O(1).
        Space complexity: O(1).
        """
        # Since input x is a 32-bit integer, -2^31 <= x <= 2^31 - 1.
        x_str = str(x)
        if x < 0:
            x_rev = int(x_str[::-1][-1] + x_str[::-1][:-1])
        else:
            x_rev = int(x_str[::-1])

        # If reversed integer is overflow.
        if abs(x_rev) > 0x7FFFFFFF:
            x_rev = 0

        return x_rev


def main():
    print SolutionNegativeOverflow().reverse(123)
    print SolutionNegativeOverflow().reverse(-123)
    print SolutionNegativeOverflow().reverse(-pow(2, 31))


if __name__ == '__main__':
    main()
