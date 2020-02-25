"""Leetcode 253. Meeting Rooms II (Premium)
Medium

URL: https://leetcode.com/problems/meeting-rooms-ii

Given an array of meeting time intervals consisting of start and end times
[[s1,e1],[s2,e2],...] (si < ei),
find the minimum number of conference rooms required.

Example1
Input: intervals = [[0,30],[5,10],[15,20]]
Output: 2
Explanation:
We need two meeting rooms
room1: (0,30)
room2: (5,10),(15,20)

Example2
Input: intervals = [[7, 10], [2, 4]]
Output: 1
Explanation: 
Only need one meeting room
"""

class SolutionSortEndMinHeapEnd(object):
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
        end_minheap = []
        heapq.heappush(end_minheap, intervals[0][1])

        for i in range(1, len(intervals)):
            # If next start time is after min end time, remove min end time.
            if intervals[i][0] >= end_minheap[0]:
                heapq.heappop(end_minheap)

            # Add next end time to min heap.
            heapq.heappush(end_minheap, intervals[i][1])

        return len(end_minheap)


class SolutionTimeCounterListInsort(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int

        Time complexity: O(n).
        Space complexity: O(n).
        """
        from bisect import insort

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
    print SolutionSortEndMinHeapEnd().minMeetingRooms(intervals)
    print SolutionTimeCounterListInsort().minMeetingRooms(intervals)

    # Output: 1.
    intervals = [[7, 10], [2, 4]]
    print SolutionSortEndMinHeapEnd().minMeetingRooms(intervals)
    print SolutionTimeCounterListInsort().minMeetingRooms(intervals)


if __name__ == '__main__':
    main()
