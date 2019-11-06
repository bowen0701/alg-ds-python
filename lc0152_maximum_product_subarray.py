"""Leetcode 152. Maximum Product Subarray
Medium

URL: https://leetcode.com/problems/maximum-product-subarray/

Given an integer array nums, find the contiguous subarray within an array
(containing at least one number) which has the largest product.

Example 1:
Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.

Example 2:
Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
"""

class SolutionDP(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        Time complexity: O(n), where n is the nums length.
        Space complexity: O(n).
        """
        cur_max_prod = [0] * len(nums)
        cur_min_prod = [0] * len(nums)
        cur_max_prod[0] = nums[0]
        cur_min_prod[0] = nums[0]

        global_max_prod = nums[0]

        for i in range(1, len(nums)):
            # Compute current max/min product before pos i:
            cur_max_prod[i] = max(cur_max_prod[i - 1] * nums[i],
                                  cur_min_prod[i - 1] * nums[i],
                                  nums[i])
            cur_min_prod[i] = min(cur_max_prod[i - 1] * nums[i],
                                  cur_min_prod[i - 1] * nums[i],
                                  nums[i])

            # Update global max prod before pos i.
            global_max_prod = max(cur_max_prod[i], global_max_prod)

        return global_max_prod


def main():
    # Output: 6
    nums = [2,3,-2,4]
    print SolutionDP().maxProduct(nums)

    # Output: 0
    nums = [-2,0,-1]
    print SolutionDP().maxProduct(nums)

    # Output: 24
    nums = [-2,3,-4]
    print SolutionDP().maxProduct(nums)



if __name__ == '__main__':
    main()
