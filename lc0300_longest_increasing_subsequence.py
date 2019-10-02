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
Your algorithm should run in O(n2) complexity.
Follow up: Could you improve it to O(n log n) time complexity?
"""


class SolutionRecur(object):
    def _LIS(self, prev, nums, start, end):
        if start == end:
            return 0

        # The LIS of nums[0:n] is either a LIS of nums[1:n], excluding nums[0],
        # or the LIS is 1 + a LIS of nums[1:n], including nums[0],
        # if nums[0] is bigger than the previous.
        lis_ex = self._LIS(prev, nums, start + 1, end)

        lis_in = -float('inf')
        if nums[start] > prev:
            lis_in = 1 + self._LIS(nums[start], nums, start + 1, end)

        lis = max(lis_ex, lis_in)
        return lis

    def lengthOfLIS(self, nums):
        """Length of LIS by recursion.

        Time complexity: O(2^n).
        Space complexity: O(1).
        """
        # Apply top-down recursion with two pointers, starting from the two sides.
        start, end = 0, len(nums) - 1
        return self._LIS(-float('inf'), nums, start, end)


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

        # Create a table and set all elements to 1,
        # because the LIS of each element is at least 1.
        T = [1] * len(nums)

        # Apply two pointer method: for each right element j,
        # check all elements i left to j; 
        # if element i is smaller than j, update T[j] = max(T[j], T[i] + 1).
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
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
        if not nums:
            return 0

        tails = [0] * len(nums)
        lis = 0
 
        # If n is larger than all tails, append it and increase the size by 1.
        # Further, if tails[i-1] < n <= tails[i], update tails[i].
        for n in nums:
            # Use binary search to find the correct tail for new item.
            left, right = 0, lis
            while left != right:
                mid = (left + right) // 2
                if tails[mid] < n:
                    left = mid + 1
                else:
                    right = mid

            tails[left] = n
            lis = max(left + 1, lis)

        return lis


def main():
    import time

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
