"""Leetcode 252. Meeting Rooms (Premium)
Easy

URL: https://leetcode.com/problems/meeting-rooms

Given an array of meeting time intervals consisting of start and end times
[[s1,e1],[s2,e2],...] (si < ei), determine if a person could attend all meetings.

Example 1:
Input: [[0,30],[5,10],[15,20]]
Output: false

Example 2:
Input: [[7,10],[2,4]]
Output: true
"""

class SolutionSortStart(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: bool
        """
        intervals.sort(key=lambda x: x[0])

        for i in range(len(intervals) - 1):
            if intervals[i][1] > intervals[i + 1][0]:
                return False

        return True


def main():
    # Output: False
    intervals = [[0,30],[5,10],[15,20]]
    print SolutionSortStart().canAttendMeetings(intervals)

    # Output: True
    intervals = [[7,10],[2,4]]
    print SolutionSortStart().canAttendMeetings(intervals)


if __name__ == '__main__':
    main()
