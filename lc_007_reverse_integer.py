"""Leetcode 7. Reverse Integer

URL: https://leetcode.com/problems/reverse-integer/description/

Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321

click to show spoilers.

Note:
The input is assumed to be a 32-bit signed integer. 
Your function should return 0 when the reversed integer overflows.
"""

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # Since input x is a 32-bit integer, -2^31 <= x <= 2^31 - 1.
        if x < 0:
            x_rev = int(str(x)[::-1][-1] + str(x)[::-1][:-1])
        else:
            x_rev = int(str(x)[::-1])
        if abs(x_rev) > 0x7FFFFFFF:
            x_rev = 0
        return x_rev


def main():
    print Solution().reverse(123)
    print Solution().reverse(-123)


if __name__ == '__main__':
    main()
