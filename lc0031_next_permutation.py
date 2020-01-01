"""Leetcode 31. Next Permutation
Medium

URL: https://leetcode.com/problems/next-permutation/

Implement next permutation, which rearranges numbers into the lexicographically
next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible
order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.
Here are some examples. Inputs are in the left-hand column and its corresponding
outputs are in the right-hand column.
1,2,3 -> 1,3,2
3,2,1 -> 1,2,3
1,1,5 -> 1,5,1
"""

class SolutionDecreasingPivotSwapReverse(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.

        Time complexity: O(n).
        Space complexity: O(1).
        """
        # From backward find the first pos (pivot) which is not in decreasing order.
        i = len(nums) - 1
        while i > 0 and nums[i - 1] >= nums[i]:
            i -= 1

        pivot = i - 1

        # If we cannot find that number, all numbers are increasing. Reverse them.
        if pivot == -1:
            nums.reverse()
            return None

        # Find the first pos j with num which is bigger than pivot number. Swap them.
        j = len(nums) - 1
        while j > pivot and nums[j] <= nums[pivot]:
            j -= 1

        nums[pivot], nums[j] = nums[j], nums[pivot]

        # Reverse the remaining numbers on the right of pivot.
        left, right = pivot + 1, len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]

            left += 1
            right -= 1


def main():
    # 1,2,3 -> 1,3,2
    nums = [1,2,3]
    SolutionDecreasingPivotSwapReverse().nextPermutation(nums)
    print nums

    # 3,2,1 -> 1,2,3
    nums = [3,2,1]
    SolutionDecreasingPivotSwapReverse().nextPermutation(nums)
    print nums

    # 1,1,5 -> 1,5,1
    nums = [1,1,5]
    SolutionDecreasingPivotSwapReverse().nextPermutation(nums)
    print nums


if __name__ == '__main__':
    main()
