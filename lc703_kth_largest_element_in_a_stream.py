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

    Time complexity: O(n*logn).
    Space complexity: O(1).
    """
    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k = k
        self.nums = nums
        self.nums.sort()
        self.nums = self.nums[-k:]

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        self.nums.append(val)
        self.nums.sort()
        self.nums = self.nums[-self.k:]
        return self.nums[0]


def main():
    # Your KthLargest object will be instantiated and called as such:
    # obj = KthLargest(k, nums)
    # param_1 = obj.add(val)
    k = 3
    nums = [4, 5, 8, 2]
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


if __name__ == '__main__':
    main()
