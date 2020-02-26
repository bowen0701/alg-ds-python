"""Leetcode 532. K-diff Pairs in an Array
Easy

URL: https://leetcode.com/problems/k-diff-pairs-in-an-array/

Given an array of integers and an integer k, you need to find the number 
of unique k-diff pairs in the array. Here a k-diff pair is defined as an
integer pair (i, j), where i and j are both numbers in the array and
their absolute difference is k.

Example 1:
Input: [3, 1, 4, 1, 5], k = 2
Output: 2
Explanation: There are two 2-diff pairs in the array, (1, 3) and (3, 5).
Although we have two 1s in the input, we should only return the number
of unique pairs.

Example 2:
Input:[1, 2, 3, 4, 5], k = 1
Output: 4
Explanation: There are four 1-diff pairs in the array, (1, 2), (2, 3),
(3, 4) and (4, 5).

Example 3:
Input: [1, 3, 1, 5, 4], k = 0
Output: 1
Explanation: There is one 0-diff pair in the array, (1, 1).

Note:
- The pairs (i, j) and (j, i) count as the same pair.
- The length of the array won't exceed 10,000.
- All the integers in the given input belong to the range: [-1e7, 1e7].
"""

class SolutionNumCountDict(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int

        Similar approach with two sum problem.

        Time complexity: O(n), where n is the length of nums.
        Space complexity: O(n).
        """
        from collections import defaultdict

        # Edge case.
        if not nums or k < 0:
            return 0

        # One scan to create dict:num->count.
        num_count_d = defaultdict(int)
        counter = 0

        # Iterate through nums to check if has k-diff.
        for num in nums:
            if num in num_count_d:
                # If visited num before, has k-diff only if k=0 & its count=1.
                if k == 0 and num_count_d[num] == 1:
                    counter += 1
                    num_count_d[num] += 1
            else:
                # If not, check if has k-diff.
                if num + k in num_count_d:
                    counter += 1
                if num - k in num_count_d:
                    counter += 1
                num_count_d[num] = 1

        return counter


def main():
    # Output: 2
    nums = [3, 1, 4, 1, 5]
    k = 2
    print SolutionNumCountDict().findPairs(nums, k)

    # Output: 4
    nums = [1, 2, 3, 4, 5]
    k = 1
    print SolutionNumCountDict().findPairs(nums, k)

    # Output: 1
    nums = [1, 3, 1, 5, 4]
    k = 0
    print SolutionNumCountDict().findPairs(nums, k)


if __name__ == '__main__':
    main()

