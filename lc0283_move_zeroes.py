"""Leetcode 283. Move Zeroes
Easy

Given an array nums, write a function to move all 0's to the right of it 
while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.
"""

class SolutionPopAppend(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.

        Time complexity: O(n).
        Space complexity: O(n).
        """
        left = 0
        right = len(nums) - 1
        while left < right:
            if nums[left] == 0:
                nums.append(nums.pop(left))
                right -= 1
            else:
                left += 1


class SolutionUpdate(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.

        Time complexity: O(n).
        Space complexity: O(1).
        """
        # Use idx to denote non-zero index.
        idx = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[idx] = nums[i]
                idx += 1

        for i in range(idx, len(nums)):
            nums[i] = 0


class SolutionTwoPointers(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.

        Time complexity: O(n).
        Space complexity: O(1).
        """
        n = len(nums)

        # Find the 1st zero.
        i = 0
        while nums[i] != 0 and i + 1 < n:
            i += 1

        # Iterate to find the 1st non-zero at the right of i, switch i & j.
        j = i + 1
        while j < n:
            while nums[j] == 0 and j + 1 < n:
                j += 1
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j += 1


def main():
    import time

    start_time = time.time()
    nums1 = [0, 1, 0, 3, 12]
    SolutionPopAppend().moveZeroes(nums1)
    print nums1
    nums2 = [0, 0, 3, 12, 1, 0, 5]
    SolutionPopAppend().moveZeroes(nums2)
    print nums2
    print 'Time for pop/append: {}'.format(time.time() - start_time)

    start_time = time.time()
    nums1 = [0, 1, 0, 3, 12]
    SolutionUpdate().moveZeroes(nums1)
    print nums1
    nums2 = [0, 0, 3, 12, 1, 0, 5]
    SolutionUpdate().moveZeroes(nums2)
    print nums2
    print 'Time for update: {}'.format(time.time() - start_time)

    start_time = time.time()
    nums1 = [0, 1, 0, 3, 12]
    SolutionTwoPointers().moveZeroes(nums1)
    print nums1
    nums2 = [0, 0, 3, 12, 1, 0, 5]
    SolutionTwoPointers().moveZeroes(nums2)
    print nums2
    print 'Time for update: {}'.format(time.time() - start_time)


if __name__ == '__main__':
    main()
