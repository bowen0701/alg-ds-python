"""Leetcode 435. Non-overlapping Intervals
Medium

URL: https://leetcode.com/problems/non-overlapping-intervals/

Given an array of intervals intervals where intervals[i] = [starti, endi],
return the minimum number of intervals you need to remove to make the rest
of the intervals non-overlapping.

Note that intervals which only touch at a point are non-overlapping.
For example, [1, 2] and [2, 3] are non-overlapping.

Example 1:
Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of the intervals are
non-overlapping.

Example 2:
Input: intervals = [[1,2],[1,2],[1,2]]
Output: 2

Example 3:
Input: intervals = [[1,2],[2,3]]
Output: 0

Constraints:
- 1 <= intervals.length <= 10^5
- intervals[i].length == 2
- -5 * 10^4 <= starti < endi <= 5 * 10^4
"""

from typing import List


class SolutionGreedySortByStart:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """
        Time complexity: O(n*logn).
        Space complexity: O(1).
        """
        # Sort by start time; on overlap, keep the one that ends earlier.
        intervals.sort()

        removals = 0
        prev_end = float('-inf')

        for start, end in intervals:
            if start >= prev_end:
                # No overlap: keep this interval.
                prev_end = end
            else:
                # Overlap: remove the interval with the larger end.
                removals += 1
                prev_end = min(prev_end, end)

        return removals


def main():
    # Output: 1.
    intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]
    print(SolutionGreedySortByStart().eraseOverlapIntervals(intervals))

    # Output: 2.
    intervals = [[1, 2], [1, 2], [1, 2]]
    print(SolutionGreedySortByStart().eraseOverlapIntervals(intervals))

    # Output: 0.
    intervals = [[1, 2], [2, 3]]
    print(SolutionGreedySortByStart().eraseOverlapIntervals(intervals))


if __name__ == '__main__':
    main()
