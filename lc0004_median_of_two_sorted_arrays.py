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
    def _selectKth(self, nums1, lo1, hi1, nums2, lo2, hi2, k):
        # Base cases: one array exhausted, select kth from the other.
        if lo1 > hi1:
            return nums2[lo2 + k]
        if lo2 > hi2:
            return nums1[lo1 + k]

        i1 = (lo1 + hi1) // 2
        i2 = (lo2 + hi2) // 2
        mid1, mid2 = nums1[i1], nums2[i2]

        # Combined elements before midpoints in both arrays.
        if k <= (i1 - lo1) + (i2 - lo2):
            # kth is in the first halves; discard the larger's second half.
            if mid1 > mid2:
                return self._selectKth(nums1, lo1, i1 - 1, nums2, lo2, hi2, k)
            else:
                return self._selectKth(nums1, lo1, hi1, nums2, lo2, i2 - 1, k)
        else:
            # kth is in the second halves; discard the smaller's first half.
            if mid1 > mid2:
                return self._selectKth(
                    nums1, lo1, hi1, nums2, i2 + 1, hi2,
                    k - (i2 - lo2) - 1
                )
            else:
                return self._selectKth(
                    nums1, i1 + 1, hi1, nums2, lo2, hi2,
                    k - (i1 - lo1) - 1
                )

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float

        Time complexity: O(log(m + n)).
        Space complexity: O(log(m + n)), for recursion stack.
        """
        # Apply selection method. Note: starting index is 0.
        l = len(nums1) + len(nums2)
        if l % 2 == 1:
            return self._selectKth(
                nums1, 0, len(nums1) - 1,
                nums2, 0, len(nums2) - 1,
                l // 2
            )
        else:
            return (
                self._selectKth(
                    nums1, 0, len(nums1) - 1,
                    nums2, 0, len(nums2) - 1,
                    l // 2 - 1
                )
                + self._selectKth(
                    nums1, 0, len(nums1) - 1,
                    nums2, 0, len(nums2) - 1,
                    l // 2
                )
            ) / 2.0


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
