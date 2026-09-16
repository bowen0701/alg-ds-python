"""Leetcode 253. Meeting Rooms II (Premium)
Medium

URL: https://leetcode.com/problems/meeting-rooms-ii/

Given an array of meeting time intervals intervals where
intervals[i] = [starti, endi], return the minimum number of conference
rooms required.

Example 1:
Input: intervals = [[0,30],[5,10],[15,20]]
Output: 2

Example 2:
Input: intervals = [[7,10],[2,4]]
Output: 1

Constraints:
- 1 <= intervals.length <= 10^4
- 0 <= starti < endi <= 10^6
"""

class SolutionSortStartMinHeapEnd:
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int

        Time complexity: O(n*logn).
        Space complexity: O(n).
        """
        import heapq

        if not intervals or not intervals[0]:
            return 0

        # Sort intervals by start time.
        intervals.sort()

        # Use min heap to store end times.
        end_hq = []
        heapq.heappush(end_hq, intervals[0][1])

        for i in range(1, len(intervals)):
            # If next start time is after min end time, remove min end time.
            if intervals[i][0] >= end_hq[0]:
                heapq.heappop(end_hq)

            # Add next end time to min heap.
            heapq.heappush(end_hq, intervals[i][1])

        return len(end_hq)


class SolutionTimeCountersInsort:
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int

        Time complexity: O(n).
        Space complexity: O(n).
        """
        from bisect import insort

        # Sort times and add increment/decrement counters by start/end.
        time_counters = []
        for i in range(len(intervals)):
            insort(time_counters, (intervals[i][0], 1))
            insort(time_counters, (intervals[i][1], -1))

        cur_n, max_n = 0, 0
        for t, counter in time_counters:
            cur_n += counter
            max_n = max(max_n, cur_n)

        return max_n


def main():
    # Output: 2.
    intervals = [[0,30],[5,10],[15,20]]
    print(SolutionSortStartMinHeapEnd().minMeetingRooms(intervals))
    print(SolutionTimeCountersInsort().minMeetingRooms(intervals))

    # Output: 1.
    intervals = [[7, 10], [2, 4]]
    print(SolutionSortStartMinHeapEnd().minMeetingRooms(intervals))
    print(SolutionTimeCountersInsort().minMeetingRooms(intervals))


if __name__ == '__main__':
    main()
