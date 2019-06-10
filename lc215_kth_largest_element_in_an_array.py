"""Leetcode 215. Kth Largest Element in an Array
Medium

URL: https://leetcode.com/problems/kth-largest-element-in-an-array/

Find the kth largest element in an unsorted array. 
Note that it is the kth largest element in the sorted order, 
not the kth distinct element.

Example 1:
Input: [3,2,1,5,6,4] and k = 2
Output: 5

Example 2:
Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4

Note: 
You may assume k is always valid, 1 <= k <= array's length.
"""

class SolutionQuickSort(object):
    def quicksort(self, nums):
        if len(nums) <= 1:
            return nums

        pivot = nums[len(nums) // 2]

        left_nums = [n for n in nums if n < pivot]
        mid_nums = [n for n in nums if n == pivot]
        right_nums = [n for n in nums if n > pivot]

        return self.quicksort(left_nums) + mid_nums + self.quicksort(right_nums)

    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int

        Apply quick sort algorithm.

        Time complexity: O(n*logn), where n is the length of nums.
        Space complexity: O(n).
        """
        sorted_nums = self.quick_sort(nums)
        return sorted_nums[-k]


class SolutionSelectionSort(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int

        Apply selection sort.

        Time complexity: O(nk).
        Space complexity: O(1).
        """
        for i in range(len(nums) - 1, len(nums) - k - 1, -1):
            s = 0
            for j in range(1, i + 1):
                if nums[s] < nums[j]:
                    s = j
            nums[s], nums[i] = nums[i], nums[s]

        return nums[-k]


class SolutionIter(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int

        Apply iteration to insert element.

        Time complexity: O(nk).
        Space complexity: O(k).
        """
        # Create a base list of length k with value -inf.
        k_nums = [-float('inf')] * k

        # Iterate over nums, and insert it to suitable position w/ pop.
        for n in nums:
            for j in range(k - 1, -1, -1):
                if n > k_nums[j]:
                    k_nums.insert(j + 1, n)
                    k_nums.pop(0)
                    break

        return k_nums[0]


def main():
    import time

    # Input: [3,2,1,5,6,4] and k = 2
    # Output: 5
    nums = [3, 2, 1, 5, 6, 4]
    k = 2

    start_time = time.time()
    print SolutionQuickSort().findKthLargest(nums, k)
    print 'Time by quick sort:', time.time() - start_time

    start_time = time.time()
    print SolutionSelectionSort().findKthLargest(nums, k)
    print 'Time by selection sort:', time.time() - start_time

    start_time = time.time()
    print SolutionIter().findKthLargest(nums, k)
    print 'Time by iteration:', time.time() - start_time

    # Input: [3,2,3,1,2,4,5,5,6] and k = 4
    # Output: 4
    nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    k = 4

    start_time = time.time()
    print SolutionQuickSort().findKthLargest(nums, k)
    print 'Time by sorting:', time.time() - start_time

    start_time = time.time()
    print SolutionSelectionSort().findKthLargest(nums, k)
    print 'Time by selection sort:', time.time() - start_time

    start_time = time.time()
    print SolutionIter().findKthLargest(nums, k)
    print 'Time by iteration:', time.time() - start_time


if __name__ == '__main__':
    main()
