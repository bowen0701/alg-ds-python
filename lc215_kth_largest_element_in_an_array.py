"""Leetcode 215. Kth Largest Element in an Array
Medium

URL: https://leetcode.com/problems/kth-largest-element-in-an-array/

Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example 1:
Input: [3,2,1,5,6,4] and k = 2
Output: 5

Example 2:
Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4

Note: 
You may assume k is always valid, 1 <= k <= array's length.
"""

class Solution(object):
    def quick_sort(self, nums):
        if len(nums) <= 1:
            return nums

        pivot = nums[len(nums) // 2]

        left_nums = [n for n in nums if n < pivot]
        mid_nums = [n for n in nums if n == pivot]
        right_nums = [n for n in nums if n > pivot]

        return self.quick_sort(left_nums) + mid_nums + self.quick_sort(right_nums)

    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int

        Find the Kth largest by quick sort algorithm.

        Time complexity: O(n*logn), where n is the length of nums.
        Space complexity: O(n).
        """
        sorted_nums = self.quick_sort(nums)
        return sorted_nums[-k]


def main():
    # Input: [3,2,1,5,6,4] and k = 2
    # Output: 5
    nums = [3, 2, 1, 5, 6, 4]
    k = 2
    print Solution().findKthLargest(nums, k)

    # Input: [3,2,3,1,2,4,5,5,6] and k = 4
    # Output: 4
    nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    k = 4
    print Solution().findKthLargest(nums, k)


if __name__ == '__main__':
    main()
