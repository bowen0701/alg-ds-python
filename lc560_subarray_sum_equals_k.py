"""560. Subarray Sum Equals K
Medium

Given an array of integers and an integer k, you need to find the total 
number of continuous subarrays whose sum equals to k.

Example 1:
Input: nums = [1,1,1], k = 2
Output: 2

Note:
The length of the array is in range [1, 20,000].
The range of numbers in the array is [-1000, 1000] and the range of the 
integer k is [-1e7, 1e7].
"""

class SolutionNaive(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int

        Time complexity: O(n^3).
        Space complexity: O(n).
        """
        count = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if sum(nums[i:(j + 1)]) == k:
                    count += 1
        return count


def main():
    import time

    nums = [1, 1, 1]
    k = 2

    print SolutionNaive().subarraySum(nums, k)


    nums =  [10, 2, -2, -20, 10]   
    k = -10 
    print SolutionNaive().subarraySum(nums, k)


if __name__ == '__main__':
    main()
