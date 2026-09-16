"""Leetcode 875. Koko Eating Bananas
Medium

URL: https://leetcode.com/problems/koko-eating-bananas/

Koko loves to eat bananas. There are n piles of bananas, the ith pile
has piles[i] bananas. The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she
chooses some pile of bananas and eats k bananas from that pile. If the
pile has less than k bananas, she eats all of them instead and will not
eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the
bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas
within h hours.

Example 1:
Input: piles = [3,6,7,11], h = 8
Output: 4
Explanation: At k=4, hours = ceil(3/4)+ceil(6/4)+ceil(7/4)+ceil(11/4)
= 1+2+2+3 = 8 <= 8. k=3 would need 1+2+3+4 = 10 > 8.

Example 2:
Input: piles = [30,11,23,4,20], h = 5
Output: 30
Explanation: h == len(piles), so Koko has exactly 1 hour per pile.
k must be >= max(piles) = 30.

Example 3:
Input: piles = [30,11,23,4,20], h = 6
Output: 23
Explanation: At k=23, hours = 2+1+1+1+1 = 6 <= 6.

Constraints:
- 1 <= piles.length <= 10^4
- piles.length <= h <= 10^9
- 1 <= piles[i] <= 10^9
"""

from typing import List
import math


class SolutionBinarySearch:
    def _hours_needed(self, piles: List[int], k: int) -> int:
        """Calculate total hours to eat all piles at speed k."""
        return sum(math.ceil(p / k) for p in piles)

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        Time complexity: O(n * log(max(piles))).
        Space complexity: O(1).
        """
        # right = max(piles): faster speeds waste capacity.
        left, right = 1, max(piles)

        while left < right:
            mid = left + (right - left) // 2

            if self._hours_needed(piles, mid) <= h:
                right = mid
            else:
                left = mid + 1

        return left


def main():
    # Output: 4.
    piles = [3, 6, 7, 11]
    h = 8
    print(SolutionBinarySearch().minEatingSpeed(piles, h))

    # Output: 30.
    piles = [30, 11, 23, 4, 20]
    h = 5
    print(SolutionBinarySearch().minEatingSpeed(piles, h))

    # Output: 23.
    piles = [30, 11, 23, 4, 20]
    h = 6
    print(SolutionBinarySearch().minEatingSpeed(piles, h))


if __name__ == '__main__':
    main()
