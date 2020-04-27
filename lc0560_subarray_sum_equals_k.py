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

class SolutionBruteForce(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int

        Time complexity: O(n^3).
        Space complexity: O(n).
        """
        result = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if sum(nums[i:(j + 1)]) == k:
                    result += 1
        return result


class SolutionCusumCountDict(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int

        Time complexity: O(n).
        Space complexity: O(n).
        """
        from collections import defaultdict

        # Create a dict: cusum->count.
        cusum_count_d = defaultdict(int)
        result = 0
        cusum = 0
        
        for num in nums:
            # Compute cumulative sum.
            cusum += num

            # If cusum equals k, then increment result by 1.
            if cusum == k:
                result += 1

            # If cusum - k exists in cusum counts,
            # the subarray from (cusum - k) to "current" cusum equals k.
            if cusum - k in cusum_count_d:
                result += cusum_count_d[cusum - k]

            # Save cusum to cusum counts.
            cusum_count_d[cusum] += 1

        return result
        

def main():
    import time

    # Output: 2
    nums = [1, 1, 1]
    k = 2

    start_time = time.time()
    print 'Brute force: {}'.format(SolutionBruteForce().subarraySum(nums, k))
    print 'Time: {}'.format(time.time() - start_time)

    start_time = time.time()
    print 'Cusum count dict: {}'.format(SolutionCusumCountDict().subarraySum(nums, k))
    print 'Time: {}'.format(time.time() - start_time)

    # Output: 3
    nums =  [10, 2, -2, -20, 10]
    k = -10

    start_time = time.time()
    print 'Brute force: {}'.format(SolutionBruteForce().subarraySum(nums, k))
    print 'Time: {}'.format(time.time() - start_time)

    start_time = time.time()
    print 'Cusum count dict: {}'.format(SolutionCusumCountDict().subarraySum(nums, k))
    print 'Time: {}'.format(time.time() - start_time)

    # Output: 0
    nums = [1]
    k = 0

    start_time = time.time()
    print 'Brute force: {}'.format(SolutionBruteForce().subarraySum(nums, k))
    print 'Time: {}'.format(time.time() - start_time)

    start_time = time.time()
    print 'Cusum count dict: {}'.format(SolutionCusumCountDict().subarraySum(nums, k))
    print 'Time: {}'.format(time.time() - start_time)


if __name__ == '__main__':
    main()
