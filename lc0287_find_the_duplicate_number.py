"""Leetcode 287. Find the Duplicate Number
Medium

URL: https://leetcode.com/problems/find-the-duplicate-number/

Given an array nums containing n + 1 integers where 
each integer is between 1 and n (inclusive), 
prove that at least one duplicate number must exist. 
Assume that there is only one duplicate number, find the duplicate one.

Example 1:
Input: [1,3,4,2,2]
Output: 2

Example 2:
Input: [3,1,3,4,2]
Output: 3

Note:
- You must not modify the array (assume the array is read only).
- You must use only constant, O(1) extra space.
- Your runtime complexity should be less than O(n2).
- There is only one duplicate number in the array, but it could be 
  repeated more than once.
"""

class SolutionNaive(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        Note: Time Limit Exceeded.

        Time complexity: O(n^2).
        Space complexity: O(1).
        """
        # For each number, iterate through the following numbers.
        n = len(nums)
        for i in range(n - 1):
            for j in range(i + 1, n):
                if nums[i] == nums[j]:
                    return nums[j]


class SolutionDict(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        Time complexity: O(n).
        Space complexity: O(n).
        """
        # Iterate through each numbers, if the number is visited left time, 
        # store it in set; if not, get duplicate numbder.
        num_set = set()
        for n in nums:
            if n not in num_set:
                num_set.add(n)
            else:
                return n


class SolutionBinarySearch(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        Time complexity: O(n*logn).
        Space complexity: O(1).
        """
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = left + (right - left) // 2

            # Count how many numbers fall in the 2nd half.
            n_nums_second_half = 0
            for n in nums:
                if mid < n <= right:
                    n_nums_second_half += 1

            # Check if n_nums_second_half is larger than the capacity, right - mid,
            # update left or right correspondingly.
            if n_nums_second_half > right - mid:
                left = mid + 1
            else:
                right = mid

        return left


def main():
    import time

    # Should be 2.
    nums = [1, 3, 4, 2, 2]

    start_time = time.time()
    print 'By naive: {}'.format(SolutionNaive().findDuplicate(nums))
    print 'Time: {}'.format(time.time() - start_time)

    start_time = time.time()
    print 'By dict: {}'.format(SolutionDict().findDuplicate(nums))
    print 'Time: {}'.format(time.time() - start_time)

    start_time = time.time()
    print 'By binary search: {}'.format(SolutionBinarySearch().findDuplicate(nums))
    print 'Time: {}'.format(time.time() - start_time)

    # Should be 3.
    nums = [3, 1, 3, 4, 2]

    start_time = time.time()
    print 'By naive: {}'.format(SolutionNaive().findDuplicate(nums))
    print 'Time: {}'.format(time.time() - start_time)

    start_time = time.time()
    print 'By dict: {}'.format(SolutionDict().findDuplicate(nums))
    print 'Time: {}'.format(time.time() - start_time)

    start_time = time.time()
    print 'By binary search: {}'.format(SolutionBinarySearch().findDuplicate(nums))
    print 'Time: {}'.format(time.time() - start_time)


if __name__ == '__main__':
    main()
