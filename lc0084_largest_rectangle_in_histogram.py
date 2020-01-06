"""Leetcode 84. Largest Rectangle in Histogram
Hard

URL: https://leetcode.com/problems/largest-rectangle-in-histogram/

Given n non-negative integers representing the histogram's bar height where the
width of each bar is 1, find the area of largest rectangle in the histogram.

Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].
The largest rectangle is shown in the shaded area, which has area = 10 unit:
5 * 2 = 10.

Example:
Input: [2,1,5,6,2,3]
Output: 10
"""

class SolutionIncreasingHeightIdxStack(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int

        Time complexity: O(n).
        Space complexity: O(n).
        """
        # Use stack to collect idx of buildings with increasing heights.
        # Boundary case handled by height = 0 & idx = -1.
        heights.append(0)
        idx_stack = [-1]

        max_area = 0

        for i in range(len(heights)):
            # Before adding a new building, pop buildings taller than the new one.
            while heights[i] < heights[idx_stack[-1]]:
                # The building popped out represents the height.
                h = heights[idx_stack.pop()]

                # Last stack top & new building are the left & right boundaries.
                w = i - idx_stack[-1] - 1

                max_area = max(max_area, h * w)

            idx_stack.append(i)

        # Recover the original heights.
        heights.append(0)

        return max_area


def main():
    # Output: 10 = 5 * 2.
    heights = [2,1,5,6,2,3]
    print heights
    print SolutionIncreasingHeightIdxStack().largestRectangleArea(heights)


if __name__ == '__main__':
    main()
