"""Leetcode 57. Insert Interval
Hard

Given a set of non-overlapping intervals, insert a new interval into the intervals
(merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

Example 1:
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]

Example 2:
Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
"""

class SolutionIter(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]

        Time complexity: O(n).
        Space complexity: O(n).
        """
        if not intervals:
            return [newInterval]

        is_inserted = False
        res_intervals = []

        for interval in intervals:
            # If overlapped with the internal, update new's start and end.
            if newInterval[0] <= interval[1] and newInterval[1] >= interval[0]:
                newInterval[0] = min(newInterval[0], interval[0])
                newInterval[1] = max(newInterval[1], interval[1])
            else:
                # If not overlapped.
                # Further, if the new is ahead of the interval, append the former.
                if not is_inserted and newInterval[0] < interval[0]: 
                    res_intervals.append(newInterval)
                    is_inserted = True

                # If not, append the interval to res.           
                res_intervals.append(interval)

        # If the new is not inserted yet, append it.
        if not is_inserted:
            res_intervals.append(newInterval)

        return res_intervals


def main():
    # Output: [[1,5],[6,9]]
    intervals = [[1,3],[6,9]]
    newInterval = [2,5]
    print SolutionIter().insert(intervals, newInterval)

    # Output: [[1,2],[3,10],[12,16]]
    intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
    newInterval = [4,8]
    print SolutionIter().insert(intervals, newInterval)

    # Output: [[1,5]]
    intervals = [[1,5]]
    newInterval = [2,3]
    print SolutionIter().insert(intervals, newInterval)


if __name__ == '__main__':
    main()
