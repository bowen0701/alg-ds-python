"""Leetcode 611. Valid Triangle Number
Medium

URL: https://leetcode.com/problems/valid-triangle-number/

Given an array consists of non-negative integers, 
your task is to count the number of triplets chosen from the array that can
make triangles if we take them as side lengths of a triangle.

Example 1:
Input: [2,2,3,4]
Output: 3
Explanation:
Valid combinations are: 
2,3,4 (using the first 2)
2,3,4 (using the second 2)
2,2,3

Note:
- The length of the given array won't exceed 1000.
- The integers in the given array are in the range of [0, 1000].
"""

class SolutionThreePointers(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Apply three pointer method.
        n = len(nums)

        # First sort nums in increasing order.
        nums.sort()

        n_triplets = 0

        for i in range(n - 1, 1, -1):
            # For each i, it suffices to apply two pointer method on the left of i.
            # Since if num l + r > i, triangle number condition is satisfied.
            l, r = 0, i - 1
            while l < r:
                if nums[l] + nums[r] > nums[i]:
                    n_triplets += r - l
                    r -= 1
                else:
                    l += 1

        return n_triplets


def main():
    import time

    nums = [2,2,3,4]
    print SolutionThreePointers().triangleNumber(nums)


if __name__ == '__main__':
    main()
