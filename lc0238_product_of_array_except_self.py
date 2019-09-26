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

class SolutionLeftRightProducts(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]

        Time complexity: O(n).
        Space complexity: O(n).
        """
        size = len(nums)

        # Compute left_prods as product of left numbers and nums[i].
        left_prods = [1] * size
        left_prods[0] = nums[0]

        for i in range(1, size):
            left_prods[i] = left_prods[i - 1] * nums[i]

        # Compute right_prods as product of right numbers and nums[i].
        right_prods = [1] * size
        right_prods[size - 1] = nums[size - 1]

        for i in range(size - 2, -1, -1):
            right_prods[i] = right_prods[i + 1] * nums[i]

        # Multiply left_prods and right_prods excluding nums[i].
        prods = [1] * size

        for i, n in enumerate(nums):
            if i == 0:
                # Leftmost = neighbor's right product.
                prods[i] = right_prods[i + 1]
            elif i == size - 1:
                # Rightmost = neighbor's left product.
                prods[i] = left_prods[i - 1]
            if 1 <= i <= size - 2:
                # Middles = product of neighbors's left & right products.
                prods[i] = left_prods[i - 1] * right_prods[i + 1]

        return prods


class SolutionLeftRightProducts2(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]

        Time complexity: O(n).
        Space complexity: O(1).
        """
        size = len(nums)
        prods = [1] * size

        # Compute prods as product of numbers left to nums[i].
        # Say nums: [a, b, c, d] => prods: [1, a, ab, abc].
        for i in range(1, size):
            prods[i] = prods[i - 1] * nums[i - 1]

        # Product prods and product of numbers right to nums[i],
        # by right_prods: bcd <- cd <- d <- 1.
        right_prods = 1
        for i in range(size - 1, -1, -1):
            prods[i] *= right_prods
            right_prods *= nums[i]

        return prods


def main():
    # Input:  [2, 3, 4, 5]
    # Output: [60, 40, 30, 24]
    nums = [2, 3, 4, 5]

    print SolutionLeftRightProducts().productExceptSelf(nums)
    print SolutionLeftRightProducts2().productExceptSelf(nums)


if __name__ == '__main__':
    main()
