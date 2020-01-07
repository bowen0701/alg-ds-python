"""Leetcode 85. Maximal Rectangle
Hard

URL: https://leetcode.com/problems/maximal-rectangle/

Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle
containing only 1's and return its area.

Example:
Input:
[
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
Output: 6
"""

class SolutionEachRowHeightRectangleHistogram(object):
    def maximalRectangle(self, matrix):
        """
        View each row as ground with buildings of consecutive 1s on it. 
        Then apply solution for "Largest Rectangle in Histogram":
        - Build each row's heights with consecutive 1s above, with boundary handling.
        - Use stack to collect idx of increasing heights.
        - When visit smaller height than top of stack, pop heights from stack
          until fulfill increasing heights.

        :type matrix: List[List[str]]
        :rtype: int

        Time complexity: O(n), where n is the number of columns.
        Space complexity: O(n).
        """
        # Edge cases.
        if not matrix or not matrix[0]:
            return 0

        n_cols = len(matrix[0])

        # Height's boundary case handled by height = 0.
        heights = [0] * (n_cols + 1)

        max_area = 0

        for row in matrix:
            # First build each row's heights with consecutive 1s above.
            for i in range(n_cols):
                if row[i] == '1':
                    heights[i] += 1
                else:
                    # Start over heights if there is a disconnection.
                    heights[i] = 0

            # Use stack to collect idx of increasing heights with boundary idx -1.
            idx_stack = [-1]

            for i in range(n_cols + 1):
                # Before appending a new building, pop buildings taller than it.
                while heights[i] < heights[idx_stack[-1]]:
                    # The building popped out represents the height.
                    h = heights[idx_stack.pop()]

                    # Last stack top & new buildings are the left & right boundaries.
                    w = i - idx_stack[-1] - 1

                    max_area = max(max_area, h * w)

                idx_stack.append(i)

        return max_area


def main():
    # Output: 6
    matrix = [
        ["1","0","1","0","0"],
        ["1","0","1","1","1"],
        ["1","1","1","1","1"],
        ["1","0","0","1","0"]
    ]
    print SolutionEachRowHeightRectangleHistogram().maximalRectangle(matrix)


if __name__ == '__main__':
    main()
