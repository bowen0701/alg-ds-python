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

class SolutionIter(object):
    def _padding(self, a, b):
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

        Time complexity: O(n), where n is the length of the longer string.
        Space complexity: O(1).
        """
        from collections import deque

        # Normalize a and b to equal length by padding 0's to shorer one.
        a, b = self._padding(a, b)

        # Add binary from backward if not out of boundary or exists carry.
        sum_deq = deque([])
        carry = 0
        i = len(a) - 1

        while i >= 0 or carry > 0:
            if i >= 0: 
                val = int(a[i]) + int(b[i]) + carry
            else:
                val = carry

            carry, val = val // 2, val % 2

            sum_deq.appendleft(str(val))
            i -= 1
        
        return ''.join(list(sum_deq))


def main():
    # Output: "100"
    a = "11"
    b = "1"
    print SolutionIter().addBinary(a, b)

    # Output: "10101"
    a = "1010"
    b = "1011"
    print SolutionIter().addBinary(a, b)


if __name__ == '__main__':
    main()
