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
    def _compute_sum_squares(self, n: int) -> int:
        ss = 0
        while n > 0:
            n, digit = n // 10, n % 10
            ss += digit * digit
        return ss

    def isHappy(self, n: int) -> bool:
        # Use set to store visited numbers.
        visited = set()
        
        # Loop to compute sum of squares and add it to visited set.
        while n != 1:
            n = self._compute_sum_squares(n)
            
            if n in visited:
                return False
            visited.add(n)
            
        return True


def main():
    # Output: True.
    n = 19
    print SolutionSumSquaresSet().isHappy(n)

    # Output: False.
    n = 14
    print SolutionSumSquaresSet().isHappy(n)


if __name__ == '__main__':
    main()
