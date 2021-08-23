"""Leetcode 56. Merge Intervals
Medium

URL: https://leetcode.com/problems/merge-intervals/

Given a collection of intervals, merge all overlapping intervals.

Example 1:
Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

Example 2:
Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
"""

from typing import List


class SolutionSortAppendOrMerge(object):
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        Time complexity: O(n*logn).
        Space complexity: O(1).
        """
        if not intervals:
            return []

        # Sort by interval's start.
        intervals = sorted(intervals)

        result = [intervals[0]]
        
        for i in range(1, len(intervals)):
            if intervals[i][0] > result[-1][1]:
                # Append non-overlapping interval.
                result.append(intervals[i])
            else:
                # Merge overlapped interval.
                result[-1][1] = max(intervals[i][1], result[-1][1])

        return result


def main():
    import time

    print('By appending interval or updating end:')
    start_time = time.time()

    # Ans: [[1,6],[8,10],[15,18]]
    intervals = [[1,3], [2,6], [8,10], [15,18]]
    print(SolutionSortAppendOrMerge().merge(intervals))

    # Ans: [[1,5]]
    intervals = [[1,4], [4,5]]
    print(SolutionSortAppendOrMerge().merge(intervals))

    # Ans: [[0,4]]
    intervals = [[1,4], [0,4]]
    print(SolutionSortAppendOrMerge().merge(intervals))

    # Ans: [[0,5]]
    intervals = [[1,4], [0,5]]
    print(SolutionSortAppendOrMerge().merge(intervals))

    # Ans: [[1,10]]
    intervals = [[2,3], [4,5], [6,7], [8,9], [1,10]]
    print(SolutionSortAppendOrMerge().merge(intervals))

    print('Time: {}'.format(time.time() - start_time))


if __name__ == '__main__':
    main()
