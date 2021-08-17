"""Leetcode 703. Kth Largest Element in a Stream
Easy

URL: https://leetcode.com/problems/kth-largest-element-in-a-stream/

Design a class to find the kth largest element in a stream. 
Note that it is the kth largest element in the sorted order, 
not the kth distinct element.

Your KthLargest class will have a constructor which accepts an integer k 
and an integer array nums, which contains initial elements from the stream. 
For each call to the method KthLargest.add, 
return the element representing the kth largest element in the stream.

Example:
int k = 3;
int[] arr = [4,5,8,2];
KthLargest kthLargest = new KthLargest(3, arr);
kthLargest.add(3);   // returns 4
kthLargest.add(5);   // returns 5
kthLargest.add(10);  // returns 5
kthLargest.add(9);   // returns 8
kthLargest.add(4);   // returns 8

Note: 
You may assume that nums' length >= k-1 and k >= 1.
"""

from typing import List

import heapq


class KthLargestSort(object):
    """Kth Largest Element in a Stream

    Apply naive sorting to obtain the top k largest elements.
    """
    def __init__(self, k: int, nums: List[int]):
        """
        Time complexity: O(n*logn), where n is the length of the original nums.
        Space complexity: O(k).
        """
        # Sort nums in descending order.
        nums.sort(reverse=True)
        self.k = k
        self.topk = nums[:k]

    def add(self, val: int) -> int:
        """
        Time complexity: O(k*logk).
        Space complexity: O(k).
        """
        self.topk.append(val)
        self.topk.sort(reverse=True)

        if len(self.topk) > self.k:
            self.topk.pop()

        return self.topk[-1]


class KthLargestSortAndBinarySearch(object):
    """Kth Largest Element in a Stream

    Apply sorting to obtain the top k largest elements, and
    insert new element by binary search in sorted list.
    """
    def __init__(self, k: int, nums: List[int]):
        """
        Time complexity: O(n*logn), where n is the length of the original nums.
        Space complexity: O(k).
        """
        nums.sort(reverse=True)
        self.k = k
        self.topk = nums[:k]
        
    def add(self, val: int) -> int:
        """
        Time complexity: O(logk).
        Space complexity: O(k).
        """
        if len(self.topk) == self.k and val < self.topk[-1]:
            return self.topk[-1]

        # Apply binary search in reversed sorted list to 
        # decide the position to add new element.
        left = 0
        right = self.k - 1

        while left < right:
            mid = left + (right - left) // 2

            # Binary search with right & left in decreasing list.
            if self.topk[mid] < val:
                right = mid
            elif self.topk[mid] >= val:
                left = mid + 1

        self.topk.insert(left, val)
        
        if len(self.topk) > self.k:
            self.topk.pop()

        return self.topk[-1]


class KthLargestHeapq(object):
    def __init__(self, k: int, nums: List[int]):
        """
        Time complexity: O(logn).
        Space complexity: O(n).
        """
        self.minheap = nums
        self.k = k

        # Heapify the original nums, and pop min until the len equals to k.
        heapq.heapify(self.minheap)

        while len(self.minheap) > self.k:
            heapq.heappop(self.minheap)

    def add(self, val: int) -> int:
        """
        Time complexity: O(logk).
        Space complexity: O(1). 
        """
        if len(self.minheap) < self.k:
            # If heap size < k, push val to heap and heapify it.
            heapq.heappush(self.minheap, val)
        elif self.minheap[0] < val:
            # If heap size = k and min < val, replace (pop & push) min by val.
            heapq.heapreplace(self.minheap, val)

        return self.minheap[0]


def main():
    import time
    # Your KthLargest object will be instantiated and called as such:
    # obj = KthLargest(k, nums)
    # param_1 = obj.add(val)
    k = 3
    nums = [4, 5, 8, 2]

    start_time = time.time()
    obj = KthLargestSort(k, nums)
    # Adding 3 returns 4
    print(obj.add(3))
    # Adding 5 returns 5
    print(obj.add(5))
    # Adding 10 returns 5
    print(obj.add(10))
    # Adding 9 returns 8
    print(obj.add(9))
    # Adding 4 returns 8
    print(obj.add(4))
    print('Time by naive sort: {}'.format(time.time() - start_time))

    start_time = time.time()
    obj = KthLargestSortAndBinarySearch(k, nums)
    # Adding 3 returns 4
    print(obj.add(3))
    # Adding 5 returns 5
    print(obj.add(5))
    # Adding 10 returns 5
    print(obj.add(10))
    # Adding 9 returns 8
    print(obj.add(9))
    # Adding 4 returns 8
    print(obj.add(4))
    print('Time by sort + binary search: {}'.format(
          time.time() - start_time))

    start_time = time.time()
    obj = KthLargestHeapq(k, nums)
    # Adding 3 returns 4
    print(obj.add(3))
    # Adding 5 returns 5
    print(obj.add(5))
    # Adding 10 returns 5
    print(obj.add(10))
    # Adding 9 returns 8
    print(obj.add(9))
    # Adding 4 returns 8
    print(obj.add(4))
    print('Time by heapq: {}'.format(
          time.time() - start_time))

    k = 1
    nums = []

    start_time = time.time()
    obj = KthLargestHeapq(k, nums)
    # Adding -3 returns -3
    print(obj.add(-3))
    # Adding -2 returns -2
    print(obj.add(-2))
    # Adding -4 returns -2
    print(obj.add(-4))
    # Adding 0 returns 0
    print(obj.add(0))
    # Adding 4 returns 4
    print(obj.add(4))
    print('Time by min heap: {}'.format(
          time.time() - start_time))


if __name__ == '__main__':
    main()
