"""Leetcode 11. Container With Most Water
Medium

Given n non-negative integers a1, a2, ..., an , where each represents a 
point at coordinate (i, ai). n vertical lines are drawn such that the two 
endpoints of line i is at (i, ai) and (i, 0). Find two lines, 
which together with x-axis forms a container, such that the container 
contains the most water.

Note: You may not slant the container and n is at least 2.

Example:
Input: [1,8,6,2,5,4,8,3,7]
Output: 49
"""

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int

        Two pointer method:
        - Start from the widest container, its area = shorter height * wide.
        - Since all of the remaining containers are less wide, 
          to get bigger area, they must be higher. 
          Thus skip those containers which are not higher.

        Time complexity: O(n).
        Space complexity: O(1).
        """
        max_area = 0
        l, r = 0, len(height) - 1

        while l < r:
            hl, hr = height[l], height[r]
            hm = min(hl, hr)

            max_area = max(max_area, (r - l) * hm)

            while height[l] <= hm and l < r:
                l += 1
            while height[r] <= hm and l < r:
                r -= 1

        return max_area


def main():
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    # Ans: 49 = (8 - 1) * 7
    print Solution().maxArea(height)


if __name__ == '__main__':
    main()
