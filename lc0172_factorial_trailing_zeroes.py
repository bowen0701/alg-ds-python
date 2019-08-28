"""Leetcode 172. Factorial Trailing Zeroes
Easy

URL: https://leetcode.com/problems/factorial-trailing-zeroes/

Given an integer n, return the number of trailing zeroes in n!.

Example 1:
Input: 3
Output: 0
Explanation: 3! = 6, no trailing zero.

Example 2:
Input: 5
Output: 1
Explanation: 5! = 120, one trailing zero.

Note: Your solution should be in logarithmic time complexity.
"""

class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int

        Time complexity: O(log_5 n).
        Space complexity: O(1).
        """
        zeros = 0
        temp = n

        while temp // 5 > 0:
            temp = temp // 5
            zeros += temp

        return zeros


def main():
    # Ans: 0
    n = 3
    print Solution().trailingZeroes(n)

    # Ans: 1
    n = 5
    print Solution().trailingZeroes(n)



if __name__ == '__main__':
    main()
