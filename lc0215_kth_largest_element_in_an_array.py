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

class SolutionSelectionSort(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int

        Time complexity: O(nk).
        Space complexity: O(1).
        """
        n = len(nums)

        # Selection sort to put the biggest, 2nd biggest,... from tail to head.
        for i in range(n - 1, n - k - 1, -1):
            cur = 0
            for j in range(1, i + 1):
                if nums[cur] < nums[j]:
                    cur = j
            nums[cur], nums[i] = nums[i], nums[cur]

        return nums[-k]


class SolutionQuickSort(object):
    def _quicksort(self, nums):
        if len(nums) <= 1:
            return nums

        pivot = nums[len(nums) // 2]

        small_nums = [x for x in nums if x < pivot]
        mid_nums = [x for x in nums if x == pivot]
        large_nums = [x for x in nums if x > pivot]

        return (self._quicksort(small_nums) +
                mid_nums +
                self._quicksort(large_nums))

    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int

        Time complexity: O(n*logn), where n is the length of nums.
        Space complexity: O(n).
        """
        # Apply quick sort and get the element directly.
        sorted_nums = self._quicksort(nums)
        return sorted_nums[-k]


class SolutionMinHeap(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int

        Time complexity: O(n*logk).
        Space complexity: O(k).
        """
        import heapq

        minheap = []

        # Push the first k nums into min heap.
        for i in range(k):
            heapq.heappush(minheap, nums[i])

        # Push the remaining nums into minheap if > minheap's root.
        # Then keep maxheap with k elements.
        for j in range(k + 1, len(nums)):
            if nums[j] > minheap[0]:
                heapq.heappop(minheap)
                heapq.heappush(minheap, nums[j])

        return minheap[0]


class SolutionSelect(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int

        Time complexity: O(n).
        Space complexity: O(n).
        """
        # Select w/o consider the relative order of other elements.
        pivot = nums[len(nums) // 2]

        large_pos = [pos for pos, x in enumerate(nums) if x > pivot]
        mid_pos = [pos for pos, x in enumerate(nums) if x == pivot]
        small_pos = [pos for pos, x in enumerate(nums) if x < pivot]

        n_large = len(large_pos)
        n_mid = len(mid_pos)

        if k <= n_large:
            large_nums = [nums[pos] for pos in large_pos]
            return self.findKthLargest(large_nums, k)
        elif n_large < k <= n_mid + n_large:
            return pivot
        elif k > n_mid + n_large:
            small_nums = [nums[pos] for pos in small_pos]
            return self.findKthLargest(small_nums, k - n_large - n_mid)


def main():
    import time

    # Input: [3,2,1,5,6,4] and k = 2
    # Output: 5
    nums = [3, 2, 1, 5, 6, 4]
    k = 2

    start_time = time.time()
    print 'Selection sort:', SolutionSelectionSort().findKthLargest(nums, k)
    print 'Time:', time.time() - start_time

    start_time = time.time()
    print 'Quick sort:', SolutionQuickSort().findKthLargest(nums, k)
    print 'Time:', time.time() - start_time

    start_time = time.time()
    print 'Selection: ', SolutionMinHeap().findKthLargest(nums, k)
    print 'Time:', time.time() - start_time

    start_time = time.time()
    print 'Selection: ', SolutionSelect().findKthLargest(nums, k)
    print 'Time:', time.time() - start_time

    # Input: [3,2,3,1,2,4,5,5,6] and k = 4
    # Output: 4
    nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    k = 5

    start_time = time.time()
    print 'Selection sort:', SolutionSelectionSort().findKthLargest(nums, k)
    print 'Time:', time.time() - start_time

    start_time = time.time()
    print 'Quick sort:', SolutionQuickSort().findKthLargest(nums, k)
    print 'Time:', time.time() - start_time

    start_time = time.time()
    print 'Selection: ', SolutionMinHeap().findKthLargest(nums, k)
    print 'Time:', time.time() - start_time

    start_time = time.time()
    print 'Selection: ', SolutionSelect().findKthLargest(nums, k)
    print 'Time:', time.time() - start_time


if __name__ == '__main__':
    main()
