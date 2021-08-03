"""Leetcode 169. Majority Element
Easy

URL: https://leetcode.com/problems/majority-element/

Given an array of size n, find the majority element.
The majority element is the element that appears more than n//2 times.

You may assume that the array is non-empty and the majority element always
exist in the array.

Example 1:
Input: [3,2,3]
Output: 3

Example 2:
Input: [2,2,1,1,1,2,2]
Output: 2
"""

from typing import List


class SolutionNumCountDict(object):
    def majorityElement(self, nums: List[int]) -> int:
        """
        Time complexity: O(n).
        Space complexity: O(n).
        """
        from collections import defaultdict

        # Create dict:number->count.
        num_count_d = defaultdict(int)

        for n in nums:
            num_count_d[n] += 1

            if num_count_d[n] > len(nums) // 2:
                return n


def main():
    # Output: 3
    nums = [3,2,3]
    print(SolutionNumCountDict().majorityElement(nums))

    # Output: 2
    nums = [2,2,1,1,1,2,2]
    print(SolutionNumCountDict().majorityElement(nums))


if __name__ == '__main__':
    main()
