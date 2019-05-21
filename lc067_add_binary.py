"""Leetcode 67. Add Binary
Easy

URL: https://leetcode.com/problems/add-binary/

Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:
Input: a = "11", b = "1"
Output: "100"

Example 2:
Input: a = "1010", b = "1011"
Output: "10101"
"""

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        pass


def main():
    a = "11"
    b = "1"
    # Output: "100"
    print Solution().addBinary(a, b)

    a = "1010"
    b = "1011"
    # Output: "10101"
    print Solution().addBinary(a, b)


if __name__ == '__main__':
    main()
