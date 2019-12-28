"""Leetcode 4. Median of Two Sorted Arrays
Hard

There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. 
The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

Example 1:
nums1 = [1, 3]
nums2 = [2]
The median is 2.0

Example 2:
nums1 = [1, 2]
nums2 = [3, 4]
The median is (2 + 3)/2 = 2.5
"""

class SolutionSelect(object):
    def _findKth(self, nums1, nums2, k):
        # Base cases for the divide-and-conquer method.
        if not nums1:
            return nums2[k]
        if not nums2:
            return nums1[k]

        i1, i2 = len(nums1) // 2, len(nums2) // 2
        n1, n2 = nums1[i1], nums2[i2]

        if k <= i1 + i2:
            # When k is smaller than or equal to the sum of nums1 & nums2's 
            # middle indices.
            if n1 > n2:
                # When nums1's middle element is bigger than nums2's,
                # the 2nd half of nums1 does not contain the kth. 
                return self._findKth(nums1[:i1], nums2, k)
            else:
                return self._findKth(nums1, nums2[:i2], k)
        else:
            # When k is bigger than the sum of nums1 & nums2's middle indices.
            if n1 > n2:
                # When nums1's middle element is bigger than nums2's,
                # the 1st half of nums2 does not contain the kth.
                return self._findKth(nums1, nums2[(i2 + 1):], k - i2 - 1)
            else:
                return self._findKth(nums1[(i1 + 1):], nums2, k - i1 - 1)

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float

        Time complexity: O(log(m + n)).
        Space complexity: O(m + n).
        """
        # Apply selection method.
        l = len(nums1) + len(nums2)
        if l % 2 == 1:
            return self._findKth(nums1, nums2, l // 2)
        else:
            return (
                self._findKth(nums1, nums2, l // 2 - 1)
                + self._findKth(nums1, nums2, l // 2)) / 2.0


def main():
    # Ans: 2.
    nums1 = [1, 3]
    nums2 = [2]
    print(SolutionSelect().findMedianSortedArrays(nums1, nums2))

    # Ans: 2.5.
    nums1 = [1, 2]
    nums2 = [3, 4]
    print(SolutionSelect().findMedianSortedArrays(nums1, nums2))


if __name__ == '__main__':
    main()
