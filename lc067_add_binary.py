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
    def normalize(self, a, b):
        if len(a) < len(b):
            a = '0' * (len(b) - len(a)) + a
        elif len(a) > len(b):
            b = '0' * (len(a) - len(b)) + b
        return a, b

    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        # Normalize a and b to equal size by padding 0's to shorer one.
        a, b = self.normalize(a, b)

        # Add numbers in a reversed order with carry.
        s, carry = '', 0
        i = len(a) - 1
        
        while i >= 0 or carry > 0:
            if i >= 0: 
                total = int(a[i]) + int(b[i]) + carry
            else:
                total = carry
            carry, val = total // 2, total % 2
            s = str(val) + s
            i -= 1
        
        return s


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
