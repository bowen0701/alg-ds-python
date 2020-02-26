"""LC300. Longest Increasing Subsequence
Medium

URL: https://leetcode.com/problems/longest-increasing-subsequence/

Given an unsorted array of integers, 
find the length of longest increasing subsequence.

Example:
Input: [10,9,2,5,3,7,101,18]
Output: 4 
Explanation: The longest increasing subsequence is [2,3,7,101], 
therefore the length is 4. 

Note:
There may be more than one LIS combination, 
it is only necessary for you to return the length.
Your algorithm should run in O(n^2) complexity.
Follow up: Could you improve it to O(n*logn) time complexity?
"""


class SolutionRecur(object):
    def _LIS(self, nums, cur_max, start, end):
        # Base case.
        if start > end:
            return 0

        # LIS of nums[1:n], excluding nums[0].
        lis_ex = self._LIS(nums, cur_max, start + 1, end)

        # LIS is 1 + a LIS of nums[1:n], including nums[0],
        # if nums[0] is bigger than the current max.
        if nums[start] > cur_max:
            lis_in = 1 + self._LIS(nums, nums[start], start + 1, end)
        else:
            lis_in = -float('inf')

        return max(lis_ex, lis_in)

    def lengthOfLIS(self, nums):
        """Length of LIS by recursion.

        Time complexity: O(2^n).
        Space complexity: O(1).
        """
        # Apply top-down recursion with two pointers, starting from the two sides.
        start, end = 0, len(nums) - 1
        cur_max = -float('inf')
        return self._LIS(nums, cur_max, start, end)


class SolutionDp(object):
    def lengthOfLIS(self, nums):
        """Length of LIS by dynamic programming.
        :type nums: List[int]
        :rtype: int

        Time complexity: O(n^2), where n is the length of the nums.
        Space complexity: O(n).
        """
        # Apply bottom-up DP.
        if not nums:
            return 0

        # Create a table T with each T[i] denoting LIS up to i.
        # Init all elements to 1, since LIS of each num is at least 1.
        T = [1] * len(nums)

        # Apply two pointer method: for each j, check all i < j; 
        # if num i is smaller than num j, set T[j] = max(T[j], T[i] + 1).
        for j in range(1, len(nums)):
            for i in range(j):
                if nums[i] < nums[j]:
                    T[j] = max(T[j], T[i] + 1)

        # Return max elements of table as LIS. 
        return max(T)


class SolutionBinarySearch(object):
    def lengthOfLIS(self, nums):
        """Length of LIS by binary search.
        :type nums: List[int]
        :rtype: int

        Time complexity: O(n*logn), where n is the length of the nums.
        Space complexity: O(n).
        """
        # Apply binary search with memoization.
        if not nums:
            return 0

        # tails stores the smallest tail of all increasing subsequences
        # with length i+1 in tails[i].
        tails = [0] * len(nums)
        lis = 0
 
        # If n is larger than all tails, append it and increase the size by 1.
        # Further, if tails[i-1] < n <= tails[i], update tails[i].
        for n in nums:
            # Use binary search to find the correct tail for new item.
            left, right = 0, lis
            while left < right:
                mid = left + (right - left) // 2
                if tails[mid] < n:
                    left = mid + 1
                else:
                    right = mid

            tails[left] = n
            lis = max(left + 1, lis)

        return lis


def main():
    import time

    # Output: 4.
    nums = [10, 9, 2, 5, 3, 7, 101, 18]

    start_time = time.time()
    print SolutionRecur().lengthOfLIS(nums)
    print 'By recur: {}'.format(time.time() - start_time)

    start_time = time.time()   
    print SolutionDp().lengthOfLIS(nums)
    print 'By DP: {}'.format(time.time() - start_time)

    start_time = time.time()   
    print SolutionBinarySearch().lengthOfLIS(nums)
    print 'By binary search: {}'.format(time.time() - start_time)


if __name__ == '__main__':
    main()
