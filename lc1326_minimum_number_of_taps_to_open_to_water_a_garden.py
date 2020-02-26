"""Leetcode 1326. Minimum Number of Taps to Open to Water a Garden
Hard

URL: https://leetcode.com/problems/minimum-number-of-taps-to-open-to-water-a-garden/

There is a one-dimensional garden on the x-axis. The garden starts at
the point 0 and ends at the point n. (i.e The length of the garden is n).

There are n + 1 taps located at points [0, 1, ..., n] in the garden.

Given an integer n and an integer array ranges of length n + 1 where
ranges[i] (0-indexed) means the i-th tap can water the area
[i - ranges[i], i + ranges[i]] if it was open.

Return the minimum number of taps that should be open to water the whole
garden, If the garden cannot be watered return -1.

Example 1:
Input: n = 5, ranges = [3,4,1,1,0,0]
Output: 1
Explanation: The tap at point 0 can cover the interval [-3,3]
The tap at point 1 can cover the interval [-3,5]
The tap at point 2 can cover the interval [1,3]
The tap at point 3 can cover the interval [2,4]
The tap at point 4 can cover the interval [4,4]
The tap at point 5 can cover the interval [5,5]
Opening Only the second tap will water the whole garden [0,5]

Example 2:
Input: n = 3, ranges = [0,0,0,0]
Output: -1
Explanation: Even if you activate all the four taps you cannot water
the whole garden.

Example 3:
Input: n = 7, ranges = [1,2,1,0,2,1,0,1]
Output: 3

Example 4:
Input: n = 8, ranges = [4,0,0,0,0,0,0,0,4]
Output: 2

Example 5:
Input: n = 8, ranges = [4,0,0,0,4,0,0,0,4]
Output: 1

Constraints:
- 1 <= n <= 10^4
- ranges.length == n + 1
- 0 <= ranges[i] <= 100
"""

class SolutionSortStartPrevEndAndEndGreedy(object):
    def minTaps(self, n, ranges):
        """
        :type n: int
        :type ranges: List[int]
        :rtype: int

        Apply the same approach for Leetcode 1024. Video Stitching.

        Time complexity: O(n*logn).
        Space complexity: O(n).
        """
        # Create intervals based on ranges.
        intervals = [[i - r, i + r] for i, r in enumerate(ranges) if r > 0]

        # Sort intervals by start.
        intervals.sort()

        # Apply greedy algorithm to check (start, end) in previous end and end.
        prev_end, end = -float('inf'), 0
        counter = 0

        for s, e in intervals:
            if end >= n or s > end:
                # If reached n already or s falls behind end.
                break
            elif prev_end < s:
                # If s falls in between prev_end and end.
                counter += 1
                prev_end = end

            # Update end by new interval.
            end = max(end, e)

        # Check if end passes n.s
        if end >= n:
            return counter
        else:
            return -1


def main():
    # Output: 1
    n = 5
    ranges = [3,4,1,1,0,0]
    print SolutionSortStartPrevEndAndEndGreedy().minTaps(n, ranges)

    # Output: -1
    n = 3
    ranges = [0,0,0,0]
    print SolutionSortStartPrevEndAndEndGreedy().minTaps(n, ranges)

    # Output: 3
    n = 7
    ranges = [1,2,1,0,2,1,0,1]
    print SolutionSortStartPrevEndAndEndGreedy().minTaps(n, ranges)

    # Output: 2
    n = 8
    ranges = [4,0,0,0,0,0,0,0,4]
    print SolutionSortStartPrevEndAndEndGreedy().minTaps(n, ranges)

    # Output: 1
    n = 8
    ranges = [4,0,0,0,4,0,0,0,4]
    print SolutionSortStartPrevEndAndEndGreedy().minTaps(n, ranges)


if __name__ == '__main__':
    main()
