"""Leetcode 202. Happy Number
Easy

URL: https://leetcode.com/problems/happy-number/

Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process:
Starting with any positive integer,
replace the number by the sum of the squares of its digits,
and repeat the process until the number equals 1 (where it will stay),
or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy numbers.

Example: 
Input: 19
Output: true
Explanation: 
1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1
"""

class SolutionSumSquaresSet(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # Use set to collect all sum of squares.
        sum_squares = set()

        while True:
            # Compute sum of squares from the reverse order.
            ss = 0
            while n:
                n, d = n // 10, n % 10
                ss += d * d

            if ss == 1:
                return True
            elif ss in sum_squares:
                # If sum of squares occurred before.
                return False
            else:
                # Add sum of squares to set and update n.
                sum_squares.add(ss)
                n = ss


def main():
    # Output: True.
    n = 19
    print SolutionSumSquaresSet().isHappy(n)

    # Output: False.
    n = 14
    print SolutionSumSquaresSet().isHappy(n)


if __name__ == '__main__':
    main()
