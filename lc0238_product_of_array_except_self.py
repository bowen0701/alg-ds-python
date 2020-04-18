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
        n = len(nums)

        # Compute left products: nums=[a,b,c] => lprods=[a,ab,abc]
        lprods = [1] * n
        lprods[0] = nums[0]
        for i in range(1, n):
            lprods[i] = lprods[i - 1] * nums[i]

        # Compute right products: rprods=[abc,bc,c]
        rprods = [1] * n
        rprods[-1] = nums[-1]
        for i in range(n - 2, -1, -1):
            rprods[i] = nums[i] * rprods[i + 1]

        prods = [1] * n
        for i in range(n):
            if i == 0:
                # Leftmost = neighbor's right product.
                prods[i] = rprods[1]
            elif i == n - 1:
                # Rightmost = neighbor's left product.
                prods[i] = lprods[n - 2]
            else:
                # Middles: multiply left & right products excluding nums[i].
                prods[i] = lprods[i - 1] * rprods[i + 1]

        return prods


class SolutionLeftRightProductsOptim(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]

        Time complexity: O(n).
        Space complexity: O(1).
        """
        n = len(nums)

        # Compute prods (excluding nums[i]): nums=[a,b,c] => prods=[1,a,ab].
        prods = [1] * n
        for i in range(1, n):
            prods[i] = prods[i - 1] * nums[i - 1]

        # Compute prods by rprods (excluding nums[i]): bc<-c<-1.
        rprods = 1
        for i in range(n - 1, -1, -1):
            prods[i] *= rprods
            rprods *= nums[i]

        return prods


def main():
    # Output: [60, 40, 30, 24]
    nums = [2, 3, 4, 5]
    print SolutionLeftRightProducts().productExceptSelf(nums)
    print SolutionLeftRightProductsOptim().productExceptSelf(nums)


if __name__ == '__main__':
    main()
