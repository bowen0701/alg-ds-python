"""Leetcode 633. Sum of Square Numbers
Easy

URL: https://leetcode.com/problems/sum-of-square-numbers/

Given a non-negative integer c, your task is to decide whether
there're two integers a and b such that a2 + b2 = c.

Example 1:
Input: 5
Output: True
Explanation: 1 * 1 + 2 * 2 = 5
 
Example 2:
Input: 3
Output: False
"""

class SolutionTwoPointers(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool

        Time complexity: O(sqrt(c)).
        Space complexity: O(1).
        """
        # Apply binary search in [0, c^0.5].
        l, r = 0, int(c ** 0.5)
        while l <= r:
            ss = l ** 2 + r ** 2
            if ss == c:
                return True
            elif ss < c:
                l += 1
            else:
                r -= 1

        return False


def main():
    # Output: True.
    c = 5
    print SolutionTwoPointers().judgeSquareSum(c)

    # Output: False.
    c = 3
    print SolutionTwoPointers().judgeSquareSum(c)    


if __name__ == '__main__':
    main()
