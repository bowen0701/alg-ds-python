"""Leetcode 70. Climbing Stairs
Easy

URL: https://leetcode.com/problems/climbing-stairs/

You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways 
can you climb to the top?

Note: Given n will be a positive integer.

Example 1:
Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
- 1. 1 step + 1 step
- 2. 2 steps

Example 2:
Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
- 1. 1 step + 1 step + 1 step
- 2. 1 step + 2 steps
- 3. 2 steps + 1 step
"""

class SolutionIter(object):
    def climbStairs(self, n: int) -> int:
        """
        Time complexity: O(n).
        Sapce complexity: O(1).
        """
        # Exactly the same as Fibonacci numbers: F[n] = F[n-1] + F[n-2].
        # Apply bottom-up dynamic programming by iteration.  
        if n == 1 or n == 2:
            return n

        a, b = 1, 2

        for i in range(3, n + 1):
            a, b = b, a + b

        return b


def main():
    n = 2
    print(SolutionIter().climbStairs(n))

    n = 3
    print(SolutionIter().climbStairs(n))


if __name__ == '__main__':
    main()
