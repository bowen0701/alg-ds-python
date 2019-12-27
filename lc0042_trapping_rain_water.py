"""Leetcode 42. Trapping Rain Water
Hard

URL: https://leetcode.com/problems/trapping-rain-water/

Given n non-negative integers representing an elevation map where the width of each
bar is 1, compute how much water it is able to trap after raining.


The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. 
In this case, 6 units of rain water (blue section) are being trapped. 

Example:
Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
"""

class SolutionTwoPointersLeftmaxRightmaxHeights(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int

        Time complexity: O(n).
        Space complexity: O(1).
        """
        # Apply two pointers from both sides with leftmax & rightmax heights.

        n = len(height)

        # Edge cases.
        if not height or n < 3:
            return 0

        # Start checking max left & right heights to check walls from both sides.
        h_leftmax, h_rightmax = height[0], height[n - 1]

        # Start moving two pointers from 2nd last pos from both sides.
        left, right = 1, n - 2
        water = 0

        # Iteratively move two pointers until they meet with each other.
        while left <= right:
            # Move the lower wall since the taller one may leak water.
            if h_leftmax <= h_rightmax:
                h_leftmax = max(h_leftmax, height[left])
                water += h_leftmax - height[left]
                left += 1
            else:
                h_rightmax = max(h_rightmax, height[right])
                water += h_rightmax - height[right]
                right -= 1

        return water


def main():
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    print SolutionTwoPointersLeftmaxRightmaxHeights().trap(height)


if __name__ == '__main__':
    main()
