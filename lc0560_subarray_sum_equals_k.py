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
        n_subarrs = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if sum(nums[i:(j + 1)]) == k:
                    n_subarrs += 1
        return n_subarrs


class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int

        Time complexity: O(n).
        Space complexity: O(n).
        """
        n_subarrs = 0
        sums_d = {}
        cusum = 0
        
        for n in nums:
            # Compute cumulative sum.
            cusum += n

            # If cusum equals k, then increment 1.
            if cusum == k:
                n_subarrs += 1

            # If cusum - k exists in sums_d, it means the subarray
            # from index of (cusum - k) to "current" index equals k.
            if cusum - k in sums_d:
                n_subarrs += sums_d[cusum - k]

            # Save cusum to sum dict.
            if cusum in sums_d:
                sums_d[cusum] += 1
            else:
                sums_d[cusum] = 1

        return n_subarrs
        

def main():
    import time

    # Ans: 2
    nums = [1, 1, 1]
    k = 2

    start_time = time.time()
    print 'Naive: {}'.format(SolutionNaive().subarraySum(nums, k))
    print 'Time: {}'.format(time.time() - start_time)

    start_time = time.time()
    print 'Dict: {}'.format(Solution().subarraySum(nums, k))
    print 'Time: {}'.format(time.time() - start_time)

    # Ans: 3
    nums =  [10, 2, -2, -20, 10]
    k = -10

    start_time = time.time()
    print 'Naive: {}'.format(SolutionNaive().subarraySum(nums, k))
    print 'Time: {}'.format(time.time() - start_time)

    start_time = time.time()
    print 'Dict: {}'.format(Solution().subarraySum(nums, k))
    print 'Time: {}'.format(time.time() - start_time)

    # Ans: 0
    nums = [1]
    k = 0

    start_time = time.time()
    print 'Naive: {}'.format(SolutionNaive().subarraySum(nums, k))
    print 'Time: {}'.format(time.time() - start_time)

    start_time = time.time()
    print 'Dict: {}'.format(Solution().subarraySum(nums, k))
    print 'Time: {}'.format(time.time() - start_time)


if __name__ == '__main__':
    main()
