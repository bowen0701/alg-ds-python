"""Leetcode 581. Shortest Unsorted Continuous Subarray
Easy

URL: https://leetcode.com/problems/shortest-unsorted-continuous-subarray/

Given an integer array, you need to find one continuous subarray that if you only
sort this subarray in ascending order, then the whole array will be sorted in
ascending order, too.

You need to find the shortest such subarray and output its length.

Example 1:
Input: [2, 6, 4, 8, 10, 9, 15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the
whole array sorted in ascending order.

Note:
- Then length of the input array is in range [1, 10,000].
- The input array may contain duplicates, so ascending order here means <=.
"""

class SolutionSort(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        Sort the nums and check element match from left and from right.

        Time complexity: O(n*logn).
        Space complexity: O(n).
        """
        # Store sorted nums in a new list.
        sorted_nums = sorted(nums)

        # Iterate from left/right to check element match of nums and sorted nums.
        n = len(nums)
        i, j = 0, n - 1

        while i < n and nums[i] == sorted_nums[i]:
            i += 1

        while j > i and nums[j] == sorted_nums[j]:
            j -= 1

        return j - (i - 1)


def main():
    # Output: 5
    nums = [2, 6, 4, 8, 10, 9, 15]
    print SolutionSort().findUnsortedSubarray(nums)


if __name__ == '__main__':
    main()
