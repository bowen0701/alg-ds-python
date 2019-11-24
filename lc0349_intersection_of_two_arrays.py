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


class SolutionSet(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]

        Time complexity: O(max(n1, n2)).
        Space complexity: O(max(n1, n2)).
        """
        from collections import defaultdict

        res = []

        # Convert smaller nums to nums1.
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        # Set smaller nums to dict.
        nums1_count = defaultdict(int)

        for n1 in nums1:
            nums1_count[n1] += 1

        for n2 in nums2:
            if n2 in nums1_count and nums1_count[n2] > 0:
                res.append(n2)

                # Set n2 count to 0 to prevent duplicates.
                nums1_count[n2] = 0

        return res


def main():
    # Output: [2]
    nums1 = [1,2,2,1]
    nums2 = [2,2]
    print SolutionBuiltIn().intersection(nums1, nums2)
    print SolutionSet().intersection(nums1, nums2)

    # Output: [9, 4]
    nums1 = [4,9,5]
    nums2 = [9,4,9,8,4]
    print SolutionBuiltIn().intersection(nums1, nums2)
    print SolutionSet().intersection(nums1, nums2)


if __name__ == '__main__':
    main()
