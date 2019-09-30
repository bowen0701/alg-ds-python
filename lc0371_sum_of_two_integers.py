"""Leetcode 371. Sum of Two Integers
Easy

URL: https://leetcode.com/problems/sum-of-two-integers/

Calculate the sum of two integers a and b, but you are not allowed to use
the operator + and -.

Example 1:
Input: a = 1, b = 2
Output: 3

Example 2:
Input: a = -2, b = 3
Output: 1
"""

class SolutionBit(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        # 32-bits max integer.
        MAX = 0x7FFFFFFF
        # 32-bits min interger.
        MIN = 0x80000000
        # Mask to get last 32-bits.
        MASK = 0xFFFFFFFF

        while b != 0:
            # ^ gets different bits and & gets double 1s, << moves carry.
            a, b = (a ^ b) & MASK, ((a & b) << 1) & MASK

        # If a is negative, get a's 32 bits complement positive first,
        # then get 32-bit positive's complement negative in Python.
        if a <= MAX:
            return a
        else:
            return ~(a ^ MASK)


def main():
    # Output: 3
    a = 1
    b = 2
    print SolutionBit().getSum(a, b)

    # Output: 1
    a = -2
    b = 3
    print SolutionBit().getSum(a, b)


if __name__ == '__main__':
    main()
