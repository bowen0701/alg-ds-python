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

class KthLargestNaiveSort(object):
    """Kth Largest Element in a Stream

    Apply naive sorting to obtain the top k largest elements.

    Time complexity: O(n*logn), where n is the length of the original nums.
    Space complexity: O(k).
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
        """
        self.topk.append(val)
        self.topk.sort(reverse=True)

        if len(self.topk) > self.k:
            self.topk.pop()

        return self.topk[-1]


class KthLargestSortAndBinarySearch(object):
    """Kth Largest Element in a Stream

    Apply sorting to obtain the top k largest elements, with
    inserting new element by binary search in sorted list.

    Time complexity: O(n*logn), where n is the length of the original nums.
    Space complexity: O(k).
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


def main():
    import time
    # Your KthLargest object will be instantiated and called as such:
    # obj = KthLargest(k, nums)
    # param_1 = obj.add(val)
    k = 3
    nums = [4, 5, 8, 2]

    start_time = time.time()
    obj = KthLargestNaiveSort(k, nums)
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


if __name__ == '__main__':
    main()
