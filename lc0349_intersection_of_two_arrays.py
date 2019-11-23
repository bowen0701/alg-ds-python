"""Leetcode 349. Intersection of Two Arrays
Easy

URL: 

Given two arrays, write a function to compute their intersection.

Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]

Example 2:
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]

Note:
- Each element in the result must be unique.
- The result can be in any order.
"""

class SolutionBuiltIn(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]

        Time complexity: O(n1*n2).
        Space complexity: O(n1+n2).
        """
        return list(set(nums1).intersection(set(nums2)))


def main():
    # Output: [2]
    nums1 = [1,2,2,1]
    nums2 = [2,2]
    print SolutionBuiltIn().intersection(nums1, nums2)

    # Output: [9, 4]
    nums1 = [4,9,5]
    nums2 = [9,4,9,8,4]
    print SolutionBuiltIn().intersection(nums1, nums2)


if __name__ == '__main__':
    main()
