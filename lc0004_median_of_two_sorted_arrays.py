"""Leetcode 4. Median of Two Sorted Arrays
Hard

URL: https://leetcode.com/problems/median-of-two-sorted-arrays/

Given two sorted arrays nums1 and nums2 of size m and n respectively, return
the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

Example 1:
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Example 2:
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

Constraints:
- nums1.length == m
- nums2.length == n
- 0 <= m <= 1000
- 0 <= n <= 1000
- 1 <= m + n <= 2000
- -10^6 <= nums1[i], nums2[i] <= 10^6
"""

class SolutionSelect:
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
        # Apply selection method. Note: starting index is 0.
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
