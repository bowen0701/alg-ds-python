"""Leetcode 41. First Missing Positive
Hard

URL: https://leetcode.com/problems/first-missing-positive/

Given an unsorted integer array, find the smallest missing positive integer.

Example 1:
Input: [1,2,0]
Output: 3

Example 2:
Input: [3,4,-1,1]
Output: 2

Example 3:
Input: [7,8,9,11,12]
Output: 1

Note:
Your algorithm should run in O(n) time and uses constant extra space.
"""

class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)

        for i in range(n):
            # Keep swapping old & new nums[i] to their correct positions.
            while nums[i] > 0 and nums[i] <= n and nums[i] != nums[nums[i] - 1]:
                # If nums[i] = k, swap it and nums[k - 1], with correct position k - 1.
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]

        # Check each updated elements in nums with true positive integer.
        for i in range(n):
            if i + 1 != nums[i]:
                return i + 1

        # If all elements in nums are correct, return the last one plus one.
        return n + 1


def main():
    # Ans: 3
    nums = [1,2,0]
    print Solution().firstMissingPositive(nums)

    # Ans: 2
    nums = [3,4,-1,1]
    print Solution().firstMissingPositive(nums)

    # Ans: 1
    nums = [7,8,9,11,12]
    print Solution().firstMissingPositive(nums)

    # Ans: 1
    nums = []
    print Solution().firstMissingPositive(nums)

    # Ans: 2
    nums = [1]
    print Solution().firstMissingPositive(nums)

    # Ans: 3
    nums = [-1,4,2,1,9,10]
    print Solution().firstMissingPositive(nums)


if __name__ == '__main__':
    main()
