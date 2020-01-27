"""Leetcode 350. Intersection of Two Arrays II
Easy

URL: https://leetcode.com/problems/intersection-of-two-arrays-ii/

Given two arrays, write a function to compute their intersection.

Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]

Example 2:
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]

Note:
- Each element in the result should appear as many times as it shows in both arrays.
- The result can be in any order.

Follow up:
- What if the given array is already sorted? How would you optimize your algorithm?
- What if nums1's size is small compared to nums2's size? Which algorithm is better?
- What if elements of nums2 are stored on disk, and the memory is limited such that
  you cannot load all elements into the memory at once?
"""


class SolutionTwoNumCountDicts(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]

        Time complexity: O(n1+n2), where ni is the length of numsi.
        Space complexity: O(n1+n2).
        """
        # Use dict to collect number counts.
        from collections import defaultdict

        if not nums1 or not nums2:
            return []

        # Create dict: num->count for two nums.
        nums1_count_d = defaultdict(int)
        nums2_count_d = defaultdict(int)

        for n1 in nums1:
            nums1_count_d[n1] += 1
        for n2 in nums2:
            nums2_count_d[n2] += 1

        # Obtain intersection set of number count keys.
        unique_nums1 = set(nums1_count_d.keys())
        unique_nums2 = set(nums2_count_d.keys())
        intersect_nums = unique_nums1.intersection(unique_nums2)

        # Collect smaller number counts.
        intersect = []
        for n in intersect_nums:
            if nums1_count_d[n] < nums2_count_d[n]:
                intersect_times = nums1_count_d[n]
            else:
                intersect_times = nums2_count_d[n]

            intersect.extend([n] * intersect_times)

        return intersect


class SolutionNumCountDict(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]

        Time complexity: O(n1+n2), where ni is the length of numsi.
        Space complexity: O(n1).
        """
        # Use dict to collect number counts.
        from collections import defaultdict

        if not nums1 or not nums2:
            return []

        # Collect nums1's number->count.
        nums1_count_d= defaultdict(int)
        for n1 in nums1:
            nums1_count_d[n1] += 1

        # Iterate through nums1, if number is in nums2 and decrement its count.
        intersect = []
        for n2 in nums2:
            if n2 in nums1_count_d and nums1_count_d[n2] > 0:
                intersect.append(n2)
                nums1_count_d[n2] -= 1

        return intersect


def main():
    # Output: [2,2]
    nums1 = [1,2,2,1]
    nums2 = [2,2]
    # print SolutionNaiveIter().intersect(nums1, nums2)
    print SolutionTwoNumCountDicts().intersect(nums1, nums2)
    print SolutionNumCountDict().intersect(nums1, nums2)

    # Output: [4,9]
    nums1 = [4,9,5]
    nums2 = [9,4,9,8,4]
    # print SolutionNaiveIter().intersect(nums1, nums2)
    print SolutionTwoNumCountDicts().intersect(nums1, nums2)
    print SolutionNumCountDict().intersect(nums1, nums2)

    # Output: [2]
    nums1 = [1,2,2,1]
    nums2 = [2]
    # print SolutionNaiveIter().intersect(nums1, nums2)
    print SolutionTwoNumCountDicts().intersect(nums1, nums2)
    print SolutionNumCountDict().intersect(nums1, nums2)


if __name__ == '__main__':
    main()
