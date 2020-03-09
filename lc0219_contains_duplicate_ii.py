"""Leetcode 219. Contains Duplicate II
Easy

URL: https://leetcode.com/problems/contains-duplicate-ii/

Given an array of integers and an integer k,
find out whether there are two distinct indices i and j in the array such that
nums[i] = nums[j] and the absolute difference between i and j is at most k.

Example 1:
Input: nums = [1,2,3,1], k = 3
Output: true

Example 2:
Input: nums = [1,0,1,1], k = 1
Output: true

Example 3:
Input: nums = [1,2,3,1,2,3], k = 2
Output: false
"""

class SolutionNumIdxDict(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool

        Time complexity: O(n).
        Space complexity: O(n).
        """
        # Create a dict to collect number and their indices.
        num_idx_d = dict()

        for i, num in enumerate(nums):
            if num in num_idx_d and i - num_idx_d[num] <= k:
                return True
            else:
                num_idx_d[num] = i

        return False


def main():
    # Output: True
    nums = [1,2,3,1]
    k = 3
    print SolutionNumIdxDict().containsNearbyDuplicate(nums, k)

    # Output: True
    nums = [1,0,1,1]
    k = 1
    print SolutionNumIdxDict().containsNearbyDuplicate(nums, k)

    # Output: False
    nums = [1,2,3,1,2,3]
    k = 2
    print SolutionNumIdxDict().containsNearbyDuplicate(nums, k)


if __name__ == '__main__':
    main()
