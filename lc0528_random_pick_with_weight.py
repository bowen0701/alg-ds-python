"""Leetcode 528. Random Pick with Weight
Medium

URL: https://leetcode.com/problems/random-pick-with-weight/

You are given a 0-indexed array of positive integers w where w[i]
describes the weight of the ith index.

You need to implement the function pickIndex() which randomly picks an
index in the range [0, w.length - 1] (inclusive) and returns it. The
probability of picking an index i is w[i] / sum(w).

For example, if w = [1, 3], the probability of picking index 0 is
1 / (1 + 3) = 0.25 (i.e., 25%), and the probability of picking index 1
is 3 / (1 + 3) = 0.75 (i.e., 75%).

Example 1:
Input: ["Solution","pickIndex"], [[[1]],[]]
Output: [null,0]

Example 2:
Input: ["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"],
[[[1,3]],[],[],[],[],[]]
Output: [null,1,1,1,1,0]

Constraints:
- 1 <= w.length <= 10^4
- 1 <= w[i] <= 10^5
- pickIndex will be called at most 10^4 times.
"""

from typing import List
from itertools import accumulate
import random
import bisect


class SolutionPrefixSumBisect:
    def __init__(self, w: List[int]) -> None:
        """
        Time complexity: O(n).
        Space complexity: O(n).
        """
        self.prefix = list(accumulate(w))
        self.total = self.prefix[-1]

    def pickIndex(self) -> int:
        """
        Time complexity: O(log(n)).
        Space complexity: O(1).
        """
        target = random.random() * self.total
        return bisect.bisect_right(self.prefix, target)


def main():
    # w = [1, 3]: P(0) = 0.25, P(1) = 0.75.
    sol = SolutionPrefixSumBisect([1, 3])
    results = [sol.pickIndex() for _ in range(20)]
    print(results)

    # Verify distribution.
    from collections import Counter
    counts = Counter(sol.pickIndex() for _ in range(100000))
    print({k: counts[k] for k in sorted(counts)})

    # w = [1]: P(0) = 1.0.
    sol = SolutionPrefixSumBisect([1])
    print(sol.pickIndex())


if __name__ == '__main__':
    main()
