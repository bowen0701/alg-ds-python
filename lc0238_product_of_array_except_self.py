"""Leetcode 238. Product of Array Except Self
Medium

Given an array nums of n integers where n > 1, return an array output 
such that output[i] is equal to the product of all the elements of nums 
except nums[i].

Example:
Input:  [1,2,3,4]
Output: [24,12,8,6]

Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? 
(The output array does not count as extra space for the purpose of 
space complexity analysis.)
"""

from typing import List


class SolutionLeftRightProducts(object):
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        :type nums: List[int]
        :rtype: List[int]

        Time complexity: O(n).
        Space complexity: O(n).
        """
        n = len(nums)

        # Compute left products: [a,b,c] => lprods=[a,ab,abc]
        lprods = [1] * n
        lprods[0] = nums[0]
        for i in range(1, n):
            lprods[i] = lprods[i - 1] * nums[i]

        # Compute right products: [a,b,c] => rprods=[abc,bc,c]
        rprods = [1] * n
        rprods[-1] = nums[-1]
        for i in range(n - 2, -1, -1):
            rprods[i] = nums[i] * rprods[i + 1]

        result = [1] * n
        for i in range(n):
            if i == 0:
                # Leftmost = neighbor's right product.
                result[i] = rprods[1]
            elif i == n - 1:
                # Rightmost = neighbor's left product.
                result[i] = lprods[n - 2]
            else:
                # Middles: multiply left & right products excluding nums[i].
                result[i] = lprods[i - 1] * rprods[i + 1]

        return result


class SolutionLeftRightProductsOptim(object):
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        :type nums: List[int]
        :rtype: List[int]

        Time complexity: O(n).
        Space complexity: O(1).
        """
        n = len(nums)

        # Compute "shift-left" prods (exclude nums[i]): [a,b,c] => [1,a,ab].
        result = [1] * n
        for i in range(1, n):
            result[i] = result[i - 1] * nums[i - 1]

        # Compute "shift-right" prods (exclude nums[i]): [a,b,c] => [bc, c, 1].
        rprods = 1
        for i in range(n - 1, -1, -1):
            result[i] *= rprods
            rprods *= nums[i]

        return result


def main():
    # Output: [60, 40, 30, 24]
    nums = [2, 3, 4, 5]
    print(SolutionLeftRightProducts().productExceptSelf(nums))
    print(SolutionLeftRightProductsOptim().productExceptSelf(nums))


if __name__ == '__main__':
    main()
