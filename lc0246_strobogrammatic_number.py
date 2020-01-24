"""Leetcode 246. Strobogrammatic Number
Easy

URL: https://leetcode.com/problems/strobogrammatic-number/A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

Write a function to determine if a number is strobogrammatic. The number is
represented as a string.

Example 1:
Input:  "69"
Output: true

Example 2:
Input:  "88"
Output: true

Example 3:
Input:  "962"
Output: false
"""


class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        pass


def main():
    # Output: true
    num = "69"
    print Solution().isStrobogrammatic(num)

    # Output: true
    num = "88"
    print Solution().isStrobogrammatic(num)

    # Output: false
    num = "962"
    print Solution().isStrobogrammatic(num)


if __name__ == '__main__':
    main()
