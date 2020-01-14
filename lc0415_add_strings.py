"""Leetcode 415. Add Strings
Easy

URL: https://leetcode.com/problems/add-strings/

Given two non-negative integers num1 and num2 represented as string,
return the sum of num1 and num2.

Note:
- The length of both num1 and num2 is < 5100.
- Both num1 and num2 contains only digits 0-9.
- Both num1 and num2 does not contain any leading zero.
- You must not use any built-in BigInteger library or convert the inputs to 
  integer directly.
"""

class SolutionPaddingAddBackwardIter(object):
    def _padding(self, num1, num2):
        n1, n2 = len(num1), len(num2)
        if n1 < n2:
            num1 = '0' * (n2 - n1) + num1
        elif n1 > n2:
            num2 = '0' * (n1 - n2) + num2
        return num1, num2

    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str

        Time complexity: O(n).
        Space complexity: O(1).
        """
        from collections import deque

        # Pad shorter num with leading zeros to string of equal length.
        num1, num2 = self._padding(num1, num2)

        # Start with carry 0, add digits of num1 & num2 from backward to array.
        sum_arr = deque([])

        i = len(num1) - 1
        carry = 0

        while i >= 0 or carry > 0:
            if i >= 0:
                _sum = int(num1[i]) + int(num2[i]) + carry
            else:
                _sum = carry

            carry, _sum = _sum // 10, _sum % 10
            sum_arr.appendleft(str(_sum))

            i -= 1

        return ''.join(list(sum_arr))


def main():
    # Output: 807.
    num1 = '342'
    num2 = '465'
    print SolutionPaddingAddBackwardIter().addStrings(num1, num2)

    # Output: 10110.
    num1 = '9999'
    num2 = '111'
    print SolutionPaddingAddBackwardIter().addStrings(num1, num2)


if __name__ == '__main__':
    main()
