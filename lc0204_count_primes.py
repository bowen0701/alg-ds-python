"""Leetcode 204. Count Primes
Easy

URL: https://leetcode.com/problems/count-primes/

Count the number of prime numbers less than a non-negative number, n.

Example:

Input: 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
"""

class SolutionSqrt(object):
    def _is_prime(self, i):
        if i <= 1:
            return False

        # Only check sqrt(i) for prime, since i = p*q <= p^2 for small p.
        for p in range(2, int(i ** 0.5) + 1):
            if i % p == 0:
                return False
        return True

    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int

        Time complexity: O(n^1.5).
        Space complexity: O(1).
        """
        count = 0
        for i in range(n):
            if self._is_prime(i):
                count += 1
        return count


def main():
    n = 10
    print SolutionSqrt().countPrimes(n)


if __name__ == '__main__':
    main()
