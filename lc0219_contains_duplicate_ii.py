"""Leetcode 219. Contains Duplicate II
Easy

URL: https://leetcode.com/problems/contains-duplicate-ii/

Given an array of integers and an integer k,
find out whether there are two distinct indices i and j in the array such that
nums[i] = nums[j] and the absolute difference between i and j is at most k.

Example 1:
Input: nums = [1,2,3,1], k = 3
Output: true

Example 2:
Input: nums = [1,0,1,1], k = 1
Output: true

Example 3:
Input: nums = [1,2,3,1,2,3], k = 2
Output: false
"""

class SolutionDict(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        from collections import defaultdict

        # Create a dict to collect number and their indices.
        num_idx_d = defaultdict()

        for i, n in enumerate(nums):
            if n not in num_idx_d:
                num_idx_d[n] = [i]
            else:
                # If same number's indices are nearby.  
                if i - num_idx_d[n][-1] <= k:
                    return True

                num_idx_d[n].append(i)

        return False


def main():
    # Output: True
    nums = [1,2,3,1]
    k = 3
    print SolutionDict().containsNearbyDuplicate(nums, k)

    # Output: True
    nums = [1,0,1,1]
    k = 1
    print SolutionDict().containsNearbyDuplicate(nums, k)

    # Output: False
    nums = [1,2,3,1,2,3]
    k = 2
    print SolutionDict().containsNearbyDuplicate(nums, k)


if __name__ == '__main__':
    main()
