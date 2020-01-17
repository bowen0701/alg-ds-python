"""Leetcode 523. Continuous Subarray Sum
Medium

URL: https://leetcode.com/problems/continuous-subarray-sum/

Given a list of non-negative numbers and a target integer k, write a function to
check if the array has a continuous subarray of size at least 2 that sums up to a
multiple of k, that is, sums up to n*k where n is also an integer.

Example 1:
Input: [23, 2, 4, 6, 7],  k=6
Output: True
Explanation: Because [2, 4] is a continuous subarray of size 2 and sums up to 6.

Example 2:
Input: [23, 2, 6, 4, 7],  k=6
Output: True
Explanation: Because [23, 2, 6, 4, 7] is an continuous subarray of size 5 and sums
up to 42.

Note:
- The length of the array won't exceed 10,000.
- You may assume the sum of all the numbers is in the range of a signed 32-bit integer.
"""


class SolutionModCumsumPosDictIter(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool

        Time complexity: O(n), where n is the length of nums.
        Space complexity: O(k).
        """
        from collections import defaultdict

        # Edge case.
        if not nums:
            return k == 0

        # Create dict: cumsum->pos.
        cumsum_pos_d = defaultdict()
        cumsum_pos_d[0] = -1

        cumsum = 0

        # Iterate through nums to add cumsum % k to dict.
        for i in range(len(nums)):
            cumsum += nums[i]

            # Update cumsum by taking % k.
            if k != 0:
                cumsum %= k

            if cumsum in cumsum_pos_d:
                # If cumsum in dict and more than 1 nums lie between pos i & j.
                # then subarray - nums[:j] is a multiple of k.
                j = cumsum_pos_d[cumsum]
                if j is not None and i - j > 1:
                    return True
            else:
                # If not, add cumsum to dict.
                cumsum_pos_d[cumsum] = i

        return False


def main():
    # Output: True
    nums = [23, 2, 4, 6, 7]
    k = 6
    print SolutionModCumsumPosDictIter().checkSubarraySum(nums, k)

    # Output: True
    nums = [23, 2, 6, 4, 7]
    k = 6
    print SolutionModCumsumPosDictIter().checkSubarraySum(nums, k)    

    # Output: True
    nums = [5,0,0]
    k = 0
    print SolutionModCumsumPosDictIter().checkSubarraySum(nums, k)    


if __name__ == '__main__':
    main()
