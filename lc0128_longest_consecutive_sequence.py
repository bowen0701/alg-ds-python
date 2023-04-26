"""Leetcode 128. Longest Consecutive Sequence
Medium

URL: https://leetcode.com/problems/longest-consecutive-sequence/

Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

Example 1:
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
 
Constraints:
- 0 <= nums.length <= 10^5
- 10^9 <= nums[i] <= 10^9
"""

from typing import List


class SolutionLeftRightIncrements:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Edge case.
        if not nums:
            return 0

        # Iterate through nums to check its consecutive lefts & rights to get the length.
        nums_set = set(nums)
        result = 1

        for n in nums:
            if n not in nums_set:
                continue
            
            nums_set.remove(n)

            left, right = n - 1, n + 1
            while left in nums_set:
                nums_set.remove(left)
                left -= 1
            while right in nums_set:
                nums_set.remove(right)
                right += 1

            result = max(result, right - left - 1)

        return result


def main():
    # Output: 4
    nums = [100,4,200,1,3,2]
    print(SolutionLeftRightIncrements().longestConsecutive(nums))

    # Output: 9
    nums = [0,3,7,2,5,8,4,6,0,1]
    print(SolutionLeftRightIncrements().longestConsecutive(nums))


if __name__ == "__main__":
    main()
