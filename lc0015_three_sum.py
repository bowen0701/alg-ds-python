"""Leetcode 15. 3Sum
Medium

URL: https://leetcode.com/problems/3sum/

Given an array nums of n integers, are there elements a, b, c in nums 
such that a + b + c = 0? Find all unique triplets in the array which gives 
the sum of zero.

Note:
The solution set must not contain duplicate triplets.

Example:
Given array nums = [-1, 0, 1, 2, -1, -4],
A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]

        Time complexity: O(n*logn + n^2) = O(n^2).
        Space complexity: O(n).
        """
        three_sum_ls = []

        # Sort the list for easily iterating to check the triplets.
        nums.sort()

        for i in range(len(nums) - 2):
            # In sorted nums, if entry i > 0, no triplets can satisfy 3 sum.
            if nums[i] > 0:
                break
            
            # Check the previous num to avoid duplicates.
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Check triplets starting from the RHS of entry i by two pointers.
            l, r = i + 1, len(nums) - 1
            while l < r:
                total = nums[i] + nums[l] + nums[r]

                if total == 0:
                    three_sum_ls.append([nums[i], nums[l], nums[r]])
                    # If left's right and right's left is the same as left and 
                    # right, respectively, increment it to avoid duplicates.
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    # Checkout another triplet by incrementing left and right.
                    l += 1
                    r -= 1
                elif total < 0:
                    # The 3 sum is too small, increase it by moving left to right. 
                    l += 1
                elif total > 0:
                    # The 3 sum is too big, decrease it by moving right to left. 
                    r -= 1

        return three_sum_ls


def main():
    nums = [-1, 0, 1, 2, -1, -4]
    # Output: [[-1, 0, 1], [-1, -1, 2]]
    print Solution().threeSum(nums)


if __name__ == '__main__':
    main()
