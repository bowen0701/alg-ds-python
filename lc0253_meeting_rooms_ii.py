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

class SolutionSortMinHeap(object):
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required

    Time complexity: O(n*logn).
    Space complexity: O(n).
    """
    def minMeetingRooms(self, intervals):
        import heapq

        if not intervals or not intervals[0]:
            return 0

        # Sort intervals by start time.
        intervals.sort()

        # Use min heap to store end times.
        endtimes_minheap = []
        heapq.heappush(endtimes_minheap, intervals[0][1])

        for i in range(1, len(intervals)):
            # If next start time is after min end time, remove min end time.
            if intervals[i][0] >= endtimes_minheap[0]:
                heapq.heappop(endtimes_minheap)

            # Add next end time to min heap.
            heapq.heappush(endtimes_minheap, intervals[i][1])

        return len(endtimes_minheap)


def main():
    # Output: 2.
    intervals = [[0,30],[5,10],[15,20]]
    print SolutionSortMinHeap().minMeetingRooms(intervals)

    # Output: 1.
    intervals = [[7, 10], [2, 4]]
    print SolutionSortMinHeap().minMeetingRooms(intervals)


if __name__ == '__main__':
    main()
