"""Leetcode 681. Next Closest Time (Premium)
Medium

URL: https://leetcode.com/problems/next-closest-time

Given a time represented in the format "HH:MM", form the next closest time by
reusing the current digits. There is no limit on how many times a digit can be
reused.

You may assume the given input string is always valid. For example, "01:34",
"12:09" are valid. "1:34", "12:9" are invalid.

Example 1:
Input: "19:34"
Output: "19:39"
Explanation:
The next closest time choosing from digits 1, 9, 3, 4, is 19:39, which occurs
5 minutes later.  
It is not 19:33, because this occurs 23 hours and 59 minutes later.

Example 2:
Input: "23:59"
Output: "22:22"
Explanation: It may be assumed that the returned time is next day's time since
it is smaller than the input time numerically.
"""

class Solution:
    def nextClosestTime(self, time):
        """
        @param time: the given time
        @return: the next closest time
        """
        pass


def main():
    pass


if __name__ == '__main__':
    main()
