"""Leetcode 416. Partition Equal Subset Sum
Medium

URL: https://leetcode.com/problems/partition-equal-subset-sum/

Given a non-empty array containing only positive integers, find if the array
can be partitioned into two subsets such that the sum of elements in both
subsets is equal.

Note:
- Each of the array element will not exceed 100.
- The array size will not exceed 200.

Example 1:
Input: [1, 5, 11, 5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].

Example 2:
Input: [1, 2, 3, 5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.
"""

class SolutionIndexSumFoundDpMemo(object):
    def partition(self, idx, cur_sum, idxsum_found_d, nums, total):
        if (idx, cur_sum) in idxsum_found_d:
            return idxsum_found_d[(idx, cur_sum)]

        if cur_sum * 2 == total:
            return True

        if cur_sum * 2 > total or idx >= len(nums):
            return False

        # Take or not take nums[idx].
        is_found = (
            self.partition(idx + 1, cur_sum + nums[idx], idxsum_found_d, nums, total) or
            self.partition(idx + 1, cur_sum, idxsum_found_d, nums, total))
        idxsum_found_d[(idx, cur_sum)] = is_found
        return is_found

    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool

        Apply bottom-up dynamic programming with memoization.

        Time complexity: O(n), where n is the length of nums.
        Space complexity: O(n).
        """
        total = sum(nums)
        
        # Check if total is even.
        if total % 2:
            return False

        # Apply (idx, sum)->found dict to memorize temporary found.
        idx = 0
        cur_sum = 0
        idxsum_found_d = {}
        return self.partition(idx, cur_sum, idxsum_found_d, nums, total)


def main():
    # Output: True
    nums = [1, 5, 11, 5]
    print SolutionIndexSumFoundDpMemo().canPartition(nums)

    # Output: False
    nums = [1, 2, 3, 5]
    print SolutionIndexSumFoundDpMemo().canPartition(nums)


if __name__ == '__main__':
    main()
