"""Leetcode 703. Kth Largest Element in a Stream

URL: https://leetcode.com/problems/kth-largest-element-in-a-stream/

Easy

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

class KthLargestSort(object):
    """Kth Largest Element in a Stream

    Apply naive sorting to obtain the top k largest elements.
    """
    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        # Sort nums in descending order.
        nums.sort(reverse=True)
        self.k = k
        self.topk = nums[:k]

    def add(self, val):
        """
        :type val: int
        :rtype: int

        Time complexity: O(n*logn), where n is the length of the original nums.
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
    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        nums.sort(reverse=True)
        self.k = k
        self.topk = nums[:k]
        
    def add(self, val):
        """
        :type val: int
        :rtype: int

        Time complexity: O(logn), where n is the length of the original nums.
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
            if self.topk[mid] < val:
                right = mid
            elif self.topk[mid] >= val:
                left = mid + 1

        self.topk.insert(left, val)
        
        if len(self.topk) > self.k:
            self.topk.pop()

        return self.topk[-1]


class KthLargestMinHeap(object):
    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        nums.sort()
        self.k = k
        self.heap = [0]
        self.size = 0

        self.heap.extend(nums[-k:])
        self.size += len(nums[-k:])

    def _parent(self, i):
        return i // 2

    def _left(self, i):
        return i * 2

    def _right(self, i):
        return i * 2 + 1

    def heapify_up(self, i):
        """Min heapify up by iteration.

        Time complexity: O(logk).
        Space complexity: O(1).
        """
        # For node i, check it is "smaller" than parent, if yes, swap them.
        while i > 1 and self.heap[i] < self.heap[self._parent(i)]:
            self.heap[i], self.heap[self._parent(i)] = (
                self.heap[self._parent(i)], self.heap[i])
        
    def heapify_down(self, i):
        """Min heapify down by recursion.

        Time complexity: O(log(n)).
        Space complexity: O(1).
        """
        # Get min index from node i and its two child nodes.
        l, r = self._left(i), self._right(i)
        if l <= self.size and self.heap[l] < self.heap[i]:
            min_i = l
        else:
            min_i = i
        if r <= self.size and self.heap[r] < self.heap[min_i]:
            min_i = r

        # If node i is not min, swap node i and node min_i.
        if min_i != i:
            self.heap[i], self.heap[min_i] = self.heap[min_i], self.heap[i]
            self.heapify_down(min_i)

    def add(self, val):
        """
        :type val: int
        :rtype: int

        Time complexity: O(logn).
        Space complexity: O(1). 
        """
        if self.size < self.k:
            # If size < k, append new val to heap and run heapify_up(size).
            self.heap.append(val)
            self.size += 1
            self.heapify_up(self.size)
        elif self.heap[1] < val:
            # If size = k and min < val, replace it by val and 
            # run heapify_down(1).
            self.heap[1] = val
            self.heapify_down(1)

        return self.heap[1]


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
    print obj.add(3)
    # Adding 5 returns 5
    print obj.add(5)
    # Adding 10 returns 5
    print obj.add(10)
    # Adding 9 returns 8
    print obj.add(9)
    # Adding 4 returns 8
    print obj.add(4)
    print 'Time by naive sort: {}'.format(time.time() - start_time)

    start_time = time.time()
    obj = KthLargestSortAndBinarySearch(k, nums)
    # Adding 3 returns 4
    print obj.add(3)
    # Adding 5 returns 5
    print obj.add(5)
    # Adding 10 returns 5
    print obj.add(10)
    # Adding 9 returns 8
    print obj.add(9)
    # Adding 4 returns 8
    print obj.add(4)
    print 'Time by sort + binary search: {}'.format(
        time.time() - start_time)

    start_time = time.time()
    obj = KthLargestMinHeap(k, nums)
    # Adding 3 returns 4
    print obj.add(3)
    # Adding 5 returns 5
    print obj.add(5)
    # Adding 10 returns 5
    print obj.add(10)
    # Adding 9 returns 8
    print obj.add(9)
    # Adding 4 returns 8
    print obj.add(4)
    print 'Time by min heap: {}'.format(
        time.time() - start_time)

    k = 1
    nums = []
    
    start_time = time.time()
    obj = KthLargestMinHeap(k, nums)
    # Adding -3 returns -3
    print obj.add(-3)
    # Adding -2 returns -2
    print obj.add(-2)
    # Adding -4 returns -2
    print obj.add(-4)
    # Adding 0 returns 0
    print obj.add(0)
    # Adding 4 returns 4
    print obj.add(4)
    print 'Time by min heap: {}'.format(
        time.time() - start_time)


if __name__ == '__main__':
    main()
