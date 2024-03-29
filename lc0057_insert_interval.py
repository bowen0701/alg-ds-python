"""Leetcode 57. Insert Interval
Medium

URL: https://leetcode.com/problems/insert-interval/

You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] 
represent the start and the end of the ith interval and intervals is sorted in ascending order by 
starti. You are also given an interval newInterval = [start, end] that represents the start and 
end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti
and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

Example 1:
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]

Example 2:
Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

Example 3:
Input: intervals = [], newInterval = [5,7]
Output: [[5,7]]

Example 4:
Input: intervals = [[1,5]], newInterval = [2,3]
Output: [[1,5]]

Example 5:
Input: intervals = [[1,5]], newInterval = [2,7]
Output: [[1,7]]

Constraints:
- 0 <= intervals.length <= 104
- intervals[i].length == 2
- 0 <= starti <= endi <= 105
- intervals is sorted by starti in ascending order.
- newInterval.length == 2
- 0 <= start <= end <= 105
"""

from typing import List


class SolutionIter(object):
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        Time complexity: O(n).
        Space complexity: O(n).
        """
        if not intervals:
            return [newInterval]

        is_inserted = False
        result = []

        for interval in intervals:
            # If overlapped with current internal, update new's start and end.
            if newInterval[0] <= interval[1] and newInterval[1] >= interval[0]:
                newInterval[0] = min(newInterval[0], interval[0])
                newInterval[1] = max(newInterval[1], interval[1])
            else:
                # If not, check if new interval is ahead of current, append the former.
                if not is_inserted and newInterval[0] < interval[0]: 
                    result.append(newInterval)
                    is_inserted = True

                # If not both, append current interval.
                result.append(interval)

        # If new interval is not inserted yet, append it to the tail.
        if not is_inserted:
            result.append(newInterval)

        return result


def main():
    # Output: [[1,5],[6,9]]
    intervals = [[1,3],[6,9]]
    newInterval = [2,5]
    print(SolutionIter().insert(intervals, newInterval))

    # Output: [[1,2],[3,10],[12,16]]
    intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
    newInterval = [4,8]
    print(SolutionIter().insert(intervals, newInterval))

    # Output: [[1,5]]
    intervals = [[1,5]]
    newInterval = [2,3]
    print(SolutionIter().insert(intervals, newInterval))


if __name__ == '__main__':
    main()
