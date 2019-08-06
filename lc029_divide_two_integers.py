"""Leetcodee 29. Divide Two Integers
Medium

URL: https://leetcode.com/problems/divide-two-integers/

Given two integers dividend and divisor, divide two integers without using 
multiplication, division and mod operator.

Return the quotient after dividing dividend by divisor.

The integer division should truncate toward zero.

Example 1:
Input: dividend = 10, divisor = 3
Output: 3

Example 2:
Input: dividend = 7, divisor = -3
Output: -2

Note:
Both dividend and divisor will be 32-bit signed integers.
The divisor will never be 0.
Assume we are dealing with an environment which could only store integers within
the 32-bit signed integer range: [-2^31,  2^31 - 1]. 
For the purpose of this problem, assume that your function returns 2^31 - 1 
when the division result overflows.
"""

class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int

        Time complexity: O((log(dividend))^2).
        Space complexity: O(1).
        """
        if dividend == 0:
            return 0

        # Return 2**31 - 1 when overflow.
        if dividend == -(2**31) and divisor == -1:
            return 2**31 - 1

        quotient = 0
        sign = 1

        # Decide the quotient sign.
        if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
            sign = -1
        
        abs_dividend, abs_divisor = abs(dividend), abs(divisor)

        # In each iteration, we substract divisor from dividend.
        while abs_dividend >= abs_divisor:
            # To speed up iterations, in each iteration we double the divisor.
            # Until the updated divisor is too big, we go back to the original.
            abs_divisor_tmp, quotient_tmp = abs_divisor, 1

            while abs_dividend >= abs_divisor_tmp:
                abs_dividend -= abs_divisor_tmp
                quotient += quotient_tmp

                abs_divisor_tmp += abs_divisor_tmp
                quotient_tmp += quotient_tmp

        if sign > 0:
            return quotient
        else:
            return -quotient


def main():
    # Ans: 3
    dividend = 10
    divisor = 3
    print Solution().divide(dividend, divisor)

    # Ans: -2
    dividend = 7
    divisor = -3
    print Solution().divide(dividend, divisor)


if __name__ == '__main__':
    main()
